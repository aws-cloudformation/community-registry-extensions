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
class AwsSesEmailidentity(BaseModel):
    EmailIdentity: Optional[str]
    ConfigurationSetAttributes: Optional["_ConfigurationSetAttributes"]
    DkimSigningAttributes: Optional["_DkimSigningAttributes"]
    DkimAttributes: Optional["_DkimAttributes"]
    MailFromAttributes: Optional["_MailFromAttributes"]
    FeedbackAttributes: Optional["_FeedbackAttributes"]
    DkimDNSTokenName1: Optional[str]
    DkimDNSTokenName2: Optional[str]
    DkimDNSTokenName3: Optional[str]
    DkimDNSTokenValue1: Optional[str]
    DkimDNSTokenValue2: Optional[str]
    DkimDNSTokenValue3: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSesEmailidentity"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSesEmailidentity"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            EmailIdentity=json_data.get("EmailIdentity"),
            ConfigurationSetAttributes=ConfigurationSetAttributes._deserialize(json_data.get("ConfigurationSetAttributes")),
            DkimSigningAttributes=DkimSigningAttributes._deserialize(json_data.get("DkimSigningAttributes")),
            DkimAttributes=DkimAttributes._deserialize(json_data.get("DkimAttributes")),
            MailFromAttributes=MailFromAttributes._deserialize(json_data.get("MailFromAttributes")),
            FeedbackAttributes=FeedbackAttributes._deserialize(json_data.get("FeedbackAttributes")),
            DkimDNSTokenName1=json_data.get("DkimDNSTokenName1"),
            DkimDNSTokenName2=json_data.get("DkimDNSTokenName2"),
            DkimDNSTokenName3=json_data.get("DkimDNSTokenName3"),
            DkimDNSTokenValue1=json_data.get("DkimDNSTokenValue1"),
            DkimDNSTokenValue2=json_data.get("DkimDNSTokenValue2"),
            DkimDNSTokenValue3=json_data.get("DkimDNSTokenValue3"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSesEmailidentity = AwsSesEmailidentity


@dataclass
class ConfigurationSetAttributes(BaseModel):
    ConfigurationSetName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigurationSetAttributes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigurationSetAttributes"]:
        if not json_data:
            return None
        return cls(
            ConfigurationSetName=json_data.get("ConfigurationSetName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigurationSetAttributes = ConfigurationSetAttributes


@dataclass
class DkimSigningAttributes(BaseModel):
    DomainSigningSelector: Optional[str]
    DomainSigningPrivateKey: Optional[str]
    NextSigningKeyLength: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DkimSigningAttributes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DkimSigningAttributes"]:
        if not json_data:
            return None
        return cls(
            DomainSigningSelector=json_data.get("DomainSigningSelector"),
            DomainSigningPrivateKey=json_data.get("DomainSigningPrivateKey"),
            NextSigningKeyLength=json_data.get("NextSigningKeyLength"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DkimSigningAttributes = DkimSigningAttributes


@dataclass
class DkimAttributes(BaseModel):
    SigningEnabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_DkimAttributes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DkimAttributes"]:
        if not json_data:
            return None
        return cls(
            SigningEnabled=json_data.get("SigningEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DkimAttributes = DkimAttributes


@dataclass
class MailFromAttributes(BaseModel):
    MailFromDomain: Optional[str]
    BehaviorOnMxFailure: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MailFromAttributes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MailFromAttributes"]:
        if not json_data:
            return None
        return cls(
            MailFromDomain=json_data.get("MailFromDomain"),
            BehaviorOnMxFailure=json_data.get("BehaviorOnMxFailure"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MailFromAttributes = MailFromAttributes


@dataclass
class FeedbackAttributes(BaseModel):
    EmailForwardingEnabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_FeedbackAttributes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FeedbackAttributes"]:
        if not json_data:
            return None
        return cls(
            EmailForwardingEnabled=json_data.get("EmailForwardingEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FeedbackAttributes = FeedbackAttributes


