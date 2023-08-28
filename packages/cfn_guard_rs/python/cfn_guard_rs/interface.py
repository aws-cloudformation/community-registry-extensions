"""
  Defines the non-verbose output format returned
  from run_checks
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, List, Dict, Sequence, Tuple

# pylint: disable=missing-class-docstring,missing-function-docstring,invalid-name

@dataclass(eq=True, frozen=True)
class Messages:
    """Messages Output"""

    custom_message: str | None = field(default=None)
    error_message: str | None = field(default=None)

    @classmethod
    def from_object(cls, obj) -> "Messages":
        return cls(
            custom_message=obj.get("custom_message"),
            error_message=obj.get("error_message"),
        )


@dataclass(eq=True, frozen=True)
class RuleReport:
    """Messages Output"""

    name: str = field()
    metadata: Dict[str, Any] = field()
    messages: Messages = field()
    checks: Sequence[ClauseReport] = field()

    @classmethod
    def from_object(cls, obj) -> "RuleReport" | None:
        if obj is None:
            return None

        return cls(
            name=obj.get("name"),
            metadata=obj.get("metadata"),
            messages=Messages.from_object(obj.get("messages")),
            checks=ClauseReport.from_array(obj.get("checks")),
        )


@dataclass(eq=True, frozen=True)
class GuardBlockReport:
    """Guard Block Report"""

    context: str = field()
    messages: Messages = field()
    unresolved: Any = field()

    @classmethod
    def from_object(cls, obj):
        if obj is None:
            return obj

        return cls(
            context=obj.get("context"),
            messages=Messages.from_object(obj.get("messages")),
            unresolved=obj.get("resolved"),
        )


@dataclass(eq=True, frozen=True)
class DisjunctionsReport:
    """Disjunctions"""

    checks: ClauseReport = field()

    @classmethod
    def from_object(cls, obj):
        if obj is None:
            return obj

        return cls(checks=ClauseReport.from_object(obj.get("checks")))

@dataclass(eq=True, frozen=True)
class UnaryComparison:
    """Unary Comparison"""

    value: Any = field()
    comparison: Tuple[str, bool] = field()

    @classmethod
    def from_object(cls, obj):
        return cls(
            value=obj.get("value"),
            comparison=tuple(obj.get("comparison")),
        )


@dataclass(eq=True, frozen=True)
class UnResolved:
    """Unresolved"""

    traversed_to: Any = field()
    remaining_query: Any = field()
    reason: Any = field()

    @classmethod
    def from_object(cls, obj):
        if obj is None:
            return None
        return cls(
            traversed_to=obj.get("traversed_to"),
            remaining_query=obj.get("remaining_query"),
            reason=obj.get("reason"),
        )


@dataclass(eq=True, frozen=True)
class ValueUnResolved:
    value: Any = field()
    comparison: Any = field()

    @classmethod
    def from_object(cls, obj):
        return cls(
            value=obj.get("value"),
            comparison=obj.get("comparison"),
        )


@dataclass(eq=True, frozen=True)
class UnaryCheck:
    """Unary Check"""

    Resolved: UnaryComparison | None = field(default=None)
    UnResolved: UnResolved | None = field(default=None)
    UnresolvedContext: Any | None = field(default=None)

    @classmethod
    def from_object(cls, obj):
        if obj is None:
            return obj

        return cls(
            Resolved=UnaryComparison.from_object(obj.get("Resolved")),
            UnResolved=UnResolved.from_object(obj.get("UnResolved")),
            UnresolvedContext=obj.get("UnresolvedContext"),
        )


@dataclass(eq=True, frozen=True)
class UnaryReport:
    """Unary Report"""

    context: str = field()
    messages: Messages = field()
    check: UnaryCheck = field()

    @classmethod
    def from_object(cls, obj):
        if obj is None:
            return None

        return cls(
            context=obj.get("context"),
            messages=Messages.from_object(obj.get("messages")),
            check=UnaryCheck.from_object(obj.get("check")),
        )


@dataclass(eq=True, frozen=True)
class BinaryComparison:
    from_: Any = field()
    to_: Any = field()
    comparison: Any = field()

    @classmethod
    def from_object(cls, obj):
        if obj is None:
            return None
        return cls(
            from_=obj.get("from"), to_=obj.get("to"), comparison=obj.get("comparison")
        )


@dataclass(eq=True, frozen=True)
class InComparison:
    def __init__(self, **kwargs) -> None:
        self.from_ = kwargs["from"]
        self.to_ = kwargs["to"]
        self.comparison = kwargs["comparison"]

    @classmethod
    def from_object(cls, obj) -> "InComparison" | None:
        return cls(
            from_=obj.get("from"),
            to_=obj.get("to"),
            comparison=obj.get("comparison"),
        )


@dataclass(eq=True, frozen=True)
class BinaryCheck:
    Resolved: BinaryComparison | None = field(default=None)
    UnResolved: UnResolved | None = field(default=None)
    InResolved: Any = field(default=None)

    @classmethod
    def from_object(cls, obj):
        return cls(
            Resolved=BinaryComparison.from_object(obj.get("Resolved")),
            UnResolved=UnResolved.from_object(obj.get("UnResolved")),
            InResolved=obj.get("InResolved"),
        )


@dataclass(eq=True, frozen=True)
class BinaryReport:
    context: str = field()
    messages: Messages = field()
    check: BinaryCheck = field()

    @classmethod
    def from_object(cls, obj):
        if obj is None:
            return obj
        return cls(
            context=obj.get("context"),
            messages=Messages.from_object(obj.get("messages")),
            check=BinaryCheck.from_object(obj.get("check")),
        )


@dataclass(eq=True, frozen=True)
class GuardClauseReport:
    """Guard Clause Report"""

    Unary: UnaryReport | None = field(default=None)
    Binary: BinaryReport | None = field(default=None)

    @classmethod
    def from_object(cls, obj):
        if obj is None:
            return obj

        return cls(
            Unary=UnaryReport.from_object(obj.get("Unary")),
            Binary=BinaryReport.from_object(obj.get("Binary")),
        )


@dataclass(eq=True, frozen=True)
class ClauseReport:
    """Clause Report"""

    Rule: RuleReport | None = field(default=None)
    Disjunctions: DisjunctionsReport | None = field(default=None)
    GuardBlock: GuardBlockReport | None = field(default=None)
    Clause: GuardClauseReport | None = field(default=None)

    @classmethod
    def from_object(cls, obj):
        return cls(
            Rule=RuleReport.from_object(obj.get("Rule")),
            Disjunctions=DisjunctionsReport.from_object(obj.get("Disjunctions")),
            GuardBlock=GuardBlockReport.from_object(obj.get("GuardBlock")),
            Clause=GuardClauseReport.from_object(obj.get("Clause")),
        )

    @classmethod
    def from_array(cls, items):
        results = []
        for item in items:
            results.append(ClauseReport.from_object(item))

        return results


# pylint: disable=too-many-instance-attributes
@dataclass(eq=True, frozen=True)
class FileReport:
    name: str = field()
    metadata: Dict[str, Any] = field()
    status: str = field()
    not_compliant: List[ClauseReport] = field()
    not_applicable: List[str] = field()
    compliant: List[str] = field()
    data_from: str = field(default="cfn_guard_rs")
    rules_from: str = field(default="cfn_guard_rs")

    @classmethod
    def from_object(cls, obj) -> "FileReport":
        return cls(
            name=obj.get("name"),
            metadata=obj.get("metadata"),
            status=obj.get("status"),
            not_compliant=ClauseReport.from_array(obj.get("not_compliant")),
            not_applicable=obj.get("not_applicable"),
            compliant=obj.get("compliant"),
            data_from=obj.get("data_from", "cfn_guard_rs"),
            rules_from=obj.get("rules_from", "cfn_guard_rs"),
        )
