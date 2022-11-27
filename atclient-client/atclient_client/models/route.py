from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Route")


@attr.s(auto_attribs=True)
class Route:
    """
    Attributes:
        route_id (Union[Unset, str]):
        agency_id (Union[Unset, None, str]):
        route_short_name (Union[Unset, None, str]):
        route_long_name (Union[Unset, None, str]):
        route_desc (Union[Unset, None, str]):
        route_type (Union[Unset, int]):
        route_url (Union[Unset, None, str]):
        route_color (Union[Unset, None, str]):
        route_text_color (Union[Unset, None, str]):
        route_sort_order (Union[Unset, None, int]):
    """

    route_id: Union[Unset, str] = UNSET
    agency_id: Union[Unset, None, str] = UNSET
    route_short_name: Union[Unset, None, str] = UNSET
    route_long_name: Union[Unset, None, str] = UNSET
    route_desc: Union[Unset, None, str] = UNSET
    route_type: Union[Unset, int] = UNSET
    route_url: Union[Unset, None, str] = UNSET
    route_color: Union[Unset, None, str] = UNSET
    route_text_color: Union[Unset, None, str] = UNSET
    route_sort_order: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        route_id = self.route_id
        agency_id = self.agency_id
        route_short_name = self.route_short_name
        route_long_name = self.route_long_name
        route_desc = self.route_desc
        route_type = self.route_type
        route_url = self.route_url
        route_color = self.route_color
        route_text_color = self.route_text_color
        route_sort_order = self.route_sort_order

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if route_id is not UNSET:
            field_dict["route_id"] = route_id
        if agency_id is not UNSET:
            field_dict["agency_id"] = agency_id
        if route_short_name is not UNSET:
            field_dict["route_short_name"] = route_short_name
        if route_long_name is not UNSET:
            field_dict["route_long_name"] = route_long_name
        if route_desc is not UNSET:
            field_dict["route_desc"] = route_desc
        if route_type is not UNSET:
            field_dict["route_type"] = route_type
        if route_url is not UNSET:
            field_dict["route_url"] = route_url
        if route_color is not UNSET:
            field_dict["route_color"] = route_color
        if route_text_color is not UNSET:
            field_dict["route_text_color"] = route_text_color
        if route_sort_order is not UNSET:
            field_dict["route_sort_order"] = route_sort_order

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        route_id = d.pop("route_id", UNSET)

        agency_id = d.pop("agency_id", UNSET)

        route_short_name = d.pop("route_short_name", UNSET)

        route_long_name = d.pop("route_long_name", UNSET)

        route_desc = d.pop("route_desc", UNSET)

        route_type = d.pop("route_type", UNSET)

        route_url = d.pop("route_url", UNSET)

        route_color = d.pop("route_color", UNSET)

        route_text_color = d.pop("route_text_color", UNSET)

        route_sort_order = d.pop("route_sort_order", UNSET)

        route = cls(
            route_id=route_id,
            agency_id=agency_id,
            route_short_name=route_short_name,
            route_long_name=route_long_name,
            route_desc=route_desc,
            route_type=route_type,
            route_url=route_url,
            route_color=route_color,
            route_text_color=route_text_color,
            route_sort_order=route_sort_order,
        )

        route.additional_properties = d
        return route

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
