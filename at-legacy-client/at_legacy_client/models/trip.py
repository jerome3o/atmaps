from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.trip_schedule_relationship import TripScheduleRelationship
from ..types import UNSET, Unset

T = TypeVar("T", bound="Trip")


@attr.s(auto_attribs=True)
class Trip:
    """
    Example:
        {'trip_id': '1033-32504-52500-2-d16dbfbd', 'route_id': '325-221', 'direction_id': 0, 'start_time': '13:54:00',
            'start_date': '20190528', 'schedule_relationship': 0}

    Attributes:
        trip_id (Union[Unset, str]):
        route_id (Union[Unset, str]):
        direction_id (Union[Unset, float]):
        start_time (Union[Unset, str]):
        start_date (Union[Unset, str]):
        schedule_relationship (Union[Unset, TripScheduleRelationship]):
    """

    trip_id: Union[Unset, str] = UNSET
    route_id: Union[Unset, str] = UNSET
    direction_id: Union[Unset, float] = UNSET
    start_time: Union[Unset, str] = UNSET
    start_date: Union[Unset, str] = UNSET
    schedule_relationship: Union[Unset, TripScheduleRelationship] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        trip_id = self.trip_id
        route_id = self.route_id
        direction_id = self.direction_id
        start_time = self.start_time
        start_date = self.start_date
        schedule_relationship: Union[Unset, int] = UNSET
        if not isinstance(self.schedule_relationship, Unset):
            schedule_relationship = self.schedule_relationship.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if trip_id is not UNSET:
            field_dict["trip_id"] = trip_id
        if route_id is not UNSET:
            field_dict["route_id"] = route_id
        if direction_id is not UNSET:
            field_dict["direction_id"] = direction_id
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if schedule_relationship is not UNSET:
            field_dict["schedule_relationship"] = schedule_relationship

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        trip_id = d.pop("trip_id", UNSET)

        route_id = d.pop("route_id", UNSET)

        direction_id = d.pop("direction_id", UNSET)

        start_time = d.pop("start_time", UNSET)

        start_date = d.pop("start_date", UNSET)

        _schedule_relationship = d.pop("schedule_relationship", UNSET)
        schedule_relationship: Union[Unset, TripScheduleRelationship]
        if isinstance(_schedule_relationship, Unset):
            schedule_relationship = UNSET
        else:
            schedule_relationship = TripScheduleRelationship(_schedule_relationship)

        trip = cls(
            trip_id=trip_id,
            route_id=route_id,
            direction_id=direction_id,
            start_time=start_time,
            start_date=start_date,
            schedule_relationship=schedule_relationship,
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
