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
class AwsBudgetsBudget(BaseModel):
    NotificationsWithSubscribers: Optional[Sequence["_NotificationWithSubscribers"]]
    Budget: Optional["_BudgetData"]
    Id: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsBudgetsBudget"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsBudgetsBudget"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            NotificationsWithSubscribers=deserialize_list(json_data.get("NotificationsWithSubscribers"), NotificationWithSubscribers),
            Budget=BudgetData._deserialize(json_data.get("Budget")),
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsBudgetsBudget = AwsBudgetsBudget


@dataclass
class NotificationWithSubscribers(BaseModel):
    Subscribers: Optional[Sequence["_Subscriber"]]
    Notification: Optional["_Notification"]

    @classmethod
    def _deserialize(
        cls: Type["_NotificationWithSubscribers"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NotificationWithSubscribers"]:
        if not json_data:
            return None
        return cls(
            Subscribers=deserialize_list(json_data.get("Subscribers"), Subscriber),
            Notification=Notification._deserialize(json_data.get("Notification")),
        )


# work around possible type aliasing issues when variable has same name as a model
_NotificationWithSubscribers = NotificationWithSubscribers


@dataclass
class Subscriber(BaseModel):
    Address: Optional[str]
    SubscriptionType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Subscriber"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Subscriber"]:
        if not json_data:
            return None
        return cls(
            Address=json_data.get("Address"),
            SubscriptionType=json_data.get("SubscriptionType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Subscriber = Subscriber


@dataclass
class Notification(BaseModel):
    ComparisonOperator: Optional[str]
    NotificationType: Optional[str]
    Threshold: Optional[float]
    ThresholdType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Notification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Notification"]:
        if not json_data:
            return None
        return cls(
            ComparisonOperator=json_data.get("ComparisonOperator"),
            NotificationType=json_data.get("NotificationType"),
            Threshold=json_data.get("Threshold"),
            ThresholdType=json_data.get("ThresholdType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Notification = Notification


@dataclass
class BudgetData(BaseModel):
    BudgetLimit: Optional["_Spend"]
    TimePeriod: Optional["_TimePeriod"]
    AutoAdjustData: Optional["_AutoAdjustData"]
    TimeUnit: Optional[str]
    PlannedBudgetLimits: Optional[MutableMapping[str, Any]]
    CostFilters: Optional[MutableMapping[str, Any]]
    BudgetName: Optional[str]
    CostTypes: Optional["_CostTypes"]
    BudgetType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BudgetData"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BudgetData"]:
        if not json_data:
            return None
        return cls(
            BudgetLimit=Spend._deserialize(json_data.get("BudgetLimit")),
            TimePeriod=TimePeriod._deserialize(json_data.get("TimePeriod")),
            AutoAdjustData=AutoAdjustData._deserialize(json_data.get("AutoAdjustData")),
            TimeUnit=json_data.get("TimeUnit"),
            PlannedBudgetLimits=json_data.get("PlannedBudgetLimits"),
            CostFilters=json_data.get("CostFilters"),
            BudgetName=json_data.get("BudgetName"),
            CostTypes=CostTypes._deserialize(json_data.get("CostTypes")),
            BudgetType=json_data.get("BudgetType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BudgetData = BudgetData


@dataclass
class Spend(BaseModel):
    Unit: Optional[str]
    Amount: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Spend"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Spend"]:
        if not json_data:
            return None
        return cls(
            Unit=json_data.get("Unit"),
            Amount=json_data.get("Amount"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Spend = Spend


@dataclass
class TimePeriod(BaseModel):
    Start: Optional[str]
    End: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimePeriod"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimePeriod"]:
        if not json_data:
            return None
        return cls(
            Start=json_data.get("Start"),
            End=json_data.get("End"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimePeriod = TimePeriod


@dataclass
class AutoAdjustData(BaseModel):
    AutoAdjustType: Optional[str]
    HistoricalOptions: Optional["_HistoricalOptions"]

    @classmethod
    def _deserialize(
        cls: Type["_AutoAdjustData"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoAdjustData"]:
        if not json_data:
            return None
        return cls(
            AutoAdjustType=json_data.get("AutoAdjustType"),
            HistoricalOptions=HistoricalOptions._deserialize(json_data.get("HistoricalOptions")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoAdjustData = AutoAdjustData


@dataclass
class HistoricalOptions(BaseModel):
    BudgetAdjustmentPeriod: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_HistoricalOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HistoricalOptions"]:
        if not json_data:
            return None
        return cls(
            BudgetAdjustmentPeriod=json_data.get("BudgetAdjustmentPeriod"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HistoricalOptions = HistoricalOptions


@dataclass
class CostTypes(BaseModel):
    IncludeSupport: Optional[bool]
    IncludeOtherSubscription: Optional[bool]
    IncludeTax: Optional[bool]
    IncludeSubscription: Optional[bool]
    UseBlended: Optional[bool]
    IncludeUpfront: Optional[bool]
    IncludeDiscount: Optional[bool]
    IncludeCredit: Optional[bool]
    IncludeRecurring: Optional[bool]
    UseAmortized: Optional[bool]
    IncludeRefund: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_CostTypes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CostTypes"]:
        if not json_data:
            return None
        return cls(
            IncludeSupport=json_data.get("IncludeSupport"),
            IncludeOtherSubscription=json_data.get("IncludeOtherSubscription"),
            IncludeTax=json_data.get("IncludeTax"),
            IncludeSubscription=json_data.get("IncludeSubscription"),
            UseBlended=json_data.get("UseBlended"),
            IncludeUpfront=json_data.get("IncludeUpfront"),
            IncludeDiscount=json_data.get("IncludeDiscount"),
            IncludeCredit=json_data.get("IncludeCredit"),
            IncludeRecurring=json_data.get("IncludeRecurring"),
            UseAmortized=json_data.get("UseAmortized"),
            IncludeRefund=json_data.get("IncludeRefund"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CostTypes = CostTypes


