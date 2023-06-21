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
class AwsIdentitystoreGroupmembership(BaseModel):
    GroupId: Optional[str]
    IdentityStoreId: Optional[str]
    MemberId: Optional["_MemberId"]
    MembershipId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIdentitystoreGroupmembership"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIdentitystoreGroupmembership"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            GroupId=json_data.get("GroupId"),
            IdentityStoreId=json_data.get("IdentityStoreId"),
            MemberId=MemberId._deserialize(json_data.get("MemberId")),
            MembershipId=json_data.get("MembershipId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIdentitystoreGroupmembership = AwsIdentitystoreGroupmembership


@dataclass
class MemberId(BaseModel):
    UserId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MemberId"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MemberId"]:
        if not json_data:
            return None
        return cls(
            UserId=json_data.get("UserId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MemberId = MemberId


