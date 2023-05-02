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
class AwsEventsEndpoint(BaseModel):
    Name: Optional[str]
    Arn: Optional[str]
    RoleArn: Optional[str]
    Description: Optional[str]
    RoutingConfig: Optional["_RoutingConfig"]
    ReplicationConfig: Optional["_ReplicationConfig"]
    EventBuses: Optional[Sequence["_EndpointEventBus"]]
    EndpointId: Optional[str]
    EndpointUrl: Optional[str]
    State: Optional[str]
    StateReason: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEventsEndpoint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEventsEndpoint"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Name=json_data.get("Name"),
            Arn=json_data.get("Arn"),
            RoleArn=json_data.get("RoleArn"),
            Description=json_data.get("Description"),
            RoutingConfig=RoutingConfig._deserialize(json_data.get("RoutingConfig")),
            ReplicationConfig=ReplicationConfig._deserialize(json_data.get("ReplicationConfig")),
            EventBuses=deserialize_list(json_data.get("EventBuses"), EndpointEventBus),
            EndpointId=json_data.get("EndpointId"),
            EndpointUrl=json_data.get("EndpointUrl"),
            State=json_data.get("State"),
            StateReason=json_data.get("StateReason"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEventsEndpoint = AwsEventsEndpoint


@dataclass
class RoutingConfig(BaseModel):
    FailoverConfig: Optional["_FailoverConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_RoutingConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RoutingConfig"]:
        if not json_data:
            return None
        return cls(
            FailoverConfig=FailoverConfig._deserialize(json_data.get("FailoverConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_RoutingConfig = RoutingConfig


@dataclass
class FailoverConfig(BaseModel):
    Primary: Optional["_Primary"]
    Secondary: Optional["_Secondary"]

    @classmethod
    def _deserialize(
        cls: Type["_FailoverConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FailoverConfig"]:
        if not json_data:
            return None
        return cls(
            Primary=Primary._deserialize(json_data.get("Primary")),
            Secondary=Secondary._deserialize(json_data.get("Secondary")),
        )


# work around possible type aliasing issues when variable has same name as a model
_FailoverConfig = FailoverConfig


@dataclass
class Primary(BaseModel):
    HealthCheck: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Primary"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Primary"]:
        if not json_data:
            return None
        return cls(
            HealthCheck=json_data.get("HealthCheck"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Primary = Primary


@dataclass
class Secondary(BaseModel):
    Route: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Secondary"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Secondary"]:
        if not json_data:
            return None
        return cls(
            Route=json_data.get("Route"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Secondary = Secondary


@dataclass
class ReplicationConfig(BaseModel):
    State: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ReplicationConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReplicationConfig"]:
        if not json_data:
            return None
        return cls(
            State=json_data.get("State"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReplicationConfig = ReplicationConfig


@dataclass
class EndpointEventBus(BaseModel):
    EventBusArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EndpointEventBus"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EndpointEventBus"]:
        if not json_data:
            return None
        return cls(
            EventBusArn=json_data.get("EventBusArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EndpointEventBus = EndpointEventBus


