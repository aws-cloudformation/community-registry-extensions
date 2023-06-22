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
class AwsIotsitewiseAccesspolicy(BaseModel):
    AccessPolicyId: Optional[str]
    AccessPolicyArn: Optional[str]
    AccessPolicyIdentity: Optional["_AccessPolicyIdentity"]
    AccessPolicyPermission: Optional[str]
    AccessPolicyResource: Optional["_AccessPolicyResource"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIotsitewiseAccesspolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIotsitewiseAccesspolicy"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AccessPolicyId=json_data.get("AccessPolicyId"),
            AccessPolicyArn=json_data.get("AccessPolicyArn"),
            AccessPolicyIdentity=AccessPolicyIdentity._deserialize(json_data.get("AccessPolicyIdentity")),
            AccessPolicyPermission=json_data.get("AccessPolicyPermission"),
            AccessPolicyResource=AccessPolicyResource._deserialize(json_data.get("AccessPolicyResource")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIotsitewiseAccesspolicy = AwsIotsitewiseAccesspolicy


@dataclass
class AccessPolicyIdentity(BaseModel):
    User: Optional["_User"]
    IamUser: Optional["_IamUser"]
    IamRole: Optional["_IamRole"]

    @classmethod
    def _deserialize(
        cls: Type["_AccessPolicyIdentity"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessPolicyIdentity"]:
        if not json_data:
            return None
        return cls(
            User=User._deserialize(json_data.get("User")),
            IamUser=IamUser._deserialize(json_data.get("IamUser")),
            IamRole=IamRole._deserialize(json_data.get("IamRole")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessPolicyIdentity = AccessPolicyIdentity


@dataclass
class User(BaseModel):
    id: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_User"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_User"]:
        if not json_data:
            return None
        return cls(
            id=json_data.get("id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_User = User


@dataclass
class IamUser(BaseModel):
    arn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IamUser"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IamUser"]:
        if not json_data:
            return None
        return cls(
            arn=json_data.get("arn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IamUser = IamUser


@dataclass
class IamRole(BaseModel):
    arn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IamRole"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IamRole"]:
        if not json_data:
            return None
        return cls(
            arn=json_data.get("arn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IamRole = IamRole


@dataclass
class AccessPolicyResource(BaseModel):
    Portal: Optional["_Portal"]
    Project: Optional["_Project"]

    @classmethod
    def _deserialize(
        cls: Type["_AccessPolicyResource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessPolicyResource"]:
        if not json_data:
            return None
        return cls(
            Portal=Portal._deserialize(json_data.get("Portal")),
            Project=Project._deserialize(json_data.get("Project")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessPolicyResource = AccessPolicyResource


@dataclass
class Portal(BaseModel):
    id: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Portal"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Portal"]:
        if not json_data:
            return None
        return cls(
            id=json_data.get("id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Portal = Portal


@dataclass
class Project(BaseModel):
    id: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Project"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Project"]:
        if not json_data:
            return None
        return cls(
            id=json_data.get("id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Project = Project


