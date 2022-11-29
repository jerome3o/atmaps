from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.api_frame import ApiFrame
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    callback: Union[Unset, None, str] = UNSET,
    tripid: Union[Unset, None, str] = UNSET,
    vehicleid: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/tripupdates".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["callback"] = callback

    params["tripid"] = tripid

    params["vehicleid"] = vehicleid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ApiFrame]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiFrame.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(Any, None)
        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, ApiFrame]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    callback: Union[Unset, None, str] = UNSET,
    tripid: Union[Unset, None, str] = UNSET,
    vehicleid: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, ApiFrame]]:
    """Trip Updates

     Returns realtime GTFS trip updates for the active trips in the Auckland region, updated at least
    every 30s. Protobuf supported if the Accept header is set to application/x-protobuf.

    Args:
        callback (Union[Unset, None, str]):
        tripid (Union[Unset, None, str]):
        vehicleid (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, ApiFrame]]
    """

    kwargs = _get_kwargs(
        client=client,
        callback=callback,
        tripid=tripid,
        vehicleid=vehicleid,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    callback: Union[Unset, None, str] = UNSET,
    tripid: Union[Unset, None, str] = UNSET,
    vehicleid: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, ApiFrame]]:
    """Trip Updates

     Returns realtime GTFS trip updates for the active trips in the Auckland region, updated at least
    every 30s. Protobuf supported if the Accept header is set to application/x-protobuf.

    Args:
        callback (Union[Unset, None, str]):
        tripid (Union[Unset, None, str]):
        vehicleid (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, ApiFrame]]
    """

    return sync_detailed(
        client=client,
        callback=callback,
        tripid=tripid,
        vehicleid=vehicleid,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    callback: Union[Unset, None, str] = UNSET,
    tripid: Union[Unset, None, str] = UNSET,
    vehicleid: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, ApiFrame]]:
    """Trip Updates

     Returns realtime GTFS trip updates for the active trips in the Auckland region, updated at least
    every 30s. Protobuf supported if the Accept header is set to application/x-protobuf.

    Args:
        callback (Union[Unset, None, str]):
        tripid (Union[Unset, None, str]):
        vehicleid (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, ApiFrame]]
    """

    kwargs = _get_kwargs(
        client=client,
        callback=callback,
        tripid=tripid,
        vehicleid=vehicleid,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    callback: Union[Unset, None, str] = UNSET,
    tripid: Union[Unset, None, str] = UNSET,
    vehicleid: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, ApiFrame]]:
    """Trip Updates

     Returns realtime GTFS trip updates for the active trips in the Auckland region, updated at least
    every 30s. Protobuf supported if the Accept header is set to application/x-protobuf.

    Args:
        callback (Union[Unset, None, str]):
        tripid (Union[Unset, None, str]):
        vehicleid (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, ApiFrame]]
    """

    return (
        await asyncio_detailed(
            client=client,
            callback=callback,
            tripid=tripid,
            vehicleid=vehicleid,
        )
    ).parsed
