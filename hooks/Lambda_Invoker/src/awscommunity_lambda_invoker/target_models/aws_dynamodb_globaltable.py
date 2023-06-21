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
class AwsDynamodbGlobaltable(BaseModel):
    Arn: Optional[str]
    StreamArn: Optional[str]
    AttributeDefinitions: Optional[AbstractSet["_AttributeDefinition"]]
    BillingMode: Optional[str]
    GlobalSecondaryIndexes: Optional[AbstractSet["_GlobalSecondaryIndex"]]
    KeySchema: Optional[Sequence["_KeySchema"]]
    LocalSecondaryIndexes: Optional[AbstractSet["_LocalSecondaryIndex"]]
    WriteProvisionedThroughputSettings: Optional["_WriteProvisionedThroughputSettings"]
    Replicas: Optional[AbstractSet["_ReplicaSpecification"]]
    SSESpecification: Optional["_SSESpecification"]
    StreamSpecification: Optional["_StreamSpecification"]
    TableName: Optional[str]
    TableId: Optional[str]
    TimeToLiveSpecification: Optional["_TimeToLiveSpecification"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsDynamodbGlobaltable"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsDynamodbGlobaltable"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            StreamArn=json_data.get("StreamArn"),
            AttributeDefinitions=set_or_none(json_data.get("AttributeDefinitions")),
            BillingMode=json_data.get("BillingMode"),
            GlobalSecondaryIndexes=set_or_none(json_data.get("GlobalSecondaryIndexes")),
            KeySchema=deserialize_list(json_data.get("KeySchema"), KeySchema),
            LocalSecondaryIndexes=set_or_none(json_data.get("LocalSecondaryIndexes")),
            WriteProvisionedThroughputSettings=WriteProvisionedThroughputSettings._deserialize(json_data.get("WriteProvisionedThroughputSettings")),
            Replicas=set_or_none(json_data.get("Replicas")),
            SSESpecification=SSESpecification._deserialize(json_data.get("SSESpecification")),
            StreamSpecification=StreamSpecification._deserialize(json_data.get("StreamSpecification")),
            TableName=json_data.get("TableName"),
            TableId=json_data.get("TableId"),
            TimeToLiveSpecification=TimeToLiveSpecification._deserialize(json_data.get("TimeToLiveSpecification")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsDynamodbGlobaltable = AwsDynamodbGlobaltable


@dataclass
class AttributeDefinition(BaseModel):
    AttributeName: Optional[str]
    AttributeType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AttributeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AttributeDefinition"]:
        if not json_data:
            return None
        return cls(
            AttributeName=json_data.get("AttributeName"),
            AttributeType=json_data.get("AttributeType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AttributeDefinition = AttributeDefinition


@dataclass
class GlobalSecondaryIndex(BaseModel):
    IndexName: Optional[str]
    KeySchema: Optional[Sequence["_KeySchema"]]
    Projection: Optional["_Projection"]
    WriteProvisionedThroughputSettings: Optional["_WriteProvisionedThroughputSettings"]

    @classmethod
    def _deserialize(
        cls: Type["_GlobalSecondaryIndex"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GlobalSecondaryIndex"]:
        if not json_data:
            return None
        return cls(
            IndexName=json_data.get("IndexName"),
            KeySchema=deserialize_list(json_data.get("KeySchema"), KeySchema),
            Projection=Projection._deserialize(json_data.get("Projection")),
            WriteProvisionedThroughputSettings=WriteProvisionedThroughputSettings._deserialize(json_data.get("WriteProvisionedThroughputSettings")),
        )


# work around possible type aliasing issues when variable has same name as a model
_GlobalSecondaryIndex = GlobalSecondaryIndex


@dataclass
class KeySchema(BaseModel):
    AttributeName: Optional[str]
    KeyType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KeySchema"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KeySchema"]:
        if not json_data:
            return None
        return cls(
            AttributeName=json_data.get("AttributeName"),
            KeyType=json_data.get("KeyType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KeySchema = KeySchema


@dataclass
class Projection(BaseModel):
    NonKeyAttributes: Optional[AbstractSet[str]]
    ProjectionType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Projection"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Projection"]:
        if not json_data:
            return None
        return cls(
            NonKeyAttributes=set_or_none(json_data.get("NonKeyAttributes")),
            ProjectionType=json_data.get("ProjectionType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Projection = Projection


@dataclass
class WriteProvisionedThroughputSettings(BaseModel):
    WriteCapacityAutoScalingSettings: Optional["_CapacityAutoScalingSettings"]

    @classmethod
    def _deserialize(
        cls: Type["_WriteProvisionedThroughputSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WriteProvisionedThroughputSettings"]:
        if not json_data:
            return None
        return cls(
            WriteCapacityAutoScalingSettings=CapacityAutoScalingSettings._deserialize(json_data.get("WriteCapacityAutoScalingSettings")),
        )


# work around possible type aliasing issues when variable has same name as a model
_WriteProvisionedThroughputSettings = WriteProvisionedThroughputSettings


@dataclass
class CapacityAutoScalingSettings(BaseModel):
    MinCapacity: Optional[int]
    MaxCapacity: Optional[int]
    SeedCapacity: Optional[int]
    TargetTrackingScalingPolicyConfiguration: Optional["_TargetTrackingScalingPolicyConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_CapacityAutoScalingSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CapacityAutoScalingSettings"]:
        if not json_data:
            return None
        return cls(
            MinCapacity=json_data.get("MinCapacity"),
            MaxCapacity=json_data.get("MaxCapacity"),
            SeedCapacity=json_data.get("SeedCapacity"),
            TargetTrackingScalingPolicyConfiguration=TargetTrackingScalingPolicyConfiguration._deserialize(json_data.get("TargetTrackingScalingPolicyConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_CapacityAutoScalingSettings = CapacityAutoScalingSettings


@dataclass
class TargetTrackingScalingPolicyConfiguration(BaseModel):
    DisableScaleIn: Optional[bool]
    ScaleInCooldown: Optional[int]
    ScaleOutCooldown: Optional[int]
    TargetValue: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_TargetTrackingScalingPolicyConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetTrackingScalingPolicyConfiguration"]:
        if not json_data:
            return None
        return cls(
            DisableScaleIn=json_data.get("DisableScaleIn"),
            ScaleInCooldown=json_data.get("ScaleInCooldown"),
            ScaleOutCooldown=json_data.get("ScaleOutCooldown"),
            TargetValue=json_data.get("TargetValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetTrackingScalingPolicyConfiguration = TargetTrackingScalingPolicyConfiguration


@dataclass
class LocalSecondaryIndex(BaseModel):
    IndexName: Optional[str]
    KeySchema: Optional[Sequence["_KeySchema"]]
    Projection: Optional["_Projection"]

    @classmethod
    def _deserialize(
        cls: Type["_LocalSecondaryIndex"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LocalSecondaryIndex"]:
        if not json_data:
            return None
        return cls(
            IndexName=json_data.get("IndexName"),
            KeySchema=deserialize_list(json_data.get("KeySchema"), KeySchema),
            Projection=Projection._deserialize(json_data.get("Projection")),
        )


# work around possible type aliasing issues when variable has same name as a model
_LocalSecondaryIndex = LocalSecondaryIndex


@dataclass
class ReplicaSpecification(BaseModel):
    Region: Optional[str]
    GlobalSecondaryIndexes: Optional[AbstractSet["_ReplicaGlobalSecondaryIndexSpecification"]]
    ContributorInsightsSpecification: Optional["_ContributorInsightsSpecification"]
    PointInTimeRecoverySpecification: Optional["_PointInTimeRecoverySpecification"]
    TableClass: Optional[str]
    DeletionProtectionEnabled: Optional[bool]
    SSESpecification: Optional["_ReplicaSSESpecification"]
    Tags: Optional[AbstractSet["_Tag"]]
    ReadProvisionedThroughputSettings: Optional["_ReadProvisionedThroughputSettings"]
    KinesisStreamSpecification: Optional["_KinesisStreamSpecification"]

    @classmethod
    def _deserialize(
        cls: Type["_ReplicaSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReplicaSpecification"]:
        if not json_data:
            return None
        return cls(
            Region=json_data.get("Region"),
            GlobalSecondaryIndexes=set_or_none(json_data.get("GlobalSecondaryIndexes")),
            ContributorInsightsSpecification=ContributorInsightsSpecification._deserialize(json_data.get("ContributorInsightsSpecification")),
            PointInTimeRecoverySpecification=PointInTimeRecoverySpecification._deserialize(json_data.get("PointInTimeRecoverySpecification")),
            TableClass=json_data.get("TableClass"),
            DeletionProtectionEnabled=json_data.get("DeletionProtectionEnabled"),
            SSESpecification=ReplicaSSESpecification._deserialize(json_data.get("SSESpecification")),
            Tags=set_or_none(json_data.get("Tags")),
            ReadProvisionedThroughputSettings=ReadProvisionedThroughputSettings._deserialize(json_data.get("ReadProvisionedThroughputSettings")),
            KinesisStreamSpecification=KinesisStreamSpecification._deserialize(json_data.get("KinesisStreamSpecification")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReplicaSpecification = ReplicaSpecification


@dataclass
class ReplicaGlobalSecondaryIndexSpecification(BaseModel):
    IndexName: Optional[str]
    ContributorInsightsSpecification: Optional["_ContributorInsightsSpecification"]
    ReadProvisionedThroughputSettings: Optional["_ReadProvisionedThroughputSettings"]

    @classmethod
    def _deserialize(
        cls: Type["_ReplicaGlobalSecondaryIndexSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReplicaGlobalSecondaryIndexSpecification"]:
        if not json_data:
            return None
        return cls(
            IndexName=json_data.get("IndexName"),
            ContributorInsightsSpecification=ContributorInsightsSpecification._deserialize(json_data.get("ContributorInsightsSpecification")),
            ReadProvisionedThroughputSettings=ReadProvisionedThroughputSettings._deserialize(json_data.get("ReadProvisionedThroughputSettings")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReplicaGlobalSecondaryIndexSpecification = ReplicaGlobalSecondaryIndexSpecification


@dataclass
class ContributorInsightsSpecification(BaseModel):
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ContributorInsightsSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContributorInsightsSpecification"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContributorInsightsSpecification = ContributorInsightsSpecification


@dataclass
class ReadProvisionedThroughputSettings(BaseModel):
    ReadCapacityUnits: Optional[int]
    ReadCapacityAutoScalingSettings: Optional["_CapacityAutoScalingSettings"]

    @classmethod
    def _deserialize(
        cls: Type["_ReadProvisionedThroughputSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReadProvisionedThroughputSettings"]:
        if not json_data:
            return None
        return cls(
            ReadCapacityUnits=json_data.get("ReadCapacityUnits"),
            ReadCapacityAutoScalingSettings=CapacityAutoScalingSettings._deserialize(json_data.get("ReadCapacityAutoScalingSettings")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReadProvisionedThroughputSettings = ReadProvisionedThroughputSettings


@dataclass
class PointInTimeRecoverySpecification(BaseModel):
    PointInTimeRecoveryEnabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_PointInTimeRecoverySpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PointInTimeRecoverySpecification"]:
        if not json_data:
            return None
        return cls(
            PointInTimeRecoveryEnabled=json_data.get("PointInTimeRecoveryEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PointInTimeRecoverySpecification = PointInTimeRecoverySpecification


@dataclass
class ReplicaSSESpecification(BaseModel):
    KMSMasterKeyId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ReplicaSSESpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReplicaSSESpecification"]:
        if not json_data:
            return None
        return cls(
            KMSMasterKeyId=json_data.get("KMSMasterKeyId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReplicaSSESpecification = ReplicaSSESpecification


@dataclass
class Tag(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tag"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tag = Tag


@dataclass
class KinesisStreamSpecification(BaseModel):
    StreamArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KinesisStreamSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KinesisStreamSpecification"]:
        if not json_data:
            return None
        return cls(
            StreamArn=json_data.get("StreamArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KinesisStreamSpecification = KinesisStreamSpecification


@dataclass
class SSESpecification(BaseModel):
    SSEEnabled: Optional[bool]
    SSEType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SSESpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SSESpecification"]:
        if not json_data:
            return None
        return cls(
            SSEEnabled=json_data.get("SSEEnabled"),
            SSEType=json_data.get("SSEType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SSESpecification = SSESpecification


@dataclass
class StreamSpecification(BaseModel):
    StreamViewType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StreamSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StreamSpecification"]:
        if not json_data:
            return None
        return cls(
            StreamViewType=json_data.get("StreamViewType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StreamSpecification = StreamSpecification


@dataclass
class TimeToLiveSpecification(BaseModel):
    AttributeName: Optional[str]
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_TimeToLiveSpecification"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeToLiveSpecification"]:
        if not json_data:
            return None
        return cls(
            AttributeName=json_data.get("AttributeName"),
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeToLiveSpecification = TimeToLiveSpecification


