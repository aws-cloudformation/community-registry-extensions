from dataclasses import dataclass, field
from typing import Any, Dict, List

from ..utils.miscellaneous import jinja_loader


@dataclass
class Stateless:
    """Implements Stateless type for stateless compliance assessment
    over specified list of schemas/rules

    Args:
        schemas (List[Dict[str, Any]]): Collection of Resource Provider Schemas
        rules (List[str]): Collection of Custom Compliance Rules
    """

    schemas: List[Dict[str, Any]]
    rules: List[str] = field(default_factory=list)


@dataclass
class Statefull:
    """Implements Statefull type for statefull compliance assessment
    over specified list of rules

    Args:
        current_schema (Dict[str, Any]): Current State of Resource Provider Schema
        previous_schema (Dict[str, Any]): Previous State of Resource Provider Schema
    """

    current_schema: Dict[str, Any]
    previous_schema: Dict[str, Any]
    rules: List[str] = field(default_factory=list)


@dataclass
class GuardRuleResult:
    check_id: str = field(default="unidentified")
    message: str = field(default="unidentified")


@dataclass
class GuardRuleSetResult:
    compliant: List[str] = field(default_factory=list)
    non_compliant: Dict[str, List[GuardRuleResult]] = field(default_factory=dict)
    skipped: List[str] = field(default_factory=list)

    def merge(self, guard_ruleset_result: Any):
        if not isinstance(guard_ruleset_result, GuardRuleSetResult):
            raise TypeError("cannot merge with non GuardRuleSetResult type")

        self.compliant.extend(guard_ruleset_result.compliant)
        self.skipped.extend(guard_ruleset_result.skipped)
        self.non_compliant = {
            **self.non_compliant,
            **guard_ruleset_result.non_compliant,
        }

    def __str__(self):

        if not self.compliant and not self.non_compliant and self.skipped:
            return "Couldn't retrieve the result"

        environment = jinja_loader(__name__)
        template = environment.get_template("guard-result-pojo.output")
        return template.render(
            skipped_rules=self.skipped,
            passed_rules=self.compliant,
            failed_rules=self.non_compliant,
        )
