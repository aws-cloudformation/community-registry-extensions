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
class AwsElasticloadbalancingv2Listenerrule(BaseModel):
    ListenerArn: Optional[str]
    RuleArn: Optional[str]
    Actions: Optional[Sequence["_Action"]]
    Priority: Optional[int]
    Conditions: Optional[Sequence["_RuleCondition"]]
    IsDefault: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AwsElasticloadbalancingv2Listenerrule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsElasticloadbalancingv2Listenerrule"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ListenerArn=json_data.get("ListenerArn"),
            RuleArn=json_data.get("RuleArn"),
            Actions=deserialize_list(json_data.get("Actions"), Action),
            Priority=json_data.get("Priority"),
            Conditions=deserialize_list(json_data.get("Conditions"), RuleCondition),
            IsDefault=json_data.get("IsDefault"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsElasticloadbalancingv2Listenerrule = AwsElasticloadbalancingv2Listenerrule


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
    SessionTimeout: Optional[int]
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
    SessionTimeout: Optional[int]
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
class RuleCondition(BaseModel):
    Field: Optional[str]
    Values: Optional[Sequence[str]]
    HttpRequestMethodConfig: Optional["_HttpRequestMethodConfig"]
    PathPatternConfig: Optional["_PathPatternConfig"]
    HttpHeaderConfig: Optional["_HttpHeaderConfig"]
    SourceIpConfig: Optional["_SourceIpConfig"]
    HostHeaderConfig: Optional["_HostHeaderConfig"]
    QueryStringConfig: Optional["_QueryStringConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_RuleCondition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleCondition"]:
        if not json_data:
            return None
        return cls(
            Field=json_data.get("Field"),
            Values=json_data.get("Values"),
            HttpRequestMethodConfig=HttpRequestMethodConfig._deserialize(json_data.get("HttpRequestMethodConfig")),
            PathPatternConfig=PathPatternConfig._deserialize(json_data.get("PathPatternConfig")),
            HttpHeaderConfig=HttpHeaderConfig._deserialize(json_data.get("HttpHeaderConfig")),
            SourceIpConfig=SourceIpConfig._deserialize(json_data.get("SourceIpConfig")),
            HostHeaderConfig=HostHeaderConfig._deserialize(json_data.get("HostHeaderConfig")),
            QueryStringConfig=QueryStringConfig._deserialize(json_data.get("QueryStringConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleCondition = RuleCondition


@dataclass
class HttpRequestMethodConfig(BaseModel):
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_HttpRequestMethodConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpRequestMethodConfig"]:
        if not json_data:
            return None
        return cls(
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpRequestMethodConfig = HttpRequestMethodConfig


@dataclass
class PathPatternConfig(BaseModel):
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_PathPatternConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PathPatternConfig"]:
        if not json_data:
            return None
        return cls(
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PathPatternConfig = PathPatternConfig


@dataclass
class HttpHeaderConfig(BaseModel):
    Values: Optional[Sequence[str]]
    HttpHeaderName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HttpHeaderConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpHeaderConfig"]:
        if not json_data:
            return None
        return cls(
            Values=json_data.get("Values"),
            HttpHeaderName=json_data.get("HttpHeaderName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpHeaderConfig = HttpHeaderConfig


@dataclass
class SourceIpConfig(BaseModel):
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_SourceIpConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceIpConfig"]:
        if not json_data:
            return None
        return cls(
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceIpConfig = SourceIpConfig


@dataclass
class HostHeaderConfig(BaseModel):
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_HostHeaderConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostHeaderConfig"]:
        if not json_data:
            return None
        return cls(
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostHeaderConfig = HostHeaderConfig


@dataclass
class QueryStringConfig(BaseModel):
    Values: Optional[Sequence["_QueryStringKeyValue"]]

    @classmethod
    def _deserialize(
        cls: Type["_QueryStringConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QueryStringConfig"]:
        if not json_data:
            return None
        return cls(
            Values=deserialize_list(json_data.get("Values"), QueryStringKeyValue),
        )


# work around possible type aliasing issues when variable has same name as a model
_QueryStringConfig = QueryStringConfig


@dataclass
class QueryStringKeyValue(BaseModel):
    Value: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_QueryStringKeyValue"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QueryStringKeyValue"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_QueryStringKeyValue = QueryStringKeyValue


