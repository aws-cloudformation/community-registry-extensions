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
class AwsLookoutmetricsAnomalydetector(BaseModel):
    Arn: Optional[str]
    AnomalyDetectorName: Optional[str]
    AnomalyDetectorDescription: Optional[str]
    AnomalyDetectorConfig: Optional["_AnomalyDetectorConfig"]
    MetricSetList: Optional[Sequence["_MetricSet"]]
    KmsKeyArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsLookoutmetricsAnomalydetector"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsLookoutmetricsAnomalydetector"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            AnomalyDetectorName=json_data.get("AnomalyDetectorName"),
            AnomalyDetectorDescription=json_data.get("AnomalyDetectorDescription"),
            AnomalyDetectorConfig=AnomalyDetectorConfig._deserialize(json_data.get("AnomalyDetectorConfig")),
            MetricSetList=deserialize_list(json_data.get("MetricSetList"), MetricSet),
            KmsKeyArn=json_data.get("KmsKeyArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsLookoutmetricsAnomalydetector = AwsLookoutmetricsAnomalydetector


@dataclass
class AnomalyDetectorConfig(BaseModel):
    AnomalyDetectorFrequency: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AnomalyDetectorConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnomalyDetectorConfig"]:
        if not json_data:
            return None
        return cls(
            AnomalyDetectorFrequency=json_data.get("AnomalyDetectorFrequency"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnomalyDetectorConfig = AnomalyDetectorConfig


@dataclass
class MetricSet(BaseModel):
    MetricSetName: Optional[str]
    MetricSetDescription: Optional[str]
    MetricSource: Optional["_MetricSource"]
    MetricList: Optional[Sequence["_Metric"]]
    Offset: Optional[int]
    TimestampColumn: Optional["_TimestampColumn"]
    DimensionList: Optional[Sequence[str]]
    MetricSetFrequency: Optional[str]
    Timezone: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetricSet"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricSet"]:
        if not json_data:
            return None
        return cls(
            MetricSetName=json_data.get("MetricSetName"),
            MetricSetDescription=json_data.get("MetricSetDescription"),
            MetricSource=MetricSource._deserialize(json_data.get("MetricSource")),
            MetricList=deserialize_list(json_data.get("MetricList"), Metric),
            Offset=json_data.get("Offset"),
            TimestampColumn=TimestampColumn._deserialize(json_data.get("TimestampColumn")),
            DimensionList=json_data.get("DimensionList"),
            MetricSetFrequency=json_data.get("MetricSetFrequency"),
            Timezone=json_data.get("Timezone"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricSet = MetricSet


@dataclass
class MetricSource(BaseModel):
    S3SourceConfig: Optional["_S3SourceConfig"]
    RDSSourceConfig: Optional["_RDSSourceConfig"]
    RedshiftSourceConfig: Optional["_RedshiftSourceConfig"]
    CloudwatchConfig: Optional["_CloudwatchConfig"]
    AppFlowConfig: Optional["_AppFlowConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_MetricSource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetricSource"]:
        if not json_data:
            return None
        return cls(
            S3SourceConfig=S3SourceConfig._deserialize(json_data.get("S3SourceConfig")),
            RDSSourceConfig=RDSSourceConfig._deserialize(json_data.get("RDSSourceConfig")),
            RedshiftSourceConfig=RedshiftSourceConfig._deserialize(json_data.get("RedshiftSourceConfig")),
            CloudwatchConfig=CloudwatchConfig._deserialize(json_data.get("CloudwatchConfig")),
            AppFlowConfig=AppFlowConfig._deserialize(json_data.get("AppFlowConfig")),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetricSource = MetricSource


@dataclass
class S3SourceConfig(BaseModel):
    RoleArn: Optional[str]
    TemplatedPathList: Optional[Sequence[str]]
    HistoricalDataPathList: Optional[Sequence[str]]
    FileFormatDescriptor: Optional["_FileFormatDescriptor"]

    @classmethod
    def _deserialize(
        cls: Type["_S3SourceConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3SourceConfig"]:
        if not json_data:
            return None
        return cls(
            RoleArn=json_data.get("RoleArn"),
            TemplatedPathList=json_data.get("TemplatedPathList"),
            HistoricalDataPathList=json_data.get("HistoricalDataPathList"),
            FileFormatDescriptor=FileFormatDescriptor._deserialize(json_data.get("FileFormatDescriptor")),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3SourceConfig = S3SourceConfig


@dataclass
class FileFormatDescriptor(BaseModel):
    CsvFormatDescriptor: Optional["_CsvFormatDescriptor"]
    JsonFormatDescriptor: Optional["_JsonFormatDescriptor"]

    @classmethod
    def _deserialize(
        cls: Type["_FileFormatDescriptor"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FileFormatDescriptor"]:
        if not json_data:
            return None
        return cls(
            CsvFormatDescriptor=CsvFormatDescriptor._deserialize(json_data.get("CsvFormatDescriptor")),
            JsonFormatDescriptor=JsonFormatDescriptor._deserialize(json_data.get("JsonFormatDescriptor")),
        )


# work around possible type aliasing issues when variable has same name as a model
_FileFormatDescriptor = FileFormatDescriptor


@dataclass
class CsvFormatDescriptor(BaseModel):
    FileCompression: Optional[str]
    Charset: Optional[str]
    Delimiter: Optional[str]
    HeaderList: Optional[Sequence[str]]
    QuoteSymbol: Optional[str]
    ContainsHeader: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_CsvFormatDescriptor"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CsvFormatDescriptor"]:
        if not json_data:
            return None
        return cls(
            FileCompression=json_data.get("FileCompression"),
            Charset=json_data.get("Charset"),
            Delimiter=json_data.get("Delimiter"),
            HeaderList=json_data.get("HeaderList"),
            QuoteSymbol=json_data.get("QuoteSymbol"),
            ContainsHeader=json_data.get("ContainsHeader"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CsvFormatDescriptor = CsvFormatDescriptor


@dataclass
class JsonFormatDescriptor(BaseModel):
    FileCompression: Optional[str]
    Charset: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_JsonFormatDescriptor"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JsonFormatDescriptor"]:
        if not json_data:
            return None
        return cls(
            FileCompression=json_data.get("FileCompression"),
            Charset=json_data.get("Charset"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JsonFormatDescriptor = JsonFormatDescriptor


@dataclass
class RDSSourceConfig(BaseModel):
    DBInstanceIdentifier: Optional[str]
    DatabaseHost: Optional[str]
    DatabasePort: Optional[int]
    SecretManagerArn: Optional[str]
    DatabaseName: Optional[str]
    TableName: Optional[str]
    RoleArn: Optional[str]
    VpcConfiguration: Optional["_VpcConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_RDSSourceConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RDSSourceConfig"]:
        if not json_data:
            return None
        return cls(
            DBInstanceIdentifier=json_data.get("DBInstanceIdentifier"),
            DatabaseHost=json_data.get("DatabaseHost"),
            DatabasePort=json_data.get("DatabasePort"),
            SecretManagerArn=json_data.get("SecretManagerArn"),
            DatabaseName=json_data.get("DatabaseName"),
            TableName=json_data.get("TableName"),
            RoleArn=json_data.get("RoleArn"),
            VpcConfiguration=VpcConfiguration._deserialize(json_data.get("VpcConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_RDSSourceConfig = RDSSourceConfig


@dataclass
class VpcConfiguration(BaseModel):
    SubnetIdList: Optional[Sequence[str]]
    SecurityGroupIdList: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_VpcConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpcConfiguration"]:
        if not json_data:
            return None
        return cls(
            SubnetIdList=json_data.get("SubnetIdList"),
            SecurityGroupIdList=json_data.get("SecurityGroupIdList"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpcConfiguration = VpcConfiguration


@dataclass
class RedshiftSourceConfig(BaseModel):
    ClusterIdentifier: Optional[str]
    DatabaseHost: Optional[str]
    DatabasePort: Optional[int]
    SecretManagerArn: Optional[str]
    DatabaseName: Optional[str]
    TableName: Optional[str]
    RoleArn: Optional[str]
    VpcConfiguration: Optional["_VpcConfiguration"]

    @classmethod
    def _deserialize(
        cls: Type["_RedshiftSourceConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RedshiftSourceConfig"]:
        if not json_data:
            return None
        return cls(
            ClusterIdentifier=json_data.get("ClusterIdentifier"),
            DatabaseHost=json_data.get("DatabaseHost"),
            DatabasePort=json_data.get("DatabasePort"),
            SecretManagerArn=json_data.get("SecretManagerArn"),
            DatabaseName=json_data.get("DatabaseName"),
            TableName=json_data.get("TableName"),
            RoleArn=json_data.get("RoleArn"),
            VpcConfiguration=VpcConfiguration._deserialize(json_data.get("VpcConfiguration")),
        )


# work around possible type aliasing issues when variable has same name as a model
_RedshiftSourceConfig = RedshiftSourceConfig


@dataclass
class CloudwatchConfig(BaseModel):
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CloudwatchConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudwatchConfig"]:
        if not json_data:
            return None
        return cls(
            RoleArn=json_data.get("RoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudwatchConfig = CloudwatchConfig


@dataclass
class AppFlowConfig(BaseModel):
    RoleArn: Optional[str]
    FlowName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AppFlowConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AppFlowConfig"]:
        if not json_data:
            return None
        return cls(
            RoleArn=json_data.get("RoleArn"),
            FlowName=json_data.get("FlowName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AppFlowConfig = AppFlowConfig


@dataclass
class Metric(BaseModel):
    MetricName: Optional[str]
    AggregationFunction: Optional[str]
    Namespace: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Metric"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Metric"]:
        if not json_data:
            return None
        return cls(
            MetricName=json_data.get("MetricName"),
            AggregationFunction=json_data.get("AggregationFunction"),
            Namespace=json_data.get("Namespace"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Metric = Metric


@dataclass
class TimestampColumn(BaseModel):
    ColumnName: Optional[str]
    ColumnFormat: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimestampColumn"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimestampColumn"]:
        if not json_data:
            return None
        return cls(
            ColumnName=json_data.get("ColumnName"),
            ColumnFormat=json_data.get("ColumnFormat"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimestampColumn = TimestampColumn


