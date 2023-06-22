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
class AwsApigatewayDocumentationpart(BaseModel):
    DocumentationPartId: Optional[str]
    Location: Optional["_Location"]
    Properties: Optional[str]
    RestApiId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsApigatewayDocumentationpart"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsApigatewayDocumentationpart"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            DocumentationPartId=json_data.get("DocumentationPartId"),
            Location=Location._deserialize(json_data.get("Location")),
            Properties=json_data.get("Properties"),
            RestApiId=json_data.get("RestApiId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsApigatewayDocumentationpart = AwsApigatewayDocumentationpart


@dataclass
class Location(BaseModel):
    Method: Optional[str]
    Name: Optional[str]
    Path: Optional[str]
    StatusCode: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Location"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Location"]:
        if not json_data:
            return None
        return cls(
            Method=json_data.get("Method"),
            Name=json_data.get("Name"),
            Path=json_data.get("Path"),
            StatusCode=json_data.get("StatusCode"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Location = Location


