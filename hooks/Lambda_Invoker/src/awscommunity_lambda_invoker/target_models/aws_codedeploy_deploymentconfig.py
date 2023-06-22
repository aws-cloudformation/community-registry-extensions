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
class AwsCodedeployDeploymentconfig(BaseModel):
    ComputePlatform: Optional[str]
    DeploymentConfigName: Optional[str]
    MinimumHealthyHosts: Optional["_MinimumHealthyHosts"]
    TrafficRoutingConfig: Optional["_TrafficRoutingConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCodedeployDeploymentconfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCodedeployDeploymentconfig"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ComputePlatform=json_data.get("ComputePlatform"),
            DeploymentConfigName=json_data.get("DeploymentConfigName"),
            MinimumHealthyHosts=MinimumHealthyHosts._deserialize(json_data.get("MinimumHealthyHosts")),
            TrafficRoutingConfig=TrafficRoutingConfig._deserialize(json_data.get("TrafficRoutingConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCodedeployDeploymentconfig = AwsCodedeployDeploymentconfig


@dataclass
class MinimumHealthyHosts(BaseModel):
    Value: Optional[int]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MinimumHealthyHosts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MinimumHealthyHosts"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MinimumHealthyHosts = MinimumHealthyHosts


@dataclass
class TrafficRoutingConfig(BaseModel):
    Type: Optional[str]
    TimeBasedLinear: Optional["_TimeBasedLinear"]
    TimeBasedCanary: Optional["_TimeBasedCanary"]

    @classmethod
    def _deserialize(
        cls: Type["_TrafficRoutingConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TrafficRoutingConfig"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            TimeBasedLinear=TimeBasedLinear._deserialize(json_data.get("TimeBasedLinear")),
            TimeBasedCanary=TimeBasedCanary._deserialize(json_data.get("TimeBasedCanary")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TrafficRoutingConfig = TrafficRoutingConfig


@dataclass
class TimeBasedLinear(BaseModel):
    LinearInterval: Optional[int]
    LinearPercentage: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_TimeBasedLinear"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeBasedLinear"]:
        if not json_data:
            return None
        return cls(
            LinearInterval=json_data.get("LinearInterval"),
            LinearPercentage=json_data.get("LinearPercentage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeBasedLinear = TimeBasedLinear


@dataclass
class TimeBasedCanary(BaseModel):
    CanaryPercentage: Optional[int]
    CanaryInterval: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_TimeBasedCanary"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeBasedCanary"]:
        if not json_data:
            return None
        return cls(
            CanaryPercentage=json_data.get("CanaryPercentage"),
            CanaryInterval=json_data.get("CanaryInterval"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeBasedCanary = TimeBasedCanary


