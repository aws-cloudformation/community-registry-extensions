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
class AwsSesVdmattributes(BaseModel):
    VdmAttributesResourceId: Optional[str]
    DashboardAttributes: Optional["_DashboardAttributes"]
    GuardianAttributes: Optional["_GuardianAttributes"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSesVdmattributes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSesVdmattributes"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            VdmAttributesResourceId=json_data.get("VdmAttributesResourceId"),
            DashboardAttributes=DashboardAttributes._deserialize(json_data.get("DashboardAttributes")),
            GuardianAttributes=GuardianAttributes._deserialize(json_data.get("GuardianAttributes")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSesVdmattributes = AwsSesVdmattributes


@dataclass
class DashboardAttributes(BaseModel):
    EngagementMetrics: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DashboardAttributes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DashboardAttributes"]:
        if not json_data:
            return None
        return cls(
            EngagementMetrics=json_data.get("EngagementMetrics"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DashboardAttributes = DashboardAttributes


@dataclass
class GuardianAttributes(BaseModel):
    OptimizedSharedDelivery: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GuardianAttributes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GuardianAttributes"]:
        if not json_data:
            return None
        return cls(
            OptimizedSharedDelivery=json_data.get("OptimizedSharedDelivery"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GuardianAttributes = GuardianAttributes


