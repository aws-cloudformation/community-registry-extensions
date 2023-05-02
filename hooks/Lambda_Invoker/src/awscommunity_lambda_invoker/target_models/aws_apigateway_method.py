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
class AwsApigatewayMethod(BaseModel):
    ApiKeyRequired: Optional[bool]
    AuthorizationScopes: Optional[Sequence[str]]
    AuthorizationType: Optional[str]
    AuthorizerId: Optional[str]
    HttpMethod: Optional[str]
    Integration: Optional["_Integration"]
    MethodResponses: Optional[Sequence["_MethodResponse"]]
    OperationName: Optional[str]
    RequestModels: Optional[MutableMapping[str, str]]
    RequestParameters: Optional[MutableMapping[str, bool]]
    RequestValidatorId: Optional[str]
    ResourceId: Optional[str]
    RestApiId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsApigatewayMethod"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsApigatewayMethod"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ApiKeyRequired=json_data.get("ApiKeyRequired"),
            AuthorizationScopes=json_data.get("AuthorizationScopes"),
            AuthorizationType=json_data.get("AuthorizationType"),
            AuthorizerId=json_data.get("AuthorizerId"),
            HttpMethod=json_data.get("HttpMethod"),
            Integration=Integration._deserialize(json_data.get("Integration")),
            MethodResponses=deserialize_list(json_data.get("MethodResponses"), MethodResponse),
            OperationName=json_data.get("OperationName"),
            RequestModels=json_data.get("RequestModels"),
            RequestParameters=json_data.get("RequestParameters"),
            RequestValidatorId=json_data.get("RequestValidatorId"),
            ResourceId=json_data.get("ResourceId"),
            RestApiId=json_data.get("RestApiId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsApigatewayMethod = AwsApigatewayMethod


@dataclass
class Integration(BaseModel):
    CacheKeyParameters: Optional[Sequence[str]]
    CacheNamespace: Optional[str]
    ConnectionId: Optional[str]
    ConnectionType: Optional[str]
    ContentHandling: Optional[str]
    Credentials: Optional[str]
    IntegrationHttpMethod: Optional[str]
    IntegrationResponses: Optional[Sequence["_IntegrationResponse"]]
    PassthroughBehavior: Optional[str]
    RequestParameters: Optional[MutableMapping[str, str]]
    RequestTemplates: Optional[MutableMapping[str, str]]
    TimeoutInMillis: Optional[int]
    Type: Optional[str]
    Uri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Integration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Integration"]:
        if not json_data:
            return None
        return cls(
            CacheKeyParameters=json_data.get("CacheKeyParameters"),
            CacheNamespace=json_data.get("CacheNamespace"),
            ConnectionId=json_data.get("ConnectionId"),
            ConnectionType=json_data.get("ConnectionType"),
            ContentHandling=json_data.get("ContentHandling"),
            Credentials=json_data.get("Credentials"),
            IntegrationHttpMethod=json_data.get("IntegrationHttpMethod"),
            IntegrationResponses=deserialize_list(json_data.get("IntegrationResponses"), IntegrationResponse),
            PassthroughBehavior=json_data.get("PassthroughBehavior"),
            RequestParameters=json_data.get("RequestParameters"),
            RequestTemplates=json_data.get("RequestTemplates"),
            TimeoutInMillis=json_data.get("TimeoutInMillis"),
            Type=json_data.get("Type"),
            Uri=json_data.get("Uri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Integration = Integration


@dataclass
class IntegrationResponse(BaseModel):
    ContentHandling: Optional[str]
    ResponseParameters: Optional[MutableMapping[str, str]]
    ResponseTemplates: Optional[MutableMapping[str, str]]
    SelectionPattern: Optional[str]
    StatusCode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IntegrationResponse"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IntegrationResponse"]:
        if not json_data:
            return None
        return cls(
            ContentHandling=json_data.get("ContentHandling"),
            ResponseParameters=json_data.get("ResponseParameters"),
            ResponseTemplates=json_data.get("ResponseTemplates"),
            SelectionPattern=json_data.get("SelectionPattern"),
            StatusCode=json_data.get("StatusCode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IntegrationResponse = IntegrationResponse


@dataclass
class MethodResponse(BaseModel):
    ResponseModels: Optional[MutableMapping[str, str]]
    ResponseParameters: Optional[MutableMapping[str, bool]]
    StatusCode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MethodResponse"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MethodResponse"]:
        if not json_data:
            return None
        return cls(
            ResponseModels=json_data.get("ResponseModels"),
            ResponseParameters=json_data.get("ResponseParameters"),
            StatusCode=json_data.get("StatusCode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MethodResponse = MethodResponse


