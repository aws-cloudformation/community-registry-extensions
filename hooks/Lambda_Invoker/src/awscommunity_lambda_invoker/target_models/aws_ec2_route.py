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
class AwsEc2Route(BaseModel):
    DestinationIpv6CidrBlock: Optional[str]
    RouteTableId: Optional[str]
    InstanceId: Optional[str]
    LocalGatewayId: Optional[str]
    CarrierGatewayId: Optional[str]
    DestinationCidrBlock: Optional[str]
    GatewayId: Optional[str]
    NetworkInterfaceId: Optional[str]
    VpcEndpointId: Optional[str]
    TransitGatewayId: Optional[str]
    VpcPeeringConnectionId: Optional[str]
    EgressOnlyInternetGatewayId: Optional[str]
    Id: Optional[str]
    NatGatewayId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Route"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Route"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            DestinationIpv6CidrBlock=json_data.get("DestinationIpv6CidrBlock"),
            RouteTableId=json_data.get("RouteTableId"),
            InstanceId=json_data.get("InstanceId"),
            LocalGatewayId=json_data.get("LocalGatewayId"),
            CarrierGatewayId=json_data.get("CarrierGatewayId"),
            DestinationCidrBlock=json_data.get("DestinationCidrBlock"),
            GatewayId=json_data.get("GatewayId"),
            NetworkInterfaceId=json_data.get("NetworkInterfaceId"),
            VpcEndpointId=json_data.get("VpcEndpointId"),
            TransitGatewayId=json_data.get("TransitGatewayId"),
            VpcPeeringConnectionId=json_data.get("VpcPeeringConnectionId"),
            EgressOnlyInternetGatewayId=json_data.get("EgressOnlyInternetGatewayId"),
            Id=json_data.get("Id"),
            NatGatewayId=json_data.get("NatGatewayId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Route = AwsEc2Route


