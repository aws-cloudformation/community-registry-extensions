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
class AwsEc2Host(BaseModel):
    HostId: Optional[str]
    AutoPlacement: Optional[str]
    AvailabilityZone: Optional[str]
    HostRecovery: Optional[str]
    InstanceType: Optional[str]
    InstanceFamily: Optional[str]
    OutpostArn: Optional[str]
    HostMaintenance: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Host"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Host"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            HostId=json_data.get("HostId"),
            AutoPlacement=json_data.get("AutoPlacement"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            HostRecovery=json_data.get("HostRecovery"),
            InstanceType=json_data.get("InstanceType"),
            InstanceFamily=json_data.get("InstanceFamily"),
            OutpostArn=json_data.get("OutpostArn"),
            HostMaintenance=json_data.get("HostMaintenance"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Host = AwsEc2Host


