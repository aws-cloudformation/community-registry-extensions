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
class AwsS3Multiregionaccesspointpolicy(BaseModel):
    MrapName: Optional[str]
    Policy: Optional[MutableMapping[str, Any]]
    PolicyStatus: Optional["_PolicyStatus"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsS3Multiregionaccesspointpolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsS3Multiregionaccesspointpolicy"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            MrapName=json_data.get("MrapName"),
            Policy=json_data.get("Policy"),
            PolicyStatus=PolicyStatus._deserialize(json_data.get("PolicyStatus")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsS3Multiregionaccesspointpolicy = AwsS3Multiregionaccesspointpolicy


@dataclass
class PolicyStatus(BaseModel):
    IsPublic: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PolicyStatus"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PolicyStatus"]:
        if not json_data:
            return None
        return cls(
            IsPublic=json_data.get("IsPublic"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PolicyStatus = PolicyStatus


