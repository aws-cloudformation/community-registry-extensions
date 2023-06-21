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
class AwsApigatewayv2Route(BaseModel):
    RouteId: Optional[str]
    RouteResponseSelectionExpression: Optional[str]
    RequestModels: Optional[MutableMapping[str, Any]]
    OperationName: Optional[str]
    AuthorizationScopes: Optional[Sequence[str]]
    ApiKeyRequired: Optional[bool]
    RouteKey: Optional[str]
    AuthorizationType: Optional[str]
    ModelSelectionExpression: Optional[str]
    ApiId: Optional[str]
    RequestParameters: Optional[MutableMapping[str, Any]]
    Target: Optional[str]
    AuthorizerId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsApigatewayv2Route"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsApigatewayv2Route"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            RouteId=json_data.get("RouteId"),
            RouteResponseSelectionExpression=json_data.get("RouteResponseSelectionExpression"),
            RequestModels=json_data.get("RequestModels"),
            OperationName=json_data.get("OperationName"),
            AuthorizationScopes=json_data.get("AuthorizationScopes"),
            ApiKeyRequired=json_data.get("ApiKeyRequired"),
            RouteKey=json_data.get("RouteKey"),
            AuthorizationType=json_data.get("AuthorizationType"),
            ModelSelectionExpression=json_data.get("ModelSelectionExpression"),
            ApiId=json_data.get("ApiId"),
            RequestParameters=json_data.get("RequestParameters"),
            Target=json_data.get("Target"),
            AuthorizerId=json_data.get("AuthorizerId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsApigatewayv2Route = AwsApigatewayv2Route


