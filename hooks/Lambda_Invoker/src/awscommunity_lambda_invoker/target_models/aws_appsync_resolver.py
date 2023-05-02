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
class AwsAppsyncResolver(BaseModel):
    TypeName: Optional[str]
    PipelineConfig: Optional["_PipelineConfig"]
    RequestMappingTemplate: Optional[str]
    ResponseMappingTemplate: Optional[str]
    MaxBatchSize: Optional[int]
    ResolverArn: Optional[str]
    SyncConfig: Optional["_SyncConfig"]
    Code: Optional[str]
    ResponseMappingTemplateS3Location: Optional[str]
    Runtime: Optional["_AppSyncRuntime"]
    CodeS3Location: Optional[str]
    DataSourceName: Optional[str]
    Kind: Optional[str]
    CachingConfig: Optional["_CachingConfig"]
    Id: Optional[str]
    RequestMappingTemplateS3Location: Optional[str]
    FieldName: Optional[str]
    ApiId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAppsyncResolver"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAppsyncResolver"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            TypeName=json_data.get("TypeName"),
            PipelineConfig=PipelineConfig._deserialize(json_data.get("PipelineConfig")),
            RequestMappingTemplate=json_data.get("RequestMappingTemplate"),
            ResponseMappingTemplate=json_data.get("ResponseMappingTemplate"),
            MaxBatchSize=json_data.get("MaxBatchSize"),
            ResolverArn=json_data.get("ResolverArn"),
            SyncConfig=SyncConfig._deserialize(json_data.get("SyncConfig")),
            Code=json_data.get("Code"),
            ResponseMappingTemplateS3Location=json_data.get("ResponseMappingTemplateS3Location"),
            Runtime=AppSyncRuntime._deserialize(json_data.get("Runtime")),
            CodeS3Location=json_data.get("CodeS3Location"),
            DataSourceName=json_data.get("DataSourceName"),
            Kind=json_data.get("Kind"),
            CachingConfig=CachingConfig._deserialize(json_data.get("CachingConfig")),
            Id=json_data.get("Id"),
            RequestMappingTemplateS3Location=json_data.get("RequestMappingTemplateS3Location"),
            FieldName=json_data.get("FieldName"),
            ApiId=json_data.get("ApiId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAppsyncResolver = AwsAppsyncResolver


@dataclass
class PipelineConfig(BaseModel):
    Functions: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_PipelineConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PipelineConfig"]:
        if not json_data:
            return None
        return cls(
            Functions=json_data.get("Functions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PipelineConfig = PipelineConfig


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


@dataclass
class CachingConfig(BaseModel):
    CachingKeys: Optional[Sequence[str]]
    Ttl: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CachingConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CachingConfig"]:
        if not json_data:
            return None
        return cls(
            CachingKeys=json_data.get("CachingKeys"),
            Ttl=json_data.get("Ttl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CachingConfig = CachingConfig


