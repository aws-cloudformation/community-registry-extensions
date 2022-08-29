"""
  Defines the non-verbose output format returned
  from run_checks
"""

from dataclasses import dataclass
from typing import Any, List, Dict, Optional


@dataclass(eq=True)
class Comparison:
    """Comparison Output"""

    operator: str
    not_operator_exists: bool


@dataclass(eq=True)
class NameInfo:
    """NameInfo which is per error"""

    rule: str
    path: str
    provided: Any
    expected: Any
    comparison: Optional[Comparison]
    message: str
    error: Optional[str]

    # pylint: disable=too-many-arguments
    def __init__(
        self,
        rule: str,
        path: str,
        provided: Any,
        expected: Any,
        comparison: Optional[Comparison],
        message: str,
        error: Optional[str],
    ) -> None:
        self.rule = rule
        self.path = path
        self.provided = provided
        self.expected = expected
        self.message = message
        self.error = error
        if isinstance(comparison, dict):
            self.comparison = Comparison(**comparison)
        else:
            self.comparison = comparison


@dataclass(eq=True)
class DataOutput:
    """Primary Data Output"""

    not_compliant: Dict[str, List[NameInfo]]
    not_applicable: List[str]
    compliant: List[str]
    data_from: str = "cfn_guard_rs"
    rules_from: str = "cfn_guard_rs"

    # pylint: disable=unused-argument,too-many-arguments
    def __init__(
        self,
        not_compliant: Dict[str, List[NameInfo]],
        not_applicable: List[str],
        compliant: List[str],
        data_from: str = "cfn_guard_rs",
        rules_from: str = "cfn_guard_rs",
    ) -> None:
        self.not_applicable = not_applicable
        self.compliant = compliant
        self.data_from = "cfn_guard_rs"
        self.rules_from = "cfn_guard_rs"
        self.not_compliant = {}
        if isinstance(not_compliant, dict):
            for key, value in not_compliant.items():
                self.not_compliant[key] = []
                for name_item in value:
                    if isinstance(name_item, dict):
                        self.not_compliant[key].append(NameInfo(**name_item))
                    else:
                        self.not_compliant[key].append(name_item)
