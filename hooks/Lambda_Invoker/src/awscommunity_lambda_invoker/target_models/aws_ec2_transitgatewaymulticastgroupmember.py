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
class AwsEc2Transitgatewaymulticastgroupmember(BaseModel):
    GroupIpAddress: Optional[str]
    TransitGatewayAttachmentId: Optional[str]
    TransitGatewayMulticastDomainId: Optional[str]
    SubnetId: Optional[str]
    ResourceId: Optional[str]
    ResourceType: Optional[str]
    NetworkInterfaceId: Optional[str]
    GroupMember: Optional[bool]
    GroupSource: Optional[bool]
    MemberType: Optional[str]
    SourceType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Transitgatewaymulticastgroupmember"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Transitgatewaymulticastgroupmember"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            GroupIpAddress=json_data.get("GroupIpAddress"),
            TransitGatewayAttachmentId=json_data.get("TransitGatewayAttachmentId"),
            TransitGatewayMulticastDomainId=json_data.get("TransitGatewayMulticastDomainId"),
            SubnetId=json_data.get("SubnetId"),
            ResourceId=json_data.get("ResourceId"),
            ResourceType=json_data.get("ResourceType"),
            NetworkInterfaceId=json_data.get("NetworkInterfaceId"),
            GroupMember=json_data.get("GroupMember"),
            GroupSource=json_data.get("GroupSource"),
            MemberType=json_data.get("MemberType"),
            SourceType=json_data.get("SourceType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Transitgatewaymulticastgroupmember = AwsEc2Transitgatewaymulticastgroupmember


