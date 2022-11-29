from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_alert import AlertAlert


T = TypeVar("T", bound="Alert")


@attr.s(auto_attribs=True)
class Alert:
    """
    Attributes:
        id (Union[Unset, str]):  Example: 259982000.
        is_deleted (Union[Unset, bool]):
        alert (Union[Unset, AlertAlert]):
    """

    id: Union[Unset, str] = UNSET
    is_deleted: Union[Unset, bool] = UNSET
    alert: Union[Unset, "AlertAlert"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        is_deleted = self.is_deleted
        alert: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.alert, Unset):
            alert = self.alert.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if is_deleted is not UNSET:
            field_dict["is_deleted"] = is_deleted
        if alert is not UNSET:
            field_dict["alert"] = alert

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.alert_alert import AlertAlert

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        is_deleted = d.pop("is_deleted", UNSET)

        _alert = d.pop("alert", UNSET)
        alert: Union[Unset, AlertAlert]
        if isinstance(_alert, Unset):
            alert = UNSET
        else:
            alert = AlertAlert.from_dict(_alert)

        alert = cls(
            id=id,
            is_deleted=is_deleted,
            alert=alert,
        )

        alert.additional_properties = d
        return alert

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
