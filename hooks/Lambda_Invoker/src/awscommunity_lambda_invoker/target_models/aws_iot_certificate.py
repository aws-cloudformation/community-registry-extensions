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
class AwsIotCertificate(BaseModel):
    CACertificatePem: Optional[str]
    CertificatePem: Optional[str]
    CertificateSigningRequest: Optional[str]
    CertificateMode: Optional[str]
    Status: Optional[str]
    Id: Optional[str]
    Arn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIotCertificate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIotCertificate"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            CACertificatePem=json_data.get("CACertificatePem"),
            CertificatePem=json_data.get("CertificatePem"),
            CertificateSigningRequest=json_data.get("CertificateSigningRequest"),
            CertificateMode=json_data.get("CertificateMode"),
            Status=json_data.get("Status"),
            Id=json_data.get("Id"),
            Arn=json_data.get("Arn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIotCertificate = AwsIotCertificate


