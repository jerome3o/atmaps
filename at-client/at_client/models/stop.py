from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Stop")


@attr.s(auto_attribs=True)
class Stop:
    """
    Attributes:
        stop_id (Union[Unset, str]):
        stop_code (Union[Unset, None, str]):
        stop_name (Union[Unset, None, str]):
        stop_desc (Union[Unset, None, str]):
        stop_lat (Union[Unset, None, float]):
        stop_lon (Union[Unset, None, float]):
        zone_id (Union[Unset, None, str]):
        stop_url (Union[Unset, None, str]):
        location_type (Union[Unset, None, int]):
        parent_station (Union[Unset, None, str]):
        stop_timezone (Union[Unset, None, str]):
        wheelchair_boarding (Union[Unset, None, int]):
        platform_code (Union[Unset, None, str]):
    """

    stop_id: Union[Unset, str] = UNSET
    stop_code: Union[Unset, None, str] = UNSET
    stop_name: Union[Unset, None, str] = UNSET
    stop_desc: Union[Unset, None, str] = UNSET
    stop_lat: Union[Unset, None, float] = UNSET
    stop_lon: Union[Unset, None, float] = UNSET
    zone_id: Union[Unset, None, str] = UNSET
    stop_url: Union[Unset, None, str] = UNSET
    location_type: Union[Unset, None, int] = UNSET
    parent_station: Union[Unset, None, str] = UNSET
    stop_timezone: Union[Unset, None, str] = UNSET
    wheelchair_boarding: Union[Unset, None, int] = UNSET
    platform_code: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        stop_id = self.stop_id
        stop_code = self.stop_code
        stop_name = self.stop_name
        stop_desc = self.stop_desc
        stop_lat = self.stop_lat
        stop_lon = self.stop_lon
        zone_id = self.zone_id
        stop_url = self.stop_url
        location_type = self.location_type
        parent_station = self.parent_station
        stop_timezone = self.stop_timezone
        wheelchair_boarding = self.wheelchair_boarding
        platform_code = self.platform_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stop_id is not UNSET:
            field_dict["stop_id"] = stop_id
        if stop_code is not UNSET:
            field_dict["stop_code"] = stop_code
        if stop_name is not UNSET:
            field_dict["stop_name"] = stop_name
        if stop_desc is not UNSET:
            field_dict["stop_desc"] = stop_desc
        if stop_lat is not UNSET:
            field_dict["stop_lat"] = stop_lat
        if stop_lon is not UNSET:
            field_dict["stop_lon"] = stop_lon
        if zone_id is not UNSET:
            field_dict["zone_id"] = zone_id
        if stop_url is not UNSET:
            field_dict["stop_url"] = stop_url
        if location_type is not UNSET:
            field_dict["location_type"] = location_type
        if parent_station is not UNSET:
            field_dict["parent_station"] = parent_station
        if stop_timezone is not UNSET:
            field_dict["stop_timezone"] = stop_timezone
        if wheelchair_boarding is not UNSET:
            field_dict["wheelchair_boarding"] = wheelchair_boarding
        if platform_code is not UNSET:
            field_dict["platform_code"] = platform_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        stop_id = d.pop("stop_id", UNSET)

        stop_code = d.pop("stop_code", UNSET)

        stop_name = d.pop("stop_name", UNSET)

        stop_desc = d.pop("stop_desc", UNSET)

        stop_lat = d.pop("stop_lat", UNSET)

        stop_lon = d.pop("stop_lon", UNSET)

        zone_id = d.pop("zone_id", UNSET)

        stop_url = d.pop("stop_url", UNSET)

        location_type = d.pop("location_type", UNSET)

        parent_station = d.pop("parent_station", UNSET)

        stop_timezone = d.pop("stop_timezone", UNSET)

        wheelchair_boarding = d.pop("wheelchair_boarding", UNSET)

        platform_code = d.pop("platform_code", UNSET)

        stop = cls(
            stop_id=stop_id,
            stop_code=stop_code,
            stop_name=stop_name,
            stop_desc=stop_desc,
            stop_lat=stop_lat,
            stop_lon=stop_lon,
            zone_id=zone_id,
            stop_url=stop_url,
            location_type=location_type,
            parent_station=parent_station,
            stop_timezone=stop_timezone,
            wheelchair_boarding=wheelchair_boarding,
            platform_code=platform_code,
        )

        stop.additional_properties = d
        return stop

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
