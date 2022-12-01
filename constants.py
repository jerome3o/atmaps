import os

URL = os.environ.get("URL", "https://api.at.govt.nz/gtfs/v3")
LEGACY_URL = os.environ.get("LEGACY_URL", "https://api.at.govt.nz/realtime/legacy")
AT_TOKEN = os.environ.get("AT_TOKEN")
MAPBOX_TOKEN = os.environ.get("MAPBOX_TOKEN")
