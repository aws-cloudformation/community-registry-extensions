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
class AwsCloudfrontFunction(BaseModel):
    AutoPublish: Optional[bool]
    FunctionARN: Optional[str]
    FunctionCode: Optional[str]
    FunctionConfig: Optional["_FunctionConfig"]
    FunctionMetadata: Optional["_FunctionMetadata"]
    Name: Optional[str]
    Stage: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCloudfrontFunction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCloudfrontFunction"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AutoPublish=json_data.get("AutoPublish"),
            FunctionARN=json_data.get("FunctionARN"),
            FunctionCode=json_data.get("FunctionCode"),
            FunctionConfig=FunctionConfig._deserialize(json_data.get("FunctionConfig")),
            FunctionMetadata=FunctionMetadata._deserialize(json_data.get("FunctionMetadata")),
            Name=json_data.get("Name"),
            Stage=json_data.get("Stage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCloudfrontFunction = AwsCloudfrontFunction


@dataclass
class FunctionConfig(BaseModel):
    Comment: Optional[str]
    Runtime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FunctionConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FunctionConfig"]:
        if not json_data:
            return None
        return cls(
            Comment=json_data.get("Comment"),
            Runtime=json_data.get("Runtime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FunctionConfig = FunctionConfig


@dataclass
class FunctionMetadata(BaseModel):
    FunctionARN: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FunctionMetadata"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FunctionMetadata"]:
        if not json_data:
            return None
        return cls(
            FunctionARN=json_data.get("FunctionARN"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FunctionMetadata = FunctionMetadata


