from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Trip")


@attr.s(auto_attribs=True)
class Trip:
    """
    Attributes:
        route_id (Union[Unset, str]):
        service_id (Union[Unset, str]):
        trip_id (Union[Unset, str]):
        trip_headsign (Union[Unset, None, str]):
        trip_short_name (Union[Unset, None, str]):
        direction_id (Union[Unset, None, int]):
        block_id (Union[Unset, None, str]):
        shape_id (Union[Unset, None, str]):
        wheelchair_accessible (Union[Unset, None, int]):
        bikes_allowed (Union[Unset, None, int]):
    """

    route_id: Union[Unset, str] = UNSET
    service_id: Union[Unset, str] = UNSET
    trip_id: Union[Unset, str] = UNSET
    trip_headsign: Union[Unset, None, str] = UNSET
    trip_short_name: Union[Unset, None, str] = UNSET
    direction_id: Union[Unset, None, int] = UNSET
    block_id: Union[Unset, None, str] = UNSET
    shape_id: Union[Unset, None, str] = UNSET
    wheelchair_accessible: Union[Unset, None, int] = UNSET
    bikes_allowed: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        route_id = self.route_id
        service_id = self.service_id
        trip_id = self.trip_id
        trip_headsign = self.trip_headsign
        trip_short_name = self.trip_short_name
        direction_id = self.direction_id
        block_id = self.block_id
        shape_id = self.shape_id
        wheelchair_accessible = self.wheelchair_accessible
        bikes_allowed = self.bikes_allowed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if route_id is not UNSET:
            field_dict["route_id"] = route_id
        if service_id is not UNSET:
            field_dict["service_id"] = service_id
        if trip_id is not UNSET:
            field_dict["trip_id"] = trip_id
        if trip_headsign is not UNSET:
            field_dict["trip_headsign"] = trip_headsign
        if trip_short_name is not UNSET:
            field_dict["trip_short_name"] = trip_short_name
        if direction_id is not UNSET:
            field_dict["direction_id"] = direction_id
        if block_id is not UNSET:
            field_dict["block_id"] = block_id
        if shape_id is not UNSET:
            field_dict["shape_id"] = shape_id
        if wheelchair_accessible is not UNSET:
            field_dict["wheelchair_accessible"] = wheelchair_accessible
        if bikes_allowed is not UNSET:
            field_dict["bikes_allowed"] = bikes_allowed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        route_id = d.pop("route_id", UNSET)

        service_id = d.pop("service_id", UNSET)

        trip_id = d.pop("trip_id", UNSET)

        trip_headsign = d.pop("trip_headsign", UNSET)

        trip_short_name = d.pop("trip_short_name", UNSET)

        direction_id = d.pop("direction_id", UNSET)

        block_id = d.pop("block_id", UNSET)

        shape_id = d.pop("shape_id", UNSET)

        wheelchair_accessible = d.pop("wheelchair_accessible", UNSET)

        bikes_allowed = d.pop("bikes_allowed", UNSET)

        trip = cls(
            route_id=route_id,
            service_id=service_id,
            trip_id=trip_id,
            trip_headsign=trip_headsign,
            trip_short_name=trip_short_name,
            direction_id=direction_id,
            block_id=block_id,
            shape_id=shape_id,
            wheelchair_accessible=wheelchair_accessible,
            bikes_allowed=bikes_allowed,
        )

        trip.additional_properties = d
        return trip

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
