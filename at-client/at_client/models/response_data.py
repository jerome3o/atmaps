from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.route import Route
    from ..models.stop import Stop
    from ..models.trip import Trip


T = TypeVar("T", bound="ResponseData")


@attr.s(auto_attribs=True)
class ResponseData:
    """
    Attributes:
        type (Union[Unset, str]):
        id (Union[Unset, str]):
        attributes (Union['Route', 'Stop', 'Trip', Unset]):
    """

    type: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    attributes: Union["Route", "Stop", "Trip", Unset] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.route import Route
        from ..models.stop import Stop

        type = self.type
        id = self.id
        attributes: Union[Dict[str, Any], Unset]
        if isinstance(self.attributes, Unset):
            attributes = UNSET

        elif isinstance(self.attributes, Route):
            attributes = UNSET
            if not isinstance(self.attributes, Unset):
                attributes = self.attributes.to_dict()

        elif isinstance(self.attributes, Stop):
            attributes = UNSET
            if not isinstance(self.attributes, Unset):
                attributes = self.attributes.to_dict()

        else:
            attributes = UNSET
            if not isinstance(self.attributes, Unset):
                attributes = self.attributes.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if id is not UNSET:
            field_dict["id"] = id
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.route import Route
        from ..models.stop import Stop
        from ..models.trip import Trip

        d = src_dict.copy()
        type = d.pop("type", UNSET)

        id = d.pop("id", UNSET)

        def _parse_attributes(data: object) -> Union["Route", "Stop", "Trip", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _attributes_type_0 = data
                attributes_type_0: Union[Unset, Route]
                if isinstance(_attributes_type_0, Unset):
                    attributes_type_0 = UNSET
                else:
                    attributes_type_0 = Route.from_dict(_attributes_type_0)

                return attributes_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _attributes_type_1 = data
                attributes_type_1: Union[Unset, Stop]
                if isinstance(_attributes_type_1, Unset):
                    attributes_type_1 = UNSET
                else:
                    attributes_type_1 = Stop.from_dict(_attributes_type_1)

                return attributes_type_1
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            _attributes_type_2 = data
            attributes_type_2: Union[Unset, Trip]
            if isinstance(_attributes_type_2, Unset):
                attributes_type_2 = UNSET
            else:
                attributes_type_2 = Trip.from_dict(_attributes_type_2)

            return attributes_type_2

        attributes = _parse_attributes(d.pop("attributes", UNSET))

        response_data = cls(
            type=type,
            id=id,
            attributes=attributes,
        )

        response_data.additional_properties = d
        return response_data

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
