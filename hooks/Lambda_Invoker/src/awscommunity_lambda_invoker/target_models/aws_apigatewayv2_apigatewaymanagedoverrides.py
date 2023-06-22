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
class AwsApigatewayv2Apigatewaymanagedoverrides(BaseModel):
    Stage: Optional["_StageOverrides"]
    Integration: Optional["_IntegrationOverrides"]
    Id: Optional[str]
    ApiId: Optional[str]
    Route: Optional["_RouteOverrides"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsApigatewayv2Apigatewaymanagedoverrides"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsApigatewayv2Apigatewaymanagedoverrides"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Stage=StageOverrides._deserialize(json_data.get("Stage")),
            Integration=IntegrationOverrides._deserialize(json_data.get("Integration")),
            Id=json_data.get("Id"),
            ApiId=json_data.get("ApiId"),
            Route=RouteOverrides._deserialize(json_data.get("Route")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsApigatewayv2Apigatewaymanagedoverrides = AwsApigatewayv2Apigatewaymanagedoverrides


@dataclass
class StageOverrides(BaseModel):
    Description: Optional[str]
    AccessLogSettings: Optional["_AccessLogSettings"]
    AutoDeploy: Optional[bool]
    RouteSettings: Optional[MutableMapping[str, Any]]
    StageVariables: Optional[MutableMapping[str, Any]]
    DefaultRouteSettings: Optional["_RouteSettings"]

    @classmethod
    def _deserialize(
        cls: Type["_StageOverrides"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StageOverrides"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            AccessLogSettings=AccessLogSettings._deserialize(json_data.get("AccessLogSettings")),
            AutoDeploy=json_data.get("AutoDeploy"),
            RouteSettings=json_data.get("RouteSettings"),
            StageVariables=json_data.get("StageVariables"),
            DefaultRouteSettings=RouteSettings._deserialize(json_data.get("DefaultRouteSettings")),
        )


# work around possible type aliasing issues when variable has same name as a model
_StageOverrides = StageOverrides


@dataclass
class AccessLogSettings(BaseModel):
    DestinationArn: Optional[str]
    Format: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AccessLogSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessLogSettings"]:
        if not json_data:
            return None
        return cls(
            DestinationArn=json_data.get("DestinationArn"),
            Format=json_data.get("Format"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessLogSettings = AccessLogSettings


@dataclass
class RouteSettings(BaseModel):
    DetailedMetricsEnabled: Optional[bool]
    LoggingLevel: Optional[str]
    DataTraceEnabled: Optional[bool]
    ThrottlingBurstLimit: Optional[int]
    ThrottlingRateLimit: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RouteSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RouteSettings"]:
        if not json_data:
            return None
        return cls(
            DetailedMetricsEnabled=json_data.get("DetailedMetricsEnabled"),
            LoggingLevel=json_data.get("LoggingLevel"),
            DataTraceEnabled=json_data.get("DataTraceEnabled"),
            ThrottlingBurstLimit=json_data.get("ThrottlingBurstLimit"),
            ThrottlingRateLimit=json_data.get("ThrottlingRateLimit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RouteSettings = RouteSettings


@dataclass
class IntegrationOverrides(BaseModel):
    TimeoutInMillis: Optional[int]
    Description: Optional[str]
    PayloadFormatVersion: Optional[str]
    IntegrationMethod: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IntegrationOverrides"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IntegrationOverrides"]:
        if not json_data:
            return None
        return cls(
            TimeoutInMillis=json_data.get("TimeoutInMillis"),
            Description=json_data.get("Description"),
            PayloadFormatVersion=json_data.get("PayloadFormatVersion"),
            IntegrationMethod=json_data.get("IntegrationMethod"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IntegrationOverrides = IntegrationOverrides


@dataclass
class RouteOverrides(BaseModel):
    AuthorizationScopes: Optional[Sequence[str]]
    Target: Optional[str]
    AuthorizationType: Optional[str]
    AuthorizerId: Optional[str]
    OperationName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RouteOverrides"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RouteOverrides"]:
        if not json_data:
            return None
        return cls(
            AuthorizationScopes=json_data.get("AuthorizationScopes"),
            Target=json_data.get("Target"),
            AuthorizationType=json_data.get("AuthorizationType"),
            AuthorizerId=json_data.get("AuthorizerId"),
            OperationName=json_data.get("OperationName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RouteOverrides = RouteOverrides


