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
class AwsNetworkfirewallLoggingconfiguration(BaseModel):
    FirewallName: Optional[str]
    FirewallArn: Optional[str]
    LoggingConfiguration: Optional["_LoggingConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsNetworkfirewallLoggingconfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsNetworkfirewallLoggingconfiguration"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            FirewallName=json_data.get("FirewallName"),
            FirewallArn=json_data.get("FirewallArn"),
            LoggingConfiguration=LoggingConfiguration._deserialize(json_data.get("LoggingConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsNetworkfirewallLoggingconfiguration = AwsNetworkfirewallLoggingconfiguration


@dataclass
class LoggingConfiguration(BaseModel):
    LogDestinationConfigs: Optional[Sequence["_LogDestinationConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingConfiguration"]:
        if not json_data:
            return None
        return cls(
            LogDestinationConfigs=deserialize_list(json_data.get("LogDestinationConfigs"), LogDestinationConfig),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingConfiguration = LoggingConfiguration


@dataclass
class LogDestinationConfig(BaseModel):
    LogType: Optional[str]
    LogDestinationType: Optional[str]
    LogDestination: Optional[MutableMapping[str, str]]

    @classmethod
    def _deserialize(
        cls: Type["_LogDestinationConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogDestinationConfig"]:
        if not json_data:
            return None
        return cls(
            LogType=json_data.get("LogType"),
            LogDestinationType=json_data.get("LogDestinationType"),
            LogDestination=json_data.get("LogDestination"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogDestinationConfig = LogDestinationConfig


