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
class AwsEcsClustercapacityproviderassociations(BaseModel):
    CapacityProviders: Optional[Sequence[str]]
    Cluster: Optional[str]
    DefaultCapacityProviderStrategy: Optional[Sequence["_CapacityProviderStrategy"]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEcsClustercapacityproviderassociations"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEcsClustercapacityproviderassociations"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            CapacityProviders=json_data.get("CapacityProviders"),
            Cluster=json_data.get("Cluster"),
            DefaultCapacityProviderStrategy=deserialize_list(json_data.get("DefaultCapacityProviderStrategy"), CapacityProviderStrategy),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEcsClustercapacityproviderassociations = AwsEcsClustercapacityproviderassociations


@dataclass
class CapacityProviderStrategy(BaseModel):
    Base: Optional[int]
    Weight: Optional[int]
    CapacityProvider: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CapacityProviderStrategy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CapacityProviderStrategy"]:
        if not json_data:
            return None
        return cls(
            Base=json_data.get("Base"),
            Weight=json_data.get("Weight"),
            CapacityProvider=json_data.get("CapacityProvider"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CapacityProviderStrategy = CapacityProviderStrategy


