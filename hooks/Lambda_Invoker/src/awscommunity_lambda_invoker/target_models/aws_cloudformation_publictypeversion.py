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
class AwsCloudformationPublictypeversion(BaseModel):
    Arn: Optional[str]
    TypeVersionArn: Optional[str]
    PublicVersionNumber: Optional[str]
    PublisherId: Optional[str]
    PublicTypeArn: Optional[str]
    TypeName: Optional[str]
    LogDeliveryBucket: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCloudformationPublictypeversion"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCloudformationPublictypeversion"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            TypeVersionArn=json_data.get("TypeVersionArn"),
            PublicVersionNumber=json_data.get("PublicVersionNumber"),
            PublisherId=json_data.get("PublisherId"),
            PublicTypeArn=json_data.get("PublicTypeArn"),
            TypeName=json_data.get("TypeName"),
            LogDeliveryBucket=json_data.get("LogDeliveryBucket"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCloudformationPublictypeversion = AwsCloudformationPublictypeversion


