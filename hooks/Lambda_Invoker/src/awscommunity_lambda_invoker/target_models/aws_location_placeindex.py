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
class AwsLocationPlaceindex(BaseModel):
    CreateTime: Optional[str]
    DataSource: Optional[str]
    DataSourceConfiguration: Optional["_DataSourceConfiguration"]
    Description: Optional[str]
    IndexArn: Optional[str]
    Arn: Optional[str]
    IndexName: Optional[str]
    PricingPlan: Optional[str]
    UpdateTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsLocationPlaceindex"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsLocationPlaceindex"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            CreateTime=json_data.get("CreateTime"),
            DataSource=json_data.get("DataSource"),
            DataSourceConfiguration=DataSourceConfiguration._deserialize(json_data.get("DataSourceConfiguration")),
            Description=json_data.get("Description"),
            IndexArn=json_data.get("IndexArn"),
            Arn=json_data.get("Arn"),
            IndexName=json_data.get("IndexName"),
            PricingPlan=json_data.get("PricingPlan"),
            UpdateTime=json_data.get("UpdateTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsLocationPlaceindex = AwsLocationPlaceindex


@dataclass
class DataSourceConfiguration(BaseModel):
    IntendedUse: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DataSourceConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataSourceConfiguration"]:
        if not json_data:
            return None
        return cls(
            IntendedUse=json_data.get("IntendedUse"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataSourceConfiguration = DataSourceConfiguration


