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
class AwsApigatewayv2Integrationresponse(BaseModel):
    IntegrationResponseId: Optional[str]
    ResponseTemplates: Optional[MutableMapping[str, Any]]
    TemplateSelectionExpression: Optional[str]
    ResponseParameters: Optional[MutableMapping[str, Any]]
    ContentHandlingStrategy: Optional[str]
    IntegrationId: Optional[str]
    IntegrationResponseKey: Optional[str]
    ApiId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsApigatewayv2Integrationresponse"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsApigatewayv2Integrationresponse"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            IntegrationResponseId=json_data.get("IntegrationResponseId"),
            ResponseTemplates=json_data.get("ResponseTemplates"),
            TemplateSelectionExpression=json_data.get("TemplateSelectionExpression"),
            ResponseParameters=json_data.get("ResponseParameters"),
            ContentHandlingStrategy=json_data.get("ContentHandlingStrategy"),
            IntegrationId=json_data.get("IntegrationId"),
            IntegrationResponseKey=json_data.get("IntegrationResponseKey"),
            ApiId=json_data.get("ApiId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsApigatewayv2Integrationresponse = AwsApigatewayv2Integrationresponse


