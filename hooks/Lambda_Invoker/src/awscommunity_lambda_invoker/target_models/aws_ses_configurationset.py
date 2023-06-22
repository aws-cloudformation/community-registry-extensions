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
class AwsSesConfigurationset(BaseModel):
    Name: Optional[str]
    TrackingOptions: Optional["_TrackingOptions"]
    DeliveryOptions: Optional["_DeliveryOptions"]
    ReputationOptions: Optional["_ReputationOptions"]
    SendingOptions: Optional["_SendingOptions"]
    SuppressionOptions: Optional["_SuppressionOptions"]
    VdmOptions: Optional["_VdmOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSesConfigurationset"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSesConfigurationset"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Name=json_data.get("Name"),
            TrackingOptions=TrackingOptions._deserialize(json_data.get("TrackingOptions")),
            DeliveryOptions=DeliveryOptions._deserialize(json_data.get("DeliveryOptions")),
            ReputationOptions=ReputationOptions._deserialize(json_data.get("ReputationOptions")),
            SendingOptions=SendingOptions._deserialize(json_data.get("SendingOptions")),
            SuppressionOptions=SuppressionOptions._deserialize(json_data.get("SuppressionOptions")),
            VdmOptions=VdmOptions._deserialize(json_data.get("VdmOptions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSesConfigurationset = AwsSesConfigurationset


@dataclass
class TrackingOptions(BaseModel):
    CustomRedirectDomain: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TrackingOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TrackingOptions"]:
        if not json_data:
            return None
        return cls(
            CustomRedirectDomain=json_data.get("CustomRedirectDomain"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TrackingOptions = TrackingOptions


@dataclass
class DeliveryOptions(BaseModel):
    TlsPolicy: Optional[str]
    SendingPoolName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DeliveryOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeliveryOptions"]:
        if not json_data:
            return None
        return cls(
            TlsPolicy=json_data.get("TlsPolicy"),
            SendingPoolName=json_data.get("SendingPoolName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeliveryOptions = DeliveryOptions


@dataclass
class ReputationOptions(BaseModel):
    ReputationMetricsEnabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ReputationOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReputationOptions"]:
        if not json_data:
            return None
        return cls(
            ReputationMetricsEnabled=json_data.get("ReputationMetricsEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReputationOptions = ReputationOptions


@dataclass
class SendingOptions(BaseModel):
    SendingEnabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SendingOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SendingOptions"]:
        if not json_data:
            return None
        return cls(
            SendingEnabled=json_data.get("SendingEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SendingOptions = SendingOptions


@dataclass
class SuppressionOptions(BaseModel):
    SuppressedReasons: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_SuppressionOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SuppressionOptions"]:
        if not json_data:
            return None
        return cls(
            SuppressedReasons=json_data.get("SuppressedReasons"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SuppressionOptions = SuppressionOptions


@dataclass
class VdmOptions(BaseModel):
    DashboardOptions: Optional["_DashboardOptions"]
    GuardianOptions: Optional["_GuardianOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_VdmOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VdmOptions"]:
        if not json_data:
            return None
        return cls(
            DashboardOptions=DashboardOptions._deserialize(json_data.get("DashboardOptions")),
            GuardianOptions=GuardianOptions._deserialize(json_data.get("GuardianOptions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_VdmOptions = VdmOptions


@dataclass
class DashboardOptions(BaseModel):
    EngagementMetrics: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DashboardOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DashboardOptions"]:
        if not json_data:
            return None
        return cls(
            EngagementMetrics=json_data.get("EngagementMetrics"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DashboardOptions = DashboardOptions


@dataclass
class GuardianOptions(BaseModel):
    OptimizedSharedDelivery: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GuardianOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GuardianOptions"]:
        if not json_data:
            return None
        return cls(
            OptimizedSharedDelivery=json_data.get("OptimizedSharedDelivery"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GuardianOptions = GuardianOptions


