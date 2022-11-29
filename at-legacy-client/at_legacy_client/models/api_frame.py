from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_frame_error import ApiFrameError
    from ..models.api_frame_response import ApiFrameResponse


T = TypeVar("T", bound="ApiFrame")


@attr.s(auto_attribs=True)
class ApiFrame:
    """
    Attributes:
        status (Union[Unset, str]):  Example: OK.
        response (Union[Unset, ApiFrameResponse]):
        error (Union[Unset, None, ApiFrameError]):
    """

    status: Union[Unset, str] = UNSET
    response: Union[Unset, "ApiFrameResponse"] = UNSET
    error: Union[Unset, None, "ApiFrameError"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status
        response: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.response, Unset):
            response = self.response.to_dict()

        error: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict() if self.error else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if response is not UNSET:
            field_dict["response"] = response
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_frame_error import ApiFrameError
        from ..models.api_frame_response import ApiFrameResponse

        d = src_dict.copy()
        status = d.pop("status", UNSET)

        _response = d.pop("response", UNSET)
        response: Union[Unset, ApiFrameResponse]
        if isinstance(_response, Unset):
            response = UNSET
        else:
            response = ApiFrameResponse.from_dict(_response)

        _error = d.pop("error", UNSET)
        error: Union[Unset, None, ApiFrameError]
        if _error is None:
            error = None
        elif isinstance(_error, Unset):
            error = UNSET
        else:
            error = ApiFrameError.from_dict(_error)

        api_frame = cls(
            status=status,
            response=response,
            error=error,
        )

        api_frame.additional_properties = d
        return api_frame

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
