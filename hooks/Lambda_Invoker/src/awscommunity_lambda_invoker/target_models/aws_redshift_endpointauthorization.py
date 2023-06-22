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
class AwsRedshiftEndpointauthorization(BaseModel):
    Grantor: Optional[str]
    Grantee: Optional[str]
    ClusterIdentifier: Optional[str]
    AuthorizeTime: Optional[str]
    ClusterStatus: Optional[str]
    Status: Optional[str]
    AllowedAllVPCs: Optional[bool]
    AllowedVPCs: Optional[Sequence[str]]
    EndpointCount: Optional[int]
    Account: Optional[str]
    VpcIds: Optional[Sequence[str]]
    Force: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AwsRedshiftEndpointauthorization"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsRedshiftEndpointauthorization"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Grantor=json_data.get("Grantor"),
            Grantee=json_data.get("Grantee"),
            ClusterIdentifier=json_data.get("ClusterIdentifier"),
            AuthorizeTime=json_data.get("AuthorizeTime"),
            ClusterStatus=json_data.get("ClusterStatus"),
            Status=json_data.get("Status"),
            AllowedAllVPCs=json_data.get("AllowedAllVPCs"),
            AllowedVPCs=json_data.get("AllowedVPCs"),
            EndpointCount=json_data.get("EndpointCount"),
            Account=json_data.get("Account"),
            VpcIds=json_data.get("VpcIds"),
            Force=json_data.get("Force"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsRedshiftEndpointauthorization = AwsRedshiftEndpointauthorization


