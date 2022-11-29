from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.trip import Trip


T = TypeVar("T", bound="EntitySelector")


@attr.s(auto_attribs=True)
class EntitySelector:
    """
    Example:
        {'route_id': '325-221'}

    Attributes:
        agency_id (Union[Unset, str]):
        route_id (Union[Unset, str]):
        route_type (Union[Unset, float]):
        trip (Union[Unset, Trip]):  Example: {'trip_id': '1033-32504-52500-2-d16dbfbd', 'route_id': '325-221',
            'direction_id': 0, 'start_time': '13:54:00', 'start_date': '20190528', 'schedule_relationship': 0}.
        stop_id (Union[Unset, str]):
    """

    agency_id: Union[Unset, str] = UNSET
    route_id: Union[Unset, str] = UNSET
    route_type: Union[Unset, float] = UNSET
    trip: Union[Unset, "Trip"] = UNSET
    stop_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        agency_id = self.agency_id
        route_id = self.route_id
        route_type = self.route_type
        trip: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.trip, Unset):
            trip = self.trip.to_dict()

        stop_id = self.stop_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if agency_id is not UNSET:
            field_dict["agency_id"] = agency_id
        if route_id is not UNSET:
            field_dict["route_id"] = route_id
        if route_type is not UNSET:
            field_dict["route_type"] = route_type
        if trip is not UNSET:
            field_dict["trip"] = trip
        if stop_id is not UNSET:
            field_dict["stop_id"] = stop_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.trip import Trip

        d = src_dict.copy()
        agency_id = d.pop("agency_id", UNSET)

        route_id = d.pop("route_id", UNSET)

        route_type = d.pop("route_type", UNSET)

        _trip = d.pop("trip", UNSET)
        trip: Union[Unset, Trip]
        if isinstance(_trip, Unset):
            trip = UNSET
        else:
            trip = Trip.from_dict(_trip)

        stop_id = d.pop("stop_id", UNSET)

        entity_selector = cls(
            agency_id=agency_id,
            route_id=route_id,
            route_type=route_type,
            trip=trip,
            stop_id=stop_id,
        )

        entity_selector.additional_properties = d
        return entity_selector

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
