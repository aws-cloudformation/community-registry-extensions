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
class AwsEc2Vpcendpoint(BaseModel):
    Id: Optional[str]
    CreationTimestamp: Optional[str]
    DnsEntries: Optional[Sequence[str]]
    NetworkInterfaceIds: Optional[Sequence[str]]
    PolicyDocument: Optional[Any]
    PrivateDnsEnabled: Optional[bool]
    RouteTableIds: Optional[AbstractSet[str]]
    SecurityGroupIds: Optional[AbstractSet[str]]
    ServiceName: Optional[str]
    SubnetIds: Optional[AbstractSet[str]]
    VpcEndpointType: Optional[str]
    VpcId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Vpcendpoint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Vpcendpoint"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            CreationTimestamp=json_data.get("CreationTimestamp"),
            DnsEntries=json_data.get("DnsEntries"),
            NetworkInterfaceIds=json_data.get("NetworkInterfaceIds"),
            PolicyDocument=json_data.get("PolicyDocument"),
            PrivateDnsEnabled=json_data.get("PrivateDnsEnabled"),
            RouteTableIds=set_or_none(json_data.get("RouteTableIds")),
            SecurityGroupIds=set_or_none(json_data.get("SecurityGroupIds")),
            ServiceName=json_data.get("ServiceName"),
            SubnetIds=set_or_none(json_data.get("SubnetIds")),
            VpcEndpointType=json_data.get("VpcEndpointType"),
            VpcId=json_data.get("VpcId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Vpcendpoint = AwsEc2Vpcendpoint


