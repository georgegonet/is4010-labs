"""Weather API client and response formatters for Lab 08."""

import requests


class WeatherAPI:
    """Client for interacting with the WeatherAPI service."""

    def __init__(self, api_key: str, base_url: str = "https://api.weatherapi.com/v1"):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")

    def get_current_weather(self, location: str):
        """Fetches current weather data for a location. Returns dict or None."""
        url = f"{self.base_url}/current.json"
        params = {"key": self.api_key, "q": location}
        try:
            response = requests.get(url, params=params, timeout=10)
            return response.json()
        except Exception:
            return None

    def get_forecast(self, location: str, days: int = 3):
        """Fetches forecast weather data for a location. Returns dict or None."""
        if not (1 <= days <= 3):
            raise ValueError("Forecast days must be between 1 and 3.")

        url = f"{self.base_url}/forecast.json"
        params = {"key": self.api_key, "q": location, "days": days}
        try:
            response = requests.get(url, params=params, timeout=10)
            return response.json()
        except Exception:
            return None


def format_current_weather(data: dict) -> str:
    """Formats current weather as: CITY, COUNTRY: TEMP°F, CONDITION."""
    location = data.get("location", {})
    current = data.get("current", {})

    city = location.get("name", "Unknown")
    country = location.get("country", "Unknown")
    temp = current.get("temp_f", "N/A")
    condition = current.get("condition", {}).get("text", "Unknown")

    return f"{city}, {country}: {temp}°F, {condition}"


def format_forecast(data: dict) -> str:
    """Formats each forecast day as: DATE: high TEMP°F, low TEMP°F, CONDITION."""
    forecastday_list = data.get("forecast", {}).get("forecastday", [])
    lines = []

    for day_entry in forecastday_list:
        date = day_entry.get("date", "Unknown")
        day_stats = day_entry.get("day", {})
        high = day_stats.get("maxtemp_f", "N/A")
        low = day_stats.get("mintemp_f", "N/A")
        condition = day_stats.get("condition", {}).get("text", "Unknown")
        lines.append(f"{date}: high {high}°F, low {low}°F, {condition}")

    return "\n".join(lines)
    