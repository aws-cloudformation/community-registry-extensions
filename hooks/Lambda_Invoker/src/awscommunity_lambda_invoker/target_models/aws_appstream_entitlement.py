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
class AwsAppstreamEntitlement(BaseModel):
    Name: Optional[str]
    StackName: Optional[str]
    Description: Optional[str]
    AppVisibility: Optional[str]
    Attributes: Optional[AbstractSet["_Attribute"]]
    CreatedTime: Optional[str]
    LastModifiedTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAppstreamEntitlement"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAppstreamEntitlement"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Name=json_data.get("Name"),
            StackName=json_data.get("StackName"),
            Description=json_data.get("Description"),
            AppVisibility=json_data.get("AppVisibility"),
            Attributes=set_or_none(json_data.get("Attributes")),
            CreatedTime=json_data.get("CreatedTime"),
            LastModifiedTime=json_data.get("LastModifiedTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAppstreamEntitlement = AwsAppstreamEntitlement


@dataclass
class Attribute(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Attribute"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Attribute"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Attribute = Attribute


