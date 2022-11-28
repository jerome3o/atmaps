import os

from at_client import AuthenticatedClient
from at_client.api.route import get_routes

_url = os.environ.get("URL", "https://api.at.govt.nz/gtfs/v3")
_token = os.environ.get("TOKEN")



def main():
    c = AuthenticatedClient(
            base_url=_url, 
            prefix="",
            token=_token,
            auth_header_name="Ocp-Apim-Subscription-Key",
    )
    print(get_routes.sync_detailed(client=c))


if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO)
    main()

