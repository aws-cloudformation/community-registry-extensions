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
class AwsEc2Trafficmirrorfilterrule(BaseModel):
    Id: Optional[str]
    DestinationPortRange: Optional["_TrafficMirrorPortRange"]
    Description: Optional[str]
    SourcePortRange: Optional["_TrafficMirrorPortRange"]
    RuleAction: Optional[str]
    SourceCidrBlock: Optional[str]
    RuleNumber: Optional[int]
    DestinationCidrBlock: Optional[str]
    TrafficMirrorFilterId: Optional[str]
    TrafficDirection: Optional[str]
    Protocol: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Trafficmirrorfilterrule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Trafficmirrorfilterrule"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            DestinationPortRange=TrafficMirrorPortRange._deserialize(json_data.get("DestinationPortRange")),
            Description=json_data.get("Description"),
            SourcePortRange=TrafficMirrorPortRange._deserialize(json_data.get("SourcePortRange")),
            RuleAction=json_data.get("RuleAction"),
            SourceCidrBlock=json_data.get("SourceCidrBlock"),
            RuleNumber=json_data.get("RuleNumber"),
            DestinationCidrBlock=json_data.get("DestinationCidrBlock"),
            TrafficMirrorFilterId=json_data.get("TrafficMirrorFilterId"),
            TrafficDirection=json_data.get("TrafficDirection"),
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Trafficmirrorfilterrule = AwsEc2Trafficmirrorfilterrule


@dataclass
class TrafficMirrorPortRange(BaseModel):
    FromPort: Optional[int]
    ToPort: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_TrafficMirrorPortRange"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TrafficMirrorPortRange"]:
        if not json_data:
            return None
        return cls(
            FromPort=json_data.get("FromPort"),
            ToPort=json_data.get("ToPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TrafficMirrorPortRange = TrafficMirrorPortRange


