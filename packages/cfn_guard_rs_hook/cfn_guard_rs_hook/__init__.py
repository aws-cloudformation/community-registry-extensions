"""
  CloudFormation Guard Hook

  This library makes creating hooks using CloudFormation Guard
  easier. It leverages cfn_guard_rs to run Guard and
  translates the response into the appropriate hook format.
"""

__version__ = "0.1.0"

from cfn_guard_rs_hook.guard_hook import GuardHook
from cfn_guard_rs_hook.types import Converter, to_bool, to_float, to_int
