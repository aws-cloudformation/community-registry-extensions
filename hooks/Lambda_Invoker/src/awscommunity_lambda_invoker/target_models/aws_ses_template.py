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
class AwsSesTemplate(BaseModel):
    Id: Optional[str]
    Template: Optional["_Template"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsSesTemplate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsSesTemplate"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Id=json_data.get("Id"),
            Template=Template._deserialize(json_data.get("Template")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsSesTemplate = AwsSesTemplate


@dataclass
class Template(BaseModel):
    TemplateName: Optional[str]
    SubjectPart: Optional[str]
    TextPart: Optional[str]
    HtmlPart: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Template"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Template"]:
        if not json_data:
            return None
        return cls(
            TemplateName=json_data.get("TemplateName"),
            SubjectPart=json_data.get("SubjectPart"),
            TextPart=json_data.get("TextPart"),
            HtmlPart=json_data.get("HtmlPart"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Template = Template


