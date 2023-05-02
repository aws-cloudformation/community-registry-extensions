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
class AwsLambdaUrl(BaseModel):
    TargetFunctionArn: Optional[str]
    Qualifier: Optional[str]
    AuthType: Optional[str]
    InvokeMode: Optional[str]
    FunctionArn: Optional[str]
    FunctionUrl: Optional[str]
    Cors: Optional["_Cors"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsLambdaUrl"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsLambdaUrl"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            TargetFunctionArn=json_data.get("TargetFunctionArn"),
            Qualifier=json_data.get("Qualifier"),
            AuthType=json_data.get("AuthType"),
            InvokeMode=json_data.get("InvokeMode"),
            FunctionArn=json_data.get("FunctionArn"),
            FunctionUrl=json_data.get("FunctionUrl"),
            Cors=Cors._deserialize(json_data.get("Cors")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsLambdaUrl = AwsLambdaUrl


@dataclass
class Cors(BaseModel):
    AllowCredentials: Optional[bool]
    AllowHeaders: Optional[Sequence[str]]
    AllowMethods: Optional[Sequence[str]]
    AllowOrigins: Optional[Sequence[str]]
    ExposeHeaders: Optional[Sequence[str]]
    MaxAge: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_Cors"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Cors"]:
        if not json_data:
            return None
        return cls(
            AllowCredentials=json_data.get("AllowCredentials"),
            AllowHeaders=json_data.get("AllowHeaders"),
            AllowMethods=json_data.get("AllowMethods"),
            AllowOrigins=json_data.get("AllowOrigins"),
            ExposeHeaders=json_data.get("ExposeHeaders"),
            MaxAge=json_data.get("MaxAge"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Cors = Cors


