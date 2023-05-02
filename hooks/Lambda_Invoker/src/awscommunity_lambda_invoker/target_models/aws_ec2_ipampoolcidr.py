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
class AwsEc2Ipampoolcidr(BaseModel):
    IpamPoolCidrId: Optional[str]
    IpamPoolId: Optional[str]
    Cidr: Optional[str]
    NetmaskLength: Optional[int]
    State: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsEc2Ipampoolcidr"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsEc2Ipampoolcidr"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            IpamPoolCidrId=json_data.get("IpamPoolCidrId"),
            IpamPoolId=json_data.get("IpamPoolId"),
            Cidr=json_data.get("Cidr"),
            NetmaskLength=json_data.get("NetmaskLength"),
            State=json_data.get("State"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsEc2Ipampoolcidr = AwsEc2Ipampoolcidr


