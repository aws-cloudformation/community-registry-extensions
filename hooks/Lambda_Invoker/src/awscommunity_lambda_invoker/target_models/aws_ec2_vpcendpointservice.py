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
class AwsEc2Vpcendpointservice(BaseModel):
    NetworkLoadBalancerArns: Optional[Sequence[str]]
    ContributorInsightsEnabled: Optional[bool]
    PayerResponsibility: Optional[str]
    ServiceId: Optional[str]
    AcceptanceRequired: Optional[bool]
    GatewayLoadBalancerArns: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Vpcendpointservice"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Vpcendpointservice"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            NetworkLoadBalancerArns=json_data.get("NetworkLoadBalancerArns"),
            ContributorInsightsEnabled=json_data.get("ContributorInsightsEnabled"),
            PayerResponsibility=json_data.get("PayerResponsibility"),
            ServiceId=json_data.get("ServiceId"),
            AcceptanceRequired=json_data.get("AcceptanceRequired"),
            GatewayLoadBalancerArns=json_data.get("GatewayLoadBalancerArns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Vpcendpointservice = AwsEc2Vpcendpointservice


