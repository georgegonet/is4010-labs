"""JSON contact book persistence module."""

import json
from pathlib import Path


def save_contacts_to_json(contacts, filename):
    """Write the contacts list to filename as indented JSON."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(contacts, f, indent=4)


def load_contacts_from_json(filename):
    """Return contacts from filename, or an empty list if it does not exist."""
    path = Path(filename)
    if not path.is_file():
        return []

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)