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
class AwsEmrStep(BaseModel):
    Id: Optional[str]
    ActionOnFailure: Optional[str]
    HadoopJarStep: Optional["_HadoopJarStepConfig"]
    JobFlowId: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEmrStep"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEmrStep"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            ActionOnFailure=json_data.get("ActionOnFailure"),
            HadoopJarStep=HadoopJarStepConfig._deserialize(json_data.get("HadoopJarStep")),
            JobFlowId=json_data.get("JobFlowId"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEmrStep = AwsEmrStep


@dataclass
class HadoopJarStepConfig(BaseModel):
    Args: Optional[Sequence[str]]
    Jar: Optional[str]
    MainClass: Optional[str]
    StepProperties: Optional[Sequence["_KeyValue"]]

    @classmethod
    def _deserialize(
        cls: Type["_HadoopJarStepConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HadoopJarStepConfig"]:
        if not json_data:
            return None
        return cls(
            Args=json_data.get("Args"),
            Jar=json_data.get("Jar"),
            MainClass=json_data.get("MainClass"),
            StepProperties=deserialize_list(json_data.get("StepProperties"), KeyValue),
        )


# work around possible type aliasing issues when variable has same name as a model
_HadoopJarStepConfig = HadoopJarStepConfig


@dataclass
class KeyValue(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KeyValue"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KeyValue"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KeyValue = KeyValue


