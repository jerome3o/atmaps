import os

from at_client import AuthenticatedClient
from at_legacy_client import AuthenticatedClient as LegacyClient
from at_client.api.route import get_routes, get_routes_id
from at_client.api.stop import get_stops, get_stops_id, get_trips_id_stops
from at_client.api.trip import get_trips_id
from at_legacy_client.api.default import get_all

from constants import URL, LEGACY_URL, MAPBOX_TOKEN, AT_TOKEN

def get_client():
    return AuthenticatedClient(
        base_url=URL, 
        prefix="",
        token=AT_TOKEN,
        auth_header_name="Ocp-Apim-Subscription-Key",
    )

def get_legacy_client():
    return LegacyClient(
        base_url=LEGACY_URL, 
        prefix="",
        token=_at_token,
        auth_header_name="Ocp-Apim-Subscription-Key",
    )
def main():
    c = get_client()
    lc = get_legacy_client()
    routes = get_routes.sync(client=c).to_dict()["data"]
    stops = get_stops.sync(client=c).to_dict()["data"]
    legacy_data = get_all.sync(client=lc).to_dict()["response"]
    return routes, stops, legacy_data


if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO)
    main()

