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
class AwsLocationGeofencecollection(BaseModel):
    CollectionArn: Optional[str]
    Arn: Optional[str]
    CollectionName: Optional[str]
    CreateTime: Optional[str]
    Description: Optional[str]
    KmsKeyId: Optional[str]
    PricingPlan: Optional[str]
    PricingPlanDataSource: Optional[str]
    UpdateTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsLocationGeofencecollection"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsLocationGeofencecollection"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            CollectionArn=json_data.get("CollectionArn"),
            Arn=json_data.get("Arn"),
            CollectionName=json_data.get("CollectionName"),
            CreateTime=json_data.get("CreateTime"),
            Description=json_data.get("Description"),
            KmsKeyId=json_data.get("KmsKeyId"),
            PricingPlan=json_data.get("PricingPlan"),
            PricingPlanDataSource=json_data.get("PricingPlanDataSource"),
            UpdateTime=json_data.get("UpdateTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsLocationGeofencecollection = AwsLocationGeofencecollection


