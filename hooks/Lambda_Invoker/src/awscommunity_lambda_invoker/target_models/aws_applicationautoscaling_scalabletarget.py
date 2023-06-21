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
class AwsApplicationautoscalingScalabletarget(BaseModel):
    Id: Optional[str]
    MaxCapacity: Optional[int]
    MinCapacity: Optional[int]
    ResourceId: Optional[str]
    RoleARN: Optional[str]
    ScalableDimension: Optional[str]
    ScheduledActions: Optional[AbstractSet["_ScheduledAction"]]
    ServiceNamespace: Optional[str]
    SuspendedState: Optional["_SuspendedState"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsApplicationautoscalingScalabletarget"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsApplicationautoscalingScalabletarget"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            MaxCapacity=json_data.get("MaxCapacity"),
            MinCapacity=json_data.get("MinCapacity"),
            ResourceId=json_data.get("ResourceId"),
            RoleARN=json_data.get("RoleARN"),
            ScalableDimension=json_data.get("ScalableDimension"),
            ScheduledActions=set_or_none(json_data.get("ScheduledActions")),
            ServiceNamespace=json_data.get("ServiceNamespace"),
            SuspendedState=SuspendedState._deserialize(json_data.get("SuspendedState")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsApplicationautoscalingScalabletarget = AwsApplicationautoscalingScalabletarget


@dataclass
class ScheduledAction(BaseModel):
    Timezone: Optional[str]
    ScheduledActionName: Optional[str]
    EndTime: Optional[str]
    Schedule: Optional[str]
    StartTime: Optional[str]
    ScalableTargetAction: Optional["_ScalableTargetAction"]

    @classmethod
    def _deserialize(
        cls: Type["_ScheduledAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScheduledAction"]:
        if not json_data:
            return None
        return cls(
            Timezone=json_data.get("Timezone"),
            ScheduledActionName=json_data.get("ScheduledActionName"),
            EndTime=json_data.get("EndTime"),
            Schedule=json_data.get("Schedule"),
            StartTime=json_data.get("StartTime"),
            ScalableTargetAction=ScalableTargetAction._deserialize(json_data.get("ScalableTargetAction")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScheduledAction = ScheduledAction


@dataclass
class ScalableTargetAction(BaseModel):
    MinCapacity: Optional[int]
    MaxCapacity: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_ScalableTargetAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScalableTargetAction"]:
        if not json_data:
            return None
        return cls(
            MinCapacity=json_data.get("MinCapacity"),
            MaxCapacity=json_data.get("MaxCapacity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScalableTargetAction = ScalableTargetAction


@dataclass
class SuspendedState(BaseModel):
    ScheduledScalingSuspended: Optional[bool]
    DynamicScalingOutSuspended: Optional[bool]
    DynamicScalingInSuspended: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SuspendedState"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SuspendedState"]:
        if not json_data:
            return None
        return cls(
            ScheduledScalingSuspended=json_data.get("ScheduledScalingSuspended"),
            DynamicScalingOutSuspended=json_data.get("DynamicScalingOutSuspended"),
            DynamicScalingInSuspended=json_data.get("DynamicScalingInSuspended"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SuspendedState = SuspendedState


