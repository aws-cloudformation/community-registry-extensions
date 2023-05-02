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
class AwsIotTopicruledestination(BaseModel):
    Arn: Optional[str]
    Status: Optional[str]
    HttpUrlProperties: Optional["_HttpUrlDestinationSummary"]
    StatusReason: Optional[str]
    VpcProperties: Optional["_VpcDestinationProperties"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIotTopicruledestination"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIotTopicruledestination"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            Status=json_data.get("Status"),
            HttpUrlProperties=HttpUrlDestinationSummary._deserialize(json_data.get("HttpUrlProperties")),
            StatusReason=json_data.get("StatusReason"),
            VpcProperties=VpcDestinationProperties._deserialize(json_data.get("VpcProperties")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIotTopicruledestination = AwsIotTopicruledestination


@dataclass
class HttpUrlDestinationSummary(BaseModel):
    ConfirmationUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HttpUrlDestinationSummary"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpUrlDestinationSummary"]:
        if not json_data:
            return None
        return cls(
            ConfirmationUrl=json_data.get("ConfirmationUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpUrlDestinationSummary = HttpUrlDestinationSummary


@dataclass
class VpcDestinationProperties(BaseModel):
    SubnetIds: Optional[Sequence[str]]
    SecurityGroups: Optional[Sequence[str]]
    VpcId: Optional[str]
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VpcDestinationProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpcDestinationProperties"]:
        if not json_data:
            return None
        return cls(
            SubnetIds=json_data.get("SubnetIds"),
            SecurityGroups=json_data.get("SecurityGroups"),
            VpcId=json_data.get("VpcId"),
            RoleArn=json_data.get("RoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpcDestinationProperties = VpcDestinationProperties


