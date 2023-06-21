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
class AwsCloudwatchCompositealarm(BaseModel):
    Arn: Optional[str]
    AlarmName: Optional[str]
    AlarmRule: Optional[str]
    AlarmDescription: Optional[str]
    ActionsEnabled: Optional[bool]
    OKActions: Optional[Sequence[str]]
    AlarmActions: Optional[Sequence[str]]
    InsufficientDataActions: Optional[Sequence[str]]
    ActionsSuppressor: Optional[str]
    ActionsSuppressorWaitPeriod: Optional[int]
    ActionsSuppressorExtensionPeriod: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCloudwatchCompositealarm"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCloudwatchCompositealarm"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            AlarmName=json_data.get("AlarmName"),
            AlarmRule=json_data.get("AlarmRule"),
            AlarmDescription=json_data.get("AlarmDescription"),
            ActionsEnabled=json_data.get("ActionsEnabled"),
            OKActions=json_data.get("OKActions"),
            AlarmActions=json_data.get("AlarmActions"),
            InsufficientDataActions=json_data.get("InsufficientDataActions"),
            ActionsSuppressor=json_data.get("ActionsSuppressor"),
            ActionsSuppressorWaitPeriod=json_data.get("ActionsSuppressorWaitPeriod"),
            ActionsSuppressorExtensionPeriod=json_data.get("ActionsSuppressorExtensionPeriod"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCloudwatchCompositealarm = AwsCloudwatchCompositealarm


