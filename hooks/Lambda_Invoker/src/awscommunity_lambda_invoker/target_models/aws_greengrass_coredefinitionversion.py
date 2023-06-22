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
class AwsGreengrassCoredefinitionversion(BaseModel):
    Id: Optional[str]
    Cores: Optional[Sequence["_Core"]]
    CoreDefinitionId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsGreengrassCoredefinitionversion"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsGreengrassCoredefinitionversion"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            Cores=deserialize_list(json_data.get("Cores"), Core),
            CoreDefinitionId=json_data.get("CoreDefinitionId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsGreengrassCoredefinitionversion = AwsGreengrassCoredefinitionversion


@dataclass
class Core(BaseModel):
    SyncShadow: Optional[bool]
    ThingArn: Optional[str]
    Id: Optional[str]
    CertificateArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Core"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Core"]:
        if not json_data:
            return None
        return cls(
            SyncShadow=json_data.get("SyncShadow"),
            ThingArn=json_data.get("ThingArn"),
            Id=json_data.get("Id"),
            CertificateArn=json_data.get("CertificateArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Core = Core


