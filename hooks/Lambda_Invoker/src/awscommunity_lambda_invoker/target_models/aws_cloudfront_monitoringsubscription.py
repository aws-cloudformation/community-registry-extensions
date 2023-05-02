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
class AwsCloudfrontMonitoringsubscription(BaseModel):
    DistributionId: Optional[str]
    MonitoringSubscription: Optional["_MonitoringSubscription"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCloudfrontMonitoringsubscription"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCloudfrontMonitoringsubscription"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            DistributionId=json_data.get("DistributionId"),
            MonitoringSubscription=MonitoringSubscription._deserialize(json_data.get("MonitoringSubscription")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCloudfrontMonitoringsubscription = AwsCloudfrontMonitoringsubscription


@dataclass
class MonitoringSubscription(BaseModel):
    RealtimeMetricsSubscriptionConfig: Optional["_RealtimeMetricsSubscriptionConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_MonitoringSubscription"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MonitoringSubscription"]:
        if not json_data:
            return None
        return cls(
            RealtimeMetricsSubscriptionConfig=RealtimeMetricsSubscriptionConfig._deserialize(json_data.get("RealtimeMetricsSubscriptionConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_MonitoringSubscription = MonitoringSubscription


@dataclass
class RealtimeMetricsSubscriptionConfig(BaseModel):
    RealtimeMetricsSubscriptionStatus: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RealtimeMetricsSubscriptionConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RealtimeMetricsSubscriptionConfig"]:
        if not json_data:
            return None
        return cls(
            RealtimeMetricsSubscriptionStatus=json_data.get("RealtimeMetricsSubscriptionStatus"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RealtimeMetricsSubscriptionConfig = RealtimeMetricsSubscriptionConfig


