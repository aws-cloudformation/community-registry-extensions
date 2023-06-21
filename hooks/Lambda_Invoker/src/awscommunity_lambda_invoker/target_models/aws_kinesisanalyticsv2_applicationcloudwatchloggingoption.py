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
class AwsKinesisanalyticsv2Applicationcloudwatchloggingoption(BaseModel):
    Id: Optional[str]
    ApplicationName: Optional[str]
    CloudWatchLoggingOption: Optional["_CloudWatchLoggingOption"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsKinesisanalyticsv2Applicationcloudwatchloggingoption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsKinesisanalyticsv2Applicationcloudwatchloggingoption"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            ApplicationName=json_data.get("ApplicationName"),
            CloudWatchLoggingOption=CloudWatchLoggingOption._deserialize(json_data.get("CloudWatchLoggingOption")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsKinesisanalyticsv2Applicationcloudwatchloggingoption = AwsKinesisanalyticsv2Applicationcloudwatchloggingoption


@dataclass
class CloudWatchLoggingOption(BaseModel):
    LogStreamARN: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CloudWatchLoggingOption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudWatchLoggingOption"]:
        if not json_data:
            return None
        return cls(
            LogStreamARN=json_data.get("LogStreamARN"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudWatchLoggingOption = CloudWatchLoggingOption


