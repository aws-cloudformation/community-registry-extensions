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
class AwsEventsConnection(BaseModel):
    Name: Optional[str]
    Arn: Optional[str]
    SecretArn: Optional[str]
    Description: Optional[str]
    AuthorizationType: Optional[str]
    AuthParameters: Optional["_AuthParameters"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEventsConnection"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEventsConnection"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Name=json_data.get("Name"),
            Arn=json_data.get("Arn"),
            SecretArn=json_data.get("SecretArn"),
            Description=json_data.get("Description"),
            AuthorizationType=json_data.get("AuthorizationType"),
            AuthParameters=AuthParameters._deserialize(json_data.get("AuthParameters")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEventsConnection = AwsEventsConnection


@dataclass
class AuthParameters(BaseModel):
    ApiKeyAuthParameters: Optional["_ApiKeyAuthParameters"]
    BasicAuthParameters: Optional["_BasicAuthParameters"]
    OAuthParameters: Optional["_OAuthParameters"]
    InvocationHttpParameters: Optional["_ConnectionHttpParameters"]

    @classmethod
    def _deserialize(
        cls: Type["_AuthParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthParameters"]:
        if not json_data:
            return None
        return cls(
            ApiKeyAuthParameters=ApiKeyAuthParameters._deserialize(json_data.get("ApiKeyAuthParameters")),
            BasicAuthParameters=BasicAuthParameters._deserialize(json_data.get("BasicAuthParameters")),
            OAuthParameters=OAuthParameters._deserialize(json_data.get("OAuthParameters")),
            InvocationHttpParameters=ConnectionHttpParameters._deserialize(json_data.get("InvocationHttpParameters")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthParameters = AuthParameters


@dataclass
class ApiKeyAuthParameters(BaseModel):
    ApiKeyName: Optional[str]
    ApiKeyValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ApiKeyAuthParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApiKeyAuthParameters"]:
        if not json_data:
            return None
        return cls(
            ApiKeyName=json_data.get("ApiKeyName"),
            ApiKeyValue=json_data.get("ApiKeyValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApiKeyAuthParameters = ApiKeyAuthParameters


@dataclass
class BasicAuthParameters(BaseModel):
    Username: Optional[str]
    Password: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BasicAuthParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BasicAuthParameters"]:
        if not json_data:
            return None
        return cls(
            Username=json_data.get("Username"),
            Password=json_data.get("Password"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BasicAuthParameters = BasicAuthParameters


@dataclass
class OAuthParameters(BaseModel):
    ClientParameters: Optional["_ClientParameters"]
    AuthorizationEndpoint: Optional[str]
    HttpMethod: Optional[str]
    OAuthHttpParameters: Optional["_ConnectionHttpParameters"]

    @classmethod
    def _deserialize(
        cls: Type["_OAuthParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OAuthParameters"]:
        if not json_data:
            return None
        return cls(
            ClientParameters=ClientParameters._deserialize(json_data.get("ClientParameters")),
            AuthorizationEndpoint=json_data.get("AuthorizationEndpoint"),
            HttpMethod=json_data.get("HttpMethod"),
            OAuthHttpParameters=ConnectionHttpParameters._deserialize(json_data.get("OAuthHttpParameters")),
        )


# work around possible type aliasing issues when variable has same name as a model
_OAuthParameters = OAuthParameters


@dataclass
class ClientParameters(BaseModel):
    ClientID: Optional[str]
    ClientSecret: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ClientParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientParameters"]:
        if not json_data:
            return None
        return cls(
            ClientID=json_data.get("ClientID"),
            ClientSecret=json_data.get("ClientSecret"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientParameters = ClientParameters


@dataclass
class ConnectionHttpParameters(BaseModel):
    HeaderParameters: Optional[Sequence["_Parameter"]]
    QueryStringParameters: Optional[Sequence["_Parameter"]]
    BodyParameters: Optional[Sequence["_Parameter"]]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectionHttpParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectionHttpParameters"]:
        if not json_data:
            return None
        return cls(
            HeaderParameters=deserialize_list(json_data.get("HeaderParameters"), Parameter),
            QueryStringParameters=deserialize_list(json_data.get("QueryStringParameters"), Parameter),
            BodyParameters=deserialize_list(json_data.get("BodyParameters"), Parameter),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectionHttpParameters = ConnectionHttpParameters


@dataclass
class Parameter(BaseModel):
    Key: Optional[str]
    Value: Optional[str]
    IsValueSecret: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Parameter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Parameter"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
            IsValueSecret=json_data.get("IsValueSecret"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Parameter = Parameter


