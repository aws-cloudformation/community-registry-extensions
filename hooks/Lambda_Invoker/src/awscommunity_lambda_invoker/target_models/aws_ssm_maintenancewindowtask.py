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
class AwsSsmMaintenancewindowtask(BaseModel):
    MaxErrors: Optional[str]
    Description: Optional[str]
    ServiceRoleArn: Optional[str]
    Priority: Optional[int]
    MaxConcurrency: Optional[str]
    Targets: Optional[Sequence["_Target"]]
    Name: Optional[str]
    TaskArn: Optional[str]
    TaskInvocationParameters: Optional["_TaskInvocationParameters"]
    WindowId: Optional[str]
    TaskParameters: Optional[MutableMapping[str, Any]]
    TaskType: Optional[str]
    CutoffBehavior: Optional[str]
    Id: Optional[str]
    LoggingInfo: Optional["_LoggingInfo"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSsmMaintenancewindowtask"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSsmMaintenancewindowtask"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            MaxErrors=json_data.get("MaxErrors"),
            Description=json_data.get("Description"),
            ServiceRoleArn=json_data.get("ServiceRoleArn"),
            Priority=json_data.get("Priority"),
            MaxConcurrency=json_data.get("MaxConcurrency"),
            Targets=deserialize_list(json_data.get("Targets"), Target),
            Name=json_data.get("Name"),
            TaskArn=json_data.get("TaskArn"),
            TaskInvocationParameters=TaskInvocationParameters._deserialize(json_data.get("TaskInvocationParameters")),
            WindowId=json_data.get("WindowId"),
            TaskParameters=json_data.get("TaskParameters"),
            TaskType=json_data.get("TaskType"),
            CutoffBehavior=json_data.get("CutoffBehavior"),
            Id=json_data.get("Id"),
            LoggingInfo=LoggingInfo._deserialize(json_data.get("LoggingInfo")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSsmMaintenancewindowtask = AwsSsmMaintenancewindowtask


@dataclass
class Target(BaseModel):
    Values: Optional[Sequence[str]]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Target"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Target"]:
        if not json_data:
            return None
        return cls(
            Values=json_data.get("Values"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Target = Target


@dataclass
class TaskInvocationParameters(BaseModel):
    MaintenanceWindowStepFunctionsParameters: Optional["_MaintenanceWindowStepFunctionsParameters"]
    MaintenanceWindowRunCommandParameters: Optional["_MaintenanceWindowRunCommandParameters"]
    MaintenanceWindowLambdaParameters: Optional["_MaintenanceWindowLambdaParameters"]
    MaintenanceWindowAutomationParameters: Optional["_MaintenanceWindowAutomationParameters"]

    @classmethod
    def _deserialize(
        cls: Type["_TaskInvocationParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TaskInvocationParameters"]:
        if not json_data:
            return None
        return cls(
            MaintenanceWindowStepFunctionsParameters=MaintenanceWindowStepFunctionsParameters._deserialize(json_data.get("MaintenanceWindowStepFunctionsParameters")),
            MaintenanceWindowRunCommandParameters=MaintenanceWindowRunCommandParameters._deserialize(json_data.get("MaintenanceWindowRunCommandParameters")),
            MaintenanceWindowLambdaParameters=MaintenanceWindowLambdaParameters._deserialize(json_data.get("MaintenanceWindowLambdaParameters")),
            MaintenanceWindowAutomationParameters=MaintenanceWindowAutomationParameters._deserialize(json_data.get("MaintenanceWindowAutomationParameters")),
        )


# work around possible type aliasing issues when variable has same name as a model
_TaskInvocationParameters = TaskInvocationParameters


@dataclass
class MaintenanceWindowStepFunctionsParameters(BaseModel):
    Input: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MaintenanceWindowStepFunctionsParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MaintenanceWindowStepFunctionsParameters"]:
        if not json_data:
            return None
        return cls(
            Input=json_data.get("Input"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MaintenanceWindowStepFunctionsParameters = MaintenanceWindowStepFunctionsParameters


@dataclass
class MaintenanceWindowRunCommandParameters(BaseModel):
    TimeoutSeconds: Optional[int]
    Comment: Optional[str]
    OutputS3KeyPrefix: Optional[str]
    Parameters: Optional[MutableMapping[str, Any]]
    CloudWatchOutputConfig: Optional["_CloudWatchOutputConfig"]
    DocumentHashType: Optional[str]
    ServiceRoleArn: Optional[str]
    NotificationConfig: Optional["_NotificationConfig"]
    DocumentVersion: Optional[str]
    OutputS3BucketName: Optional[str]
    DocumentHash: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MaintenanceWindowRunCommandParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MaintenanceWindowRunCommandParameters"]:
        if not json_data:
            return None
        return cls(
            TimeoutSeconds=json_data.get("TimeoutSeconds"),
            Comment=json_data.get("Comment"),
            OutputS3KeyPrefix=json_data.get("OutputS3KeyPrefix"),
            Parameters=json_data.get("Parameters"),
            CloudWatchOutputConfig=CloudWatchOutputConfig._deserialize(json_data.get("CloudWatchOutputConfig")),
            DocumentHashType=json_data.get("DocumentHashType"),
            ServiceRoleArn=json_data.get("ServiceRoleArn"),
            NotificationConfig=NotificationConfig._deserialize(json_data.get("NotificationConfig")),
            DocumentVersion=json_data.get("DocumentVersion"),
            OutputS3BucketName=json_data.get("OutputS3BucketName"),
            DocumentHash=json_data.get("DocumentHash"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MaintenanceWindowRunCommandParameters = MaintenanceWindowRunCommandParameters


@dataclass
class CloudWatchOutputConfig(BaseModel):
    CloudWatchOutputEnabled: Optional[bool]
    CloudWatchLogGroupName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CloudWatchOutputConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudWatchOutputConfig"]:
        if not json_data:
            return None
        return cls(
            CloudWatchOutputEnabled=json_data.get("CloudWatchOutputEnabled"),
            CloudWatchLogGroupName=json_data.get("CloudWatchLogGroupName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudWatchOutputConfig = CloudWatchOutputConfig


@dataclass
class NotificationConfig(BaseModel):
    NotificationEvents: Optional[Sequence[str]]
    NotificationArn: Optional[str]
    NotificationType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NotificationConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NotificationConfig"]:
        if not json_data:
            return None
        return cls(
            NotificationEvents=json_data.get("NotificationEvents"),
            NotificationArn=json_data.get("NotificationArn"),
            NotificationType=json_data.get("NotificationType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NotificationConfig = NotificationConfig


@dataclass
class MaintenanceWindowLambdaParameters(BaseModel):
    Qualifier: Optional[str]
    Payload: Optional[str]
    ClientContext: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MaintenanceWindowLambdaParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MaintenanceWindowLambdaParameters"]:
        if not json_data:
            return None
        return cls(
            Qualifier=json_data.get("Qualifier"),
            Payload=json_data.get("Payload"),
            ClientContext=json_data.get("ClientContext"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MaintenanceWindowLambdaParameters = MaintenanceWindowLambdaParameters


@dataclass
class MaintenanceWindowAutomationParameters(BaseModel):
    Parameters: Optional[MutableMapping[str, Any]]
    DocumentVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MaintenanceWindowAutomationParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MaintenanceWindowAutomationParameters"]:
        if not json_data:
            return None
        return cls(
            Parameters=json_data.get("Parameters"),
            DocumentVersion=json_data.get("DocumentVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MaintenanceWindowAutomationParameters = MaintenanceWindowAutomationParameters


@dataclass
class LoggingInfo(BaseModel):
    Region: Optional[str]
    S3Prefix: Optional[str]
    S3Bucket: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingInfo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingInfo"]:
        if not json_data:
            return None
        return cls(
            Region=json_data.get("Region"),
            S3Prefix=json_data.get("S3Prefix"),
            S3Bucket=json_data.get("S3Bucket"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingInfo = LoggingInfo


