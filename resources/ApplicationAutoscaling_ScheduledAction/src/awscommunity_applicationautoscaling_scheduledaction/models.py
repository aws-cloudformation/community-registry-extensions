# DO NOT modify this file by hand, changes will be overwritten
import sys
from dataclasses import dataclass
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

from cloudformation_cli_python_lib.interface import (
    BaseModel,
    BaseResourceHandlerRequest,
)
from cloudformation_cli_python_lib.recast import recast_object
from cloudformation_cli_python_lib.utils import deserialize_list

T = TypeVar("T")


def set_or_none(value: Optional[Sequence[T]]) -> Optional[AbstractSet[T]]:
    if value:
        return set(value)
    return None


@dataclass
class ResourceHandlerRequest(BaseResourceHandlerRequest):
    # pylint: disable=invalid-name
    desiredResourceState: Optional["ResourceModel"]
    previousResourceState: Optional["ResourceModel"]
    typeConfiguration: Optional["TypeConfigurationModel"]


@dataclass
class ResourceModel(BaseModel):
    EndTime: Optional[str]
    ResourceId: Optional[str]
    ScalableDimension: Optional[str]
    ScalableTargetAction: Optional["_ScalableTargetAction"]
    Schedule: Optional[str]
    ScheduledActionName: Optional[str]
    ServiceNamespace: Optional[str]
    StartTime: Optional[str]
    Timezone: Optional[str]
    ScheduledActionARN: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            EndTime=json_data.get("EndTime"),
            ResourceId=json_data.get("ResourceId"),
            ScalableDimension=json_data.get("ScalableDimension"),
            ScalableTargetAction=ScalableTargetAction._deserialize(
                json_data.get("ScalableTargetAction")
            ),
            Schedule=json_data.get("Schedule"),
            ScheduledActionName=json_data.get("ScheduledActionName"),
            ServiceNamespace=json_data.get("ServiceNamespace"),
            StartTime=json_data.get("StartTime"),
            Timezone=json_data.get("Timezone"),
            ScheduledActionARN=json_data.get("ScheduledActionARN"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ScalableTargetAction(BaseModel):
    MaxCapacity: Optional[float]
    MinCapacity: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ScalableTargetAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScalableTargetAction"]:
        if not json_data:
            return None
        return cls(
            MaxCapacity=json_data.get("MaxCapacity"),
            MinCapacity=json_data.get("MinCapacity"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScalableTargetAction = ScalableTargetAction


@dataclass
class TypeConfigurationModel(BaseModel):
    @classmethod
    def _deserialize(
        cls: Type["_TypeConfigurationModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TypeConfigurationModel"]:
        if not json_data:
            return None
        return cls()


# work around possible type aliasing issues when variable has same name as a model
_TypeConfigurationModel = TypeConfigurationModel
