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
class AwsApigatewayDeployment(BaseModel):
    DeploymentId: Optional[str]
    DeploymentCanarySettings: Optional["_DeploymentCanarySettings"]
    Description: Optional[str]
    RestApiId: Optional[str]
    StageDescription: Optional["_StageDescription"]
    StageName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsApigatewayDeployment"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsApigatewayDeployment"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            DeploymentId=json_data.get("DeploymentId"),
            DeploymentCanarySettings=DeploymentCanarySettings._deserialize(json_data.get("DeploymentCanarySettings")),
            Description=json_data.get("Description"),
            RestApiId=json_data.get("RestApiId"),
            StageDescription=StageDescription._deserialize(json_data.get("StageDescription")),
            StageName=json_data.get("StageName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsApigatewayDeployment = AwsApigatewayDeployment


@dataclass
class DeploymentCanarySettings(BaseModel):
    PercentTraffic: Optional[float]
    StageVariableOverrides: Optional[MutableMapping[str, str]]
    UseStageCache: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_DeploymentCanarySettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeploymentCanarySettings"]:
        if not json_data:
            return None
        return cls(
            PercentTraffic=json_data.get("PercentTraffic"),
            StageVariableOverrides=json_data.get("StageVariableOverrides"),
            UseStageCache=json_data.get("UseStageCache"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeploymentCanarySettings = DeploymentCanarySettings


@dataclass
class StageDescription(BaseModel):
    AccessLogSetting: Optional["_AccessLogSetting"]
    CacheClusterEnabled: Optional[bool]
    CacheClusterSize: Optional[str]
    CacheDataEncrypted: Optional[bool]
    CacheTtlInSeconds: Optional[int]
    CachingEnabled: Optional[bool]
    CanarySetting: Optional["_CanarySetting"]
    ClientCertificateId: Optional[str]
    DataTraceEnabled: Optional[bool]
    Description: Optional[str]
    DocumentationVersion: Optional[str]
    LoggingLevel: Optional[str]
    MethodSettings: Optional[AbstractSet["_MethodSetting"]]
    MetricsEnabled: Optional[bool]
    Tags: Optional[Sequence["_Tag"]]
    ThrottlingBurstLimit: Optional[int]
    ThrottlingRateLimit: Optional[float]
    TracingEnabled: Optional[bool]
    Variables: Optional[MutableMapping[str, str]]

    @classmethod
    def _deserialize(
        cls: Type["_StageDescription"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StageDescription"]:
        if not json_data:
            return None
        return cls(
            AccessLogSetting=AccessLogSetting._deserialize(json_data.get("AccessLogSetting")),
            CacheClusterEnabled=json_data.get("CacheClusterEnabled"),
            CacheClusterSize=json_data.get("CacheClusterSize"),
            CacheDataEncrypted=json_data.get("CacheDataEncrypted"),
            CacheTtlInSeconds=json_data.get("CacheTtlInSeconds"),
            CachingEnabled=json_data.get("CachingEnabled"),
            CanarySetting=CanarySetting._deserialize(json_data.get("CanarySetting")),
            ClientCertificateId=json_data.get("ClientCertificateId"),
            DataTraceEnabled=json_data.get("DataTraceEnabled"),
            Description=json_data.get("Description"),
            DocumentationVersion=json_data.get("DocumentationVersion"),
            LoggingLevel=json_data.get("LoggingLevel"),
            MethodSettings=set_or_none(json_data.get("MethodSettings")),
            MetricsEnabled=json_data.get("MetricsEnabled"),
            Tags=deserialize_list(json_data.get("Tags"), Tag),
            ThrottlingBurstLimit=json_data.get("ThrottlingBurstLimit"),
            ThrottlingRateLimit=json_data.get("ThrottlingRateLimit"),
            TracingEnabled=json_data.get("TracingEnabled"),
            Variables=json_data.get("Variables"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StageDescription = StageDescription


@dataclass
class AccessLogSetting(BaseModel):
    DestinationArn: Optional[str]
    Format: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AccessLogSetting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessLogSetting"]:
        if not json_data:
            return None
        return cls(
            DestinationArn=json_data.get("DestinationArn"),
            Format=json_data.get("Format"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessLogSetting = AccessLogSetting


@dataclass
class CanarySetting(BaseModel):
    PercentTraffic: Optional[float]
    StageVariableOverrides: Optional[MutableMapping[str, str]]
    UseStageCache: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_CanarySetting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CanarySetting"]:
        if not json_data:
            return None
        return cls(
            PercentTraffic=json_data.get("PercentTraffic"),
            StageVariableOverrides=json_data.get("StageVariableOverrides"),
            UseStageCache=json_data.get("UseStageCache"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CanarySetting = CanarySetting


@dataclass
class MethodSetting(BaseModel):
    CacheDataEncrypted: Optional[bool]
    CacheTtlInSeconds: Optional[int]
    CachingEnabled: Optional[bool]
    DataTraceEnabled: Optional[bool]
    HttpMethod: Optional[str]
    LoggingLevel: Optional[str]
    MetricsEnabled: Optional[bool]
    ResourcePath: Optional[str]
    ThrottlingBurstLimit: Optional[int]
    ThrottlingRateLimit: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_MethodSetting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MethodSetting"]:
        if not json_data:
            return None
        return cls(
            CacheDataEncrypted=json_data.get("CacheDataEncrypted"),
            CacheTtlInSeconds=json_data.get("CacheTtlInSeconds"),
            CachingEnabled=json_data.get("CachingEnabled"),
            DataTraceEnabled=json_data.get("DataTraceEnabled"),
            HttpMethod=json_data.get("HttpMethod"),
            LoggingLevel=json_data.get("LoggingLevel"),
            MetricsEnabled=json_data.get("MetricsEnabled"),
            ResourcePath=json_data.get("ResourcePath"),
            ThrottlingBurstLimit=json_data.get("ThrottlingBurstLimit"),
            ThrottlingRateLimit=json_data.get("ThrottlingRateLimit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MethodSetting = MethodSetting


@dataclass
class Tag(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tag"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tag = Tag


