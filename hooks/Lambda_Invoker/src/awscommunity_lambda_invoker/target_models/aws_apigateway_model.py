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
class AwsApigatewayModel(BaseModel):
    ContentType: Optional[str]
    Description: Optional[str]
    Name: Optional[str]
    RestApiId: Optional[str]
    Schema: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsApigatewayModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsApigatewayModel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ContentType=json_data.get("ContentType"),
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
            RestApiId=json_data.get("RestApiId"),
            Schema=json_data.get("Schema"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsApigatewayModel = AwsApigatewayModel


