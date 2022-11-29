from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ferry_position import FerryPosition


T = TypeVar("T", bound="FerryApiFrame")


@attr.s(auto_attribs=True)
class FerryApiFrame:
    """
    Attributes:
        status (Union[Unset, str]):  Example: OK.
        response (Union[Unset, List['FerryPosition']]):
    """

    status: Union[Unset, str] = UNSET
    response: Union[Unset, List["FerryPosition"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status
        response: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.response, Unset):
            response = []
            for response_item_data in self.response:
                response_item = response_item_data.to_dict()

                response.append(response_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if response is not UNSET:
            field_dict["response"] = response

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ferry_position import FerryPosition

        d = src_dict.copy()
        status = d.pop("status", UNSET)

        response = []
        _response = d.pop("response", UNSET)
        for response_item_data in _response or []:
            response_item = FerryPosition.from_dict(response_item_data)

            response.append(response_item)

        ferry_api_frame = cls(
            status=status,
            response=response,
        )

        ferry_api_frame.additional_properties = d
        return ferry_api_frame

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
