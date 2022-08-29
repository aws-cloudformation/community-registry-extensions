import json
from .interface import DataOutput

# pylint: disable=no-name-in-module
from .cfn_guard_rs import run_checks_rs


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
    # hard code the verbose value.  This will change the output to be a list
    output = json.loads(run_checks_rs(json.dumps(data), rules, False))
    # remove the lib set items and replace with our defaults
    result = DataOutput(**output)

    return result
