
from dataclasses import dataclass
from cloudformation_cli_python_lib.interface import BaseModel
from cloudformation_cli_python_lib import (
    BaseHookHandlerRequest,
    HookContext,
    HookInvocationPoint,
)
from typing import (
    Any,
    Mapping,
    Optional,
    Type,
)


@dataclass
class HookHandlerRequest(BaseHookHandlerRequest):
    pass


def create_request(
    invocationPoint: HookInvocationPoint, targetModel: Mapping[str, Any]
) -> BaseHookHandlerRequest:
    return BaseHookHandlerRequest(
        "",
        hookContext=HookContext(
            awsAccountId="1234567890",
            stackId="uniqueID",
            hookTypeName="AwsCommunity::Guard::Hook",
            hookTypeVersion="00000001",
            invocationPoint=invocationPoint,
            targetName="AWS::S3::Bucket",
            targetType="AWS::S3::Bucket",
            targetModel=targetModel,
            targetLogicalId="Bucket",
            changeSetId=None,
        ),
    )


@dataclass
class TypeConfigurationModel(BaseModel):
    @classmethod
    def _deserialize(
        cls: Type["_TypeConfigurationModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TypeConfigurationModel"]:
        if not json_data:
            return None
        return cls()


_TypeConfigurationModel = TypeConfigurationModel
