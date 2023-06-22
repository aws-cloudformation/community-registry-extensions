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
class AwsAutoscalingWarmpool(BaseModel):
    AutoScalingGroupName: Optional[str]
    MaxGroupPreparedCapacity: Optional[int]
    MinSize: Optional[int]
    PoolState: Optional[str]
    InstanceReusePolicy: Optional["_InstanceReusePolicy"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAutoscalingWarmpool"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAutoscalingWarmpool"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AutoScalingGroupName=json_data.get("AutoScalingGroupName"),
            MaxGroupPreparedCapacity=json_data.get("MaxGroupPreparedCapacity"),
            MinSize=json_data.get("MinSize"),
            PoolState=json_data.get("PoolState"),
            InstanceReusePolicy=InstanceReusePolicy._deserialize(json_data.get("InstanceReusePolicy")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAutoscalingWarmpool = AwsAutoscalingWarmpool


@dataclass
class InstanceReusePolicy(BaseModel):
    ReuseOnScaleIn: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_InstanceReusePolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstanceReusePolicy"]:
        if not json_data:
            return None
        return cls(
            ReuseOnScaleIn=json_data.get("ReuseOnScaleIn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstanceReusePolicy = InstanceReusePolicy


