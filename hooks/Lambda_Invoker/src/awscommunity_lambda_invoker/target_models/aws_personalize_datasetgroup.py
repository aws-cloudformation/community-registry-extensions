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
class AwsPersonalizeDatasetgroup(BaseModel):
    DatasetGroupArn: Optional[str]
    Name: Optional[str]
    KmsKeyArn: Optional[str]
    RoleArn: Optional[str]
    Domain: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsPersonalizeDatasetgroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsPersonalizeDatasetgroup"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            DatasetGroupArn=json_data.get("DatasetGroupArn"),
            Name=json_data.get("Name"),
            KmsKeyArn=json_data.get("KmsKeyArn"),
            RoleArn=json_data.get("RoleArn"),
            Domain=json_data.get("Domain"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsPersonalizeDatasetgroup = AwsPersonalizeDatasetgroup


