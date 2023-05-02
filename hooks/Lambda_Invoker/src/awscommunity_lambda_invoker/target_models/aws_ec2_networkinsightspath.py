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
class AwsEc2Networkinsightspath(BaseModel):
    Destination: Optional[str]
    NetworkInsightsPathId: Optional[str]
    NetworkInsightsPathArn: Optional[str]
    DestinationPort: Optional[int]
    Source: Optional[str]
    DestinationIp: Optional[str]
    SourceIp: Optional[str]
    SourceArn: Optional[str]
    CreatedDate: Optional[str]
    Protocol: Optional[str]
    DestinationArn: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Networkinsightspath"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Networkinsightspath"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Destination=json_data.get("Destination"),
            NetworkInsightsPathId=json_data.get("NetworkInsightsPathId"),
            NetworkInsightsPathArn=json_data.get("NetworkInsightsPathArn"),
            DestinationPort=json_data.get("DestinationPort"),
            Source=json_data.get("Source"),
            DestinationIp=json_data.get("DestinationIp"),
            SourceIp=json_data.get("SourceIp"),
            SourceArn=json_data.get("SourceArn"),
            CreatedDate=json_data.get("CreatedDate"),
            Protocol=json_data.get("Protocol"),
            DestinationArn=json_data.get("DestinationArn"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Networkinsightspath = AwsEc2Networkinsightspath


@dataclass
class Tag(BaseModel):
    Value: Optional[str]
    Key: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tag"]:
        if not json_data:
            return None
        return cls(
            Value=json_data.get("Value"),
            Key=json_data.get("Key"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tag = Tag


