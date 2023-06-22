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
class AwsSecurityhubStandard(BaseModel):
    StandardsSubscriptionArn: Optional[str]
    StandardsArn: Optional[str]
    DisabledStandardsControls: Optional[Sequence["_StandardsControl"]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSecurityhubStandard"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSecurityhubStandard"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            StandardsSubscriptionArn=json_data.get("StandardsSubscriptionArn"),
            StandardsArn=json_data.get("StandardsArn"),
            DisabledStandardsControls=deserialize_list(json_data.get("DisabledStandardsControls"), StandardsControl),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSecurityhubStandard = AwsSecurityhubStandard


@dataclass
class StandardsControl(BaseModel):
    StandardsControlArn: Optional[str]
    Reason: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StandardsControl"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StandardsControl"]:
        if not json_data:
            return None
        return cls(
            StandardsControlArn=json_data.get("StandardsControlArn"),
            Reason=json_data.get("Reason"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StandardsControl = StandardsControl


