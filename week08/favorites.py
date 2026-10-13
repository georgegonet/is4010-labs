"""Favorites manager for Lab 08 Weather CLI."""

import json
from pathlib import Path


class FavoritesManager:
    """Manages saved favorite locations stored in a JSON file."""

    def __init__(self, filename="favorites.json"):
        self.filepath = Path(filename)
        self.favorites = {}
        self._load()

    def _load(self):
        """Loads favorites from JSON. Missing or corrupted files produce an empty collection."""
        if not self.filepath.exists():
            self.favorites = {}
            return

        try:
            with open(self.filepath, "r", encoding="utf-8") as file:
                data = json.load(file)
                if isinstance(data, dict):
                    self.favorites = {str(k).lower(): str(v) for k, v in data.items()}
                else:
                    self.favorites = {}
        except (json.JSONDecodeError, OSError):
            self.favorites = {}

    def _save(self):
        """Persists the current favorites dictionary to the JSON file."""
        try:
            with open(self.filepath, "w", encoding="utf-8") as file:
                json.dump(self.favorites, file, indent=2)
        except OSError:
            pass

    def add(self, name: str, location: str) -> bool:
        """Adds a favorite. Returns True on success, False if duplicate."""
        key = name.strip().lower()
        if not key or key in self.favorites:
            return False
        self.favorites[key] = location.strip()
        self._save()
        return True

    def remove(self, name: str) -> bool:
        """Removes a favorite. Returns True on success, False if missing."""
        key = name.strip().lower()
        if key not in self.favorites:
            return False
        del self.favorites[key]
        self._save()
        return True

    def list_all(self) -> dict:
        """Returns a copy of all favorites."""
        return dict(self.favorites)

    def get_location(self, name: str):
        """Returns the location string for a given favorite name, or None."""
        return self.favorites.get(name.strip().lower())
        