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
class AwsOpensearchserverlessSecurityconfig(BaseModel):
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    SamlOptions: Optional["_SamlConfigOptions"]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsOpensearchserverlessSecurityconfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsOpensearchserverlessSecurityconfig"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            SamlOptions=SamlConfigOptions._deserialize(json_data.get("SamlOptions")),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsOpensearchserverlessSecurityconfig = AwsOpensearchserverlessSecurityconfig


@dataclass
class SamlConfigOptions(BaseModel):
    Metadata: Optional[str]
    UserAttribute: Optional[str]
    GroupAttribute: Optional[str]
    SessionTimeout: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_SamlConfigOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SamlConfigOptions"]:
        if not json_data:
            return None
        return cls(
            Metadata=json_data.get("Metadata"),
            UserAttribute=json_data.get("UserAttribute"),
            GroupAttribute=json_data.get("GroupAttribute"),
            SessionTimeout=json_data.get("SessionTimeout"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SamlConfigOptions = SamlConfigOptions


