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
class AwsRedshiftScheduledaction(BaseModel):
    ScheduledActionName: Optional[str]
    TargetAction: Optional["_ScheduledActionType"]
    Schedule: Optional[str]
    IamRole: Optional[str]
    ScheduledActionDescription: Optional[str]
    StartTime: Optional[str]
    EndTime: Optional[str]
    Enable: Optional[bool]
    State: Optional[str]
    NextInvocations: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsRedshiftScheduledaction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsRedshiftScheduledaction"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ScheduledActionName=json_data.get("ScheduledActionName"),
            TargetAction=ScheduledActionType._deserialize(json_data.get("TargetAction")),
            Schedule=json_data.get("Schedule"),
            IamRole=json_data.get("IamRole"),
            ScheduledActionDescription=json_data.get("ScheduledActionDescription"),
            StartTime=json_data.get("StartTime"),
            EndTime=json_data.get("EndTime"),
            Enable=json_data.get("Enable"),
            State=json_data.get("State"),
            NextInvocations=json_data.get("NextInvocations"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsRedshiftScheduledaction = AwsRedshiftScheduledaction


@dataclass
class ScheduledActionType(BaseModel):
    ResizeCluster: Optional["_ResizeClusterMessage"]
    PauseCluster: Optional["_PauseClusterMessage"]
    ResumeCluster: Optional["_ResumeClusterMessage"]

    @classmethod
    def _deserialize(
        cls: Type["_ScheduledActionType"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScheduledActionType"]:
        if not json_data:
            return None
        return cls(
            ResizeCluster=ResizeClusterMessage._deserialize(json_data.get("ResizeCluster")),
            PauseCluster=PauseClusterMessage._deserialize(json_data.get("PauseCluster")),
            ResumeCluster=ResumeClusterMessage._deserialize(json_data.get("ResumeCluster")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScheduledActionType = ScheduledActionType


@dataclass
class ResizeClusterMessage(BaseModel):
    ClusterIdentifier: Optional[str]
    ClusterType: Optional[str]
    NodeType: Optional[str]
    NumberOfNodes: Optional[int]
    Classic: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ResizeClusterMessage"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResizeClusterMessage"]:
        if not json_data:
            return None
        return cls(
            ClusterIdentifier=json_data.get("ClusterIdentifier"),
            ClusterType=json_data.get("ClusterType"),
            NodeType=json_data.get("NodeType"),
            NumberOfNodes=json_data.get("NumberOfNodes"),
            Classic=json_data.get("Classic"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResizeClusterMessage = ResizeClusterMessage


@dataclass
class PauseClusterMessage(BaseModel):
    ClusterIdentifier: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PauseClusterMessage"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PauseClusterMessage"]:
        if not json_data:
            return None
        return cls(
            ClusterIdentifier=json_data.get("ClusterIdentifier"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PauseClusterMessage = PauseClusterMessage


@dataclass
class ResumeClusterMessage(BaseModel):
    ClusterIdentifier: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResumeClusterMessage"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResumeClusterMessage"]:
        if not json_data:
            return None
        return cls(
            ClusterIdentifier=json_data.get("ClusterIdentifier"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResumeClusterMessage = ResumeClusterMessage


