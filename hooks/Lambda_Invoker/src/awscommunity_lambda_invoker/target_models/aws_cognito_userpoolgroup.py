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
class AwsCognitoUserpoolgroup(BaseModel):
    GroupName: Optional[str]
    Description: Optional[str]
    UserPoolId: Optional[str]
    Id: Optional[str]
    Precedence: Optional[float]
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCognitoUserpoolgroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCognitoUserpoolgroup"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            GroupName=json_data.get("GroupName"),
            Description=json_data.get("Description"),
            UserPoolId=json_data.get("UserPoolId"),
            Id=json_data.get("Id"),
            Precedence=json_data.get("Precedence"),
            RoleArn=json_data.get("RoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCognitoUserpoolgroup = AwsCognitoUserpoolgroup


