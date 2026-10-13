"""Weather CLI application main entry point."""

import argparse
import os
import sys
from pathlib import Path

try:
    from week08.favorites import FavoritesManager
    from week08.weather_api import (
        WeatherAPI,
        format_current_weather,
        format_forecast,
    )
except ImportError:
    from favorites import FavoritesManager
    from weather_api import (
        WeatherAPI,
        format_current_weather,
        format_forecast,
    )

FAVORITES_FILE = "favorites.json"


def load_api_key():
    """Loads API key from WEATHER_API_KEY environment variable first, then config.py."""
    env_key = os.getenv("WEATHER_API_KEY")
    if env_key:
        return env_key.strip()

    config_paths = [
        Path("week08/config.py"),
        Path(__file__).parent / "config.py",
        Path("config.py"),
    ]

    for cfg in config_paths:
        if cfg.exists():
            try:
                import importlib.util

                spec = importlib.util.spec_from_file_location("config", cfg)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                key = getattr(module, "API_KEY", None) or getattr(module, "WEATHER_API_KEY", None)
                if key and key.strip() and key.strip() != "YOUR_API_KEY_HERE":
                    return key.strip()
            except Exception:
                continue

    return None


def build_parser() -> argparse.ArgumentParser:
    """Builds and returns the argparse parser for the weather CLI."""
    parser = argparse.ArgumentParser(description="Weather CLI Application")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # current LOCATION
    current_parser = subparsers.add_parser("current", help="Get current weather")
    current_parser.add_argument("location", help="Location name or favorite alias")

    # forecast LOCATION --days 2
    forecast_parser = subparsers.add_parser("forecast", help="Get weather forecast")
    forecast_parser.add_argument("location", help="Location name or favorite alias")
    forecast_parser.add_argument(
        "--days", type=int, default=3, help="Number of forecast days (1-3)"
    )

    # favorites [add|list|remove]
    fav_parser = subparsers.add_parser("favorites", help="Manage favorite locations")
    fav_subparsers = fav_parser.add_subparsers(dest="favorites_command", required=True)

    # favorites add NAME LOCATION
    fav_add = fav_subparsers.add_parser("add", help="Add a favorite location")
    fav_add.add_argument("name", help="Alias name")
    fav_add.add_argument("location", help="Location string")

    # favorites list
    fav_subparsers.add_parser("list", help="List all favorites")

    # favorites remove NAME
    fav_remove = fav_subparsers.add_parser("remove", help="Remove a favorite location")
    fav_remove.add_argument("name", help="Alias name")

    return parser


def main(argv=None) -> int:
    """Main CLI execution routine. Returns 0 on success, 1 on error."""
    parser = build_parser()
    args = parser.parse_args(argv)

    fav_mgr = FavoritesManager(FAVORITES_FILE)

    if args.command == "favorites":
        if args.favorites_command == "add":
            if not fav_mgr.add(args.name, args.location):
                sys.stderr.write(f"Error: Favorite '{args.name}' already exists or invalid.\n")
                return 1
            print(f"Added favorite '{args.name}' -> '{args.location}'")
            return 0

        elif args.favorites_command == "remove":
            if not fav_mgr.remove(args.name):
                sys.stderr.write(f"Error: Favorite '{args.name}' not found.\n")
                return 1
            print(f"Removed favorite '{args.name}'")
            return 0

        elif args.favorites_command == "list":
            favorites = fav_mgr.list_all()
            for name, loc in sorted(favorites.items()):
                print(f"{name}: {loc}")
            return 0

    api_key = load_api_key()
    if not api_key:
        sys.stderr.write("Error: Missing Weather API key.\n")
        return 1

    target_location = fav_mgr.get_location(args.location) or args.location
    client = WeatherAPI(api_key=api_key)

    if args.command == "current":
        data = client.get_current_weather(target_location)
        if not data:
            sys.stderr.write(f"Error: Failed to retrieve weather for '{target_location}'.\n")
            return 1
        print(format_current_weather(data))
        return 0

    elif args.command == "forecast":
        if not (1 <= args.days <= 3):
            sys.stderr.write("Error: Forecast days must be between 1 and 3.\n")
            return 1
        data = client.get_forecast(target_location, days=args.days)
        if not data:
            sys.stderr.write(f"Error: Failed to retrieve forecast for '{target_location}'.\n")
            return 1
        print(format_forecast(data))
        return 0

    return 0


if __name__ == "__main__":
    sys.exit(main())
    
