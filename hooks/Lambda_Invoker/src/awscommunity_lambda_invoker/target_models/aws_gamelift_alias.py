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
class AwsGameliftAlias(BaseModel):
    Description: Optional[str]
    Name: Optional[str]
    RoutingStrategy: Optional["_RoutingStrategy"]
    AliasId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsGameliftAlias"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsGameliftAlias"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
            RoutingStrategy=RoutingStrategy._deserialize(json_data.get("RoutingStrategy")),
            AliasId=json_data.get("AliasId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsGameliftAlias = AwsGameliftAlias


@dataclass
class RoutingStrategy(BaseModel):
    Message: Optional[str]
    FleetId: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RoutingStrategy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RoutingStrategy"]:
        if not json_data:
            return None
        return cls(
            Message=json_data.get("Message"),
            FleetId=json_data.get("FleetId"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RoutingStrategy = RoutingStrategy


