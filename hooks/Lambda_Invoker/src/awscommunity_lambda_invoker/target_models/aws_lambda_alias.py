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
class AwsLambdaAlias(BaseModel):
    FunctionName: Optional[str]
    ProvisionedConcurrencyConfig: Optional["_ProvisionedConcurrencyConfiguration"]
    Description: Optional[str]
    FunctionVersion: Optional[str]
    Id: Optional[str]
    RoutingConfig: Optional["_AliasRoutingConfiguration"]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsLambdaAlias"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsLambdaAlias"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            FunctionName=json_data.get("FunctionName"),
            ProvisionedConcurrencyConfig=ProvisionedConcurrencyConfiguration._deserialize(json_data.get("ProvisionedConcurrencyConfig")),
            Description=json_data.get("Description"),
            FunctionVersion=json_data.get("FunctionVersion"),
            Id=json_data.get("Id"),
            RoutingConfig=AliasRoutingConfiguration._deserialize(json_data.get("RoutingConfig")),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsLambdaAlias = AwsLambdaAlias


@dataclass
class ProvisionedConcurrencyConfiguration(BaseModel):
    ProvisionedConcurrentExecutions: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_ProvisionedConcurrencyConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProvisionedConcurrencyConfiguration"]:
        if not json_data:
            return None
        return cls(
            ProvisionedConcurrentExecutions=json_data.get("ProvisionedConcurrentExecutions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProvisionedConcurrencyConfiguration = ProvisionedConcurrencyConfiguration


@dataclass
class AliasRoutingConfiguration(BaseModel):
    AdditionalVersionWeights: Optional[Sequence["_VersionWeight"]]

    @classmethod
    def _deserialize(
        cls: Type["_AliasRoutingConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AliasRoutingConfiguration"]:
        if not json_data:
            return None
        return cls(
            AdditionalVersionWeights=deserialize_list(json_data.get("AdditionalVersionWeights"), VersionWeight),
        )


# work around possible type aliasing issues when variable has same name as a model
_AliasRoutingConfiguration = AliasRoutingConfiguration


@dataclass
class VersionWeight(BaseModel):
    FunctionWeight: Optional[float]
    FunctionVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VersionWeight"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VersionWeight"]:
        if not json_data:
            return None
        return cls(
            FunctionWeight=json_data.get("FunctionWeight"),
            FunctionVersion=json_data.get("FunctionVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VersionWeight = VersionWeight


