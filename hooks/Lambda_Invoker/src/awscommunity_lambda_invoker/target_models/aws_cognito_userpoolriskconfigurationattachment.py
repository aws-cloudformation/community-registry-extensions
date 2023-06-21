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
class AwsCognitoUserpoolriskconfigurationattachment(BaseModel):
    Id: Optional[str]
    CompromisedCredentialsRiskConfiguration: Optional["_CompromisedCredentialsRiskConfigurationType"]
    UserPoolId: Optional[str]
    ClientId: Optional[str]
    AccountTakeoverRiskConfiguration: Optional["_AccountTakeoverRiskConfigurationType"]
    RiskExceptionConfiguration: Optional["_RiskExceptionConfigurationType"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCognitoUserpoolriskconfigurationattachment"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCognitoUserpoolriskconfigurationattachment"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            CompromisedCredentialsRiskConfiguration=CompromisedCredentialsRiskConfigurationType._deserialize(json_data.get("CompromisedCredentialsRiskConfiguration")),
            UserPoolId=json_data.get("UserPoolId"),
            ClientId=json_data.get("ClientId"),
            AccountTakeoverRiskConfiguration=AccountTakeoverRiskConfigurationType._deserialize(json_data.get("AccountTakeoverRiskConfiguration")),
            RiskExceptionConfiguration=RiskExceptionConfigurationType._deserialize(json_data.get("RiskExceptionConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCognitoUserpoolriskconfigurationattachment = AwsCognitoUserpoolriskconfigurationattachment


@dataclass
class CompromisedCredentialsRiskConfigurationType(BaseModel):
    Actions: Optional["_CompromisedCredentialsActionsType"]
    EventFilter: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_CompromisedCredentialsRiskConfigurationType"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CompromisedCredentialsRiskConfigurationType"]:
        if not json_data:
            return None
        return cls(
            Actions=CompromisedCredentialsActionsType._deserialize(json_data.get("Actions")),
            EventFilter=json_data.get("EventFilter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CompromisedCredentialsRiskConfigurationType = CompromisedCredentialsRiskConfigurationType


@dataclass
class CompromisedCredentialsActionsType(BaseModel):
    EventAction: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CompromisedCredentialsActionsType"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CompromisedCredentialsActionsType"]:
        if not json_data:
            return None
        return cls(
            EventAction=json_data.get("EventAction"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CompromisedCredentialsActionsType = CompromisedCredentialsActionsType


@dataclass
class AccountTakeoverRiskConfigurationType(BaseModel):
    Actions: Optional["_AccountTakeoverActionsType"]
    NotifyConfiguration: Optional["_NotifyConfigurationType"]

    @classmethod
    def _deserialize(
        cls: Type["_AccountTakeoverRiskConfigurationType"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccountTakeoverRiskConfigurationType"]:
        if not json_data:
            return None
        return cls(
            Actions=AccountTakeoverActionsType._deserialize(json_data.get("Actions")),
            NotifyConfiguration=NotifyConfigurationType._deserialize(json_data.get("NotifyConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccountTakeoverRiskConfigurationType = AccountTakeoverRiskConfigurationType


@dataclass
class AccountTakeoverActionsType(BaseModel):
    HighAction: Optional["_AccountTakeoverActionType"]
    LowAction: Optional["_AccountTakeoverActionType"]
    MediumAction: Optional["_AccountTakeoverActionType"]

    @classmethod
    def _deserialize(
        cls: Type["_AccountTakeoverActionsType"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccountTakeoverActionsType"]:
        if not json_data:
            return None
        return cls(
            HighAction=AccountTakeoverActionType._deserialize(json_data.get("HighAction")),
            LowAction=AccountTakeoverActionType._deserialize(json_data.get("LowAction")),
            MediumAction=AccountTakeoverActionType._deserialize(json_data.get("MediumAction")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccountTakeoverActionsType = AccountTakeoverActionsType


@dataclass
class AccountTakeoverActionType(BaseModel):
    Notify: Optional[bool]
    EventAction: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AccountTakeoverActionType"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccountTakeoverActionType"]:
        if not json_data:
            return None
        return cls(
            Notify=json_data.get("Notify"),
            EventAction=json_data.get("EventAction"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccountTakeoverActionType = AccountTakeoverActionType


@dataclass
class NotifyConfigurationType(BaseModel):
    BlockEmail: Optional["_NotifyEmailType"]
    ReplyTo: Optional[str]
    SourceArn: Optional[str]
    NoActionEmail: Optional["_NotifyEmailType"]
    From: Optional[str]
    MfaEmail: Optional["_NotifyEmailType"]

    @classmethod
    def _deserialize(
        cls: Type["_NotifyConfigurationType"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NotifyConfigurationType"]:
        if not json_data:
            return None
        return cls(
            BlockEmail=NotifyEmailType._deserialize(json_data.get("BlockEmail")),
            ReplyTo=json_data.get("ReplyTo"),
            SourceArn=json_data.get("SourceArn"),
            NoActionEmail=NotifyEmailType._deserialize(json_data.get("NoActionEmail")),
            From=json_data.get("From"),
            MfaEmail=NotifyEmailType._deserialize(json_data.get("MfaEmail")),
        )


# work around possible type aliasing issues when variable has same name as a model
_NotifyConfigurationType = NotifyConfigurationType


@dataclass
class NotifyEmailType(BaseModel):
    TextBody: Optional[str]
    HtmlBody: Optional[str]
    Subject: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NotifyEmailType"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NotifyEmailType"]:
        if not json_data:
            return None
        return cls(
            TextBody=json_data.get("TextBody"),
            HtmlBody=json_data.get("HtmlBody"),
            Subject=json_data.get("Subject"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NotifyEmailType = NotifyEmailType


@dataclass
class RiskExceptionConfigurationType(BaseModel):
    BlockedIPRangeList: Optional[Sequence[str]]
    SkippedIPRangeList: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_RiskExceptionConfigurationType"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RiskExceptionConfigurationType"]:
        if not json_data:
            return None
        return cls(
            BlockedIPRangeList=json_data.get("BlockedIPRangeList"),
            SkippedIPRangeList=json_data.get("SkippedIPRangeList"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RiskExceptionConfigurationType = RiskExceptionConfigurationType


