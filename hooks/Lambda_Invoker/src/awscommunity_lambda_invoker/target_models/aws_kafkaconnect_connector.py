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
class AwsKafkaconnectConnector(BaseModel):
    Capacity: Optional["_Capacity"]
    ConnectorArn: Optional[str]
    ConnectorConfiguration: Optional[MutableMapping[str, str]]
    ConnectorDescription: Optional[str]
    ConnectorName: Optional[str]
    KafkaCluster: Optional["_KafkaCluster"]
    KafkaClusterClientAuthentication: Optional["_KafkaClusterClientAuthentication"]
    KafkaClusterEncryptionInTransit: Optional["_KafkaClusterEncryptionInTransit"]
    KafkaConnectVersion: Optional[str]
    LogDelivery: Optional["_LogDelivery"]
    Plugins: Optional[AbstractSet["_Plugin"]]
    ServiceExecutionRoleArn: Optional[str]
    WorkerConfiguration: Optional["_WorkerConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsKafkaconnectConnector"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsKafkaconnectConnector"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Capacity=Capacity._deserialize(json_data.get("Capacity")),
            ConnectorArn=json_data.get("ConnectorArn"),
            ConnectorConfiguration=json_data.get("ConnectorConfiguration"),
            ConnectorDescription=json_data.get("ConnectorDescription"),
            ConnectorName=json_data.get("ConnectorName"),
            KafkaCluster=KafkaCluster._deserialize(json_data.get("KafkaCluster")),
            KafkaClusterClientAuthentication=KafkaClusterClientAuthentication._deserialize(json_data.get("KafkaClusterClientAuthentication")),
            KafkaClusterEncryptionInTransit=KafkaClusterEncryptionInTransit._deserialize(json_data.get("KafkaClusterEncryptionInTransit")),
            KafkaConnectVersion=json_data.get("KafkaConnectVersion"),
            LogDelivery=LogDelivery._deserialize(json_data.get("LogDelivery")),
            Plugins=set_or_none(json_data.get("Plugins")),
            ServiceExecutionRoleArn=json_data.get("ServiceExecutionRoleArn"),
            WorkerConfiguration=WorkerConfiguration._deserialize(json_data.get("WorkerConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsKafkaconnectConnector = AwsKafkaconnectConnector


@dataclass
class Capacity(BaseModel):
    AutoScaling: Optional["_AutoScaling"]
    ProvisionedCapacity: Optional["_ProvisionedCapacity"]

    @classmethod
    def _deserialize(
        cls: Type["_Capacity"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Capacity"]:
        if not json_data:
            return None
        return cls(
            AutoScaling=AutoScaling._deserialize(json_data.get("AutoScaling")),
            ProvisionedCapacity=ProvisionedCapacity._deserialize(json_data.get("ProvisionedCapacity")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Capacity = Capacity


@dataclass
class AutoScaling(BaseModel):
    MaxWorkerCount: Optional[int]
    MinWorkerCount: Optional[int]
    ScaleInPolicy: Optional["_ScaleInPolicy"]
    ScaleOutPolicy: Optional["_ScaleOutPolicy"]
    McuCount: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_AutoScaling"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AutoScaling"]:
        if not json_data:
            return None
        return cls(
            MaxWorkerCount=json_data.get("MaxWorkerCount"),
            MinWorkerCount=json_data.get("MinWorkerCount"),
            ScaleInPolicy=ScaleInPolicy._deserialize(json_data.get("ScaleInPolicy")),
            ScaleOutPolicy=ScaleOutPolicy._deserialize(json_data.get("ScaleOutPolicy")),
            McuCount=json_data.get("McuCount"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AutoScaling = AutoScaling


@dataclass
class ScaleInPolicy(BaseModel):
    CpuUtilizationPercentage: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_ScaleInPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScaleInPolicy"]:
        if not json_data:
            return None
        return cls(
            CpuUtilizationPercentage=json_data.get("CpuUtilizationPercentage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScaleInPolicy = ScaleInPolicy


@dataclass
class ScaleOutPolicy(BaseModel):
    CpuUtilizationPercentage: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_ScaleOutPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScaleOutPolicy"]:
        if not json_data:
            return None
        return cls(
            CpuUtilizationPercentage=json_data.get("CpuUtilizationPercentage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScaleOutPolicy = ScaleOutPolicy


@dataclass
class ProvisionedCapacity(BaseModel):
    McuCount: Optional[int]
    WorkerCount: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_ProvisionedCapacity"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProvisionedCapacity"]:
        if not json_data:
            return None
        return cls(
            McuCount=json_data.get("McuCount"),
            WorkerCount=json_data.get("WorkerCount"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProvisionedCapacity = ProvisionedCapacity


@dataclass
class KafkaCluster(BaseModel):
    ApacheKafkaCluster: Optional["_ApacheKafkaCluster"]

    @classmethod
    def _deserialize(
        cls: Type["_KafkaCluster"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KafkaCluster"]:
        if not json_data:
            return None
        return cls(
            ApacheKafkaCluster=ApacheKafkaCluster._deserialize(json_data.get("ApacheKafkaCluster")),
        )


# work around possible type aliasing issues when variable has same name as a model
_KafkaCluster = KafkaCluster


@dataclass
class ApacheKafkaCluster(BaseModel):
    BootstrapServers: Optional[str]
    Vpc: Optional["_Vpc"]

    @classmethod
    def _deserialize(
        cls: Type["_ApacheKafkaCluster"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApacheKafkaCluster"]:
        if not json_data:
            return None
        return cls(
            BootstrapServers=json_data.get("BootstrapServers"),
            Vpc=Vpc._deserialize(json_data.get("Vpc")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApacheKafkaCluster = ApacheKafkaCluster


@dataclass
class Vpc(BaseModel):
    SecurityGroups: Optional[AbstractSet[str]]
    Subnets: Optional[AbstractSet[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Vpc"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Vpc"]:
        if not json_data:
            return None
        return cls(
            SecurityGroups=set_or_none(json_data.get("SecurityGroups")),
            Subnets=set_or_none(json_data.get("Subnets")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Vpc = Vpc


@dataclass
class KafkaClusterClientAuthentication(BaseModel):
    AuthenticationType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KafkaClusterClientAuthentication"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KafkaClusterClientAuthentication"]:
        if not json_data:
            return None
        return cls(
            AuthenticationType=json_data.get("AuthenticationType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KafkaClusterClientAuthentication = KafkaClusterClientAuthentication


@dataclass
class KafkaClusterEncryptionInTransit(BaseModel):
    EncryptionType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KafkaClusterEncryptionInTransit"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KafkaClusterEncryptionInTransit"]:
        if not json_data:
            return None
        return cls(
            EncryptionType=json_data.get("EncryptionType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KafkaClusterEncryptionInTransit = KafkaClusterEncryptionInTransit


@dataclass
class LogDelivery(BaseModel):
    WorkerLogDelivery: Optional["_WorkerLogDelivery"]

    @classmethod
    def _deserialize(
        cls: Type["_LogDelivery"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogDelivery"]:
        if not json_data:
            return None
        return cls(
            WorkerLogDelivery=WorkerLogDelivery._deserialize(json_data.get("WorkerLogDelivery")),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogDelivery = LogDelivery


@dataclass
class WorkerLogDelivery(BaseModel):
    CloudWatchLogs: Optional["_CloudWatchLogsLogDelivery"]
    Firehose: Optional["_FirehoseLogDelivery"]
    S3: Optional["_S3LogDelivery"]

    @classmethod
    def _deserialize(
        cls: Type["_WorkerLogDelivery"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkerLogDelivery"]:
        if not json_data:
            return None
        return cls(
            CloudWatchLogs=CloudWatchLogsLogDelivery._deserialize(json_data.get("CloudWatchLogs")),
            Firehose=FirehoseLogDelivery._deserialize(json_data.get("Firehose")),
            S3=S3LogDelivery._deserialize(json_data.get("S3")),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkerLogDelivery = WorkerLogDelivery


@dataclass
class CloudWatchLogsLogDelivery(BaseModel):
    Enabled: Optional[bool]
    LogGroup: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CloudWatchLogsLogDelivery"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudWatchLogsLogDelivery"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            LogGroup=json_data.get("LogGroup"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudWatchLogsLogDelivery = CloudWatchLogsLogDelivery


@dataclass
class FirehoseLogDelivery(BaseModel):
    DeliveryStream: Optional[str]
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_FirehoseLogDelivery"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FirehoseLogDelivery"]:
        if not json_data:
            return None
        return cls(
            DeliveryStream=json_data.get("DeliveryStream"),
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FirehoseLogDelivery = FirehoseLogDelivery


@dataclass
class S3LogDelivery(BaseModel):
    Bucket: Optional[str]
    Enabled: Optional[bool]
    Prefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3LogDelivery"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3LogDelivery"]:
        if not json_data:
            return None
        return cls(
            Bucket=json_data.get("Bucket"),
            Enabled=json_data.get("Enabled"),
            Prefix=json_data.get("Prefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3LogDelivery = S3LogDelivery


@dataclass
class Plugin(BaseModel):
    CustomPlugin: Optional["_CustomPlugin"]

    @classmethod
    def _deserialize(
        cls: Type["_Plugin"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Plugin"]:
        if not json_data:
            return None
        return cls(
            CustomPlugin=CustomPlugin._deserialize(json_data.get("CustomPlugin")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Plugin = Plugin


@dataclass
class CustomPlugin(BaseModel):
    CustomPluginArn: Optional[str]
    Revision: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_CustomPlugin"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomPlugin"]:
        if not json_data:
            return None
        return cls(
            CustomPluginArn=json_data.get("CustomPluginArn"),
            Revision=json_data.get("Revision"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomPlugin = CustomPlugin


@dataclass
class WorkerConfiguration(BaseModel):
    Revision: Optional[int]
    WorkerConfigurationArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WorkerConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WorkerConfiguration"]:
        if not json_data:
            return None
        return cls(
            Revision=json_data.get("Revision"),
            WorkerConfigurationArn=json_data.get("WorkerConfigurationArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WorkerConfiguration = WorkerConfiguration


