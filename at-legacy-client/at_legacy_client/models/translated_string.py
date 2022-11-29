from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.translation import Translation


T = TypeVar("T", bound="TranslatedString")


@attr.s(auto_attribs=True)
class TranslatedString:
    """
    Attributes:
        translation (Union[Unset, Translation]):  Example: {'text': 'sample text', 'language': 'English'}.
    """

    translation: Union[Unset, "Translation"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        translation: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.translation, Unset):
            translation = self.translation.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if translation is not UNSET:
            field_dict["translation"] = translation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.translation import Translation

        d = src_dict.copy()
        _translation = d.pop("translation", UNSET)
        translation: Union[Unset, Translation]
        if isinstance(_translation, Unset):
            translation = UNSET
        else:
            translation = Translation.from_dict(_translation)

        translated_string = cls(
            translation=translation,
        )

        translated_string.additional_properties = d
        return translated_string

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
