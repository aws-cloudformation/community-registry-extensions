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
class AwsCognitoUserpoolresourceserver(BaseModel):
    UserPoolId: Optional[str]
    Identifier: Optional[str]
    Id: Optional[str]
    Scopes: Optional[Sequence["_ResourceServerScopeType"]]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCognitoUserpoolresourceserver"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCognitoUserpoolresourceserver"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            UserPoolId=json_data.get("UserPoolId"),
            Identifier=json_data.get("Identifier"),
            Id=json_data.get("Id"),
            Scopes=deserialize_list(json_data.get("Scopes"), ResourceServerScopeType),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCognitoUserpoolresourceserver = AwsCognitoUserpoolresourceserver


@dataclass
class ResourceServerScopeType(BaseModel):
    ScopeName: Optional[str]
    ScopeDescription: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceServerScopeType"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceServerScopeType"]:
        if not json_data:
            return None
        return cls(
            ScopeName=json_data.get("ScopeName"),
            ScopeDescription=json_data.get("ScopeDescription"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceServerScopeType = ResourceServerScopeType


