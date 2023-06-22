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
class AwsInspectorAssessmenttemplate(BaseModel):
    Arn: Optional[str]
    AssessmentTargetArn: Optional[str]
    DurationInSeconds: Optional[int]
    AssessmentTemplateName: Optional[str]
    RulesPackageArns: Optional[Sequence[str]]
    UserAttributesForFindings: Optional[Sequence["_Tag"]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsInspectorAssessmenttemplate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsInspectorAssessmenttemplate"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            AssessmentTargetArn=json_data.get("AssessmentTargetArn"),
            DurationInSeconds=json_data.get("DurationInSeconds"),
            AssessmentTemplateName=json_data.get("AssessmentTemplateName"),
            RulesPackageArns=json_data.get("RulesPackageArns"),
            UserAttributesForFindings=deserialize_list(json_data.get("UserAttributesForFindings"), Tag),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsInspectorAssessmenttemplate = AwsInspectorAssessmenttemplate


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


