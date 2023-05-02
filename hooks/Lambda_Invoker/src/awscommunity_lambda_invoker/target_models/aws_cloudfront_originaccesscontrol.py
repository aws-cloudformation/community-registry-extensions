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
class AwsCloudfrontOriginaccesscontrol(BaseModel):
    OriginAccessControlConfig: Optional["_OriginAccessControlConfig"]
    Id: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCloudfrontOriginaccesscontrol"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCloudfrontOriginaccesscontrol"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            OriginAccessControlConfig=OriginAccessControlConfig._deserialize(json_data.get("OriginAccessControlConfig")),
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCloudfrontOriginaccesscontrol = AwsCloudfrontOriginaccesscontrol


@dataclass
class OriginAccessControlConfig(BaseModel):
    Name: Optional[str]
    Description: Optional[str]
    SigningProtocol: Optional[str]
    SigningBehavior: Optional[str]
    OriginAccessControlOriginType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OriginAccessControlConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OriginAccessControlConfig"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Description=json_data.get("Description"),
            SigningProtocol=json_data.get("SigningProtocol"),
            SigningBehavior=json_data.get("SigningBehavior"),
            OriginAccessControlOriginType=json_data.get("OriginAccessControlOriginType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OriginAccessControlConfig = OriginAccessControlConfig


