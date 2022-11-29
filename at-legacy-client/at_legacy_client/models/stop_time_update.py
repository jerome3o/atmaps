from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.stop_schedule_relationship import StopScheduleRelationship
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.stop_time_event import StopTimeEvent


T = TypeVar("T", bound="StopTimeUpdate")


@attr.s(auto_attribs=True)
class StopTimeUpdate:
    """
    Attributes:
        stop_sequence (Union[Unset, float]):  Example: 1.
        stop_id (Union[Unset, str]):  Example: 1-6955.
        arrival (Union[Unset, StopTimeEvent]):  Example: {'delay': -441, 'time': 1559005659}.
        departure (Union[Unset, StopTimeEvent]):  Example: {'delay': -441, 'time': 1559005659}.
        schedule_relationship (Union[Unset, StopScheduleRelationship]):
    """

    stop_sequence: Union[Unset, float] = UNSET
    stop_id: Union[Unset, str] = UNSET
    arrival: Union[Unset, "StopTimeEvent"] = UNSET
    departure: Union[Unset, "StopTimeEvent"] = UNSET
    schedule_relationship: Union[Unset, StopScheduleRelationship] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        stop_sequence = self.stop_sequence
        stop_id = self.stop_id
        arrival: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.arrival, Unset):
            arrival = self.arrival.to_dict()

        departure: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.departure, Unset):
            departure = self.departure.to_dict()

        schedule_relationship: Union[Unset, int] = UNSET
        if not isinstance(self.schedule_relationship, Unset):
            schedule_relationship = self.schedule_relationship.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stop_sequence is not UNSET:
            field_dict["stop_sequence"] = stop_sequence
        if stop_id is not UNSET:
            field_dict["stop_id"] = stop_id
        if arrival is not UNSET:
            field_dict["arrival"] = arrival
        if departure is not UNSET:
            field_dict["departure"] = departure
        if schedule_relationship is not UNSET:
            field_dict["schedule_relationship"] = schedule_relationship

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.stop_time_event import StopTimeEvent

        d = src_dict.copy()
        stop_sequence = d.pop("stop_sequence", UNSET)

        stop_id = d.pop("stop_id", UNSET)

        _arrival = d.pop("arrival", UNSET)
        arrival: Union[Unset, StopTimeEvent]
        if isinstance(_arrival, Unset):
            arrival = UNSET
        else:
            arrival = StopTimeEvent.from_dict(_arrival)

        _departure = d.pop("departure", UNSET)
        departure: Union[Unset, StopTimeEvent]
        if isinstance(_departure, Unset):
            departure = UNSET
        else:
            departure = StopTimeEvent.from_dict(_departure)

        _schedule_relationship = d.pop("schedule_relationship", UNSET)
        schedule_relationship: Union[Unset, StopScheduleRelationship]
        if isinstance(_schedule_relationship, Unset):
            schedule_relationship = UNSET
        else:
            schedule_relationship = StopScheduleRelationship(_schedule_relationship)

        stop_time_update = cls(
            stop_sequence=stop_sequence,
            stop_id=stop_id,
            arrival=arrival,
            departure=departure,
            schedule_relationship=schedule_relationship,
        )

        stop_time_update.additional_properties = d
        return stop_time_update

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
