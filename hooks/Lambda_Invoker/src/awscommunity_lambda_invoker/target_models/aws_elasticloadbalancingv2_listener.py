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
class AwsElasticloadbalancingv2Listener(BaseModel):
    SslPolicy: Optional[str]
    LoadBalancerArn: Optional[str]
    DefaultActions: Optional[Sequence["_Action"]]
    Port: Optional[int]
    Certificates: Optional[Sequence["_Certificate"]]
    Protocol: Optional[str]
    ListenerArn: Optional[str]
    AlpnPolicy: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsElasticloadbalancingv2Listener"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsElasticloadbalancingv2Listener"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            SslPolicy=json_data.get("SslPolicy"),
            LoadBalancerArn=json_data.get("LoadBalancerArn"),
            DefaultActions=deserialize_list(json_data.get("DefaultActions"), Action),
            Port=json_data.get("Port"),
            Certificates=deserialize_list(json_data.get("Certificates"), Certificate),
            Protocol=json_data.get("Protocol"),
            ListenerArn=json_data.get("ListenerArn"),
            AlpnPolicy=json_data.get("AlpnPolicy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsElasticloadbalancingv2Listener = AwsElasticloadbalancingv2Listener


@dataclass
class Action(BaseModel):
    Order: Optional[int]
    TargetGroupArn: Optional[str]
    FixedResponseConfig: Optional["_FixedResponseConfig"]
    AuthenticateCognitoConfig: Optional["_AuthenticateCognitoConfig"]
    Type: Optional[str]
    RedirectConfig: Optional["_RedirectConfig"]
    ForwardConfig: Optional["_ForwardConfig"]
    AuthenticateOidcConfig: Optional["_AuthenticateOidcConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_Action"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Action"]:
        if not json_data:
            return None
        return cls(
            Order=json_data.get("Order"),
            TargetGroupArn=json_data.get("TargetGroupArn"),
            FixedResponseConfig=FixedResponseConfig._deserialize(json_data.get("FixedResponseConfig")),
            AuthenticateCognitoConfig=AuthenticateCognitoConfig._deserialize(json_data.get("AuthenticateCognitoConfig")),
            Type=json_data.get("Type"),
            RedirectConfig=RedirectConfig._deserialize(json_data.get("RedirectConfig")),
            ForwardConfig=ForwardConfig._deserialize(json_data.get("ForwardConfig")),
            AuthenticateOidcConfig=AuthenticateOidcConfig._deserialize(json_data.get("AuthenticateOidcConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Action = Action


@dataclass
class FixedResponseConfig(BaseModel):
    ContentType: Optional[str]
    StatusCode: Optional[str]
    MessageBody: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FixedResponseConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FixedResponseConfig"]:
        if not json_data:
            return None
        return cls(
            ContentType=json_data.get("ContentType"),
            StatusCode=json_data.get("StatusCode"),
            MessageBody=json_data.get("MessageBody"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FixedResponseConfig = FixedResponseConfig


@dataclass
class AuthenticateCognitoConfig(BaseModel):
    OnUnauthenticatedRequest: Optional[str]
    UserPoolClientId: Optional[str]
    UserPoolDomain: Optional[str]
    SessionTimeout: Optional[str]
    Scope: Optional[str]
    SessionCookieName: Optional[str]
    UserPoolArn: Optional[str]
    AuthenticationRequestExtraParams: Optional[MutableMapping[str, str]]

    @classmethod
    def _deserialize(
        cls: Type["_AuthenticateCognitoConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthenticateCognitoConfig"]:
        if not json_data:
            return None
        return cls(
            OnUnauthenticatedRequest=json_data.get("OnUnauthenticatedRequest"),
            UserPoolClientId=json_data.get("UserPoolClientId"),
            UserPoolDomain=json_data.get("UserPoolDomain"),
            SessionTimeout=json_data.get("SessionTimeout"),
            Scope=json_data.get("Scope"),
            SessionCookieName=json_data.get("SessionCookieName"),
            UserPoolArn=json_data.get("UserPoolArn"),
            AuthenticationRequestExtraParams=json_data.get("AuthenticationRequestExtraParams"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthenticateCognitoConfig = AuthenticateCognitoConfig


@dataclass
class RedirectConfig(BaseModel):
    Path: Optional[str]
    Query: Optional[str]
    Port: Optional[str]
    Host: Optional[str]
    Protocol: Optional[str]
    StatusCode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RedirectConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RedirectConfig"]:
        if not json_data:
            return None
        return cls(
            Path=json_data.get("Path"),
            Query=json_data.get("Query"),
            Port=json_data.get("Port"),
            Host=json_data.get("Host"),
            Protocol=json_data.get("Protocol"),
            StatusCode=json_data.get("StatusCode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RedirectConfig = RedirectConfig


@dataclass
class ForwardConfig(BaseModel):
    TargetGroupStickinessConfig: Optional["_TargetGroupStickinessConfig"]
    TargetGroups: Optional[Sequence["_TargetGroupTuple"]]

    @classmethod
    def _deserialize(
        cls: Type["_ForwardConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ForwardConfig"]:
        if not json_data:
            return None
        return cls(
            TargetGroupStickinessConfig=TargetGroupStickinessConfig._deserialize(json_data.get("TargetGroupStickinessConfig")),
            TargetGroups=deserialize_list(json_data.get("TargetGroups"), TargetGroupTuple),
        )


# work around possible type aliasing issues when variable has same name as a model
_ForwardConfig = ForwardConfig


@dataclass
class TargetGroupStickinessConfig(BaseModel):
    Enabled: Optional[bool]
    DurationSeconds: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_TargetGroupStickinessConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetGroupStickinessConfig"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            DurationSeconds=json_data.get("DurationSeconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetGroupStickinessConfig = TargetGroupStickinessConfig


@dataclass
class TargetGroupTuple(BaseModel):
    TargetGroupArn: Optional[str]
    Weight: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_TargetGroupTuple"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetGroupTuple"]:
        if not json_data:
            return None
        return cls(
            TargetGroupArn=json_data.get("TargetGroupArn"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetGroupTuple = TargetGroupTuple


@dataclass
class AuthenticateOidcConfig(BaseModel):
    OnUnauthenticatedRequest: Optional[str]
    TokenEndpoint: Optional[str]
    SessionTimeout: Optional[str]
    Scope: Optional[str]
    Issuer: Optional[str]
    ClientSecret: Optional[str]
    UserInfoEndpoint: Optional[str]
    ClientId: Optional[str]
    AuthorizationEndpoint: Optional[str]
    SessionCookieName: Optional[str]
    UseExistingClientSecret: Optional[bool]
    AuthenticationRequestExtraParams: Optional[MutableMapping[str, str]]

    @classmethod
    def _deserialize(
        cls: Type["_AuthenticateOidcConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthenticateOidcConfig"]:
        if not json_data:
            return None
        return cls(
            OnUnauthenticatedRequest=json_data.get("OnUnauthenticatedRequest"),
            TokenEndpoint=json_data.get("TokenEndpoint"),
            SessionTimeout=json_data.get("SessionTimeout"),
            Scope=json_data.get("Scope"),
            Issuer=json_data.get("Issuer"),
            ClientSecret=json_data.get("ClientSecret"),
            UserInfoEndpoint=json_data.get("UserInfoEndpoint"),
            ClientId=json_data.get("ClientId"),
            AuthorizationEndpoint=json_data.get("AuthorizationEndpoint"),
            SessionCookieName=json_data.get("SessionCookieName"),
            UseExistingClientSecret=json_data.get("UseExistingClientSecret"),
            AuthenticationRequestExtraParams=json_data.get("AuthenticationRequestExtraParams"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthenticateOidcConfig = AuthenticateOidcConfig


@dataclass
class Certificate(BaseModel):
    CertificateArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Certificate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Certificate"]:
        if not json_data:
            return None
        return cls(
            CertificateArn=json_data.get("CertificateArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Certificate = Certificate


