from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.stop_time_update import StopTimeUpdate
    from ..models.trip import Trip
    from ..models.vehicle_description import VehicleDescription


T = TypeVar("T", bound="TripUpdateTripUpdate")


@attr.s(auto_attribs=True)
class TripUpdateTripUpdate:
    """
    Attributes:
        trip (Union[Unset, Trip]):  Example: {'trip_id': '1033-32504-52500-2-d16dbfbd', 'route_id': '325-221',
            'direction_id': 0, 'start_time': '13:54:00', 'start_date': '20190528', 'schedule_relationship': 0}.
        vehicle (Union[Unset, VehicleDescription]):  Example: {'id': '512000545', 'label': 'DALDY', 'license_plate':
            'ZMZ7645'}.
        stop_time_update (Union[Unset, List['StopTimeUpdate']]):
        timestamp (Union[Unset, float]):  Example: 1558997153.
        delay (Union[Unset, float]):  Example: -67.
    """

    trip: Union[Unset, "Trip"] = UNSET
    vehicle: Union[Unset, "VehicleDescription"] = UNSET
    stop_time_update: Union[Unset, List["StopTimeUpdate"]] = UNSET
    timestamp: Union[Unset, float] = UNSET
    delay: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        trip: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.trip, Unset):
            trip = self.trip.to_dict()

        vehicle: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.vehicle, Unset):
            vehicle = self.vehicle.to_dict()

        stop_time_update: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.stop_time_update, Unset):
            stop_time_update = []
            for stop_time_update_item_data in self.stop_time_update:
                stop_time_update_item = stop_time_update_item_data.to_dict()

                stop_time_update.append(stop_time_update_item)

        timestamp = self.timestamp
        delay = self.delay

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if trip is not UNSET:
            field_dict["trip"] = trip
        if vehicle is not UNSET:
            field_dict["vehicle"] = vehicle
        if stop_time_update is not UNSET:
            field_dict["stop_time_update"] = stop_time_update
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if delay is not UNSET:
            field_dict["delay"] = delay

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.stop_time_update import StopTimeUpdate
        from ..models.trip import Trip
        from ..models.vehicle_description import VehicleDescription

        d = src_dict.copy()
        _trip = d.pop("trip", UNSET)
        trip: Union[Unset, Trip]
        if isinstance(_trip, Unset):
            trip = UNSET
        else:
            trip = Trip.from_dict(_trip)

        _vehicle = d.pop("vehicle", UNSET)
        vehicle: Union[Unset, VehicleDescription]
        if isinstance(_vehicle, Unset):
            vehicle = UNSET
        else:
            vehicle = VehicleDescription.from_dict(_vehicle)

        stop_time_update = []
        _stop_time_update = d.pop("stop_time_update", UNSET)
        for stop_time_update_item_data in _stop_time_update or []:
            stop_time_update_item = StopTimeUpdate.from_dict(stop_time_update_item_data)

            stop_time_update.append(stop_time_update_item)

        timestamp = d.pop("timestamp", UNSET)

        delay = d.pop("delay", UNSET)

        trip_update_trip_update = cls(
            trip=trip,
            vehicle=vehicle,
            stop_time_update=stop_time_update,
            timestamp=timestamp,
            delay=delay,
        )

        trip_update_trip_update.additional_properties = d
        return trip_update_trip_update

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
