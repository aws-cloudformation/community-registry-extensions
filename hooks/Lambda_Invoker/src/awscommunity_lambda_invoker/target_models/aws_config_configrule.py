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
class AwsConfigConfigrule(BaseModel):
    ConfigRuleId: Optional[str]
    Description: Optional[str]
    Scope: Optional["_Scope"]
    ComplianceType: Optional[str]
    ConfigRuleName: Optional[str]
    Arn: Optional[str]
    MaximumExecutionFrequency: Optional[str]
    Source: Optional["_Source"]
    InputParameters: Optional[MutableMapping[str, Any]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsConfigConfigrule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsConfigConfigrule"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ConfigRuleId=json_data.get("ConfigRuleId"),
            Description=json_data.get("Description"),
            Scope=Scope._deserialize(json_data.get("Scope")),
            ComplianceType=json_data.get("ComplianceType"),
            ConfigRuleName=json_data.get("ConfigRuleName"),
            Arn=json_data.get("Arn"),
            MaximumExecutionFrequency=json_data.get("MaximumExecutionFrequency"),
            Source=Source._deserialize(json_data.get("Source")),
            InputParameters=json_data.get("InputParameters"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsConfigConfigrule = AwsConfigConfigrule


@dataclass
class Scope(BaseModel):
    TagKey: Optional[str]
    ComplianceResourceTypes: Optional[Sequence[str]]
    TagValue: Optional[str]
    ComplianceResourceId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Scope"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Scope"]:
        if not json_data:
            return None
        return cls(
            TagKey=json_data.get("TagKey"),
            ComplianceResourceTypes=json_data.get("ComplianceResourceTypes"),
            TagValue=json_data.get("TagValue"),
            ComplianceResourceId=json_data.get("ComplianceResourceId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Scope = Scope


@dataclass
class Source(BaseModel):
    CustomPolicyDetails: Optional["_CustomPolicyDetails"]
    SourceIdentifier: Optional[str]
    Owner: Optional[str]
    SourceDetails: Optional[Sequence["_SourceDetail"]]

    @classmethod
    def _deserialize(
        cls: Type["_Source"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Source"]:
        if not json_data:
            return None
        return cls(
            CustomPolicyDetails=CustomPolicyDetails._deserialize(json_data.get("CustomPolicyDetails")),
            SourceIdentifier=json_data.get("SourceIdentifier"),
            Owner=json_data.get("Owner"),
            SourceDetails=deserialize_list(json_data.get("SourceDetails"), SourceDetail),
        )


# work around possible type aliasing issues when variable has same name as a model
_Source = Source


@dataclass
class CustomPolicyDetails(BaseModel):
    EnableDebugLogDelivery: Optional[bool]
    PolicyText: Optional[str]
    PolicyRuntime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomPolicyDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomPolicyDetails"]:
        if not json_data:
            return None
        return cls(
            EnableDebugLogDelivery=json_data.get("EnableDebugLogDelivery"),
            PolicyText=json_data.get("PolicyText"),
            PolicyRuntime=json_data.get("PolicyRuntime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomPolicyDetails = CustomPolicyDetails


@dataclass
class SourceDetail(BaseModel):
    EventSource: Optional[str]
    MaximumExecutionFrequency: Optional[str]
    MessageType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SourceDetail"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceDetail"]:
        if not json_data:
            return None
        return cls(
            EventSource=json_data.get("EventSource"),
            MaximumExecutionFrequency=json_data.get("MaximumExecutionFrequency"),
            MessageType=json_data.get("MessageType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceDetail = SourceDetail


