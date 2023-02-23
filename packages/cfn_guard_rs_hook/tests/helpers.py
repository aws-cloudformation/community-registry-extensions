"""
    Helpers for testing
"""
from dataclasses import dataclass
from typing import Any, Mapping, Optional, Type

from cloudformation_cli_python_lib import (
    BaseHookHandlerRequest,
    HookContext,
    HookInvocationPoint,
)
from cloudformation_cli_python_lib.interface import BaseModel


@dataclass
class HookHandlerRequest(BaseHookHandlerRequest):
    """
    Mimic the cloudformation_cli_python_lib
    """


def create_request(
    invocation_point: HookInvocationPoint, target_model: Mapping[str, Any]
) -> BaseHookHandlerRequest:
    """
    Create a hook request
    """
    return BaseHookHandlerRequest(
        "",
        hookContext=HookContext(
            awsAccountId="1234567890",
            stackId="uniqueID",
            hookTypeName="AwsCommunity::Guard::Hook",
            hookTypeVersion="00000001",
            invocationPoint=invocation_point,
            targetName="AWS::S3::Bucket",
            targetType="AWS::S3::Bucket",
            targetModel=target_model,
            targetLogicalId="Bucket",
            changeSetId=None,
        ),
    )


@dataclass
class TypeConfigurationModel(BaseModel):
    """
    Mimic the cloudformation_cli_python_lib
    """

    @classmethod
    def _deserialize(
        cls: Type["_TypeConfigurationModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TypeConfigurationModel"]:
        if not json_data:
            return None
        return cls()


_TypeConfigurationModel = TypeConfigurationModel
