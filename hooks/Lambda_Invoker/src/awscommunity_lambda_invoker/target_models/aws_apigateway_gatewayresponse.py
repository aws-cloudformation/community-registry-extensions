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
class AwsApigatewayGatewayresponse(BaseModel):
    Id: Optional[str]
    RestApiId: Optional[str]
    ResponseType: Optional[str]
    StatusCode: Optional[str]
    ResponseParameters: Optional[MutableMapping[str, str]]
    ResponseTemplates: Optional[MutableMapping[str, str]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsApigatewayGatewayresponse"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsApigatewayGatewayresponse"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            RestApiId=json_data.get("RestApiId"),
            ResponseType=json_data.get("ResponseType"),
            StatusCode=json_data.get("StatusCode"),
            ResponseParameters=json_data.get("ResponseParameters"),
            ResponseTemplates=json_data.get("ResponseTemplates"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsApigatewayGatewayresponse = AwsApigatewayGatewayresponse


