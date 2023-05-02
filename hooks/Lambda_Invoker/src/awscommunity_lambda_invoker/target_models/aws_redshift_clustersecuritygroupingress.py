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
class AwsRedshiftClustersecuritygroupingress(BaseModel):
    Id: Optional[str]
    CIDRIP: Optional[str]
    ClusterSecurityGroupName: Optional[str]
    EC2SecurityGroupName: Optional[str]
    EC2SecurityGroupOwnerId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsRedshiftClustersecuritygroupingress"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsRedshiftClustersecuritygroupingress"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            CIDRIP=json_data.get("CIDRIP"),
            ClusterSecurityGroupName=json_data.get("ClusterSecurityGroupName"),
            EC2SecurityGroupName=json_data.get("EC2SecurityGroupName"),
            EC2SecurityGroupOwnerId=json_data.get("EC2SecurityGroupOwnerId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsRedshiftClustersecuritygroupingress = AwsRedshiftClustersecuritygroupingress


