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
class AwsSesReceiptrule(BaseModel):
    Id: Optional[str]
    After: Optional[str]
    Rule: Optional["_Rule"]
    RuleSetName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSesReceiptrule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSesReceiptrule"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            After=json_data.get("After"),
            Rule=Rule._deserialize(json_data.get("Rule")),
            RuleSetName=json_data.get("RuleSetName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSesReceiptrule = AwsSesReceiptrule


@dataclass
class Rule(BaseModel):
    ScanEnabled: Optional[bool]
    Recipients: Optional[Sequence[str]]
    Actions: Optional[Sequence["_Action"]]
    Enabled: Optional[bool]
    Name: Optional[str]
    TlsPolicy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Rule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Rule"]:
        if not json_data:
            return None
        return cls(
            ScanEnabled=json_data.get("ScanEnabled"),
            Recipients=json_data.get("Recipients"),
            Actions=deserialize_list(json_data.get("Actions"), Action),
            Enabled=json_data.get("Enabled"),
            Name=json_data.get("Name"),
            TlsPolicy=json_data.get("TlsPolicy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Rule = Rule


@dataclass
class Action(BaseModel):
    BounceAction: Optional["_BounceAction"]
    S3Action: Optional["_S3Action"]
    StopAction: Optional["_StopAction"]
    SNSAction: Optional["_SNSAction"]
    WorkmailAction: Optional["_WorkmailAction"]
    AddHeaderAction: Optional["_AddHeaderAction"]
    LambdaAction: Optional["_LambdaAction"]

    @classmethod
    def _deserialize(
        cls: Type["_Action"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Action"]:
        if not json_data:
            return None
        return cls(
            BounceAction=BounceAction._deserialize(json_data.get("BounceAction")),
            S3Action=S3Action._deserialize(json_data.get("S3Action")),
            StopAction=StopAction._deserialize(json_data.get("StopAction")),
            SNSAction=SNSAction._deserialize(json_data.get("SNSAction")),
            WorkmailAction=WorkmailAction._deserialize(json_data.get("WorkmailAction")),
            AddHeaderAction=AddHeaderAction._deserialize(json_data.get("AddHeaderAction")),
            LambdaAction=LambdaAction._deserialize(json_data.get("LambdaAction")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Action = Action


@dataclass
class BounceAction(BaseModel):
    Sender: Optional[str]
    SmtpReplyCode: Optional[str]
    Message: Optional[str]
    TopicArn: Optional[str]
    StatusCode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BounceAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BounceAction"]:
        if not json_data:
            return None
        return cls(
            Sender=json_data.get("Sender"),
            SmtpReplyCode=json_data.get("SmtpReplyCode"),
            Message=json_data.get("Message"),
            TopicArn=json_data.get("TopicArn"),
            StatusCode=json_data.get("StatusCode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BounceAction = BounceAction


@dataclass
class S3Action(BaseModel):
    BucketName: Optional[str]
    KmsKeyArn: Optional[str]
    TopicArn: Optional[str]
    ObjectKeyPrefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3Action"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3Action"]:
        if not json_data:
            return None
        return cls(
            BucketName=json_data.get("BucketName"),
            KmsKeyArn=json_data.get("KmsKeyArn"),
            TopicArn=json_data.get("TopicArn"),
            ObjectKeyPrefix=json_data.get("ObjectKeyPrefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3Action = S3Action


@dataclass
class StopAction(BaseModel):
    Scope: Optional[str]
    TopicArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StopAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StopAction"]:
        if not json_data:
            return None
        return cls(
            Scope=json_data.get("Scope"),
            TopicArn=json_data.get("TopicArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StopAction = StopAction


@dataclass
class SNSAction(BaseModel):
    TopicArn: Optional[str]
    Encoding: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SNSAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SNSAction"]:
        if not json_data:
            return None
        return cls(
            TopicArn=json_data.get("TopicArn"),
            Encoding=json_data.get("Encoding"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SNSAction = SNSAction


@dataclass
class WorkmailAction(BaseModel):
    TopicArn: Optional[str]
    OrganizationArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WorkmailAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkmailAction"]:
        if not json_data:
            return None
        return cls(
            TopicArn=json_data.get("TopicArn"),
            OrganizationArn=json_data.get("OrganizationArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkmailAction = WorkmailAction


@dataclass
class AddHeaderAction(BaseModel):
    HeaderValue: Optional[str]
    HeaderName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AddHeaderAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AddHeaderAction"]:
        if not json_data:
            return None
        return cls(
            HeaderValue=json_data.get("HeaderValue"),
            HeaderName=json_data.get("HeaderName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AddHeaderAction = AddHeaderAction


@dataclass
class LambdaAction(BaseModel):
    FunctionArn: Optional[str]
    TopicArn: Optional[str]
    InvocationType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LambdaAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LambdaAction"]:
        if not json_data:
            return None
        return cls(
            FunctionArn=json_data.get("FunctionArn"),
            TopicArn=json_data.get("TopicArn"),
            InvocationType=json_data.get("InvocationType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LambdaAction = LambdaAction


