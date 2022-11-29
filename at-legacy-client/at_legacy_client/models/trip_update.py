from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.trip_update_trip_update import TripUpdateTripUpdate


T = TypeVar("T", bound="TripUpdate")


@attr.s(auto_attribs=True)
class TripUpdate:
    """
    Attributes:
        id (Union[Unset, str]):  Example: 259982000.
        is_deleted (Union[Unset, bool]):
        trip_update (Union[Unset, TripUpdateTripUpdate]):
    """

    id: Union[Unset, str] = UNSET
    is_deleted: Union[Unset, bool] = UNSET
    trip_update: Union[Unset, "TripUpdateTripUpdate"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        is_deleted = self.is_deleted
        trip_update: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.trip_update, Unset):
            trip_update = self.trip_update.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if is_deleted is not UNSET:
            field_dict["is_deleted"] = is_deleted
        if trip_update is not UNSET:
            field_dict["trip_update"] = trip_update

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.trip_update_trip_update import TripUpdateTripUpdate

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        is_deleted = d.pop("is_deleted", UNSET)

        _trip_update = d.pop("trip_update", UNSET)
        trip_update: Union[Unset, TripUpdateTripUpdate]
        if isinstance(_trip_update, Unset):
            trip_update = UNSET
        else:
            trip_update = TripUpdateTripUpdate.from_dict(_trip_update)

        trip_update = cls(
            id=id,
            is_deleted=is_deleted,
            trip_update=trip_update,
        )

        trip_update.additional_properties = d
        return trip_update

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
