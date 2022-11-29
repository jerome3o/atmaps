import os

from at_client import AuthenticatedClient
from at_client.api.route import get_routes, get_routes_id
from at_client.api.stop import get_stops, get_stops_id, get_trips_id_stops
from at_client.api.trip import get_trips_id

_url = os.environ.get("URL", "https://api.at.govt.nz/gtfs/v3")
_at_token = os.environ.get("AT_TOKEN")
_mapbox_token = os.environ.get("MAPBOX_TOKEN")

def get_client():
    return AuthenticatedClient(
        base_url=_url, 
        prefix="",
        token=_at_token,
        auth_header_name="Ocp-Apim-Subscription-Key",
    )

def main():
    c = get_client()
    routes = get_routes.sync(client=c).to_dict()
    stops = get_stops.sync(client=c).to_dict()
    stop = stops[-1]
    return route


if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO)
    main()

