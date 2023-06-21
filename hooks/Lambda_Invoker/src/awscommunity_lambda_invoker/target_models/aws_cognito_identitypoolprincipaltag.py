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
class AwsCognitoIdentitypoolprincipaltag(BaseModel):
    IdentityPoolId: Optional[str]
    IdentityProviderName: Optional[str]
    UseDefaults: Optional[bool]
    PrincipalTags: Optional[MutableMapping[str, Any]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCognitoIdentitypoolprincipaltag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCognitoIdentitypoolprincipaltag"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            IdentityPoolId=json_data.get("IdentityPoolId"),
            IdentityProviderName=json_data.get("IdentityProviderName"),
            UseDefaults=json_data.get("UseDefaults"),
            PrincipalTags=json_data.get("PrincipalTags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCognitoIdentitypoolprincipaltag = AwsCognitoIdentitypoolprincipaltag


