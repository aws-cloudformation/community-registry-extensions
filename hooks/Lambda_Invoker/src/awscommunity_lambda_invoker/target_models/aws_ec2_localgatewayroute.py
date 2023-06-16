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
class AwsEc2Localgatewayroute(BaseModel):
    DestinationCidrBlock: Optional[str]
    LocalGatewayRouteTableId: Optional[str]
    LocalGatewayVirtualInterfaceGroupId: Optional[str]
    NetworkInterfaceId: Optional[str]
    State: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Localgatewayroute"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Localgatewayroute"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            DestinationCidrBlock=json_data.get("DestinationCidrBlock"),
            LocalGatewayRouteTableId=json_data.get("LocalGatewayRouteTableId"),
            LocalGatewayVirtualInterfaceGroupId=json_data.get("LocalGatewayVirtualInterfaceGroupId"),
            NetworkInterfaceId=json_data.get("NetworkInterfaceId"),
            State=json_data.get("State"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Localgatewayroute = AwsEc2Localgatewayroute


