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
class AwsKinesisanalyticsApplication(BaseModel):
    Id: Optional[str]
    ApplicationName: Optional[str]
    Inputs: Optional[Sequence["_Input"]]
    ApplicationDescription: Optional[str]
    ApplicationCode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsKinesisanalyticsApplication"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsKinesisanalyticsApplication"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            ApplicationName=json_data.get("ApplicationName"),
            Inputs=deserialize_list(json_data.get("Inputs"), Input),
            ApplicationDescription=json_data.get("ApplicationDescription"),
            ApplicationCode=json_data.get("ApplicationCode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsKinesisanalyticsApplication = AwsKinesisanalyticsApplication


@dataclass
class Input(BaseModel):
    NamePrefix: Optional[str]
    InputSchema: Optional["_InputSchema"]
    KinesisStreamsInput: Optional["_KinesisStreamsInput"]
    KinesisFirehoseInput: Optional["_KinesisFirehoseInput"]
    InputProcessingConfiguration: Optional["_InputProcessingConfiguration"]
    InputParallelism: Optional["_InputParallelism"]

    @classmethod
    def _deserialize(
        cls: Type["_Input"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Input"]:
        if not json_data:
            return None
        return cls(
            NamePrefix=json_data.get("NamePrefix"),
            InputSchema=InputSchema._deserialize(json_data.get("InputSchema")),
            KinesisStreamsInput=KinesisStreamsInput._deserialize(json_data.get("KinesisStreamsInput")),
            KinesisFirehoseInput=KinesisFirehoseInput._deserialize(json_data.get("KinesisFirehoseInput")),
            InputProcessingConfiguration=InputProcessingConfiguration._deserialize(json_data.get("InputProcessingConfiguration")),
            InputParallelism=InputParallelism._deserialize(json_data.get("InputParallelism")),
        )


# work around possible type aliasing issues when variable has same name as a model
_Input = Input


@dataclass
class InputSchema(BaseModel):
    RecordEncoding: Optional[str]
    RecordColumns: Optional[Sequence["_RecordColumn"]]
    RecordFormat: Optional["_RecordFormat"]

    @classmethod
    def _deserialize(
        cls: Type["_InputSchema"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputSchema"]:
        if not json_data:
            return None
        return cls(
            RecordEncoding=json_data.get("RecordEncoding"),
            RecordColumns=deserialize_list(json_data.get("RecordColumns"), RecordColumn),
            RecordFormat=RecordFormat._deserialize(json_data.get("RecordFormat")),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputSchema = InputSchema


@dataclass
class RecordColumn(BaseModel):
    Mapping: Optional[str]
    SqlType: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RecordColumn"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RecordColumn"]:
        if not json_data:
            return None
        return cls(
            Mapping=json_data.get("Mapping"),
            SqlType=json_data.get("SqlType"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RecordColumn = RecordColumn


@dataclass
class RecordFormat(BaseModel):
    MappingParameters: Optional["_MappingParameters"]
    RecordFormatType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RecordFormat"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RecordFormat"]:
        if not json_data:
            return None
        return cls(
            MappingParameters=MappingParameters._deserialize(json_data.get("MappingParameters")),
            RecordFormatType=json_data.get("RecordFormatType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RecordFormat = RecordFormat


@dataclass
class MappingParameters(BaseModel):
    JSONMappingParameters: Optional["_JSONMappingParameters"]
    CSVMappingParameters: Optional["_CSVMappingParameters"]

    @classmethod
    def _deserialize(
        cls: Type["_MappingParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MappingParameters"]:
        if not json_data:
            return None
        return cls(
            JSONMappingParameters=JSONMappingParameters._deserialize(json_data.get("JSONMappingParameters")),
            CSVMappingParameters=CSVMappingParameters._deserialize(json_data.get("CSVMappingParameters")),
        )


# work around possible type aliasing issues when variable has same name as a model
_MappingParameters = MappingParameters


@dataclass
class JSONMappingParameters(BaseModel):
    RecordRowPath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_JSONMappingParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JSONMappingParameters"]:
        if not json_data:
            return None
        return cls(
            RecordRowPath=json_data.get("RecordRowPath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JSONMappingParameters = JSONMappingParameters


@dataclass
class CSVMappingParameters(BaseModel):
    RecordRowDelimiter: Optional[str]
    RecordColumnDelimiter: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CSVMappingParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CSVMappingParameters"]:
        if not json_data:
            return None
        return cls(
            RecordRowDelimiter=json_data.get("RecordRowDelimiter"),
            RecordColumnDelimiter=json_data.get("RecordColumnDelimiter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CSVMappingParameters = CSVMappingParameters


@dataclass
class KinesisStreamsInput(BaseModel):
    ResourceARN: Optional[str]
    RoleARN: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KinesisStreamsInput"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KinesisStreamsInput"]:
        if not json_data:
            return None
        return cls(
            ResourceARN=json_data.get("ResourceARN"),
            RoleARN=json_data.get("RoleARN"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KinesisStreamsInput = KinesisStreamsInput


@dataclass
class KinesisFirehoseInput(BaseModel):
    ResourceARN: Optional[str]
    RoleARN: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KinesisFirehoseInput"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KinesisFirehoseInput"]:
        if not json_data:
            return None
        return cls(
            ResourceARN=json_data.get("ResourceARN"),
            RoleARN=json_data.get("RoleARN"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KinesisFirehoseInput = KinesisFirehoseInput


@dataclass
class InputProcessingConfiguration(BaseModel):
    InputLambdaProcessor: Optional["_InputLambdaProcessor"]

    @classmethod
    def _deserialize(
        cls: Type["_InputProcessingConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputProcessingConfiguration"]:
        if not json_data:
            return None
        return cls(
            InputLambdaProcessor=InputLambdaProcessor._deserialize(json_data.get("InputLambdaProcessor")),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputProcessingConfiguration = InputProcessingConfiguration


@dataclass
class InputLambdaProcessor(BaseModel):
    ResourceARN: Optional[str]
    RoleARN: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InputLambdaProcessor"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputLambdaProcessor"]:
        if not json_data:
            return None
        return cls(
            ResourceARN=json_data.get("ResourceARN"),
            RoleARN=json_data.get("RoleARN"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputLambdaProcessor = InputLambdaProcessor


@dataclass
class InputParallelism(BaseModel):
    Count: Optional[int]

    @classmethod
    def _deserialize(
        cls: Type["_InputParallelism"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputParallelism"]:
        if not json_data:
            return None
        return cls(
            Count=json_data.get("Count"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputParallelism = InputParallelism


