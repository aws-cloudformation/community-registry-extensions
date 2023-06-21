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
class AwsSsmMaintenancewindowtarget(BaseModel):
    OwnerInformation: Optional[str]
    Description: Optional[str]
    WindowId: Optional[str]
    ResourceType: Optional[str]
    Targets: Optional[Sequence["_Targets"]]
    Id: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSsmMaintenancewindowtarget"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSsmMaintenancewindowtarget"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            OwnerInformation=json_data.get("OwnerInformation"),
            Description=json_data.get("Description"),
            WindowId=json_data.get("WindowId"),
            ResourceType=json_data.get("ResourceType"),
            Targets=deserialize_list(json_data.get("Targets"), Targets),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSsmMaintenancewindowtarget = AwsSsmMaintenancewindowtarget


@dataclass
class Targets(BaseModel):
    Values: Optional[Sequence[str]]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Targets"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Targets"]:
        if not json_data:
            return None
        return cls(
            Values=json_data.get("Values"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Targets = Targets


