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
class AwsS3outpostsAccesspoint(BaseModel):
    Arn: Optional[str]
    Bucket: Optional[str]
    Name: Optional[str]
    VpcConfiguration: Optional["_VpcConfiguration"]
    Policy: Optional[MutableMapping[str, Any]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsS3outpostsAccesspoint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsS3outpostsAccesspoint"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            Bucket=json_data.get("Bucket"),
            Name=json_data.get("Name"),
            VpcConfiguration=VpcConfiguration._deserialize(json_data.get("VpcConfiguration")),
            Policy=json_data.get("Policy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsS3outpostsAccesspoint = AwsS3outpostsAccesspoint


@dataclass
class VpcConfiguration(BaseModel):
    VpcId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VpcConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpcConfiguration"]:
        if not json_data:
            return None
        return cls(
            VpcId=json_data.get("VpcId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpcConfiguration = VpcConfiguration


