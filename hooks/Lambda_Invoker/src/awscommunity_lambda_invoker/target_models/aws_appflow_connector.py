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
class AwsAppflowConnector(BaseModel):
    ConnectorLabel: Optional[str]
    ConnectorArn: Optional[str]
    ConnectorProvisioningType: Optional[str]
    ConnectorProvisioningConfig: Optional["_ConnectorProvisioningConfig"]
    Description: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAppflowConnector"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAppflowConnector"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            ConnectorLabel=json_data.get("ConnectorLabel"),
            ConnectorArn=json_data.get("ConnectorArn"),
            ConnectorProvisioningType=json_data.get("ConnectorProvisioningType"),
            ConnectorProvisioningConfig=ConnectorProvisioningConfig._deserialize(json_data.get("ConnectorProvisioningConfig")),
            Description=json_data.get("Description"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAppflowConnector = AwsAppflowConnector


@dataclass
class ConnectorProvisioningConfig(BaseModel):
    Lambda: Optional["_LambdaConnectorProvisioningConfig"]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectorProvisioningConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectorProvisioningConfig"]:
        if not json_data:
            return None
        return cls(
            Lambda=LambdaConnectorProvisioningConfig._deserialize(json_data.get("Lambda")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectorProvisioningConfig = ConnectorProvisioningConfig


@dataclass
class LambdaConnectorProvisioningConfig(BaseModel):
    LambdaArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LambdaConnectorProvisioningConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LambdaConnectorProvisioningConfig"]:
        if not json_data:
            return None
        return cls(
            LambdaArn=json_data.get("LambdaArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LambdaConnectorProvisioningConfig = LambdaConnectorProvisioningConfig


