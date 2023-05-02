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
class AwsCloudformationHookversion(BaseModel):
    Arn: Optional[str]
    TypeArn: Optional[str]
    ExecutionRoleArn: Optional[str]
    IsDefaultVersion: Optional[bool]
    LoggingConfig: Optional["_LoggingConfig"]
    SchemaHandlerPackage: Optional[str]
    TypeName: Optional[str]
    VersionId: Optional[str]
    Visibility: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCloudformationHookversion"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCloudformationHookversion"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            TypeArn=json_data.get("TypeArn"),
            ExecutionRoleArn=json_data.get("ExecutionRoleArn"),
            IsDefaultVersion=json_data.get("IsDefaultVersion"),
            LoggingConfig=LoggingConfig._deserialize(json_data.get("LoggingConfig")),
            SchemaHandlerPackage=json_data.get("SchemaHandlerPackage"),
            TypeName=json_data.get("TypeName"),
            VersionId=json_data.get("VersionId"),
            Visibility=json_data.get("Visibility"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCloudformationHookversion = AwsCloudformationHookversion


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


