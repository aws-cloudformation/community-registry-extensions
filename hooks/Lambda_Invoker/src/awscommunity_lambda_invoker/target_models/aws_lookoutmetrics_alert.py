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
class AwsLookoutmetricsAlert(BaseModel):
    AlertName: Optional[str]
    Arn: Optional[str]
    AlertDescription: Optional[str]
    AnomalyDetectorArn: Optional[str]
    AlertSensitivityThreshold: Optional[int]
    Action: Optional["_Action"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsLookoutmetricsAlert"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsLookoutmetricsAlert"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AlertName=json_data.get("AlertName"),
            Arn=json_data.get("Arn"),
            AlertDescription=json_data.get("AlertDescription"),
            AnomalyDetectorArn=json_data.get("AnomalyDetectorArn"),
            AlertSensitivityThreshold=json_data.get("AlertSensitivityThreshold"),
            Action=Action._deserialize(json_data.get("Action")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsLookoutmetricsAlert = AwsLookoutmetricsAlert


@dataclass
class Action(BaseModel):
    SNSConfiguration: Optional["_SNSConfiguration"]
    LambdaConfiguration: Optional["_LambdaConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_Action"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Action"]:
        if not json_data:
            return None
        return cls(
            SNSConfiguration=SNSConfiguration._deserialize(json_data.get("SNSConfiguration")),
            LambdaConfiguration=LambdaConfiguration._deserialize(json_data.get("LambdaConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Action = Action


@dataclass
class SNSConfiguration(BaseModel):
    RoleArn: Optional[str]
    SnsTopicArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SNSConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SNSConfiguration"]:
        if not json_data:
            return None
        return cls(
            RoleArn=json_data.get("RoleArn"),
            SnsTopicArn=json_data.get("SnsTopicArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SNSConfiguration = SNSConfiguration


@dataclass
class LambdaConfiguration(BaseModel):
    RoleArn: Optional[str]
    LambdaArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LambdaConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LambdaConfiguration"]:
        if not json_data:
            return None
        return cls(
            RoleArn=json_data.get("RoleArn"),
            LambdaArn=json_data.get("LambdaArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LambdaConfiguration = LambdaConfiguration


