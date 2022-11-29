from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="FeedHeader")


@attr.s(auto_attribs=True)
class FeedHeader:
    """
    Attributes:
        gtfs_realtime_version (Union[Unset, str]):  Example: 1.0.
        incrementality (Union[Unset, float]):  Example: 1.
        timestamp (Union[Unset, float]):  Example: 259982000.
    """

    gtfs_realtime_version: Union[Unset, str] = UNSET
    incrementality: Union[Unset, float] = UNSET
    timestamp: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        gtfs_realtime_version = self.gtfs_realtime_version
        incrementality = self.incrementality
        timestamp = self.timestamp

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gtfs_realtime_version is not UNSET:
            field_dict["gtfs_realtime_version"] = gtfs_realtime_version
        if incrementality is not UNSET:
            field_dict["incrementality"] = incrementality
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        gtfs_realtime_version = d.pop("gtfs_realtime_version", UNSET)

        incrementality = d.pop("incrementality", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        feed_header = cls(
            gtfs_realtime_version=gtfs_realtime_version,
            incrementality=incrementality,
            timestamp=timestamp,
        )

        feed_header.additional_properties = d
        return feed_header

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
