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
class AwsPinpointAdmchannel(BaseModel):
    Id: Optional[str]
    ClientSecret: Optional[str]
    Enabled: Optional[bool]
    ClientId: Optional[str]
    ApplicationId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsPinpointAdmchannel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsPinpointAdmchannel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            ClientSecret=json_data.get("ClientSecret"),
            Enabled=json_data.get("Enabled"),
            ClientId=json_data.get("ClientId"),
            ApplicationId=json_data.get("ApplicationId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsPinpointAdmchannel = AwsPinpointAdmchannel


