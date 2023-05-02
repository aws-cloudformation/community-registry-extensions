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
class AwsCloudfrontRealtimelogconfig(BaseModel):
    Arn: Optional[str]
    EndPoints: Optional[Sequence["_EndPoint"]]
    Fields: Optional[Sequence[str]]
    Name: Optional[str]
    SamplingRate: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCloudfrontRealtimelogconfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCloudfrontRealtimelogconfig"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            EndPoints=deserialize_list(json_data.get("EndPoints"), EndPoint),
            Fields=json_data.get("Fields"),
            Name=json_data.get("Name"),
            SamplingRate=json_data.get("SamplingRate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCloudfrontRealtimelogconfig = AwsCloudfrontRealtimelogconfig


@dataclass
class EndPoint(BaseModel):
    KinesisStreamConfig: Optional["_KinesisStreamConfig"]
    StreamType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EndPoint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EndPoint"]:
        if not json_data:
            return None
        return cls(
            KinesisStreamConfig=KinesisStreamConfig._deserialize(json_data.get("KinesisStreamConfig")),
            StreamType=json_data.get("StreamType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EndPoint = EndPoint


@dataclass
class KinesisStreamConfig(BaseModel):
    RoleArn: Optional[str]
    StreamArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KinesisStreamConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KinesisStreamConfig"]:
        if not json_data:
            return None
        return cls(
            RoleArn=json_data.get("RoleArn"),
            StreamArn=json_data.get("StreamArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KinesisStreamConfig = KinesisStreamConfig


