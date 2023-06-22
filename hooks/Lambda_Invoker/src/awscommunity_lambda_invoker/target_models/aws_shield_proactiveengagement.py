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
class AwsShieldProactiveengagement(BaseModel):
    AccountId: Optional[str]
    ProactiveEngagementStatus: Optional[str]
    EmergencyContactList: Optional[Sequence["_EmergencyContact"]]

    @classmethod
    def _deserialize(
        cls: Type["_AwsShieldProactiveengagement"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsShieldProactiveengagement"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            AccountId=json_data.get("AccountId"),
            ProactiveEngagementStatus=json_data.get("ProactiveEngagementStatus"),
            EmergencyContactList=deserialize_list(json_data.get("EmergencyContactList"), EmergencyContact),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsShieldProactiveengagement = AwsShieldProactiveengagement


@dataclass
class EmergencyContact(BaseModel):
    ContactNotes: Optional[str]
    EmailAddress: Optional[str]
    PhoneNumber: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EmergencyContact"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EmergencyContact"]:
        if not json_data:
            return None
        return cls(
            ContactNotes=json_data.get("ContactNotes"),
            EmailAddress=json_data.get("EmailAddress"),
            PhoneNumber=json_data.get("PhoneNumber"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EmergencyContact = EmergencyContact


