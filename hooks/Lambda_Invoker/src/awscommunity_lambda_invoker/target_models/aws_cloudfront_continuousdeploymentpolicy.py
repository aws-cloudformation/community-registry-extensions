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
class AwsCloudfrontContinuousdeploymentpolicy(BaseModel):
    ContinuousDeploymentPolicyConfig: Optional["_ContinuousDeploymentPolicyConfig"]
    LastModifiedTime: Optional[str]
    Id: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCloudfrontContinuousdeploymentpolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCloudfrontContinuousdeploymentpolicy"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ContinuousDeploymentPolicyConfig=ContinuousDeploymentPolicyConfig._deserialize(json_data.get("ContinuousDeploymentPolicyConfig")),
            LastModifiedTime=json_data.get("LastModifiedTime"),
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCloudfrontContinuousdeploymentpolicy = AwsCloudfrontContinuousdeploymentpolicy


@dataclass
class ContinuousDeploymentPolicyConfig(BaseModel):
    Enabled: Optional[bool]
    StagingDistributionDnsNames: Optional[Sequence[str]]
    TrafficConfig: Optional["_TrafficConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_ContinuousDeploymentPolicyConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContinuousDeploymentPolicyConfig"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            StagingDistributionDnsNames=json_data.get("StagingDistributionDnsNames"),
            TrafficConfig=TrafficConfig._deserialize(json_data.get("TrafficConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContinuousDeploymentPolicyConfig = ContinuousDeploymentPolicyConfig


@dataclass
class TrafficConfig(BaseModel):
    SingleWeightConfig: Optional["_SingleWeightConfig"]
    Type: Optional[str]
    SingleHeaderConfig: Optional["_SingleHeaderConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_TrafficConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TrafficConfig"]:
        if not json_data:
            return None
        return cls(
            SingleWeightConfig=SingleWeightConfig._deserialize(json_data.get("SingleWeightConfig")),
            Type=json_data.get("Type"),
            SingleHeaderConfig=SingleHeaderConfig._deserialize(json_data.get("SingleHeaderConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TrafficConfig = TrafficConfig


@dataclass
class SingleWeightConfig(BaseModel):
    SessionStickinessConfig: Optional["_SessionStickinessConfig"]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SingleWeightConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SingleWeightConfig"]:
        if not json_data:
            return None
        return cls(
            SessionStickinessConfig=SessionStickinessConfig._deserialize(json_data.get("SessionStickinessConfig")),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SingleWeightConfig = SingleWeightConfig


@dataclass
class SessionStickinessConfig(BaseModel):
    IdleTTL: Optional[int]
    MaximumTTL: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_SessionStickinessConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SessionStickinessConfig"]:
        if not json_data:
            return None
        return cls(
            IdleTTL=json_data.get("IdleTTL"),
            MaximumTTL=json_data.get("MaximumTTL"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SessionStickinessConfig = SessionStickinessConfig


@dataclass
class SingleHeaderConfig(BaseModel):
    Header: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SingleHeaderConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SingleHeaderConfig"]:
        if not json_data:
            return None
        return cls(
            Header=json_data.get("Header"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SingleHeaderConfig = SingleHeaderConfig


