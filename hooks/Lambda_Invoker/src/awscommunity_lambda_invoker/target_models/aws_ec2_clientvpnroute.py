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
class AwsEc2Clientvpnroute(BaseModel):
    Id: Optional[str]
    ClientVpnEndpointId: Optional[str]
    TargetVpcSubnetId: Optional[str]
    Description: Optional[str]
    DestinationCidrBlock: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Clientvpnroute"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Clientvpnroute"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            ClientVpnEndpointId=json_data.get("ClientVpnEndpointId"),
            TargetVpcSubnetId=json_data.get("TargetVpcSubnetId"),
            Description=json_data.get("Description"),
            DestinationCidrBlock=json_data.get("DestinationCidrBlock"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Clientvpnroute = AwsEc2Clientvpnroute


