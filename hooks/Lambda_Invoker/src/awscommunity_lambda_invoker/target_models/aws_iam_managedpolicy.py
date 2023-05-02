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
class AwsIamManagedpolicy(BaseModel):
    Id: Optional[str]
    Description: Optional[str]
    Groups: Optional[Sequence[str]]
    ManagedPolicyName: Optional[str]
    Path: Optional[str]
    PolicyDocument: Optional[MutableMapping[str, Any]]
    Roles: Optional[Sequence[str]]
    Users: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIamManagedpolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIamManagedpolicy"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            Description=json_data.get("Description"),
            Groups=json_data.get("Groups"),
            ManagedPolicyName=json_data.get("ManagedPolicyName"),
            Path=json_data.get("Path"),
            PolicyDocument=json_data.get("PolicyDocument"),
            Roles=json_data.get("Roles"),
            Users=json_data.get("Users"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIamManagedpolicy = AwsIamManagedpolicy


