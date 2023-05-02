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
class AwsLambdaEventinvokeconfig(BaseModel):
    FunctionName: Optional[str]
    MaximumRetryAttempts: Optional[int]
    Qualifier: Optional[str]
    DestinationConfig: Optional["_DestinationConfig"]
    Id: Optional[str]
    MaximumEventAgeInSeconds: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_AwsLambdaEventinvokeconfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsLambdaEventinvokeconfig"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            FunctionName=json_data.get("FunctionName"),
            MaximumRetryAttempts=json_data.get("MaximumRetryAttempts"),
            Qualifier=json_data.get("Qualifier"),
            DestinationConfig=DestinationConfig._deserialize(json_data.get("DestinationConfig")),
            Id=json_data.get("Id"),
            MaximumEventAgeInSeconds=json_data.get("MaximumEventAgeInSeconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsLambdaEventinvokeconfig = AwsLambdaEventinvokeconfig


@dataclass
class DestinationConfig(BaseModel):
    OnSuccess: Optional["_OnSuccess"]
    OnFailure: Optional["_OnFailure"]

    @classmethod
    def _deserialize(
        cls: Type["_DestinationConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DestinationConfig"]:
        if not json_data:
            return None
        return cls(
            OnSuccess=OnSuccess._deserialize(json_data.get("OnSuccess")),
            OnFailure=OnFailure._deserialize(json_data.get("OnFailure")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DestinationConfig = DestinationConfig


@dataclass
class OnSuccess(BaseModel):
    Destination: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OnSuccess"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OnSuccess"]:
        if not json_data:
            return None
        return cls(
            Destination=json_data.get("Destination"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OnSuccess = OnSuccess


@dataclass
class OnFailure(BaseModel):
    Destination: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OnFailure"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OnFailure"]:
        if not json_data:
            return None
        return cls(
            Destination=json_data.get("Destination"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OnFailure = OnFailure


