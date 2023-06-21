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
class AwsLogsSubscriptionfilter(BaseModel):
    FilterName: Optional[str]
    DestinationArn: Optional[str]
    FilterPattern: Optional[str]
    LogGroupName: Optional[str]
    RoleArn: Optional[str]
    Distribution: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsLogsSubscriptionfilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsLogsSubscriptionfilter"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            FilterName=json_data.get("FilterName"),
            DestinationArn=json_data.get("DestinationArn"),
            FilterPattern=json_data.get("FilterPattern"),
            LogGroupName=json_data.get("LogGroupName"),
            RoleArn=json_data.get("RoleArn"),
            Distribution=json_data.get("Distribution"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsLogsSubscriptionfilter = AwsLogsSubscriptionfilter


