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
class AwsApigatewayv2Integration(BaseModel):
    Description: Optional[str]
    TemplateSelectionExpression: Optional[str]
    ConnectionType: Optional[str]
    ResponseParameters: Optional[MutableMapping[str, Any]]
    IntegrationMethod: Optional[str]
    PassthroughBehavior: Optional[str]
    RequestParameters: Optional[MutableMapping[str, Any]]
    ConnectionId: Optional[str]
    IntegrationUri: Optional[str]
    PayloadFormatVersion: Optional[str]
    CredentialsArn: Optional[str]
    RequestTemplates: Optional[MutableMapping[str, Any]]
    TimeoutInMillis: Optional[int]
    TlsConfig: Optional["_TlsConfig"]
    ContentHandlingStrategy: Optional[str]
    Id: Optional[str]
    IntegrationSubtype: Optional[str]
    ApiId: Optional[str]
    IntegrationType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsApigatewayv2Integration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsApigatewayv2Integration"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Description=json_data.get("Description"),
            TemplateSelectionExpression=json_data.get("TemplateSelectionExpression"),
            ConnectionType=json_data.get("ConnectionType"),
            ResponseParameters=json_data.get("ResponseParameters"),
            IntegrationMethod=json_data.get("IntegrationMethod"),
            PassthroughBehavior=json_data.get("PassthroughBehavior"),
            RequestParameters=json_data.get("RequestParameters"),
            ConnectionId=json_data.get("ConnectionId"),
            IntegrationUri=json_data.get("IntegrationUri"),
            PayloadFormatVersion=json_data.get("PayloadFormatVersion"),
            CredentialsArn=json_data.get("CredentialsArn"),
            RequestTemplates=json_data.get("RequestTemplates"),
            TimeoutInMillis=json_data.get("TimeoutInMillis"),
            TlsConfig=TlsConfig._deserialize(json_data.get("TlsConfig")),
            ContentHandlingStrategy=json_data.get("ContentHandlingStrategy"),
            Id=json_data.get("Id"),
            IntegrationSubtype=json_data.get("IntegrationSubtype"),
            ApiId=json_data.get("ApiId"),
            IntegrationType=json_data.get("IntegrationType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsApigatewayv2Integration = AwsApigatewayv2Integration


@dataclass
class TlsConfig(BaseModel):
    ServerNameToVerify: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TlsConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TlsConfig"]:
        if not json_data:
            return None
        return cls(
            ServerNameToVerify=json_data.get("ServerNameToVerify"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TlsConfig = TlsConfig


