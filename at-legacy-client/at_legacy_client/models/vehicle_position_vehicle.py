from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.congestion_level import CongestionLevel
from ..models.occupancy_status import OccupancyStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.position import Position
    from ..models.trip import Trip
    from ..models.vehicle_description import VehicleDescription


T = TypeVar("T", bound="VehiclePositionVehicle")


@attr.s(auto_attribs=True)
class VehiclePositionVehicle:
    """
    Attributes:
        trip (Union[Unset, Trip]):  Example: {'trip_id': '1033-32504-52500-2-d16dbfbd', 'route_id': '325-221',
            'direction_id': 0, 'start_time': '13:54:00', 'start_date': '20190528', 'schedule_relationship': 0}.
        vehicle (Union[Unset, VehicleDescription]):  Example: {'id': '512000545', 'label': 'DALDY', 'license_plate':
            'ZMZ7645'}.
        position (Union[Unset, Position]):  Example: {'latitude': -36.84022, 'longitude': 174.776726666667, 'speed':
            0.0514444}.
        timestamp (Union[Unset, float]):  Example: 1559011152.
        congestion_level (Union[Unset, CongestionLevel]):  Example: 2.
        occupancy_status (Union[Unset, OccupancyStatus]):  Example: 1.
    """

    trip: Union[Unset, "Trip"] = UNSET
    vehicle: Union[Unset, "VehicleDescription"] = UNSET
    position: Union[Unset, "Position"] = UNSET
    timestamp: Union[Unset, float] = UNSET
    congestion_level: Union[Unset, CongestionLevel] = UNSET
    occupancy_status: Union[Unset, OccupancyStatus] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        trip: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.trip, Unset):
            trip = self.trip.to_dict()

        vehicle: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.vehicle, Unset):
            vehicle = self.vehicle.to_dict()

        position: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.position, Unset):
            position = self.position.to_dict()

        timestamp = self.timestamp
        congestion_level: Union[Unset, int] = UNSET
        if not isinstance(self.congestion_level, Unset):
            congestion_level = self.congestion_level.value

        occupancy_status: Union[Unset, int] = UNSET
        if not isinstance(self.occupancy_status, Unset):
            occupancy_status = self.occupancy_status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if trip is not UNSET:
            field_dict["trip"] = trip
        if vehicle is not UNSET:
            field_dict["vehicle"] = vehicle
        if position is not UNSET:
            field_dict["position"] = position
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if congestion_level is not UNSET:
            field_dict["congestion_level"] = congestion_level
        if occupancy_status is not UNSET:
            field_dict["occupancy_status"] = occupancy_status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.position import Position
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

        _position = d.pop("position", UNSET)
        position: Union[Unset, Position]
        if isinstance(_position, Unset):
            position = UNSET
        else:
            position = Position.from_dict(_position)

        timestamp = d.pop("timestamp", UNSET)

        _congestion_level = d.pop("congestion_level", UNSET)
        congestion_level: Union[Unset, CongestionLevel]
        if isinstance(_congestion_level, Unset):
            congestion_level = UNSET
        else:
            congestion_level = CongestionLevel(_congestion_level)

        _occupancy_status = d.pop("occupancy_status", UNSET)
        occupancy_status: Union[Unset, OccupancyStatus]
        if isinstance(_occupancy_status, Unset):
            occupancy_status = UNSET
        else:
            occupancy_status = OccupancyStatus(_occupancy_status)

        vehicle_position_vehicle = cls(
            trip=trip,
            vehicle=vehicle,
            position=position,
            timestamp=timestamp,
            congestion_level=congestion_level,
            occupancy_status=occupancy_status,
        )

        vehicle_position_vehicle.additional_properties = d
        return vehicle_position_vehicle

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
