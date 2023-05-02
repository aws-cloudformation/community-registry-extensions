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
class AwsConfigRemediationconfiguration(BaseModel):
    TargetVersion: Optional[str]
    ExecutionControls: Optional["_ExecutionControls"]
    Parameters: Optional[MutableMapping[str, Any]]
    TargetType: Optional[str]
    ConfigRuleName: Optional[str]
    ResourceType: Optional[str]
    RetryAttemptSeconds: Optional[int]
    MaximumAutomaticAttempts: Optional[int]
    Id: Optional[str]
    TargetId: Optional[str]
    Automatic: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AwsConfigRemediationconfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsConfigRemediationconfiguration"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            TargetVersion=json_data.get("TargetVersion"),
            ExecutionControls=ExecutionControls._deserialize(json_data.get("ExecutionControls")),
            Parameters=json_data.get("Parameters"),
            TargetType=json_data.get("TargetType"),
            ConfigRuleName=json_data.get("ConfigRuleName"),
            ResourceType=json_data.get("ResourceType"),
            RetryAttemptSeconds=json_data.get("RetryAttemptSeconds"),
            MaximumAutomaticAttempts=json_data.get("MaximumAutomaticAttempts"),
            Id=json_data.get("Id"),
            TargetId=json_data.get("TargetId"),
            Automatic=json_data.get("Automatic"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsConfigRemediationconfiguration = AwsConfigRemediationconfiguration


@dataclass
class ExecutionControls(BaseModel):
    SsmControls: Optional["_SsmControls"]

    @classmethod
    def _deserialize(
        cls: Type["_ExecutionControls"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExecutionControls"]:
        if not json_data:
            return None
        return cls(
            SsmControls=SsmControls._deserialize(json_data.get("SsmControls")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExecutionControls = ExecutionControls


@dataclass
class SsmControls(BaseModel):
    ErrorPercentage: Optional[int]
    ConcurrentExecutionRatePercentage: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_SsmControls"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SsmControls"]:
        if not json_data:
            return None
        return cls(
            ErrorPercentage=json_data.get("ErrorPercentage"),
            ConcurrentExecutionRatePercentage=json_data.get("ConcurrentExecutionRatePercentage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SsmControls = SsmControls


