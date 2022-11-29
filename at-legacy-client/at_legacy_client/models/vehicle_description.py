from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="VehicleDescription")


@attr.s(auto_attribs=True)
class VehicleDescription:
    """
    Example:
        {'id': '512000545', 'label': 'DALDY', 'license_plate': 'ZMZ7645'}

    Attributes:
        id (Union[Unset, str]):
        label (Union[Unset, str]):
        license_plate (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    license_plate: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        label = self.label
        license_plate = self.license_plate

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if label is not UNSET:
            field_dict["label"] = label
        if license_plate is not UNSET:
            field_dict["license_plate"] = license_plate

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        label = d.pop("label", UNSET)

        license_plate = d.pop("license_plate", UNSET)

        vehicle_description = cls(
            id=id,
            label=label,
            license_plate=license_plate,
        )

        vehicle_description.additional_properties = d
        return vehicle_description

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
