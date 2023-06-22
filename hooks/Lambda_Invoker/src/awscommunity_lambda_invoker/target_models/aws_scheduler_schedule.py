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
class AwsSchedulerSchedule(BaseModel):
    Arn: Optional[str]
    Description: Optional[str]
    EndDate: Optional[str]
    FlexibleTimeWindow: Optional["_FlexibleTimeWindow"]
    GroupName: Optional[str]
    KmsKeyArn: Optional[str]
    Name: Optional[str]
    ScheduleExpression: Optional[str]
    ScheduleExpressionTimezone: Optional[str]
    StartDate: Optional[str]
    State: Optional[str]
    Target: Optional["_Target"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSchedulerSchedule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSchedulerSchedule"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            Description=json_data.get("Description"),
            EndDate=json_data.get("EndDate"),
            FlexibleTimeWindow=FlexibleTimeWindow._deserialize(json_data.get("FlexibleTimeWindow")),
            GroupName=json_data.get("GroupName"),
            KmsKeyArn=json_data.get("KmsKeyArn"),
            Name=json_data.get("Name"),
            ScheduleExpression=json_data.get("ScheduleExpression"),
            ScheduleExpressionTimezone=json_data.get("ScheduleExpressionTimezone"),
            StartDate=json_data.get("StartDate"),
            State=json_data.get("State"),
            Target=Target._deserialize(json_data.get("Target")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSchedulerSchedule = AwsSchedulerSchedule


@dataclass
class FlexibleTimeWindow(BaseModel):
    Mode: Optional[str]
    MaximumWindowInMinutes: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_FlexibleTimeWindow"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FlexibleTimeWindow"]:
        if not json_data:
            return None
        return cls(
            Mode=json_data.get("Mode"),
            MaximumWindowInMinutes=json_data.get("MaximumWindowInMinutes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FlexibleTimeWindow = FlexibleTimeWindow


@dataclass
class Target(BaseModel):
    Arn: Optional[str]
    RoleArn: Optional[str]
    DeadLetterConfig: Optional["_DeadLetterConfig"]
    RetryPolicy: Optional["_RetryPolicy"]
    Input: Optional[str]
    EcsParameters: Optional["_EcsParameters"]
    EventBridgeParameters: Optional["_EventBridgeParameters"]
    KinesisParameters: Optional["_KinesisParameters"]
    SageMakerPipelineParameters: Optional["_SageMakerPipelineParameters"]
    SqsParameters: Optional["_SqsParameters"]

    @classmethod
    def _deserialize(
        cls: Type["_Target"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Target"]:
        if not json_data:
            return None
        return cls(
            Arn=json_data.get("Arn"),
            RoleArn=json_data.get("RoleArn"),
            DeadLetterConfig=DeadLetterConfig._deserialize(json_data.get("DeadLetterConfig")),
            RetryPolicy=RetryPolicy._deserialize(json_data.get("RetryPolicy")),
            Input=json_data.get("Input"),
            EcsParameters=EcsParameters._deserialize(json_data.get("EcsParameters")),
            EventBridgeParameters=EventBridgeParameters._deserialize(json_data.get("EventBridgeParameters")),
            KinesisParameters=KinesisParameters._deserialize(json_data.get("KinesisParameters")),
            SageMakerPipelineParameters=SageMakerPipelineParameters._deserialize(json_data.get("SageMakerPipelineParameters")),
            SqsParameters=SqsParameters._deserialize(json_data.get("SqsParameters")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Target = Target


@dataclass
class DeadLetterConfig(BaseModel):
    Arn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DeadLetterConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeadLetterConfig"]:
        if not json_data:
            return None
        return cls(
            Arn=json_data.get("Arn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeadLetterConfig = DeadLetterConfig


@dataclass
class RetryPolicy(BaseModel):
    MaximumEventAgeInSeconds: Optional[float]
    MaximumRetryAttempts: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RetryPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RetryPolicy"]:
        if not json_data:
            return None
        return cls(
            MaximumEventAgeInSeconds=json_data.get("MaximumEventAgeInSeconds"),
            MaximumRetryAttempts=json_data.get("MaximumRetryAttempts"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RetryPolicy = RetryPolicy


@dataclass
class EcsParameters(BaseModel):
    TaskDefinitionArn: Optional[str]
    TaskCount: Optional[float]
    LaunchType: Optional[str]
    NetworkConfiguration: Optional["_NetworkConfiguration"]
    PlatformVersion: Optional[str]
    Group: Optional[str]
    CapacityProviderStrategy: Optional[Sequence["_CapacityProviderStrategyItem"]]
    EnableECSManagedTags: Optional[bool]
    EnableExecuteCommand: Optional[bool]
    PlacementConstraints: Optional[Sequence["_PlacementConstraint"]]
    PlacementStrategy: Optional[Sequence["_PlacementStrategy"]]
    PropagateTags: Optional[str]
    ReferenceId: Optional[str]
    Tags: Optional[Sequence[MutableMapping[str, str]]]

    @classmethod
    def _deserialize(
        cls: Type["_EcsParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EcsParameters"]:
        if not json_data:
            return None
        return cls(
            TaskDefinitionArn=json_data.get("TaskDefinitionArn"),
            TaskCount=json_data.get("TaskCount"),
            LaunchType=json_data.get("LaunchType"),
            NetworkConfiguration=NetworkConfiguration._deserialize(json_data.get("NetworkConfiguration")),
            PlatformVersion=json_data.get("PlatformVersion"),
            Group=json_data.get("Group"),
            CapacityProviderStrategy=deserialize_list(json_data.get("CapacityProviderStrategy"), CapacityProviderStrategyItem),
            EnableECSManagedTags=json_data.get("EnableECSManagedTags"),
            EnableExecuteCommand=json_data.get("EnableExecuteCommand"),
            PlacementConstraints=deserialize_list(json_data.get("PlacementConstraints"), PlacementConstraint),
            PlacementStrategy=deserialize_list(json_data.get("PlacementStrategy"), PlacementStrategy),
            PropagateTags=json_data.get("PropagateTags"),
            ReferenceId=json_data.get("ReferenceId"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EcsParameters = EcsParameters


@dataclass
class NetworkConfiguration(BaseModel):
    AwsvpcConfiguration: Optional["_AwsVpcConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkConfiguration"]:
        if not json_data:
            return None
        return cls(
            AwsvpcConfiguration=AwsVpcConfiguration._deserialize(json_data.get("AwsvpcConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkConfiguration = NetworkConfiguration


@dataclass
class AwsVpcConfiguration(BaseModel):
    Subnets: Optional[Sequence[str]]
    SecurityGroups: Optional[Sequence[str]]
    AssignPublicIp: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsVpcConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsVpcConfiguration"]:
        if not json_data:
            return None
        return cls(
            Subnets=json_data.get("Subnets"),
            SecurityGroups=json_data.get("SecurityGroups"),
            AssignPublicIp=json_data.get("AssignPublicIp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsVpcConfiguration = AwsVpcConfiguration


@dataclass
class CapacityProviderStrategyItem(BaseModel):
    CapacityProvider: Optional[str]
    Weight: Optional[float]
    Base: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CapacityProviderStrategyItem"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CapacityProviderStrategyItem"]:
        if not json_data:
            return None
        return cls(
            CapacityProvider=json_data.get("CapacityProvider"),
            Weight=json_data.get("Weight"),
            Base=json_data.get("Base"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CapacityProviderStrategyItem = CapacityProviderStrategyItem


@dataclass
class PlacementConstraint(BaseModel):
    Type: Optional[str]
    Expression: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PlacementConstraint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlacementConstraint"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Expression=json_data.get("Expression"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlacementConstraint = PlacementConstraint


@dataclass
class PlacementStrategy(BaseModel):
    Type: Optional[str]
    Field: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PlacementStrategy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlacementStrategy"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Field=json_data.get("Field"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlacementStrategy = PlacementStrategy


@dataclass
class EventBridgeParameters(BaseModel):
    DetailType: Optional[str]
    Source: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EventBridgeParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EventBridgeParameters"]:
        if not json_data:
            return None
        return cls(
            DetailType=json_data.get("DetailType"),
            Source=json_data.get("Source"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EventBridgeParameters = EventBridgeParameters


@dataclass
class KinesisParameters(BaseModel):
    PartitionKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KinesisParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KinesisParameters"]:
        if not json_data:
            return None
        return cls(
            PartitionKey=json_data.get("PartitionKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KinesisParameters = KinesisParameters


@dataclass
class SageMakerPipelineParameters(BaseModel):
    PipelineParameterList: Optional[Sequence["_SageMakerPipelineParameter"]]

    @classmethod
    def _deserialize(
        cls: Type["_SageMakerPipelineParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SageMakerPipelineParameters"]:
        if not json_data:
            return None
        return cls(
            PipelineParameterList=deserialize_list(json_data.get("PipelineParameterList"), SageMakerPipelineParameter),
        )


# work around possible type aliasing issues when variable has same name as a model
_SageMakerPipelineParameters = SageMakerPipelineParameters


@dataclass
class SageMakerPipelineParameter(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SageMakerPipelineParameter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SageMakerPipelineParameter"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SageMakerPipelineParameter = SageMakerPipelineParameter


@dataclass
class SqsParameters(BaseModel):
    MessageGroupId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SqsParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SqsParameters"]:
        if not json_data:
            return None
        return cls(
            MessageGroupId=json_data.get("MessageGroupId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SqsParameters = SqsParameters


