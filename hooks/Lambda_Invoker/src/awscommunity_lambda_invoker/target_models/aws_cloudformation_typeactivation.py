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
class AwsCloudformationTypeactivation(BaseModel):
    Arn: Optional[str]
    ExecutionRoleArn: Optional[str]
    PublisherId: Optional[str]
    LoggingConfig: Optional["_LoggingConfig"]
    PublicTypeArn: Optional[str]
    AutoUpdate: Optional[bool]
    TypeNameAlias: Optional[str]
    VersionBump: Optional[str]
    MajorVersion: Optional[str]
    TypeName: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCloudformationTypeactivation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCloudformationTypeactivation"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            ExecutionRoleArn=json_data.get("ExecutionRoleArn"),
            PublisherId=json_data.get("PublisherId"),
            LoggingConfig=LoggingConfig._deserialize(json_data.get("LoggingConfig")),
            PublicTypeArn=json_data.get("PublicTypeArn"),
            AutoUpdate=json_data.get("AutoUpdate"),
            TypeNameAlias=json_data.get("TypeNameAlias"),
            VersionBump=json_data.get("VersionBump"),
            MajorVersion=json_data.get("MajorVersion"),
            TypeName=json_data.get("TypeName"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCloudformationTypeactivation = AwsCloudformationTypeactivation


@dataclass
class LoggingConfig(BaseModel):
    LogGroupName: Optional[str]
    LogRoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingConfig"]:
        if not json_data:
            return None
        return cls(
            LogGroupName=json_data.get("LogGroupName"),
            LogRoleArn=json_data.get("LogRoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingConfig = LoggingConfig


