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
class AwsKinesisanalyticsv2Applicationoutput(BaseModel):
    Id: Optional[str]
    ApplicationName: Optional[str]
    Output: Optional["_Output"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsKinesisanalyticsv2Applicationoutput"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsKinesisanalyticsv2Applicationoutput"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            ApplicationName=json_data.get("ApplicationName"),
            Output=Output._deserialize(json_data.get("Output")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsKinesisanalyticsv2Applicationoutput = AwsKinesisanalyticsv2Applicationoutput


@dataclass
class Output(BaseModel):
    DestinationSchema: Optional["_DestinationSchema"]
    LambdaOutput: Optional["_LambdaOutput"]
    KinesisFirehoseOutput: Optional["_KinesisFirehoseOutput"]
    KinesisStreamsOutput: Optional["_KinesisStreamsOutput"]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Output"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Output"]:
        if not json_data:
            return None
        return cls(
            DestinationSchema=DestinationSchema._deserialize(json_data.get("DestinationSchema")),
            LambdaOutput=LambdaOutput._deserialize(json_data.get("LambdaOutput")),
            KinesisFirehoseOutput=KinesisFirehoseOutput._deserialize(json_data.get("KinesisFirehoseOutput")),
            KinesisStreamsOutput=KinesisStreamsOutput._deserialize(json_data.get("KinesisStreamsOutput")),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Output = Output


@dataclass
class DestinationSchema(BaseModel):
    RecordFormatType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DestinationSchema"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DestinationSchema"]:
        if not json_data:
            return None
        return cls(
            RecordFormatType=json_data.get("RecordFormatType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DestinationSchema = DestinationSchema


@dataclass
class LambdaOutput(BaseModel):
    ResourceARN: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LambdaOutput"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LambdaOutput"]:
        if not json_data:
            return None
        return cls(
            ResourceARN=json_data.get("ResourceARN"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LambdaOutput = LambdaOutput


@dataclass
class KinesisFirehoseOutput(BaseModel):
    ResourceARN: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KinesisFirehoseOutput"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KinesisFirehoseOutput"]:
        if not json_data:
            return None
        return cls(
            ResourceARN=json_data.get("ResourceARN"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KinesisFirehoseOutput = KinesisFirehoseOutput


@dataclass
class KinesisStreamsOutput(BaseModel):
    ResourceARN: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KinesisStreamsOutput"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KinesisStreamsOutput"]:
        if not json_data:
            return None
        return cls(
            ResourceARN=json_data.get("ResourceARN"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KinesisStreamsOutput = KinesisStreamsOutput


