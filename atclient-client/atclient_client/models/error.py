from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_source import ErrorSource


T = TypeVar("T", bound="Error")


@attr.s(auto_attribs=True)
class Error:
    """
    Attributes:
        status (Union[Unset, str]):
        code (Union[Unset, str]):
        title (Union[Unset, str]):
        detail (Union[Unset, str]):
        source (Union[Unset, ErrorSource]):
    """

    status: Union[Unset, str] = UNSET
    code: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    detail: Union[Unset, str] = UNSET
    source: Union[Unset, "ErrorSource"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status = self.status
        code = self.code
        title = self.title
        detail = self.detail
        source: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if code is not UNSET:
            field_dict["code"] = code
        if title is not UNSET:
            field_dict["title"] = title
        if detail is not UNSET:
            field_dict["detail"] = detail
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.error_source import ErrorSource

        d = src_dict.copy()
        status = d.pop("status", UNSET)

        code = d.pop("code", UNSET)

        title = d.pop("title", UNSET)

        detail = d.pop("detail", UNSET)

        _source = d.pop("source", UNSET)
        source: Union[Unset, ErrorSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = ErrorSource.from_dict(_source)

        error = cls(
            status=status,
            code=code,
            title=title,
            detail=detail,
            source=source,
        )

        error.additional_properties = d
        return error

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
