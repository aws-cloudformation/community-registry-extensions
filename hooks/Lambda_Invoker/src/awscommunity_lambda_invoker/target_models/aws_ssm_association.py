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
class AwsSsmAssociation(BaseModel):
    AssociationId: Optional[str]
    AssociationName: Optional[str]
    DocumentVersion: Optional[str]
    InstanceId: Optional[str]
    Name: Optional[str]
    Parameters: Optional[MutableMapping[str, Sequence[str]]]
    ScheduleExpression: Optional[str]
    Targets: Optional[Sequence["_Target"]]
    OutputLocation: Optional["_InstanceAssociationOutputLocation"]
    AutomationTargetParameterName: Optional[str]
    MaxErrors: Optional[str]
    MaxConcurrency: Optional[str]
    ComplianceSeverity: Optional[str]
    SyncCompliance: Optional[str]
    WaitForSuccessTimeoutSeconds: Optional[int]
    ApplyOnlyAtCronInterval: Optional[bool]
    CalendarNames: Optional[Sequence[str]]
    ScheduleOffset: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSsmAssociation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSsmAssociation"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AssociationId=json_data.get("AssociationId"),
            AssociationName=json_data.get("AssociationName"),
            DocumentVersion=json_data.get("DocumentVersion"),
            InstanceId=json_data.get("InstanceId"),
            Name=json_data.get("Name"),
            Parameters=json_data.get("Parameters"),
            ScheduleExpression=json_data.get("ScheduleExpression"),
            Targets=deserialize_list(json_data.get("Targets"), Target),
            OutputLocation=InstanceAssociationOutputLocation._deserialize(json_data.get("OutputLocation")),
            AutomationTargetParameterName=json_data.get("AutomationTargetParameterName"),
            MaxErrors=json_data.get("MaxErrors"),
            MaxConcurrency=json_data.get("MaxConcurrency"),
            ComplianceSeverity=json_data.get("ComplianceSeverity"),
            SyncCompliance=json_data.get("SyncCompliance"),
            WaitForSuccessTimeoutSeconds=json_data.get("WaitForSuccessTimeoutSeconds"),
            ApplyOnlyAtCronInterval=json_data.get("ApplyOnlyAtCronInterval"),
            CalendarNames=json_data.get("CalendarNames"),
            ScheduleOffset=json_data.get("ScheduleOffset"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSsmAssociation = AwsSsmAssociation


@dataclass
class Target(BaseModel):
    Key: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Target"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Target"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Target = Target


@dataclass
class InstanceAssociationOutputLocation(BaseModel):
    S3Location: Optional["_S3OutputLocation"]

    @classmethod
    def _deserialize(
        cls: Type["_InstanceAssociationOutputLocation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstanceAssociationOutputLocation"]:
        if not json_data:
            return None
        return cls(
            S3Location=S3OutputLocation._deserialize(json_data.get("S3Location")),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstanceAssociationOutputLocation = InstanceAssociationOutputLocation


@dataclass
class S3OutputLocation(BaseModel):
    OutputS3Region: Optional[str]
    OutputS3BucketName: Optional[str]
    OutputS3KeyPrefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3OutputLocation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3OutputLocation"]:
        if not json_data:
            return None
        return cls(
            OutputS3Region=json_data.get("OutputS3Region"),
            OutputS3BucketName=json_data.get("OutputS3BucketName"),
            OutputS3KeyPrefix=json_data.get("OutputS3KeyPrefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3OutputLocation = S3OutputLocation


