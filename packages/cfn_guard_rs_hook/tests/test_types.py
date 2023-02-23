"""
    Test cfn_guard_rs_hook
"""
import pytest

from cfn_guard_rs_hook import types


@pytest.mark.parametrize(
    "func,value_in,value_out",
    [
        (types.to_int, "0", 0),
        (types.to_float, "1.3", 1.3),
        (types.to_float, "1", 1.0),
        (types.to_bool, "true", True),
        (types.to_bool, "false", False),
        (types.to_bool, "True", True),
        (types.to_bool, "False", False),
    ],
)
# pylint: disable=too-many-arguments
def test_type_conversions(func, value_in, value_out):
    """
    Test types
    """
    assert func(value_in) == value_out
