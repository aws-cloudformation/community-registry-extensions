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
class AwsMediaconnectFlowvpcinterface(BaseModel):
    FlowArn: Optional[str]
    Name: Optional[str]
    RoleArn: Optional[str]
    SecurityGroupIds: Optional[Sequence[str]]
    SubnetId: Optional[str]
    NetworkInterfaceIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsMediaconnectFlowvpcinterface"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsMediaconnectFlowvpcinterface"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            FlowArn=json_data.get("FlowArn"),
            Name=json_data.get("Name"),
            RoleArn=json_data.get("RoleArn"),
            SecurityGroupIds=json_data.get("SecurityGroupIds"),
            SubnetId=json_data.get("SubnetId"),
            NetworkInterfaceIds=json_data.get("NetworkInterfaceIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsMediaconnectFlowvpcinterface = AwsMediaconnectFlowvpcinterface


