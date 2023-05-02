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
class AwsConfigConfigurationrecorder(BaseModel):
    Id: Optional[str]
    RecordingGroup: Optional["_RecordingGroup"]
    RoleARN: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsConfigConfigurationrecorder"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsConfigConfigurationrecorder"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            RecordingGroup=RecordingGroup._deserialize(json_data.get("RecordingGroup")),
            RoleARN=json_data.get("RoleARN"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsConfigConfigurationrecorder = AwsConfigConfigurationrecorder


@dataclass
class RecordingGroup(BaseModel):
    IncludeGlobalResourceTypes: Optional[bool]
    ResourceTypes: Optional[Sequence[str]]
    AllSupported: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_RecordingGroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RecordingGroup"]:
        if not json_data:
            return None
        return cls(
            IncludeGlobalResourceTypes=json_data.get("IncludeGlobalResourceTypes"),
            ResourceTypes=json_data.get("ResourceTypes"),
            AllSupported=json_data.get("AllSupported"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RecordingGroup = RecordingGroup


