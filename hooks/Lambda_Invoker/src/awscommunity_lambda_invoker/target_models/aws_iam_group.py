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
class AwsIamGroup(BaseModel):
    Id: Optional[str]
    Arn: Optional[str]
    GroupName: Optional[str]
    ManagedPolicyArns: Optional[Sequence[str]]
    Path: Optional[str]
    Policies: Optional[Sequence["_Policy"]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIamGroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIamGroup"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
            GroupName=json_data.get("GroupName"),
            ManagedPolicyArns=json_data.get("ManagedPolicyArns"),
            Path=json_data.get("Path"),
            Policies=deserialize_list(json_data.get("Policies"), Policy),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIamGroup = AwsIamGroup


@dataclass
class Policy(BaseModel):
    PolicyDocument: Optional[MutableMapping[str, Any]]
    PolicyName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Policy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Policy"]:
        if not json_data:
            return None
        return cls(
            PolicyDocument=json_data.get("PolicyDocument"),
            PolicyName=json_data.get("PolicyName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Policy = Policy


