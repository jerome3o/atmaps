from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.error_response import ErrorResponse
from ...models.single_entity_response import SingleEntityResponse
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/trips/{id}".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ErrorResponse, SingleEntityResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SingleEntityResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ErrorResponse, SingleEntityResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Client,
) -> Response[Union[ErrorResponse, SingleEntityResponse]]:
    """Trip by id

     Retrieves trip by it's id

    Args:
        id (str):

    Returns:
        Response[Union[ErrorResponse, SingleEntityResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    *,
    client: Client,
) -> Optional[Union[ErrorResponse, SingleEntityResponse]]:
    """Trip by id

     Retrieves trip by it's id

    Args:
        id (str):

    Returns:
        Response[Union[ErrorResponse, SingleEntityResponse]]
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Client,
) -> Response[Union[ErrorResponse, SingleEntityResponse]]:
    """Trip by id

     Retrieves trip by it's id

    Args:
        id (str):

    Returns:
        Response[Union[ErrorResponse, SingleEntityResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    *,
    client: Client,
) -> Optional[Union[ErrorResponse, SingleEntityResponse]]:
    """Trip by id

     Retrieves trip by it's id

    Args:
        id (str):

    Returns:
        Response[Union[ErrorResponse, SingleEntityResponse]]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
