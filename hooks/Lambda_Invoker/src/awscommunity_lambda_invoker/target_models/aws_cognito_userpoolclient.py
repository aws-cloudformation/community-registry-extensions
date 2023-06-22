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
class AwsCognitoUserpoolclient(BaseModel):
    AnalyticsConfiguration: Optional["_AnalyticsConfiguration"]
    GenerateSecret: Optional[bool]
    CallbackURLs: Optional[Sequence[str]]
    IdTokenValidity: Optional[int]
    TokenValidityUnits: Optional["_TokenValidityUnits"]
    ReadAttributes: Optional[Sequence[str]]
    AllowedOAuthFlowsUserPoolClient: Optional[bool]
    DefaultRedirectURI: Optional[str]
    Name: Optional[str]
    ClientName: Optional[str]
    ExplicitAuthFlows: Optional[Sequence[str]]
    AccessTokenValidity: Optional[int]
    EnableTokenRevocation: Optional[bool]
    EnablePropagateAdditionalUserContextData: Optional[bool]
    AuthSessionValidity: Optional[int]
    AllowedOAuthScopes: Optional[Sequence[str]]
    SupportedIdentityProviders: Optional[Sequence[str]]
    UserPoolId: Optional[str]
    AllowedOAuthFlows: Optional[Sequence[str]]
    ClientSecret: Optional[str]
    LogoutURLs: Optional[Sequence[str]]
    RefreshTokenValidity: Optional[int]
    Id: Optional[str]
    WriteAttributes: Optional[Sequence[str]]
    PreventUserExistenceErrors: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCognitoUserpoolclient"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCognitoUserpoolclient"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AnalyticsConfiguration=AnalyticsConfiguration._deserialize(json_data.get("AnalyticsConfiguration")),
            GenerateSecret=json_data.get("GenerateSecret"),
            CallbackURLs=json_data.get("CallbackURLs"),
            IdTokenValidity=json_data.get("IdTokenValidity"),
            TokenValidityUnits=TokenValidityUnits._deserialize(json_data.get("TokenValidityUnits")),
            ReadAttributes=json_data.get("ReadAttributes"),
            AllowedOAuthFlowsUserPoolClient=json_data.get("AllowedOAuthFlowsUserPoolClient"),
            DefaultRedirectURI=json_data.get("DefaultRedirectURI"),
            Name=json_data.get("Name"),
            ClientName=json_data.get("ClientName"),
            ExplicitAuthFlows=json_data.get("ExplicitAuthFlows"),
            AccessTokenValidity=json_data.get("AccessTokenValidity"),
            EnableTokenRevocation=json_data.get("EnableTokenRevocation"),
            EnablePropagateAdditionalUserContextData=json_data.get("EnablePropagateAdditionalUserContextData"),
            AuthSessionValidity=json_data.get("AuthSessionValidity"),
            AllowedOAuthScopes=json_data.get("AllowedOAuthScopes"),
            SupportedIdentityProviders=json_data.get("SupportedIdentityProviders"),
            UserPoolId=json_data.get("UserPoolId"),
            AllowedOAuthFlows=json_data.get("AllowedOAuthFlows"),
            ClientSecret=json_data.get("ClientSecret"),
            LogoutURLs=json_data.get("LogoutURLs"),
            RefreshTokenValidity=json_data.get("RefreshTokenValidity"),
            Id=json_data.get("Id"),
            WriteAttributes=json_data.get("WriteAttributes"),
            PreventUserExistenceErrors=json_data.get("PreventUserExistenceErrors"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCognitoUserpoolclient = AwsCognitoUserpoolclient


@dataclass
class AnalyticsConfiguration(BaseModel):
    ApplicationArn: Optional[str]
    ApplicationId: Optional[str]
    UserDataShared: Optional[bool]
    RoleArn: Optional[str]
    ExternalId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AnalyticsConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnalyticsConfiguration"]:
        if not json_data:
            return None
        return cls(
            ApplicationArn=json_data.get("ApplicationArn"),
            ApplicationId=json_data.get("ApplicationId"),
            UserDataShared=json_data.get("UserDataShared"),
            RoleArn=json_data.get("RoleArn"),
            ExternalId=json_data.get("ExternalId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnalyticsConfiguration = AnalyticsConfiguration


@dataclass
class TokenValidityUnits(BaseModel):
    IdToken: Optional[str]
    RefreshToken: Optional[str]
    AccessToken: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TokenValidityUnits"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TokenValidityUnits"]:
        if not json_data:
            return None
        return cls(
            IdToken=json_data.get("IdToken"),
            RefreshToken=json_data.get("RefreshToken"),
            AccessToken=json_data.get("AccessToken"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TokenValidityUnits = TokenValidityUnits


