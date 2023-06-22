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
class AwsSagemakerNotebookinstancelifecycleconfig(BaseModel):
    Id: Optional[str]
    NotebookInstanceLifecycleConfigName: Optional[str]
    OnStart: Optional[Sequence["_NotebookInstanceLifecycleHook"]]
    OnCreate: Optional[Sequence["_NotebookInstanceLifecycleHook"]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSagemakerNotebookinstancelifecycleconfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSagemakerNotebookinstancelifecycleconfig"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            NotebookInstanceLifecycleConfigName=json_data.get("NotebookInstanceLifecycleConfigName"),
            OnStart=deserialize_list(json_data.get("OnStart"), NotebookInstanceLifecycleHook),
            OnCreate=deserialize_list(json_data.get("OnCreate"), NotebookInstanceLifecycleHook),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSagemakerNotebookinstancelifecycleconfig = AwsSagemakerNotebookinstancelifecycleconfig


@dataclass
class NotebookInstanceLifecycleHook(BaseModel):
    Content: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NotebookInstanceLifecycleHook"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NotebookInstanceLifecycleHook"]:
        if not json_data:
            return None
        return cls(
            Content=json_data.get("Content"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NotebookInstanceLifecycleHook = NotebookInstanceLifecycleHook


