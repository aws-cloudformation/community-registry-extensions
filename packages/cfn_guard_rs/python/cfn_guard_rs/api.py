"""
  Defines the api for cfn_guard_rs

  Supports running the non-verbose version of
  run_checks from CloudFormation Guard
"""
import logging
import json
from cfn_guard_rs.interface import DataOutput

# pylint: disable=no-name-in-module
from cfn_guard_rs.cfn_guard_rs import (
    CfnGuardParseError,
    CfnGuardMissingValue,
    run_checks_rs,
)

from . import errors

LOG = logging.getLogger(__name__)


def run_checks(data: dict, rules: str) -> DataOutput:
    """
    Executes run_checks against Guard

    Run non-verbose checks against data for rules

    Parameters
    ----------
    data : dict
        Data is the object being checked by guard
    rules : str
        A string representation of the ruels being used

    Returns
    -------
    DataOuptut
        DataOutput representation of the result of running guard
    """
    try:
        raw_output = run_checks_rs(json.dumps(data), rules, False)
        output = json.loads(raw_output)
        # remove the lib set items and replace with our defaults
        result = DataOutput(**output)

        return result
    except json.JSONDecodeError as err:
        LOG.debug(
            "JSON decoding error when processing return value [%s] got error: %s",
            raw_output,
            err,
        )
        raise err
    except CfnGuardMissingValue as err:
        raise errors.MissingValueError(str(err))
    except CfnGuardParseError as err:
        raise errors.ParseError(str(err))
    except Exception as err:
        LOG.debug(
            "Received unknown exception [%s] while running checks, got error: %s",
            type(err),
            err,
        )
        raise errors.UnknownError(str(err))
