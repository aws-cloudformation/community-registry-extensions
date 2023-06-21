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
class AwsGreengrassLoggerdefinitionversion(BaseModel):
    Id: Optional[str]
    LoggerDefinitionId: Optional[str]
    Loggers: Optional[Sequence["_Logger"]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsGreengrassLoggerdefinitionversion"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsGreengrassLoggerdefinitionversion"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            LoggerDefinitionId=json_data.get("LoggerDefinitionId"),
            Loggers=deserialize_list(json_data.get("Loggers"), Logger),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsGreengrassLoggerdefinitionversion = AwsGreengrassLoggerdefinitionversion


@dataclass
class Logger(BaseModel):
    Space: Optional[int]
    Type: Optional[str]
    Level: Optional[str]
    Id: Optional[str]
    Component: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Logger"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Logger"]:
        if not json_data:
            return None
        return cls(
            Space=json_data.get("Space"),
            Type=json_data.get("Type"),
            Level=json_data.get("Level"),
            Id=json_data.get("Id"),
            Component=json_data.get("Component"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Logger = Logger


