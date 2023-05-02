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
class AwsApigatewayv2Model(BaseModel):
    ModelId: Optional[str]
    Description: Optional[str]
    ContentType: Optional[str]
    Schema: Optional[MutableMapping[str, Any]]
    ApiId: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsApigatewayv2Model"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsApigatewayv2Model"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ModelId=json_data.get("ModelId"),
            Description=json_data.get("Description"),
            ContentType=json_data.get("ContentType"),
            Schema=json_data.get("Schema"),
            ApiId=json_data.get("ApiId"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsApigatewayv2Model = AwsApigatewayv2Model


