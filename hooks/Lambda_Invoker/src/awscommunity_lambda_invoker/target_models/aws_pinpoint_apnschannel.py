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
class AwsPinpointApnschannel(BaseModel):
    Id: Optional[str]
    BundleId: Optional[str]
    PrivateKey: Optional[str]
    Enabled: Optional[bool]
    DefaultAuthenticationMethod: Optional[str]
    TokenKey: Optional[str]
    ApplicationId: Optional[str]
    TeamId: Optional[str]
    Certificate: Optional[str]
    TokenKeyId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsPinpointApnschannel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsPinpointApnschannel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            BundleId=json_data.get("BundleId"),
            PrivateKey=json_data.get("PrivateKey"),
            Enabled=json_data.get("Enabled"),
            DefaultAuthenticationMethod=json_data.get("DefaultAuthenticationMethod"),
            TokenKey=json_data.get("TokenKey"),
            ApplicationId=json_data.get("ApplicationId"),
            TeamId=json_data.get("TeamId"),
            Certificate=json_data.get("Certificate"),
            TokenKeyId=json_data.get("TokenKeyId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsPinpointApnschannel = AwsPinpointApnschannel


