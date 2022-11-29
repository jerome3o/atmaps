from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vehicle_position_vehicle import VehiclePositionVehicle


T = TypeVar("T", bound="VehiclePosition")


@attr.s(auto_attribs=True)
class VehiclePosition:
    """
    Attributes:
        id (Union[Unset, str]):  Example: 259982000.
        is_deleted (Union[Unset, bool]):
        vehicle (Union[Unset, VehiclePositionVehicle]):
    """

    id: Union[Unset, str] = UNSET
    is_deleted: Union[Unset, bool] = UNSET
    vehicle: Union[Unset, "VehiclePositionVehicle"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        is_deleted = self.is_deleted
        vehicle: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.vehicle, Unset):
            vehicle = self.vehicle.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if is_deleted is not UNSET:
            field_dict["is_deleted"] = is_deleted
        if vehicle is not UNSET:
            field_dict["vehicle"] = vehicle

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.vehicle_position_vehicle import VehiclePositionVehicle

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        is_deleted = d.pop("is_deleted", UNSET)

        _vehicle = d.pop("vehicle", UNSET)
        vehicle: Union[Unset, VehiclePositionVehicle]
        if isinstance(_vehicle, Unset):
            vehicle = UNSET
        else:
            vehicle = VehiclePositionVehicle.from_dict(_vehicle)

        vehicle_position = cls(
            id=id,
            is_deleted=is_deleted,
            vehicle=vehicle,
        )

        vehicle_position.additional_properties = d
        return vehicle_position

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
