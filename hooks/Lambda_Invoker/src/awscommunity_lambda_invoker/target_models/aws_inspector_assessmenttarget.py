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
class AwsInspectorAssessmenttarget(BaseModel):
    Arn: Optional[str]
    AssessmentTargetName: Optional[str]
    ResourceGroupArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsInspectorAssessmenttarget"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsInspectorAssessmenttarget"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            AssessmentTargetName=json_data.get("AssessmentTargetName"),
            ResourceGroupArn=json_data.get("ResourceGroupArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsInspectorAssessmenttarget = AwsInspectorAssessmenttarget


