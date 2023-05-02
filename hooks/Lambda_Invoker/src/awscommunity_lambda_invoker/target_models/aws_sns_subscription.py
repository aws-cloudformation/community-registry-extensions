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
class AwsSnsSubscription(BaseModel):
    RawMessageDelivery: Optional[bool]
    Endpoint: Optional[str]
    FilterPolicy: Optional[MutableMapping[str, Any]]
    TopicArn: Optional[str]
    RedrivePolicy: Optional[MutableMapping[str, Any]]
    DeliveryPolicy: Optional[MutableMapping[str, Any]]
    Region: Optional[str]
    SubscriptionRoleArn: Optional[str]
    FilterPolicyScope: Optional[str]
    Id: Optional[str]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSnsSubscription"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSnsSubscription"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            RawMessageDelivery=json_data.get("RawMessageDelivery"),
            Endpoint=json_data.get("Endpoint"),
            FilterPolicy=json_data.get("FilterPolicy"),
            TopicArn=json_data.get("TopicArn"),
            RedrivePolicy=json_data.get("RedrivePolicy"),
            DeliveryPolicy=json_data.get("DeliveryPolicy"),
            Region=json_data.get("Region"),
            SubscriptionRoleArn=json_data.get("SubscriptionRoleArn"),
            FilterPolicyScope=json_data.get("FilterPolicyScope"),
            Id=json_data.get("Id"),
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSnsSubscription = AwsSnsSubscription


