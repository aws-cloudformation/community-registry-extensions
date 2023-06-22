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
class AwsApigatewayv2Routeresponse(BaseModel):
    RouteResponseKey: Optional[str]
    ResponseParameters: Optional[MutableMapping[str, "_ParameterConstraints"]]
    RouteId: Optional[str]
    ModelSelectionExpression: Optional[str]
    ApiId: Optional[str]
    ResponseModels: Optional[MutableMapping[str, Any]]
    RouteResponseId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsApigatewayv2Routeresponse"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsApigatewayv2Routeresponse"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            RouteResponseKey=json_data.get("RouteResponseKey"),
            ResponseParameters=json_data.get("ResponseParameters"),
            RouteId=json_data.get("RouteId"),
            ModelSelectionExpression=json_data.get("ModelSelectionExpression"),
            ApiId=json_data.get("ApiId"),
            ResponseModels=json_data.get("ResponseModels"),
            RouteResponseId=json_data.get("RouteResponseId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsApigatewayv2Routeresponse = AwsApigatewayv2Routeresponse


@dataclass
class ParameterConstraints(BaseModel):
    Required: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ParameterConstraints"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParameterConstraints"]:
        if not json_data:
            return None
        return cls(
            Required=json_data.get("Required"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParameterConstraints = ParameterConstraints


