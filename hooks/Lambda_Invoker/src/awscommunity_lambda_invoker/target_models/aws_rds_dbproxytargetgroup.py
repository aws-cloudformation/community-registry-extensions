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
class AwsRdsDbproxytargetgroup(BaseModel):
    DBProxyName: Optional[str]
    TargetGroupArn: Optional[str]
    TargetGroupName: Optional[str]
    ConnectionPoolConfigurationInfo: Optional["_ConnectionPoolConfigurationInfoFormat"]
    DBInstanceIdentifiers: Optional[Sequence[str]]
    DBClusterIdentifiers: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsRdsDbproxytargetgroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsRdsDbproxytargetgroup"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            DBProxyName=json_data.get("DBProxyName"),
            TargetGroupArn=json_data.get("TargetGroupArn"),
            TargetGroupName=json_data.get("TargetGroupName"),
            ConnectionPoolConfigurationInfo=ConnectionPoolConfigurationInfoFormat._deserialize(json_data.get("ConnectionPoolConfigurationInfo")),
            DBInstanceIdentifiers=json_data.get("DBInstanceIdentifiers"),
            DBClusterIdentifiers=json_data.get("DBClusterIdentifiers"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsRdsDbproxytargetgroup = AwsRdsDbproxytargetgroup


@dataclass
class ConnectionPoolConfigurationInfoFormat(BaseModel):
    MaxConnectionsPercent: Optional[int]
    MaxIdleConnectionsPercent: Optional[int]
    ConnectionBorrowTimeout: Optional[int]
    SessionPinningFilters: Optional[Sequence[str]]
    InitQuery: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectionPoolConfigurationInfoFormat"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectionPoolConfigurationInfoFormat"]:
        if not json_data:
            return None
        return cls(
            MaxConnectionsPercent=json_data.get("MaxConnectionsPercent"),
            MaxIdleConnectionsPercent=json_data.get("MaxIdleConnectionsPercent"),
            ConnectionBorrowTimeout=json_data.get("ConnectionBorrowTimeout"),
            SessionPinningFilters=json_data.get("SessionPinningFilters"),
            InitQuery=json_data.get("InitQuery"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectionPoolConfigurationInfoFormat = ConnectionPoolConfigurationInfoFormat


