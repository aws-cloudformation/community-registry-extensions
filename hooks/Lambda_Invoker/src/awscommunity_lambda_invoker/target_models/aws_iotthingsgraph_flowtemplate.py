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
class AwsIotthingsgraphFlowtemplate(BaseModel):
    Id: Optional[str]
    CompatibleNamespaceVersion: Optional[float]
    Definition: Optional["_DefinitionDocument"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIotthingsgraphFlowtemplate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIotthingsgraphFlowtemplate"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            CompatibleNamespaceVersion=json_data.get("CompatibleNamespaceVersion"),
            Definition=DefinitionDocument._deserialize(json_data.get("Definition")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIotthingsgraphFlowtemplate = AwsIotthingsgraphFlowtemplate


@dataclass
class DefinitionDocument(BaseModel):
    Language: Optional[str]
    Text: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinitionDocument"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinitionDocument"]:
        if not json_data:
            return None
        return cls(
            Language=json_data.get("Language"),
            Text=json_data.get("Text"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinitionDocument = DefinitionDocument


