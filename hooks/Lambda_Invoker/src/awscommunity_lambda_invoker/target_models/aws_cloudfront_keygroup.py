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
class AwsCloudfrontKeygroup(BaseModel):
    Id: Optional[str]
    KeyGroupConfig: Optional["_KeyGroupConfig"]
    LastModifiedTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCloudfrontKeygroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCloudfrontKeygroup"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            KeyGroupConfig=KeyGroupConfig._deserialize(json_data.get("KeyGroupConfig")),
            LastModifiedTime=json_data.get("LastModifiedTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCloudfrontKeygroup = AwsCloudfrontKeygroup


@dataclass
class KeyGroupConfig(BaseModel):
    Comment: Optional[str]
    Items: Optional[Sequence[str]]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KeyGroupConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KeyGroupConfig"]:
        if not json_data:
            return None
        return cls(
            Comment=json_data.get("Comment"),
            Items=json_data.get("Items"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KeyGroupConfig = KeyGroupConfig


