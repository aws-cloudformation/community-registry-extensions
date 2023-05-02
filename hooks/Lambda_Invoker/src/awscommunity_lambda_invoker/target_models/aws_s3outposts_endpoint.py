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
class AwsS3outpostsEndpoint(BaseModel):
    Arn: Optional[str]
    CidrBlock: Optional[str]
    CreationTime: Optional[str]
    Id: Optional[str]
    NetworkInterfaces: Optional[AbstractSet["_NetworkInterface"]]
    OutpostId: Optional[str]
    SecurityGroupId: Optional[str]
    Status: Optional[str]
    SubnetId: Optional[str]
    AccessType: Optional[str]
    CustomerOwnedIpv4Pool: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsS3outpostsEndpoint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsS3outpostsEndpoint"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            CidrBlock=json_data.get("CidrBlock"),
            CreationTime=json_data.get("CreationTime"),
            Id=json_data.get("Id"),
            NetworkInterfaces=set_or_none(json_data.get("NetworkInterfaces")),
            OutpostId=json_data.get("OutpostId"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            Status=json_data.get("Status"),
            SubnetId=json_data.get("SubnetId"),
            AccessType=json_data.get("AccessType"),
            CustomerOwnedIpv4Pool=json_data.get("CustomerOwnedIpv4Pool"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsS3outpostsEndpoint = AwsS3outpostsEndpoint


@dataclass
class NetworkInterface(BaseModel):
    NetworkInterfaceId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkInterface"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkInterface"]:
        if not json_data:
            return None
        return cls(
            NetworkInterfaceId=json_data.get("NetworkInterfaceId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkInterface = NetworkInterface


