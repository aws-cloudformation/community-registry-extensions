"""
  Provides the TypeConfigurationModel
"""
from dataclasses import dataclass
from typing import (
    Any,
    Mapping,
    Optional,
    Type,
)
from cloudformation_cli_python_lib.interface import BaseModel


@dataclass
class TypeConfigurationModel(BaseModel):
    """
    Mimic the cloudformation_cli_python_lib
    """

    @classmethod
    def _deserialize(
        cls: Type["_TypeConfigurationModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TypeConfigurationModel"]:
        if not json_data:
            return None
        return cls()


_TypeConfigurationModel = TypeConfigurationModel
