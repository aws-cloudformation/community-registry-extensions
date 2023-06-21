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
class AwsCurReportdefinition(BaseModel):
    ReportName: Optional[str]
    TimeUnit: Optional[str]
    Format: Optional[str]
    Compression: Optional[str]
    AdditionalSchemaElements: Optional[Sequence[str]]
    S3Bucket: Optional[str]
    S3Prefix: Optional[str]
    S3Region: Optional[str]
    AdditionalArtifacts: Optional[Sequence[str]]
    RefreshClosedReports: Optional[bool]
    ReportVersioning: Optional[str]
    BillingViewArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCurReportdefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCurReportdefinition"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ReportName=json_data.get("ReportName"),
            TimeUnit=json_data.get("TimeUnit"),
            Format=json_data.get("Format"),
            Compression=json_data.get("Compression"),
            AdditionalSchemaElements=json_data.get("AdditionalSchemaElements"),
            S3Bucket=json_data.get("S3Bucket"),
            S3Prefix=json_data.get("S3Prefix"),
            S3Region=json_data.get("S3Region"),
            AdditionalArtifacts=json_data.get("AdditionalArtifacts"),
            RefreshClosedReports=json_data.get("RefreshClosedReports"),
            ReportVersioning=json_data.get("ReportVersioning"),
            BillingViewArn=json_data.get("BillingViewArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCurReportdefinition = AwsCurReportdefinition


