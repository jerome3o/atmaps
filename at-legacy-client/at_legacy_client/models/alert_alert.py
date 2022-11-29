from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.cause import Cause
from ..models.effect import Effect
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entity_selector import EntitySelector
    from ..models.time_range import TimeRange
    from ..models.translated_string import TranslatedString


T = TypeVar("T", bound="AlertAlert")


@attr.s(auto_attribs=True)
class AlertAlert:
    """
    Attributes:
        active_period (Union[Unset, TimeRange]):  Example: {'start': 1559008444, 'end': 1559008746}.
        informed_entity (Union[Unset, EntitySelector]):  Example: {'route_id': '325-221'}.
        cause (Union[Unset, Cause]):  Example: 1.
        effect (Union[Unset, Effect]):  Example: 8.
        url (Union[Unset, TranslatedString]):
        header_text (Union[Unset, TranslatedString]):
        description_text (Union[Unset, TranslatedString]):
    """

    active_period: Union[Unset, "TimeRange"] = UNSET
    informed_entity: Union[Unset, "EntitySelector"] = UNSET
    cause: Union[Unset, Cause] = UNSET
    effect: Union[Unset, Effect] = UNSET
    url: Union[Unset, "TranslatedString"] = UNSET
    header_text: Union[Unset, "TranslatedString"] = UNSET
    description_text: Union[Unset, "TranslatedString"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        active_period: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.active_period, Unset):
            active_period = self.active_period.to_dict()

        informed_entity: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.informed_entity, Unset):
            informed_entity = self.informed_entity.to_dict()

        cause: Union[Unset, int] = UNSET
        if not isinstance(self.cause, Unset):
            cause = self.cause.value

        effect: Union[Unset, int] = UNSET
        if not isinstance(self.effect, Unset):
            effect = self.effect.value

        url: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.url, Unset):
            url = self.url.to_dict()

        header_text: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.header_text, Unset):
            header_text = self.header_text.to_dict()

        description_text: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.description_text, Unset):
            description_text = self.description_text.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active_period is not UNSET:
            field_dict["active_period"] = active_period
        if informed_entity is not UNSET:
            field_dict["informed_entity"] = informed_entity
        if cause is not UNSET:
            field_dict["cause"] = cause
        if effect is not UNSET:
            field_dict["effect"] = effect
        if url is not UNSET:
            field_dict["url"] = url
        if header_text is not UNSET:
            field_dict["header_text"] = header_text
        if description_text is not UNSET:
            field_dict["description_text"] = description_text

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.entity_selector import EntitySelector
        from ..models.time_range import TimeRange
        from ..models.translated_string import TranslatedString

        d = src_dict.copy()
        _active_period = d.pop("active_period", UNSET)
        active_period: Union[Unset, TimeRange]
        if isinstance(_active_period, Unset):
            active_period = UNSET
        else:
            active_period = TimeRange.from_dict(_active_period)

        _informed_entity = d.pop("informed_entity", UNSET)
        informed_entity: Union[Unset, EntitySelector]
        if isinstance(_informed_entity, Unset):
            informed_entity = UNSET
        else:
            informed_entity = EntitySelector.from_dict(_informed_entity)

        _cause = d.pop("cause", UNSET)
        cause: Union[Unset, Cause]
        if isinstance(_cause, Unset):
            cause = UNSET
        else:
            cause = Cause(_cause)

        _effect = d.pop("effect", UNSET)
        effect: Union[Unset, Effect]
        if isinstance(_effect, Unset):
            effect = UNSET
        else:
            effect = Effect(_effect)

        _url = d.pop("url", UNSET)
        url: Union[Unset, TranslatedString]
        if isinstance(_url, Unset):
            url = UNSET
        else:
            url = TranslatedString.from_dict(_url)

        _header_text = d.pop("header_text", UNSET)
        header_text: Union[Unset, TranslatedString]
        if isinstance(_header_text, Unset):
            header_text = UNSET
        else:
            header_text = TranslatedString.from_dict(_header_text)

        _description_text = d.pop("description_text", UNSET)
        description_text: Union[Unset, TranslatedString]
        if isinstance(_description_text, Unset):
            description_text = UNSET
        else:
            description_text = TranslatedString.from_dict(_description_text)

        alert_alert = cls(
            active_period=active_period,
            informed_entity=informed_entity,
            cause=cause,
            effect=effect,
            url=url,
            header_text=header_text,
            description_text=description_text,
        )

        alert_alert.additional_properties = d
        return alert_alert

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
