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
class AwsEc2Networkperformancemetricsubscription(BaseModel):
    Source: Optional[str]
    Destination: Optional[str]
    Metric: Optional[str]
    Statistic: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Networkperformancemetricsubscription"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Networkperformancemetricsubscription"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Source=json_data.get("Source"),
            Destination=json_data.get("Destination"),
            Metric=json_data.get("Metric"),
            Statistic=json_data.get("Statistic"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Networkperformancemetricsubscription = AwsEc2Networkperformancemetricsubscription


