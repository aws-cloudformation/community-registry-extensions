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
class AwsApigatewayv2Authorizer(BaseModel):
    IdentityValidationExpression: Optional[str]
    AuthorizerUri: Optional[str]
    AuthorizerCredentialsArn: Optional[str]
    AuthorizerType: Optional[str]
    JwtConfiguration: Optional["_JWTConfiguration"]
    AuthorizerResultTtlInSeconds: Optional[int]
    IdentitySource: Optional[Sequence[str]]
    AuthorizerPayloadFormatVersion: Optional[str]
    ApiId: Optional[str]
    EnableSimpleResponses: Optional[bool]
    AuthorizerId: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsApigatewayv2Authorizer"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsApigatewayv2Authorizer"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            IdentityValidationExpression=json_data.get("IdentityValidationExpression"),
            AuthorizerUri=json_data.get("AuthorizerUri"),
            AuthorizerCredentialsArn=json_data.get("AuthorizerCredentialsArn"),
            AuthorizerType=json_data.get("AuthorizerType"),
            JwtConfiguration=JWTConfiguration._deserialize(json_data.get("JwtConfiguration")),
            AuthorizerResultTtlInSeconds=json_data.get("AuthorizerResultTtlInSeconds"),
            IdentitySource=json_data.get("IdentitySource"),
            AuthorizerPayloadFormatVersion=json_data.get("AuthorizerPayloadFormatVersion"),
            ApiId=json_data.get("ApiId"),
            EnableSimpleResponses=json_data.get("EnableSimpleResponses"),
            AuthorizerId=json_data.get("AuthorizerId"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsApigatewayv2Authorizer = AwsApigatewayv2Authorizer


@dataclass
class JWTConfiguration(BaseModel):
    Issuer: Optional[str]
    Audience: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_JWTConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JWTConfiguration"]:
        if not json_data:
            return None
        return cls(
            Issuer=json_data.get("Issuer"),
            Audience=json_data.get("Audience"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JWTConfiguration = JWTConfiguration


