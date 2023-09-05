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
class AwsRoute53Keysigningkey(BaseModel):
    HostedZoneId: Optional[str]
    Status: Optional[str]
    Name: Optional[str]
    KeyManagementServiceArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsRoute53Keysigningkey"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsRoute53Keysigningkey"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            HostedZoneId=json_data.get("HostedZoneId"),
            Status=json_data.get("Status"),
            Name=json_data.get("Name"),
            KeyManagementServiceArn=json_data.get("KeyManagementServiceArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsRoute53Keysigningkey = AwsRoute53Keysigningkey

