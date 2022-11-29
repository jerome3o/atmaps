from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Position")


@attr.s(auto_attribs=True)
class Position:
    """
    Example:
        {'latitude': -36.84022, 'longitude': 174.776726666667, 'speed': 0.0514444}

    Attributes:
        latitude (Union[Unset, float]):
        longitude (Union[Unset, float]):
        bearing (Union[Unset, float]):
        odometer (Union[Unset, float]):
        speed (Union[Unset, float]):
    """

    latitude: Union[Unset, float] = UNSET
    longitude: Union[Unset, float] = UNSET
    bearing: Union[Unset, float] = UNSET
    odometer: Union[Unset, float] = UNSET
    speed: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        latitude = self.latitude
        longitude = self.longitude
        bearing = self.bearing
        odometer = self.odometer
        speed = self.speed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if bearing is not UNSET:
            field_dict["bearing"] = bearing
        if odometer is not UNSET:
            field_dict["odometer"] = odometer
        if speed is not UNSET:
            field_dict["speed"] = speed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        bearing = d.pop("bearing", UNSET)

        odometer = d.pop("odometer", UNSET)

        speed = d.pop("speed", UNSET)

        position = cls(
            latitude=latitude,
            longitude=longitude,
            bearing=bearing,
            odometer=odometer,
            speed=speed,
        )

        position.additional_properties = d
        return position

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
