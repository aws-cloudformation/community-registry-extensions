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
class AwsConfigOrganizationconformancepack(BaseModel):
    OrganizationConformancePackName: Optional[str]
    TemplateS3Uri: Optional[str]
    TemplateBody: Optional[str]
    DeliveryS3Bucket: Optional[str]
    DeliveryS3KeyPrefix: Optional[str]
    ConformancePackInputParameters: Optional[Sequence["_ConformancePackInputParameter"]]
    ExcludedAccounts: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsConfigOrganizationconformancepack"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsConfigOrganizationconformancepack"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            OrganizationConformancePackName=json_data.get("OrganizationConformancePackName"),
            TemplateS3Uri=json_data.get("TemplateS3Uri"),
            TemplateBody=json_data.get("TemplateBody"),
            DeliveryS3Bucket=json_data.get("DeliveryS3Bucket"),
            DeliveryS3KeyPrefix=json_data.get("DeliveryS3KeyPrefix"),
            ConformancePackInputParameters=deserialize_list(json_data.get("ConformancePackInputParameters"), ConformancePackInputParameter),
            ExcludedAccounts=json_data.get("ExcludedAccounts"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsConfigOrganizationconformancepack = AwsConfigOrganizationconformancepack


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


