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
class AwsServicecatalogServiceaction(BaseModel):
    AcceptLanguage: Optional[str]
    Name: Optional[str]
    DefinitionType: Optional[str]
    Definition: Optional[Sequence["_DefinitionParameter"]]
    Description: Optional[str]
    Id: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsServicecatalogServiceaction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsServicecatalogServiceaction"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AcceptLanguage=json_data.get("AcceptLanguage"),
            Name=json_data.get("Name"),
            DefinitionType=json_data.get("DefinitionType"),
            Definition=deserialize_list(json_data.get("Definition"), DefinitionParameter),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsServicecatalogServiceaction = AwsServicecatalogServiceaction


@dataclass
class DefinitionParameter(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinitionParameter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinitionParameter"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinitionParameter = DefinitionParameter


