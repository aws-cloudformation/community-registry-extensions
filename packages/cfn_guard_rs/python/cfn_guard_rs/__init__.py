"""
  CloudFormation Guard

  This library converts CloudFormation Guard into a Python
  library.  It leverages the Guard API of run_checks
  to validate a payload using a string version of the rules
"""

from .api import run_checks

from .interface import (
    FileReport,
    RuleReport,
    Messages,
    ClauseReport,
    UnaryReport,
    BinaryReport,
    UnaryComparison,
    UnaryCheck,
    GuardClauseReport,
    BinaryCheck,
    BinaryComparison,
)
