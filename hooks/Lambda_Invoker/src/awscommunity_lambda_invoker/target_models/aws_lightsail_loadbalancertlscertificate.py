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
class AwsLightsailLoadbalancertlscertificate(BaseModel):
    LoadBalancerName: Optional[str]
    CertificateName: Optional[str]
    CertificateDomainName: Optional[str]
    CertificateAlternativeNames: Optional[AbstractSet[str]]
    LoadBalancerTlsCertificateArn: Optional[str]
    IsAttached: Optional[bool]
    HttpsRedirectionEnabled: Optional[bool]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsLightsailLoadbalancertlscertificate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsLightsailLoadbalancertlscertificate"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            LoadBalancerName=json_data.get("LoadBalancerName"),
            CertificateName=json_data.get("CertificateName"),
            CertificateDomainName=json_data.get("CertificateDomainName"),
            CertificateAlternativeNames=set_or_none(json_data.get("CertificateAlternativeNames")),
            LoadBalancerTlsCertificateArn=json_data.get("LoadBalancerTlsCertificateArn"),
            IsAttached=json_data.get("IsAttached"),
            HttpsRedirectionEnabled=json_data.get("HttpsRedirectionEnabled"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsLightsailLoadbalancertlscertificate = AwsLightsailLoadbalancertlscertificate


