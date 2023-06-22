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
class AwsSesConfigurationseteventdestination(BaseModel):
    Id: Optional[str]
    ConfigurationSetName: Optional[str]
    EventDestination: Optional["_EventDestination"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSesConfigurationseteventdestination"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSesConfigurationseteventdestination"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            ConfigurationSetName=json_data.get("ConfigurationSetName"),
            EventDestination=EventDestination._deserialize(json_data.get("EventDestination")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSesConfigurationseteventdestination = AwsSesConfigurationseteventdestination


@dataclass
class EventDestination(BaseModel):
    Name: Optional[str]
    Enabled: Optional[bool]
    MatchingEventTypes: Optional[Sequence[str]]
    CloudWatchDestination: Optional["_CloudWatchDestination"]
    KinesisFirehoseDestination: Optional["_KinesisFirehoseDestination"]
    SnsDestination: Optional["_SnsDestination"]

    @classmethod
    def _deserialize(
        cls: Type["_EventDestination"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EventDestination"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Enabled=json_data.get("Enabled"),
            MatchingEventTypes=json_data.get("MatchingEventTypes"),
            CloudWatchDestination=CloudWatchDestination._deserialize(json_data.get("CloudWatchDestination")),
            KinesisFirehoseDestination=KinesisFirehoseDestination._deserialize(json_data.get("KinesisFirehoseDestination")),
            SnsDestination=SnsDestination._deserialize(json_data.get("SnsDestination")),
        )


# work around possible type aliasing issues when variable has same name as a model
_EventDestination = EventDestination


@dataclass
class CloudWatchDestination(BaseModel):
    DimensionConfigurations: Optional[Sequence["_DimensionConfiguration"]]

    @classmethod
    def _deserialize(
        cls: Type["_CloudWatchDestination"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudWatchDestination"]:
        if not json_data:
            return None
        return cls(
            DimensionConfigurations=deserialize_list(json_data.get("DimensionConfigurations"), DimensionConfiguration),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudWatchDestination = CloudWatchDestination


@dataclass
class DimensionConfiguration(BaseModel):
    DimensionValueSource: Optional[str]
    DefaultDimensionValue: Optional[str]
    DimensionName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DimensionConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DimensionConfiguration"]:
        if not json_data:
            return None
        return cls(
            DimensionValueSource=json_data.get("DimensionValueSource"),
            DefaultDimensionValue=json_data.get("DefaultDimensionValue"),
            DimensionName=json_data.get("DimensionName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DimensionConfiguration = DimensionConfiguration


@dataclass
class KinesisFirehoseDestination(BaseModel):
    IAMRoleARN: Optional[str]
    DeliveryStreamARN: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KinesisFirehoseDestination"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KinesisFirehoseDestination"]:
        if not json_data:
            return None
        return cls(
            IAMRoleARN=json_data.get("IAMRoleARN"),
            DeliveryStreamARN=json_data.get("DeliveryStreamARN"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KinesisFirehoseDestination = KinesisFirehoseDestination


@dataclass
class SnsDestination(BaseModel):
    TopicARN: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SnsDestination"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnsDestination"]:
        if not json_data:
            return None
        return cls(
            TopicARN=json_data.get("TopicARN"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnsDestination = SnsDestination


