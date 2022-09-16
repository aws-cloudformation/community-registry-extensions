import importlib.resources as pkg_resources
from ast import literal_eval
from functools import singledispatch
from typing import Dict

import cfn_guard_rs

from ..rule_library import combiners, core
from ..utils.common import is_guard_rule
from ..utils.logger import LOG, logdebug
from .data_types import GuardRuleResult, GuardRuleSetResult, Statefull, Stateless


@logdebug
def prepare_ruleset():
    static_rule_modules = [core, combiners]
    rule_set = set()
    for module in static_rule_modules:
        for content in pkg_resources.contents(module):
            if not is_guard_rule(content):
                continue
            rule_set.add(pkg_resources.read_text(module, content))
    return rule_set


@logdebug
def __exec_rules__(schema: Dict):
    """Closure factory function for schema compliace execution -
    Read rule compliance status and output guard rule set result
    Creates closure, modifies, and retains the previous state between calls (rule set evaluations)
    Args:
        schema ([Dict]): Resource Provider Schema
    Returns:
        [function]: Closure
    """
    exec_result = GuardRuleSetResult()

    @logdebug
    def __exec__(rules: str):
        guard_result = cfn_guard_rs.run_checks(schema, rules)

        def __render_output(evaluation_result: object):
            non_compliant = {}
            for rule_name, checks in guard_result.not_compliant.items():

                non_compliant[rule_name] = []

                for check in checks:
                    try:
                        _message_dict = literal_eval(check.message.strip())
                        non_compliant[rule_name].append(
                            GuardRuleResult(
                                check_id=_message_dict["check_id"],
                                message=_message_dict["message"],
                            )
                        )
                    except SyntaxError as ex:
                        LOG.info("%s %s", str(ex), check.message)
                        non_compliant[rule_name].append(GuardRuleResult())

            return GuardRuleSetResult(
                compliant=evaluation_result.compliant,
                non_compliant=non_compliant,
                skipped=evaluation_result.not_applicable,
            )

        exec_result.merge(__render_output(guard_result))
        return exec_result

    return __exec__


@singledispatch
def exec_compliance(*args, **kwards):
    """Placeholder for exec_compliance
    This function holds no implementation,
    There are two types of compliance checks:
    * Stateless - works with current schema state
    * Statefull - works with current and previous schema states
    Raises:
        NotImplementedError: not supported implementation
    """
    raise NotImplementedError("not supported implementation")


# https://stackoverflow.com/questions/62700774/singledispatchmethod-with-typing-types
# Have to switch to class type instead of typing due to functools known bug
@exec_compliance.register(Stateless)
def _(payload):
    """Implements exec_compliance for stateless compliance assessment
    over specified list of schemas/rules

    Args:
        payload (Stateless): Stateless payload
    Returns:
        [GuardRuleSetResult]: Collection of Rule Results
    """

    compliance_output = []
    ruleset = prepare_ruleset() | set(payload.rules)

    def __execute__(schema_exec, ruleset):
        output = None
        for rules in ruleset:
            output = schema_exec(rules)
        return output

    for schema in payload.schemas:
        schema_to_execute = __exec_rules__(schema=schema)
        output = __execute__(schema_exec=schema_to_execute, ruleset=ruleset)
        compliance_output.append(output)

    return compliance_output


@exec_compliance.register(Statefull)
def _(payload):
    """Implements exec_compliance for statefull compliance assessment
    over specified list of rules

    Args:
        payload (Statefull): Statefull payload
    Returns:
        GuardRuleSetResult: Rule Result
    """
    raise NotImplementedError("Statefull evaluation is not supported yet")
