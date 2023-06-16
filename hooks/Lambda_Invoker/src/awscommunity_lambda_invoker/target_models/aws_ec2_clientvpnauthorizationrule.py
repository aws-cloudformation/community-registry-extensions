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
class AwsEc2Clientvpnauthorizationrule(BaseModel):
    Id: Optional[str]
    ClientVpnEndpointId: Optional[str]
    Description: Optional[str]
    AccessGroupId: Optional[str]
    TargetNetworkCidr: Optional[str]
    AuthorizeAllGroups: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Clientvpnauthorizationrule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Clientvpnauthorizationrule"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            ClientVpnEndpointId=json_data.get("ClientVpnEndpointId"),
            Description=json_data.get("Description"),
            AccessGroupId=json_data.get("AccessGroupId"),
            TargetNetworkCidr=json_data.get("TargetNetworkCidr"),
            AuthorizeAllGroups=json_data.get("AuthorizeAllGroups"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Clientvpnauthorizationrule = AwsEc2Clientvpnauthorizationrule


