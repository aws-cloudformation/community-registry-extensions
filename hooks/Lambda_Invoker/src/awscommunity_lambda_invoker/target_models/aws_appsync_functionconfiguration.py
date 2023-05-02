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
class AwsAppsyncFunctionconfiguration(BaseModel):
    FunctionId: Optional[str]
    FunctionArn: Optional[str]
    Description: Optional[str]
    RequestMappingTemplate: Optional[str]
    ResponseMappingTemplate: Optional[str]
    MaxBatchSize: Optional[int]
    SyncConfig: Optional["_SyncConfig"]
    Code: Optional[str]
    Name: Optional[str]
    ResponseMappingTemplateS3Location: Optional[str]
    Runtime: Optional["_AppSyncRuntime"]
    CodeS3Location: Optional[str]
    DataSourceName: Optional[str]
    FunctionVersion: Optional[str]
    Id: Optional[str]
    RequestMappingTemplateS3Location: Optional[str]
    ApiId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAppsyncFunctionconfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAppsyncFunctionconfiguration"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            FunctionId=json_data.get("FunctionId"),
            FunctionArn=json_data.get("FunctionArn"),
            Description=json_data.get("Description"),
            RequestMappingTemplate=json_data.get("RequestMappingTemplate"),
            ResponseMappingTemplate=json_data.get("ResponseMappingTemplate"),
            MaxBatchSize=json_data.get("MaxBatchSize"),
            SyncConfig=SyncConfig._deserialize(json_data.get("SyncConfig")),
            Code=json_data.get("Code"),
            Name=json_data.get("Name"),
            ResponseMappingTemplateS3Location=json_data.get("ResponseMappingTemplateS3Location"),
            Runtime=AppSyncRuntime._deserialize(json_data.get("Runtime")),
            CodeS3Location=json_data.get("CodeS3Location"),
            DataSourceName=json_data.get("DataSourceName"),
            FunctionVersion=json_data.get("FunctionVersion"),
            Id=json_data.get("Id"),
            RequestMappingTemplateS3Location=json_data.get("RequestMappingTemplateS3Location"),
            ApiId=json_data.get("ApiId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAppsyncFunctionconfiguration = AwsAppsyncFunctionconfiguration


@dataclass
class SyncConfig(BaseModel):
    ConflictHandler: Optional[str]
    ConflictDetection: Optional[str]
    LambdaConflictHandlerConfig: Optional["_LambdaConflictHandlerConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_SyncConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SyncConfig"]:
        if not json_data:
            return None
        return cls(
            ConflictHandler=json_data.get("ConflictHandler"),
            ConflictDetection=json_data.get("ConflictDetection"),
            LambdaConflictHandlerConfig=LambdaConflictHandlerConfig._deserialize(json_data.get("LambdaConflictHandlerConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SyncConfig = SyncConfig


@dataclass
class LambdaConflictHandlerConfig(BaseModel):
    LambdaConflictHandlerArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LambdaConflictHandlerConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LambdaConflictHandlerConfig"]:
        if not json_data:
            return None
        return cls(
            LambdaConflictHandlerArn=json_data.get("LambdaConflictHandlerArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LambdaConflictHandlerConfig = LambdaConflictHandlerConfig


@dataclass
class AppSyncRuntime(BaseModel):
    RuntimeVersion: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AppSyncRuntime"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AppSyncRuntime"]:
        if not json_data:
            return None
        return cls(
            RuntimeVersion=json_data.get("RuntimeVersion"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AppSyncRuntime = AppSyncRuntime


