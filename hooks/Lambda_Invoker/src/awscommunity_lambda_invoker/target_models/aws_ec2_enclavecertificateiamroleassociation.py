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
class AwsEc2Enclavecertificateiamroleassociation(BaseModel):
    CertificateArn: Optional[str]
    RoleArn: Optional[str]
    CertificateS3BucketName: Optional[str]
    CertificateS3ObjectKey: Optional[str]
    EncryptionKmsKeyId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Enclavecertificateiamroleassociation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Enclavecertificateiamroleassociation"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            CertificateArn=json_data.get("CertificateArn"),
            RoleArn=json_data.get("RoleArn"),
            CertificateS3BucketName=json_data.get("CertificateS3BucketName"),
            CertificateS3ObjectKey=json_data.get("CertificateS3ObjectKey"),
            EncryptionKmsKeyId=json_data.get("EncryptionKmsKeyId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Enclavecertificateiamroleassociation = AwsEc2Enclavecertificateiamroleassociation


