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
class AwsEc2Networkaclentry(BaseModel):
    PortRange: Optional["_PortRange"]
    NetworkAclId: Optional[str]
    RuleAction: Optional[str]
    CidrBlock: Optional[str]
    Egress: Optional[bool]
    RuleNumber: Optional[int]
    Id: Optional[str]
    Ipv6CidrBlock: Optional[str]
    Protocol: Optional[int]
    Icmp: Optional["_Icmp"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Networkaclentry"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Networkaclentry"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            PortRange=PortRange._deserialize(json_data.get("PortRange")),
            NetworkAclId=json_data.get("NetworkAclId"),
            RuleAction=json_data.get("RuleAction"),
            CidrBlock=json_data.get("CidrBlock"),
            Egress=json_data.get("Egress"),
            RuleNumber=json_data.get("RuleNumber"),
            Id=json_data.get("Id"),
            Ipv6CidrBlock=json_data.get("Ipv6CidrBlock"),
            Protocol=json_data.get("Protocol"),
            Icmp=Icmp._deserialize(json_data.get("Icmp")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Networkaclentry = AwsEc2Networkaclentry


@dataclass
class PortRange(BaseModel):
    From: Optional[int]
    To: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_PortRange"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortRange"]:
        if not json_data:
            return None
        return cls(
            From=json_data.get("From"),
            To=json_data.get("To"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortRange = PortRange


@dataclass
class Icmp(BaseModel):
    Code: Optional[int]
    Type: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_Icmp"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Icmp"]:
        if not json_data:
            return None
        return cls(
            Code=json_data.get("Code"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Icmp = Icmp


