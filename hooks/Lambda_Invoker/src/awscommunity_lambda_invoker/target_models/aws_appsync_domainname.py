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
class AwsAppsyncDomainname(BaseModel):
    DomainName: Optional[str]
    Description: Optional[str]
    CertificateArn: Optional[str]
    AppSyncDomainName: Optional[str]
    HostedZoneId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsAppsyncDomainname"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsAppsyncDomainname"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            DomainName=json_data.get("DomainName"),
            Description=json_data.get("Description"),
            CertificateArn=json_data.get("CertificateArn"),
            AppSyncDomainName=json_data.get("AppSyncDomainName"),
            HostedZoneId=json_data.get("HostedZoneId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsAppsyncDomainname = AwsAppsyncDomainname


