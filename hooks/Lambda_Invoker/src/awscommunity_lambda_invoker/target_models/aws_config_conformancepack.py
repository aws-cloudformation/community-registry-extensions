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
class AwsConfigConformancepack(BaseModel):
    ConformancePackName: Optional[str]
    DeliveryS3Bucket: Optional[str]
    DeliveryS3KeyPrefix: Optional[str]
    TemplateBody: Optional[str]
    TemplateS3Uri: Optional[str]
    TemplateSSMDocumentDetails: Optional["_TemplateSSMDocumentDetails"]
    ConformancePackInputParameters: Optional[Sequence["_ConformancePackInputParameter"]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsConfigConformancepack"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsConfigConformancepack"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ConformancePackName=json_data.get("ConformancePackName"),
            DeliveryS3Bucket=json_data.get("DeliveryS3Bucket"),
            DeliveryS3KeyPrefix=json_data.get("DeliveryS3KeyPrefix"),
            TemplateBody=json_data.get("TemplateBody"),
            TemplateS3Uri=json_data.get("TemplateS3Uri"),
            TemplateSSMDocumentDetails=TemplateSSMDocumentDetails._deserialize(json_data.get("TemplateSSMDocumentDetails")),
            ConformancePackInputParameters=deserialize_list(json_data.get("ConformancePackInputParameters"), ConformancePackInputParameter),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsConfigConformancepack = AwsConfigConformancepack


@dataclass
class TemplateSSMDocumentDetails(BaseModel):
    DocumentName: Optional[str]
    DocumentVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TemplateSSMDocumentDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TemplateSSMDocumentDetails"]:
        if not json_data:
            return None
        return cls(
            DocumentName=json_data.get("DocumentName"),
            DocumentVersion=json_data.get("DocumentVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TemplateSSMDocumentDetails = TemplateSSMDocumentDetails


@dataclass
class ConformancePackInputParameter(BaseModel):
    ParameterName: Optional[str]
    ParameterValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConformancePackInputParameter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConformancePackInputParameter"]:
        if not json_data:
            return None
        return cls(
            ParameterName=json_data.get("ParameterName"),
            ParameterValue=json_data.get("ParameterValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConformancePackInputParameter = ConformancePackInputParameter


