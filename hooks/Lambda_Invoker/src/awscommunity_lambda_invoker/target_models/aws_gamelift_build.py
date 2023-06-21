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
class AwsGameliftBuild(BaseModel):
    BuildId: Optional[str]
    Name: Optional[str]
    OperatingSystem: Optional[str]
    StorageLocation: Optional["_StorageLocation"]
    Version: Optional[str]
    ServerSdkVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsGameliftBuild"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsGameliftBuild"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            BuildId=json_data.get("BuildId"),
            Name=json_data.get("Name"),
            OperatingSystem=json_data.get("OperatingSystem"),
            StorageLocation=StorageLocation._deserialize(json_data.get("StorageLocation")),
            Version=json_data.get("Version"),
            ServerSdkVersion=json_data.get("ServerSdkVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsGameliftBuild = AwsGameliftBuild


@dataclass
class StorageLocation(BaseModel):
    Bucket: Optional[str]
    Key: Optional[str]
    ObjectVersion: Optional[str]
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StorageLocation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageLocation"]:
        if not json_data:
            return None
        return cls(
            Bucket=json_data.get("Bucket"),
            Key=json_data.get("Key"),
            ObjectVersion=json_data.get("ObjectVersion"),
            RoleArn=json_data.get("RoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StorageLocation = StorageLocation


