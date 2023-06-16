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
class AwsEc2Vpccidrblock(BaseModel):
    Ipv6NetmaskLength: Optional[int]
    Ipv6IpamPoolId: Optional[str]
    VpcId: Optional[str]
    Ipv4NetmaskLength: Optional[int]
    CidrBlock: Optional[str]
    Ipv4IpamPoolId: Optional[str]
    Ipv6Pool: Optional[str]
    Id: Optional[str]
    Ipv6CidrBlock: Optional[str]
    AmazonProvidedIpv6CidrBlock: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Vpccidrblock"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Vpccidrblock"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Ipv6NetmaskLength=json_data.get("Ipv6NetmaskLength"),
            Ipv6IpamPoolId=json_data.get("Ipv6IpamPoolId"),
            VpcId=json_data.get("VpcId"),
            Ipv4NetmaskLength=json_data.get("Ipv4NetmaskLength"),
            CidrBlock=json_data.get("CidrBlock"),
            Ipv4IpamPoolId=json_data.get("Ipv4IpamPoolId"),
            Ipv6Pool=json_data.get("Ipv6Pool"),
            Id=json_data.get("Id"),
            Ipv6CidrBlock=json_data.get("Ipv6CidrBlock"),
            AmazonProvidedIpv6CidrBlock=json_data.get("AmazonProvidedIpv6CidrBlock"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Vpccidrblock = AwsEc2Vpccidrblock


