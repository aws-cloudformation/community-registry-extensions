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
class AwsAppstreamUser(BaseModel):
    Id: Optional[str]
    UserName: Optional[str]
    FirstName: Optional[str]
    MessageAction: Optional[str]
    LastName: Optional[str]
    AuthenticationType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAppstreamUser"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAppstreamUser"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            UserName=json_data.get("UserName"),
            FirstName=json_data.get("FirstName"),
            MessageAction=json_data.get("MessageAction"),
            LastName=json_data.get("LastName"),
            AuthenticationType=json_data.get("AuthenticationType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAppstreamUser = AwsAppstreamUser


