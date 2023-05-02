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
class AwsEcsPrimarytaskset(BaseModel):
    Cluster: Optional[str]
    TaskSetId: Optional[str]
    Service: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEcsPrimarytaskset"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEcsPrimarytaskset"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Cluster=json_data.get("Cluster"),
            TaskSetId=json_data.get("TaskSetId"),
            Service=json_data.get("Service"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEcsPrimarytaskset = AwsEcsPrimarytaskset


