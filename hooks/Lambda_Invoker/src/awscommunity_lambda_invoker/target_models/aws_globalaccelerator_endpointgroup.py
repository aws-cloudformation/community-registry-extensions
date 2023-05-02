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
class AwsGlobalacceleratorEndpointgroup(BaseModel):
    ListenerArn: Optional[str]
    EndpointGroupRegion: Optional[str]
    EndpointConfigurations: Optional[Sequence["_EndpointConfiguration"]]
    TrafficDialPercentage: Optional[float]
    HealthCheckPort: Optional[int]
    HealthCheckProtocol: Optional[str]
    HealthCheckPath: Optional[str]
    HealthCheckIntervalSeconds: Optional[int]
    ThresholdCount: Optional[int]
    EndpointGroupArn: Optional[str]
    PortOverrides: Optional[Sequence["_PortOverride"]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsGlobalacceleratorEndpointgroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsGlobalacceleratorEndpointgroup"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ListenerArn=json_data.get("ListenerArn"),
            EndpointGroupRegion=json_data.get("EndpointGroupRegion"),
            EndpointConfigurations=deserialize_list(json_data.get("EndpointConfigurations"), EndpointConfiguration),
            TrafficDialPercentage=json_data.get("TrafficDialPercentage"),
            HealthCheckPort=json_data.get("HealthCheckPort"),
            HealthCheckProtocol=json_data.get("HealthCheckProtocol"),
            HealthCheckPath=json_data.get("HealthCheckPath"),
            HealthCheckIntervalSeconds=json_data.get("HealthCheckIntervalSeconds"),
            ThresholdCount=json_data.get("ThresholdCount"),
            EndpointGroupArn=json_data.get("EndpointGroupArn"),
            PortOverrides=deserialize_list(json_data.get("PortOverrides"), PortOverride),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsGlobalacceleratorEndpointgroup = AwsGlobalacceleratorEndpointgroup


@dataclass
class EndpointConfiguration(BaseModel):
    EndpointId: Optional[str]
    Weight: Optional[int]
    ClientIPPreservationEnabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_EndpointConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EndpointConfiguration"]:
        if not json_data:
            return None
        return cls(
            EndpointId=json_data.get("EndpointId"),
            Weight=json_data.get("Weight"),
            ClientIPPreservationEnabled=json_data.get("ClientIPPreservationEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EndpointConfiguration = EndpointConfiguration


@dataclass
class PortOverride(BaseModel):
    ListenerPort: Optional[int]
    EndpointPort: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_PortOverride"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortOverride"]:
        if not json_data:
            return None
        return cls(
            ListenerPort=json_data.get("ListenerPort"),
            EndpointPort=json_data.get("EndpointPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortOverride = PortOverride


