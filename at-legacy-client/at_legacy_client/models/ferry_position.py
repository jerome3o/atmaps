from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="FerryPosition")


@attr.s(auto_attribs=True)
class FerryPosition:
    """
    Attributes:
        mmsi (Union[Unset, float]):
        callsign (Union[Unset, None, str]):
        eta (Union[Unset, None, str]):
        lat (Union[Unset, None, str]):
        lng (Union[Unset, None, str]):
        operator (Union[Unset, str]):
        timestamp (Union[Unset, str]):
        vessel (Union[Unset, None, str]):
    """

    mmsi: Union[Unset, float] = UNSET
    callsign: Union[Unset, None, str] = UNSET
    eta: Union[Unset, None, str] = UNSET
    lat: Union[Unset, None, str] = UNSET
    lng: Union[Unset, None, str] = UNSET
    operator: Union[Unset, str] = UNSET
    timestamp: Union[Unset, str] = UNSET
    vessel: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mmsi = self.mmsi
        callsign = self.callsign
        eta = self.eta
        lat = self.lat
        lng = self.lng
        operator = self.operator
        timestamp = self.timestamp
        vessel = self.vessel

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mmsi is not UNSET:
            field_dict["mmsi"] = mmsi
        if callsign is not UNSET:
            field_dict["callsign"] = callsign
        if eta is not UNSET:
            field_dict["eta"] = eta
        if lat is not UNSET:
            field_dict["lat"] = lat
        if lng is not UNSET:
            field_dict["lng"] = lng
        if operator is not UNSET:
            field_dict["operator"] = operator
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if vessel is not UNSET:
            field_dict["vessel"] = vessel

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mmsi = d.pop("mmsi", UNSET)

        callsign = d.pop("callsign", UNSET)

        eta = d.pop("eta", UNSET)

        lat = d.pop("lat", UNSET)

        lng = d.pop("lng", UNSET)

        operator = d.pop("operator", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        vessel = d.pop("vessel", UNSET)

        ferry_position = cls(
            mmsi=mmsi,
            callsign=callsign,
            eta=eta,
            lat=lat,
            lng=lng,
            operator=operator,
            timestamp=timestamp,
            vessel=vessel,
        )

        ferry_position.additional_properties = d
        return ferry_position

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
