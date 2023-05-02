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
class AwsConfigOrganizationconfigrule(BaseModel):
    OrganizationCustomRuleMetadata: Optional["_OrganizationCustomRuleMetadata"]
    OrganizationManagedRuleMetadata: Optional["_OrganizationManagedRuleMetadata"]
    ExcludedAccounts: Optional[Sequence[str]]
    OrganizationConfigRuleName: Optional[str]
    Id: Optional[str]
    OrganizationCustomPolicyRuleMetadata: Optional["_OrganizationCustomPolicyRuleMetadata"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsConfigOrganizationconfigrule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsConfigOrganizationconfigrule"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            OrganizationCustomRuleMetadata=OrganizationCustomRuleMetadata._deserialize(json_data.get("OrganizationCustomRuleMetadata")),
            OrganizationManagedRuleMetadata=OrganizationManagedRuleMetadata._deserialize(json_data.get("OrganizationManagedRuleMetadata")),
            ExcludedAccounts=json_data.get("ExcludedAccounts"),
            OrganizationConfigRuleName=json_data.get("OrganizationConfigRuleName"),
            Id=json_data.get("Id"),
            OrganizationCustomPolicyRuleMetadata=OrganizationCustomPolicyRuleMetadata._deserialize(json_data.get("OrganizationCustomPolicyRuleMetadata")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsConfigOrganizationconfigrule = AwsConfigOrganizationconfigrule


@dataclass
class OrganizationCustomRuleMetadata(BaseModel):
    TagKeyScope: Optional[str]
    TagValueScope: Optional[str]
    Description: Optional[str]
    ResourceIdScope: Optional[str]
    LambdaFunctionArn: Optional[str]
    OrganizationConfigRuleTriggerTypes: Optional[Sequence[str]]
    ResourceTypesScope: Optional[Sequence[str]]
    MaximumExecutionFrequency: Optional[str]
    InputParameters: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OrganizationCustomRuleMetadata"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OrganizationCustomRuleMetadata"]:
        if not json_data:
            return None
        return cls(
            TagKeyScope=json_data.get("TagKeyScope"),
            TagValueScope=json_data.get("TagValueScope"),
            Description=json_data.get("Description"),
            ResourceIdScope=json_data.get("ResourceIdScope"),
            LambdaFunctionArn=json_data.get("LambdaFunctionArn"),
            OrganizationConfigRuleTriggerTypes=json_data.get("OrganizationConfigRuleTriggerTypes"),
            ResourceTypesScope=json_data.get("ResourceTypesScope"),
            MaximumExecutionFrequency=json_data.get("MaximumExecutionFrequency"),
            InputParameters=json_data.get("InputParameters"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OrganizationCustomRuleMetadata = OrganizationCustomRuleMetadata


@dataclass
class OrganizationManagedRuleMetadata(BaseModel):
    TagKeyScope: Optional[str]
    TagValueScope: Optional[str]
    Description: Optional[str]
    ResourceIdScope: Optional[str]
    RuleIdentifier: Optional[str]
    ResourceTypesScope: Optional[Sequence[str]]
    MaximumExecutionFrequency: Optional[str]
    InputParameters: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OrganizationManagedRuleMetadata"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OrganizationManagedRuleMetadata"]:
        if not json_data:
            return None
        return cls(
            TagKeyScope=json_data.get("TagKeyScope"),
            TagValueScope=json_data.get("TagValueScope"),
            Description=json_data.get("Description"),
            ResourceIdScope=json_data.get("ResourceIdScope"),
            RuleIdentifier=json_data.get("RuleIdentifier"),
            ResourceTypesScope=json_data.get("ResourceTypesScope"),
            MaximumExecutionFrequency=json_data.get("MaximumExecutionFrequency"),
            InputParameters=json_data.get("InputParameters"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OrganizationManagedRuleMetadata = OrganizationManagedRuleMetadata


@dataclass
class OrganizationCustomPolicyRuleMetadata(BaseModel):
    TagKeyScope: Optional[str]
    TagValueScope: Optional[str]
    Runtime: Optional[str]
    PolicyText: Optional[str]
    Description: Optional[str]
    ResourceIdScope: Optional[str]
    OrganizationConfigRuleTriggerTypes: Optional[Sequence[str]]
    DebugLogDeliveryAccounts: Optional[Sequence[str]]
    ResourceTypesScope: Optional[Sequence[str]]
    MaximumExecutionFrequency: Optional[str]
    InputParameters: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OrganizationCustomPolicyRuleMetadata"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OrganizationCustomPolicyRuleMetadata"]:
        if not json_data:
            return None
        return cls(
            TagKeyScope=json_data.get("TagKeyScope"),
            TagValueScope=json_data.get("TagValueScope"),
            Runtime=json_data.get("Runtime"),
            PolicyText=json_data.get("PolicyText"),
            Description=json_data.get("Description"),
            ResourceIdScope=json_data.get("ResourceIdScope"),
            OrganizationConfigRuleTriggerTypes=json_data.get("OrganizationConfigRuleTriggerTypes"),
            DebugLogDeliveryAccounts=json_data.get("DebugLogDeliveryAccounts"),
            ResourceTypesScope=json_data.get("ResourceTypesScope"),
            MaximumExecutionFrequency=json_data.get("MaximumExecutionFrequency"),
            InputParameters=json_data.get("InputParameters"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OrganizationCustomPolicyRuleMetadata = OrganizationCustomPolicyRuleMetadata


