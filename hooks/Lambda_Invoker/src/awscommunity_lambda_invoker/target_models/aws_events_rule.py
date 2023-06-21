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
class AwsEventsRule(BaseModel):
    EventBusName: Optional[str]
    EventPattern: Optional[MutableMapping[str, Any]]
    ScheduleExpression: Optional[str]
    Description: Optional[str]
    State: Optional[str]
    Targets: Optional[Sequence["_Target"]]
    Id: Optional[str]
    Arn: Optional[str]
    RoleArn: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEventsRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEventsRule"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            EventBusName=json_data.get("EventBusName"),
            EventPattern=json_data.get("EventPattern"),
            ScheduleExpression=json_data.get("ScheduleExpression"),
            Description=json_data.get("Description"),
            State=json_data.get("State"),
            Targets=deserialize_list(json_data.get("Targets"), Target),
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            RoleArn=json_data.get("RoleArn"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEventsRule = AwsEventsRule


@dataclass
class Target(BaseModel):
    InputPath: Optional[str]
    HttpParameters: Optional["_HttpParameters"]
    DeadLetterConfig: Optional["_DeadLetterConfig"]
    RunCommandParameters: Optional["_RunCommandParameters"]
    InputTransformer: Optional["_InputTransformer"]
    KinesisParameters: Optional["_KinesisParameters"]
    RoleArn: Optional[str]
    RedshiftDataParameters: Optional["_RedshiftDataParameters"]
    Input: Optional[str]
    SqsParameters: Optional["_SqsParameters"]
    EcsParameters: Optional["_EcsParameters"]
    BatchParameters: Optional["_BatchParameters"]
    Id: Optional[str]
    Arn: Optional[str]
    SageMakerPipelineParameters: Optional["_SageMakerPipelineParameters"]
    RetryPolicy: Optional["_RetryPolicy"]

    @classmethod
    def _deserialize(
        cls: Type["_Target"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Target"]:
        if not json_data:
            return None
        return cls(
            InputPath=json_data.get("InputPath"),
            HttpParameters=HttpParameters._deserialize(json_data.get("HttpParameters")),
            DeadLetterConfig=DeadLetterConfig._deserialize(json_data.get("DeadLetterConfig")),
            RunCommandParameters=RunCommandParameters._deserialize(json_data.get("RunCommandParameters")),
            InputTransformer=InputTransformer._deserialize(json_data.get("InputTransformer")),
            KinesisParameters=KinesisParameters._deserialize(json_data.get("KinesisParameters")),
            RoleArn=json_data.get("RoleArn"),
            RedshiftDataParameters=RedshiftDataParameters._deserialize(json_data.get("RedshiftDataParameters")),
            Input=json_data.get("Input"),
            SqsParameters=SqsParameters._deserialize(json_data.get("SqsParameters")),
            EcsParameters=EcsParameters._deserialize(json_data.get("EcsParameters")),
            BatchParameters=BatchParameters._deserialize(json_data.get("BatchParameters")),
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            SageMakerPipelineParameters=SageMakerPipelineParameters._deserialize(json_data.get("SageMakerPipelineParameters")),
            RetryPolicy=RetryPolicy._deserialize(json_data.get("RetryPolicy")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Target = Target


@dataclass
class HttpParameters(BaseModel):
    PathParameterValues: Optional[Sequence[str]]
    HeaderParameters: Optional[MutableMapping[str, str]]
    QueryStringParameters: Optional[MutableMapping[str, str]]

    @classmethod
    def _deserialize(
        cls: Type["_HttpParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpParameters"]:
        if not json_data:
            return None
        return cls(
            PathParameterValues=json_data.get("PathParameterValues"),
            HeaderParameters=json_data.get("HeaderParameters"),
            QueryStringParameters=json_data.get("QueryStringParameters"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpParameters = HttpParameters


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
class RunCommandParameters(BaseModel):
    RunCommandTargets: Optional[Sequence["_RunCommandTarget"]]

    @classmethod
    def _deserialize(
        cls: Type["_RunCommandParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RunCommandParameters"]:
        if not json_data:
            return None
        return cls(
            RunCommandTargets=deserialize_list(json_data.get("RunCommandTargets"), RunCommandTarget),
        )


# work around possible type aliasing issues when variable has same name as a model
_RunCommandParameters = RunCommandParameters


@dataclass
class RunCommandTarget(BaseModel):
    Values: Optional[Sequence[str]]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RunCommandTarget"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RunCommandTarget"]:
        if not json_data:
            return None
        return cls(
            Values=json_data.get("Values"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RunCommandTarget = RunCommandTarget


@dataclass
class InputTransformer(BaseModel):
    InputTemplate: Optional[str]
    InputPathsMap: Optional[MutableMapping[str, str]]

    @classmethod
    def _deserialize(
        cls: Type["_InputTransformer"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputTransformer"]:
        if not json_data:
            return None
        return cls(
            InputTemplate=json_data.get("InputTemplate"),
            InputPathsMap=json_data.get("InputPathsMap"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputTransformer = InputTransformer


@dataclass
class KinesisParameters(BaseModel):
    PartitionKeyPath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KinesisParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KinesisParameters"]:
        if not json_data:
            return None
        return cls(
            PartitionKeyPath=json_data.get("PartitionKeyPath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KinesisParameters = KinesisParameters


@dataclass
class RedshiftDataParameters(BaseModel):
    StatementName: Optional[str]
    Database: Optional[str]
    SecretManagerArn: Optional[str]
    DbUser: Optional[str]
    Sql: Optional[str]
    WithEvent: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_RedshiftDataParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RedshiftDataParameters"]:
        if not json_data:
            return None
        return cls(
            StatementName=json_data.get("StatementName"),
            Database=json_data.get("Database"),
            SecretManagerArn=json_data.get("SecretManagerArn"),
            DbUser=json_data.get("DbUser"),
            Sql=json_data.get("Sql"),
            WithEvent=json_data.get("WithEvent"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RedshiftDataParameters = RedshiftDataParameters


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


@dataclass
class EcsParameters(BaseModel):
    PlatformVersion: Optional[str]
    Group: Optional[str]
    EnableECSManagedTags: Optional[bool]
    EnableExecuteCommand: Optional[bool]
    PlacementConstraints: Optional[Sequence["_PlacementConstraint"]]
    PropagateTags: Optional[str]
    TaskCount: Optional[int]
    PlacementStrategies: Optional[Sequence["_PlacementStrategy"]]
    CapacityProviderStrategy: Optional[Sequence["_CapacityProviderStrategyItem"]]
    LaunchType: Optional[str]
    ReferenceId: Optional[str]
    TagList: Optional[Sequence["_Tag"]]
    NetworkConfiguration: Optional["_NetworkConfiguration"]
    TaskDefinitionArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EcsParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EcsParameters"]:
        if not json_data:
            return None
        return cls(
            PlatformVersion=json_data.get("PlatformVersion"),
            Group=json_data.get("Group"),
            EnableECSManagedTags=json_data.get("EnableECSManagedTags"),
            EnableExecuteCommand=json_data.get("EnableExecuteCommand"),
            PlacementConstraints=deserialize_list(json_data.get("PlacementConstraints"), PlacementConstraint),
            PropagateTags=json_data.get("PropagateTags"),
            TaskCount=json_data.get("TaskCount"),
            PlacementStrategies=deserialize_list(json_data.get("PlacementStrategies"), PlacementStrategy),
            CapacityProviderStrategy=deserialize_list(json_data.get("CapacityProviderStrategy"), CapacityProviderStrategyItem),
            LaunchType=json_data.get("LaunchType"),
            ReferenceId=json_data.get("ReferenceId"),
            TagList=deserialize_list(json_data.get("TagList"), Tag),
            NetworkConfiguration=NetworkConfiguration._deserialize(json_data.get("NetworkConfiguration")),
            TaskDefinitionArn=json_data.get("TaskDefinitionArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EcsParameters = EcsParameters


@dataclass
class PlacementConstraint(BaseModel):
    Expression: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PlacementConstraint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlacementConstraint"]:
        if not json_data:
            return None
        return cls(
            Expression=json_data.get("Expression"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlacementConstraint = PlacementConstraint


@dataclass
class PlacementStrategy(BaseModel):
    Field: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PlacementStrategy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlacementStrategy"]:
        if not json_data:
            return None
        return cls(
            Field=json_data.get("Field"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlacementStrategy = PlacementStrategy


@dataclass
class CapacityProviderStrategyItem(BaseModel):
    Base: Optional[int]
    Weight: Optional[int]
    CapacityProvider: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CapacityProviderStrategyItem"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CapacityProviderStrategyItem"]:
        if not json_data:
            return None
        return cls(
            Base=json_data.get("Base"),
            Weight=json_data.get("Weight"),
            CapacityProvider=json_data.get("CapacityProvider"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CapacityProviderStrategyItem = CapacityProviderStrategyItem


@dataclass
class Tag(BaseModel):
    Value: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tag"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tag = Tag


@dataclass
class NetworkConfiguration(BaseModel):
    AwsVpcConfiguration: Optional["_AwsVpcConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkConfiguration"]:
        if not json_data:
            return None
        return cls(
            AwsVpcConfiguration=AwsVpcConfiguration._deserialize(json_data.get("AwsVpcConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkConfiguration = NetworkConfiguration


@dataclass
class AwsVpcConfiguration(BaseModel):
    SecurityGroups: Optional[Sequence[str]]
    Subnets: Optional[Sequence[str]]
    AssignPublicIp: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsVpcConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsVpcConfiguration"]:
        if not json_data:
            return None
        return cls(
            SecurityGroups=json_data.get("SecurityGroups"),
            Subnets=json_data.get("Subnets"),
            AssignPublicIp=json_data.get("AssignPublicIp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsVpcConfiguration = AwsVpcConfiguration


@dataclass
class BatchParameters(BaseModel):
    JobName: Optional[str]
    RetryStrategy: Optional["_BatchRetryStrategy"]
    ArrayProperties: Optional["_BatchArrayProperties"]
    JobDefinition: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BatchParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BatchParameters"]:
        if not json_data:
            return None
        return cls(
            JobName=json_data.get("JobName"),
            RetryStrategy=BatchRetryStrategy._deserialize(json_data.get("RetryStrategy")),
            ArrayProperties=BatchArrayProperties._deserialize(json_data.get("ArrayProperties")),
            JobDefinition=json_data.get("JobDefinition"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BatchParameters = BatchParameters


@dataclass
class BatchRetryStrategy(BaseModel):
    Attempts: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_BatchRetryStrategy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BatchRetryStrategy"]:
        if not json_data:
            return None
        return cls(
            Attempts=json_data.get("Attempts"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BatchRetryStrategy = BatchRetryStrategy


@dataclass
class BatchArrayProperties(BaseModel):
    Size: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_BatchArrayProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BatchArrayProperties"]:
        if not json_data:
            return None
        return cls(
            Size=json_data.get("Size"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BatchArrayProperties = BatchArrayProperties


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
    Value: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SageMakerPipelineParameter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SageMakerPipelineParameter"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SageMakerPipelineParameter = SageMakerPipelineParameter


@dataclass
class RetryPolicy(BaseModel):
    MaximumEventAgeInSeconds: Optional[int]
    MaximumRetryAttempts: Optional[int]

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


