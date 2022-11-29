from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="StopTimeEvent")


@attr.s(auto_attribs=True)
class StopTimeEvent:
    """
    Example:
        {'delay': -441, 'time': 1559005659}

    Attributes:
        delay (Union[Unset, float]):
        time (Union[Unset, float]):
        uncertainty (Union[Unset, float]):
    """

    delay: Union[Unset, float] = UNSET
    time: Union[Unset, float] = UNSET
    uncertainty: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        delay = self.delay
        time = self.time
        uncertainty = self.uncertainty

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if delay is not UNSET:
            field_dict["delay"] = delay
        if time is not UNSET:
            field_dict["time"] = time
        if uncertainty is not UNSET:
            field_dict["uncertainty"] = uncertainty

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        delay = d.pop("delay", UNSET)

        time = d.pop("time", UNSET)

        uncertainty = d.pop("uncertainty", UNSET)

        stop_time_event = cls(
            delay=delay,
            time=time,
            uncertainty=uncertainty,
        )

        stop_time_event.additional_properties = d
        return stop_time_event

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
