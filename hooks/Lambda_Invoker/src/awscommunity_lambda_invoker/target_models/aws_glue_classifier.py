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
class AwsGlueClassifier(BaseModel):
    Id: Optional[str]
    XMLClassifier: Optional["_XMLClassifier"]
    JsonClassifier: Optional["_JsonClassifier"]
    CsvClassifier: Optional["_CsvClassifier"]
    GrokClassifier: Optional["_GrokClassifier"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsGlueClassifier"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsGlueClassifier"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            XMLClassifier=XMLClassifier._deserialize(json_data.get("XMLClassifier")),
            JsonClassifier=JsonClassifier._deserialize(json_data.get("JsonClassifier")),
            CsvClassifier=CsvClassifier._deserialize(json_data.get("CsvClassifier")),
            GrokClassifier=GrokClassifier._deserialize(json_data.get("GrokClassifier")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsGlueClassifier = AwsGlueClassifier


@dataclass
class XMLClassifier(BaseModel):
    RowTag: Optional[str]
    Classification: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_XMLClassifier"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_XMLClassifier"]:
        if not json_data:
            return None
        return cls(
            RowTag=json_data.get("RowTag"),
            Classification=json_data.get("Classification"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_XMLClassifier = XMLClassifier


@dataclass
class JsonClassifier(BaseModel):
    JsonPath: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_JsonClassifier"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JsonClassifier"]:
        if not json_data:
            return None
        return cls(
            JsonPath=json_data.get("JsonPath"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JsonClassifier = JsonClassifier


@dataclass
class CsvClassifier(BaseModel):
    QuoteSymbol: Optional[str]
    ContainsHeader: Optional[str]
    Delimiter: Optional[str]
    Header: Optional[Sequence[str]]
    AllowSingleColumn: Optional[bool]
    DisableValueTrimming: Optional[bool]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CsvClassifier"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CsvClassifier"]:
        if not json_data:
            return None
        return cls(
            QuoteSymbol=json_data.get("QuoteSymbol"),
            ContainsHeader=json_data.get("ContainsHeader"),
            Delimiter=json_data.get("Delimiter"),
            Header=json_data.get("Header"),
            AllowSingleColumn=json_data.get("AllowSingleColumn"),
            DisableValueTrimming=json_data.get("DisableValueTrimming"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CsvClassifier = CsvClassifier


@dataclass
class GrokClassifier(BaseModel):
    CustomPatterns: Optional[str]
    GrokPattern: Optional[str]
    Classification: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GrokClassifier"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GrokClassifier"]:
        if not json_data:
            return None
        return cls(
            CustomPatterns=json_data.get("CustomPatterns"),
            GrokPattern=json_data.get("GrokPattern"),
            Classification=json_data.get("Classification"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GrokClassifier = GrokClassifier


