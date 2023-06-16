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
class AwsEc2Securitygroupegress(BaseModel):
    Id: Optional[str]
    CidrIp: Optional[str]
    CidrIpv6: Optional[str]
    Description: Optional[str]
    DestinationPrefixListId: Optional[str]
    DestinationSecurityGroupId: Optional[str]
    FromPort: Optional[int]
    GroupId: Optional[str]
    IpProtocol: Optional[str]
    ToPort: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Securitygroupegress"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Securitygroupegress"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            CidrIp=json_data.get("CidrIp"),
            CidrIpv6=json_data.get("CidrIpv6"),
            Description=json_data.get("Description"),
            DestinationPrefixListId=json_data.get("DestinationPrefixListId"),
            DestinationSecurityGroupId=json_data.get("DestinationSecurityGroupId"),
            FromPort=json_data.get("FromPort"),
            GroupId=json_data.get("GroupId"),
            IpProtocol=json_data.get("IpProtocol"),
            ToPort=json_data.get("ToPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Securitygroupegress = AwsEc2Securitygroupegress


