# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass

from cloudformation_cli_python_lib.interface import BaseModel
from cloudformation_cli_python_lib.recast import recast_object
from cloudformation_cli_python_lib.utils import deserialize_list

import sys
from inspect import getmembers, isclass
from typing import (
    AbstractSet,
    Any,
    Generic,
    Mapping,
    MutableMapping,
    Optional,
    Sequence,
    Type,
    TypeVar,
)

T = TypeVar("T")


def set_or_none(value: Optional[Sequence[T]]) -> Optional[AbstractSet[T]]:
    if value:
        return set(value)
    return None


@dataclass
class AwsIot1clickProject(BaseModel):
    Id: Optional[str]
    ProjectName: Optional[str]
    Arn: Optional[str]
    Description: Optional[str]
    PlacementTemplate: Optional["_PlacementTemplate"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIot1clickProject"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIot1clickProject"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            ProjectName=json_data.get("ProjectName"),
            Arn=json_data.get("Arn"),
            Description=json_data.get("Description"),
            PlacementTemplate=PlacementTemplate._deserialize(json_data.get("PlacementTemplate")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIot1clickProject = AwsIot1clickProject


@dataclass
class PlacementTemplate(BaseModel):
    DeviceTemplates: Optional[MutableMapping[str, Any]]
    DefaultAttributes: Optional[MutableMapping[str, Any]]

    @classmethod
    def _deserialize(
        cls: Type["_PlacementTemplate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlacementTemplate"]:
        if not json_data:
            return None
        return cls(
            DeviceTemplates=json_data.get("DeviceTemplates"),
            DefaultAttributes=json_data.get("DefaultAttributes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlacementTemplate = PlacementTemplate


