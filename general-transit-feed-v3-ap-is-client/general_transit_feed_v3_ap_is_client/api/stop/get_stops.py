from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.error_response import ErrorResponse
from ...models.multiple_entity_response import MultipleEntityResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    filterdate: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/stops".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["filter[date]"] = filterdate

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ErrorResponse, MultipleEntityResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = MultipleEntityResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ErrorResponse, MultipleEntityResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    filterdate: Union[Unset, None, str] = UNSET,
) -> Response[Union[ErrorResponse, MultipleEntityResponse]]:
    """Stops

     List of all stops for a specific date.  Defaults to the date of the request if the filter[date]
    parameter is not provided.

    Args:
        filterdate (Union[Unset, None, str]):

    Returns:
        Response[Union[ErrorResponse, MultipleEntityResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        filterdate=filterdate,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    filterdate: Union[Unset, None, str] = UNSET,
) -> Optional[Union[ErrorResponse, MultipleEntityResponse]]:
    """Stops

     List of all stops for a specific date.  Defaults to the date of the request if the filter[date]
    parameter is not provided.

    Args:
        filterdate (Union[Unset, None, str]):

    Returns:
        Response[Union[ErrorResponse, MultipleEntityResponse]]
    """

    return sync_detailed(
        client=client,
        filterdate=filterdate,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    filterdate: Union[Unset, None, str] = UNSET,
) -> Response[Union[ErrorResponse, MultipleEntityResponse]]:
    """Stops

     List of all stops for a specific date.  Defaults to the date of the request if the filter[date]
    parameter is not provided.

    Args:
        filterdate (Union[Unset, None, str]):

    Returns:
        Response[Union[ErrorResponse, MultipleEntityResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        filterdate=filterdate,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    filterdate: Union[Unset, None, str] = UNSET,
) -> Optional[Union[ErrorResponse, MultipleEntityResponse]]:
    """Stops

     List of all stops for a specific date.  Defaults to the date of the request if the filter[date]
    parameter is not provided.

    Args:
        filterdate (Union[Unset, None, str]):

    Returns:
        Response[Union[ErrorResponse, MultipleEntityResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
            filterdate=filterdate,
        )
    ).parsed
