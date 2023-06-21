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
class AwsPinpointemailConfigurationseteventdestination(BaseModel):
    Id: Optional[str]
    EventDestinationName: Optional[str]
    ConfigurationSetName: Optional[str]
    EventDestination: Optional["_EventDestination"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsPinpointemailConfigurationseteventdestination"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsPinpointemailConfigurationseteventdestination"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            EventDestinationName=json_data.get("EventDestinationName"),
            ConfigurationSetName=json_data.get("ConfigurationSetName"),
            EventDestination=EventDestination._deserialize(json_data.get("EventDestination")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsPinpointemailConfigurationseteventdestination = AwsPinpointemailConfigurationseteventdestination


@dataclass
class EventDestination(BaseModel):
    SnsDestination: Optional["_SnsDestination"]
    CloudWatchDestination: Optional["_CloudWatchDestination"]
    Enabled: Optional[bool]
    MatchingEventTypes: Optional[Sequence[str]]
    PinpointDestination: Optional["_PinpointDestination"]
    KinesisFirehoseDestination: Optional["_KinesisFirehoseDestination"]

    @classmethod
    def _deserialize(
        cls: Type["_EventDestination"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EventDestination"]:
        if not json_data:
            return None
        return cls(
            SnsDestination=SnsDestination._deserialize(json_data.get("SnsDestination")),
            CloudWatchDestination=CloudWatchDestination._deserialize(json_data.get("CloudWatchDestination")),
            Enabled=json_data.get("Enabled"),
            MatchingEventTypes=json_data.get("MatchingEventTypes"),
            PinpointDestination=PinpointDestination._deserialize(json_data.get("PinpointDestination")),
            KinesisFirehoseDestination=KinesisFirehoseDestination._deserialize(json_data.get("KinesisFirehoseDestination")),
        )


# work around possible type aliasing issues when variable has same name as a model
_EventDestination = EventDestination


@dataclass
class SnsDestination(BaseModel):
    TopicArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SnsDestination"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnsDestination"]:
        if not json_data:
            return None
        return cls(
            TopicArn=json_data.get("TopicArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnsDestination = SnsDestination


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
class PinpointDestination(BaseModel):
    ApplicationArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PinpointDestination"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PinpointDestination"]:
        if not json_data:
            return None
        return cls(
            ApplicationArn=json_data.get("ApplicationArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PinpointDestination = PinpointDestination


@dataclass
class KinesisFirehoseDestination(BaseModel):
    DeliveryStreamArn: Optional[str]
    IamRoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KinesisFirehoseDestination"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KinesisFirehoseDestination"]:
        if not json_data:
            return None
        return cls(
            DeliveryStreamArn=json_data.get("DeliveryStreamArn"),
            IamRoleArn=json_data.get("IamRoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KinesisFirehoseDestination = KinesisFirehoseDestination


