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
class AwsStepfunctionsStatemachinealias(BaseModel):
    Arn: Optional[str]
    Name: Optional[str]
    Description: Optional[str]
    RoutingConfiguration: Optional[AbstractSet["_RoutingConfigurationVersion"]]
    DeploymentPreference: Optional["_DeploymentPreference"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsStepfunctionsStatemachinealias"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsStepfunctionsStatemachinealias"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            Name=json_data.get("Name"),
            Description=json_data.get("Description"),
            RoutingConfiguration=set_or_none(json_data.get("RoutingConfiguration")),
            DeploymentPreference=DeploymentPreference._deserialize(json_data.get("DeploymentPreference")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsStepfunctionsStatemachinealias = AwsStepfunctionsStatemachinealias


@dataclass
class RoutingConfigurationVersion(BaseModel):
    StateMachineVersionArn: Optional[str]
    Weight: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_RoutingConfigurationVersion"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RoutingConfigurationVersion"]:
        if not json_data:
            return None
        return cls(
            StateMachineVersionArn=json_data.get("StateMachineVersionArn"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RoutingConfigurationVersion = RoutingConfigurationVersion


@dataclass
class DeploymentPreference(BaseModel):
    StateMachineVersionArn: Optional[str]
    Type: Optional[str]
    Percentage: Optional[int]
    Interval: Optional[int]
    Alarms: Optional[AbstractSet[str]]

    @classmethod
    def _deserialize(
        cls: Type["_DeploymentPreference"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeploymentPreference"]:
        if not json_data:
            return None
        return cls(
            StateMachineVersionArn=json_data.get("StateMachineVersionArn"),
            Type=json_data.get("Type"),
            Percentage=json_data.get("Percentage"),
            Interval=json_data.get("Interval"),
            Alarms=set_or_none(json_data.get("Alarms")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeploymentPreference = DeploymentPreference


