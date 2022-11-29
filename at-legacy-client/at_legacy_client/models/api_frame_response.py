from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert import Alert
    from ..models.feed_header import FeedHeader
    from ..models.trip_update import TripUpdate
    from ..models.vehicle_position import VehiclePosition


T = TypeVar("T", bound="ApiFrameResponse")


@attr.s(auto_attribs=True)
class ApiFrameResponse:
    """
    Attributes:
        header (Union[Unset, FeedHeader]):
        entity (Union[Unset, List[Union['Alert', 'TripUpdate', 'VehiclePosition']]]):
    """

    header: Union[Unset, "FeedHeader"] = UNSET
    entity: Union[Unset, List[Union["Alert", "TripUpdate", "VehiclePosition"]]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.trip_update import TripUpdate
        from ..models.vehicle_position import VehiclePosition

        header: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.header, Unset):
            header = self.header.to_dict()

        entity: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.entity, Unset):
            entity = []
            for entity_item_data in self.entity:
                entity_item: Dict[str, Any]

                if isinstance(entity_item_data, TripUpdate):
                    entity_item = entity_item_data.to_dict()

                elif isinstance(entity_item_data, VehiclePosition):
                    entity_item = entity_item_data.to_dict()

                else:
                    entity_item = entity_item_data.to_dict()

                entity.append(entity_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if header is not UNSET:
            field_dict["header"] = header
        if entity is not UNSET:
            field_dict["entity"] = entity

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.alert import Alert
        from ..models.feed_header import FeedHeader
        from ..models.trip_update import TripUpdate
        from ..models.vehicle_position import VehiclePosition

        d = src_dict.copy()
        _header = d.pop("header", UNSET)
        header: Union[Unset, FeedHeader]
        if isinstance(_header, Unset):
            header = UNSET
        else:
            header = FeedHeader.from_dict(_header)

        entity = []
        _entity = d.pop("entity", UNSET)
        for entity_item_data in _entity or []:

            def _parse_entity_item(data: object) -> Union["Alert", "TripUpdate", "VehiclePosition"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    entity_item_type_0 = TripUpdate.from_dict(data)

                    return entity_item_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    entity_item_type_1 = VehiclePosition.from_dict(data)

                    return entity_item_type_1
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                entity_item_type_2 = Alert.from_dict(data)

                return entity_item_type_2

            entity_item = _parse_entity_item(entity_item_data)

            entity.append(entity_item)

        api_frame_response = cls(
            header=header,
            entity=entity,
        )

        api_frame_response.additional_properties = d
        return api_frame_response

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
