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
class AwsManagedblockchainMember(BaseModel):
    MemberId: Optional[str]
    NetworkId: Optional[str]
    MemberConfiguration: Optional["_MemberConfiguration"]
    NetworkConfiguration: Optional["_NetworkConfiguration"]
    InvitationId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsManagedblockchainMember"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsManagedblockchainMember"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            MemberId=json_data.get("MemberId"),
            NetworkId=json_data.get("NetworkId"),
            MemberConfiguration=MemberConfiguration._deserialize(json_data.get("MemberConfiguration")),
            NetworkConfiguration=NetworkConfiguration._deserialize(json_data.get("NetworkConfiguration")),
            InvitationId=json_data.get("InvitationId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsManagedblockchainMember = AwsManagedblockchainMember


@dataclass
class MemberConfiguration(BaseModel):
    Description: Optional[str]
    MemberFrameworkConfiguration: Optional["_MemberFrameworkConfiguration"]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MemberConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MemberConfiguration"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            MemberFrameworkConfiguration=MemberFrameworkConfiguration._deserialize(json_data.get("MemberFrameworkConfiguration")),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MemberConfiguration = MemberConfiguration


@dataclass
class MemberFrameworkConfiguration(BaseModel):
    MemberFabricConfiguration: Optional["_MemberFabricConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_MemberFrameworkConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MemberFrameworkConfiguration"]:
        if not json_data:
            return None
        return cls(
            MemberFabricConfiguration=MemberFabricConfiguration._deserialize(json_data.get("MemberFabricConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_MemberFrameworkConfiguration = MemberFrameworkConfiguration


@dataclass
class MemberFabricConfiguration(BaseModel):
    AdminUsername: Optional[str]
    AdminPassword: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MemberFabricConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MemberFabricConfiguration"]:
        if not json_data:
            return None
        return cls(
            AdminUsername=json_data.get("AdminUsername"),
            AdminPassword=json_data.get("AdminPassword"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MemberFabricConfiguration = MemberFabricConfiguration


@dataclass
class NetworkConfiguration(BaseModel):
    Description: Optional[str]
    FrameworkVersion: Optional[str]
    VotingPolicy: Optional["_VotingPolicy"]
    Framework: Optional[str]
    Name: Optional[str]
    NetworkFrameworkConfiguration: Optional["_NetworkFrameworkConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkConfiguration"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            FrameworkVersion=json_data.get("FrameworkVersion"),
            VotingPolicy=VotingPolicy._deserialize(json_data.get("VotingPolicy")),
            Framework=json_data.get("Framework"),
            Name=json_data.get("Name"),
            NetworkFrameworkConfiguration=NetworkFrameworkConfiguration._deserialize(json_data.get("NetworkFrameworkConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkConfiguration = NetworkConfiguration


@dataclass
class VotingPolicy(BaseModel):
    ApprovalThresholdPolicy: Optional["_ApprovalThresholdPolicy"]

    @classmethod
    def _deserialize(
        cls: Type["_VotingPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VotingPolicy"]:
        if not json_data:
            return None
        return cls(
            ApprovalThresholdPolicy=ApprovalThresholdPolicy._deserialize(json_data.get("ApprovalThresholdPolicy")),
        )


# work around possible type aliasing issues when variable has same name as a model
_VotingPolicy = VotingPolicy


@dataclass
class ApprovalThresholdPolicy(BaseModel):
    ThresholdComparator: Optional[str]
    ThresholdPercentage: Optional[int]
    ProposalDurationInHours: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_ApprovalThresholdPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApprovalThresholdPolicy"]:
        if not json_data:
            return None
        return cls(
            ThresholdComparator=json_data.get("ThresholdComparator"),
            ThresholdPercentage=json_data.get("ThresholdPercentage"),
            ProposalDurationInHours=json_data.get("ProposalDurationInHours"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApprovalThresholdPolicy = ApprovalThresholdPolicy


@dataclass
class NetworkFrameworkConfiguration(BaseModel):
    NetworkFabricConfiguration: Optional["_NetworkFabricConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkFrameworkConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkFrameworkConfiguration"]:
        if not json_data:
            return None
        return cls(
            NetworkFabricConfiguration=NetworkFabricConfiguration._deserialize(json_data.get("NetworkFabricConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkFrameworkConfiguration = NetworkFrameworkConfiguration


@dataclass
class NetworkFabricConfiguration(BaseModel):
    Edition: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkFabricConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkFabricConfiguration"]:
        if not json_data:
            return None
        return cls(
            Edition=json_data.get("Edition"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkFabricConfiguration = NetworkFabricConfiguration


