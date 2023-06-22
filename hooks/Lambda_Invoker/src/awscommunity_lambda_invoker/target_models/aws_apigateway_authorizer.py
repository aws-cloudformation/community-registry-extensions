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
class AwsApigatewayAuthorizer(BaseModel):
    RestApiId: Optional[str]
    AuthorizerId: Optional[str]
    AuthType: Optional[str]
    AuthorizerCredentials: Optional[str]
    AuthorizerResultTtlInSeconds: Optional[int]
    AuthorizerUri: Optional[str]
    IdentitySource: Optional[str]
    IdentityValidationExpression: Optional[str]
    Name: Optional[str]
    ProviderARNs: Optional[AbstractSet[str]]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsApigatewayAuthorizer"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsApigatewayAuthorizer"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            RestApiId=json_data.get("RestApiId"),
            AuthorizerId=json_data.get("AuthorizerId"),
            AuthType=json_data.get("AuthType"),
            AuthorizerCredentials=json_data.get("AuthorizerCredentials"),
            AuthorizerResultTtlInSeconds=json_data.get("AuthorizerResultTtlInSeconds"),
            AuthorizerUri=json_data.get("AuthorizerUri"),
            IdentitySource=json_data.get("IdentitySource"),
            IdentityValidationExpression=json_data.get("IdentityValidationExpression"),
            Name=json_data.get("Name"),
            ProviderARNs=set_or_none(json_data.get("ProviderARNs")),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsApigatewayAuthorizer = AwsApigatewayAuthorizer


