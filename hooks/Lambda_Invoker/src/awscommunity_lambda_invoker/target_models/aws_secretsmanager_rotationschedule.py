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
class AwsSecretsmanagerRotationschedule(BaseModel):
    Id: Optional[str]
    RotationLambdaARN: Optional[str]
    RotationRules: Optional["_RotationRules"]
    RotateImmediatelyOnUpdate: Optional[bool]
    SecretId: Optional[str]
    HostedRotationLambda: Optional["_HostedRotationLambda"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSecretsmanagerRotationschedule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSecretsmanagerRotationschedule"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            RotationLambdaARN=json_data.get("RotationLambdaARN"),
            RotationRules=RotationRules._deserialize(json_data.get("RotationRules")),
            RotateImmediatelyOnUpdate=json_data.get("RotateImmediatelyOnUpdate"),
            SecretId=json_data.get("SecretId"),
            HostedRotationLambda=HostedRotationLambda._deserialize(json_data.get("HostedRotationLambda")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSecretsmanagerRotationschedule = AwsSecretsmanagerRotationschedule


@dataclass
class RotationRules(BaseModel):
    ScheduleExpression: Optional[str]
    Duration: Optional[str]
    AutomaticallyAfterDays: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_RotationRules"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RotationRules"]:
        if not json_data:
            return None
        return cls(
            ScheduleExpression=json_data.get("ScheduleExpression"),
            Duration=json_data.get("Duration"),
            AutomaticallyAfterDays=json_data.get("AutomaticallyAfterDays"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RotationRules = RotationRules


@dataclass
class HostedRotationLambda(BaseModel):
    Runtime: Optional[str]
    RotationType: Optional[str]
    RotationLambdaName: Optional[str]
    KmsKeyArn: Optional[str]
    MasterSecretArn: Optional[str]
    VpcSecurityGroupIds: Optional[str]
    ExcludeCharacters: Optional[str]
    MasterSecretKmsKeyArn: Optional[str]
    SuperuserSecretArn: Optional[str]
    SuperuserSecretKmsKeyArn: Optional[str]
    VpcSubnetIds: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HostedRotationLambda"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostedRotationLambda"]:
        if not json_data:
            return None
        return cls(
            Runtime=json_data.get("Runtime"),
            RotationType=json_data.get("RotationType"),
            RotationLambdaName=json_data.get("RotationLambdaName"),
            KmsKeyArn=json_data.get("KmsKeyArn"),
            MasterSecretArn=json_data.get("MasterSecretArn"),
            VpcSecurityGroupIds=json_data.get("VpcSecurityGroupIds"),
            ExcludeCharacters=json_data.get("ExcludeCharacters"),
            MasterSecretKmsKeyArn=json_data.get("MasterSecretKmsKeyArn"),
            SuperuserSecretArn=json_data.get("SuperuserSecretArn"),
            SuperuserSecretKmsKeyArn=json_data.get("SuperuserSecretKmsKeyArn"),
            VpcSubnetIds=json_data.get("VpcSubnetIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostedRotationLambda = HostedRotationLambda


