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
class AwsLambdaEventsourcemapping(BaseModel):
    Id: Optional[str]
    BatchSize: Optional[int]
    BisectBatchOnFunctionError: Optional[bool]
    DestinationConfig: Optional["_DestinationConfig"]
    Enabled: Optional[bool]
    EventSourceArn: Optional[str]
    FilterCriteria: Optional["_FilterCriteria"]
    FunctionName: Optional[str]
    MaximumBatchingWindowInSeconds: Optional[int]
    MaximumRecordAgeInSeconds: Optional[int]
    MaximumRetryAttempts: Optional[int]
    ParallelizationFactor: Optional[int]
    StartingPosition: Optional[str]
    StartingPositionTimestamp: Optional[float]
    Topics: Optional[Sequence[str]]
    Queues: Optional[Sequence[str]]
    SourceAccessConfigurations: Optional[Sequence["_SourceAccessConfiguration"]]
    TumblingWindowInSeconds: Optional[int]
    FunctionResponseTypes: Optional[Sequence[str]]
    SelfManagedEventSource: Optional["_SelfManagedEventSource"]
    AmazonManagedKafkaEventSourceConfig: Optional["_AmazonManagedKafkaEventSourceConfig"]
    SelfManagedKafkaEventSourceConfig: Optional["_SelfManagedKafkaEventSourceConfig"]
    ScalingConfig: Optional["_ScalingConfig"]
    DocumentDBEventSourceConfig: Optional["_DocumentDBEventSourceConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsLambdaEventsourcemapping"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsLambdaEventsourcemapping"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            BatchSize=json_data.get("BatchSize"),
            BisectBatchOnFunctionError=json_data.get("BisectBatchOnFunctionError"),
            DestinationConfig=DestinationConfig._deserialize(json_data.get("DestinationConfig")),
            Enabled=json_data.get("Enabled"),
            EventSourceArn=json_data.get("EventSourceArn"),
            FilterCriteria=FilterCriteria._deserialize(json_data.get("FilterCriteria")),
            FunctionName=json_data.get("FunctionName"),
            MaximumBatchingWindowInSeconds=json_data.get("MaximumBatchingWindowInSeconds"),
            MaximumRecordAgeInSeconds=json_data.get("MaximumRecordAgeInSeconds"),
            MaximumRetryAttempts=json_data.get("MaximumRetryAttempts"),
            ParallelizationFactor=json_data.get("ParallelizationFactor"),
            StartingPosition=json_data.get("StartingPosition"),
            StartingPositionTimestamp=json_data.get("StartingPositionTimestamp"),
            Topics=json_data.get("Topics"),
            Queues=json_data.get("Queues"),
            SourceAccessConfigurations=deserialize_list(json_data.get("SourceAccessConfigurations"), SourceAccessConfiguration),
            TumblingWindowInSeconds=json_data.get("TumblingWindowInSeconds"),
            FunctionResponseTypes=json_data.get("FunctionResponseTypes"),
            SelfManagedEventSource=SelfManagedEventSource._deserialize(json_data.get("SelfManagedEventSource")),
            AmazonManagedKafkaEventSourceConfig=AmazonManagedKafkaEventSourceConfig._deserialize(json_data.get("AmazonManagedKafkaEventSourceConfig")),
            SelfManagedKafkaEventSourceConfig=SelfManagedKafkaEventSourceConfig._deserialize(json_data.get("SelfManagedKafkaEventSourceConfig")),
            ScalingConfig=ScalingConfig._deserialize(json_data.get("ScalingConfig")),
            DocumentDBEventSourceConfig=DocumentDBEventSourceConfig._deserialize(json_data.get("DocumentDBEventSourceConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsLambdaEventsourcemapping = AwsLambdaEventsourcemapping


@dataclass
class DestinationConfig(BaseModel):
    OnFailure: Optional["_OnFailure"]

    @classmethod
    def _deserialize(
        cls: Type["_DestinationConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DestinationConfig"]:
        if not json_data:
            return None
        return cls(
            OnFailure=OnFailure._deserialize(json_data.get("OnFailure")),
        )


# work around possible type aliasing issues when variable has same name as a model
_DestinationConfig = DestinationConfig


@dataclass
class OnFailure(BaseModel):
    Destination: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OnFailure"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OnFailure"]:
        if not json_data:
            return None
        return cls(
            Destination=json_data.get("Destination"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OnFailure = OnFailure


@dataclass
class FilterCriteria(BaseModel):
    Filters: Optional[Sequence["_Filter"]]

    @classmethod
    def _deserialize(
        cls: Type["_FilterCriteria"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterCriteria"]:
        if not json_data:
            return None
        return cls(
            Filters=deserialize_list(json_data.get("Filters"), Filter),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterCriteria = FilterCriteria


@dataclass
class Filter(BaseModel):
    Pattern: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Filter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Filter"]:
        if not json_data:
            return None
        return cls(
            Pattern=json_data.get("Pattern"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Filter = Filter


@dataclass
class SourceAccessConfiguration(BaseModel):
    Type: Optional[str]
    URI: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SourceAccessConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceAccessConfiguration"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            URI=json_data.get("URI"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceAccessConfiguration = SourceAccessConfiguration


@dataclass
class SelfManagedEventSource(BaseModel):
    Endpoints: Optional["_Endpoints"]

    @classmethod
    def _deserialize(
        cls: Type["_SelfManagedEventSource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SelfManagedEventSource"]:
        if not json_data:
            return None
        return cls(
            Endpoints=Endpoints._deserialize(json_data.get("Endpoints")),
        )


# work around possible type aliasing issues when variable has same name as a model
_SelfManagedEventSource = SelfManagedEventSource


@dataclass
class Endpoints(BaseModel):
    KafkaBootstrapServers: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Endpoints"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Endpoints"]:
        if not json_data:
            return None
        return cls(
            KafkaBootstrapServers=json_data.get("KafkaBootstrapServers"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Endpoints = Endpoints


@dataclass
class AmazonManagedKafkaEventSourceConfig(BaseModel):
    ConsumerGroupId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AmazonManagedKafkaEventSourceConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AmazonManagedKafkaEventSourceConfig"]:
        if not json_data:
            return None
        return cls(
            ConsumerGroupId=json_data.get("ConsumerGroupId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AmazonManagedKafkaEventSourceConfig = AmazonManagedKafkaEventSourceConfig


@dataclass
class SelfManagedKafkaEventSourceConfig(BaseModel):
    ConsumerGroupId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SelfManagedKafkaEventSourceConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SelfManagedKafkaEventSourceConfig"]:
        if not json_data:
            return None
        return cls(
            ConsumerGroupId=json_data.get("ConsumerGroupId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SelfManagedKafkaEventSourceConfig = SelfManagedKafkaEventSourceConfig


@dataclass
class ScalingConfig(BaseModel):
    MaximumConcurrency: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_ScalingConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScalingConfig"]:
        if not json_data:
            return None
        return cls(
            MaximumConcurrency=json_data.get("MaximumConcurrency"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScalingConfig = ScalingConfig


@dataclass
class DocumentDBEventSourceConfig(BaseModel):
    DatabaseName: Optional[str]
    CollectionName: Optional[str]
    FullDocument: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DocumentDBEventSourceConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DocumentDBEventSourceConfig"]:
        if not json_data:
            return None
        return cls(
            DatabaseName=json_data.get("DatabaseName"),
            CollectionName=json_data.get("CollectionName"),
            FullDocument=json_data.get("FullDocument"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DocumentDBEventSourceConfig = DocumentDBEventSourceConfig


