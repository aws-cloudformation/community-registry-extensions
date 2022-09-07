"""
    Primary Guard hook code
"""
from typing import Optional, MutableMapping, Any
import json
import logging
from dataclasses import asdict
from types import ModuleType
from jinja2 import Environment, FileSystemLoader, select_autoescape
from cloudformation_cli_python_lib import (
    Hook,
    BaseHookHandlerRequest,
    ProgressEvent,
    SessionProxy,
    HookInvocationPoint,
    OperationStatus,
    HandlerErrorCode,
)
import cfn_guard_rs

LOG = logging.getLogger(__name__)


class GuardHook(Hook):
    """
    Override the cloudformation_cli_python_lib Hook class for
    the purpose of using with CloudFormation Guard
    """

    def __init__(
        self,
        type_name: str,
        type_configuration: Any,
        rules: ModuleType,
    ) -> None:
        super().__init__(type_name, type_configuration)
        self._handlers = {
            HookInvocationPoint.CREATE_PRE_PROVISION: self.pre_create_handler,
            HookInvocationPoint.UPDATE_PRE_PROVISION: self.pre_update_handler,
            HookInvocationPoint.DELETE_PRE_PROVISION: self.pre_delete_handler,
        }
        self.jinja = Environment(
            loader=FileSystemLoader(rules.__path__), autoescape=select_autoescape()
        )
        self.rules = rules

    # pylint: disable=unused-argument
    def pre_create_handler(
        self,
        session: Optional[SessionProxy],
        request: BaseHookHandlerRequest,
        callback_context: MutableMapping[str, Any],
        type_configuration: Any,
    ) -> ProgressEvent:
        """
        Pre Create Handler for CloudFormation Hook
        """
        return self.__generic_handler(
            request=request, type_configuration=type_configuration
        )

    # pylint: disable=unused-argument
    def pre_update_handler(
        self,
        session: Optional[SessionProxy],
        request: BaseHookHandlerRequest,
        callback_context: MutableMapping[str, Any],
        type_configuration: Any,
    ) -> ProgressEvent:
        """
        Pre Update Handler for CloudFormation Hook
        """
        return self.__generic_handler(
            request=request, type_configuration=type_configuration
        )

    # pylint: disable=unused-argument
    def pre_delete_handler(
        self,
        session: Optional[SessionProxy],
        request: BaseHookHandlerRequest,
        callback_context: MutableMapping[str, Any],
        type_configuration: Any,
    ) -> ProgressEvent:
        """
        Pre Delete Handler for CloudFormation Hook
        """
        return self.__generic_handler(
            request=request, type_configuration=type_configuration
        )

    def __generic_handler(
        self,
        request: BaseHookHandlerRequest,
        type_configuration: Any,
    ) -> ProgressEvent:
        """
        A generic handler to handle all types of create, udpate, delete events

        Runs guard against a generic request to validate
        the properties against a set of rules

        Parameters
        ----------
        request : BaseHookHandlerRequest
            The request coming from the hook

        Returns
        -------
        ProgressEvent
            A ProgressEvent representing the results of running Guard
        """
        target_model = request.hookContext.targetModel
        progress: ProgressEvent = ProgressEvent(status=OperationStatus.FAILED)
        LOG.debug("Request: %s", request)
        LOG.debug("Type Configuration: %s", type_configuration)
        try:
            if (
                target_model is not None
                and request.hookContext.targetLogicalId
                and request.hookContext.targetName
            ):
                template = self.__make_cloudformation(
                    target_model.get("resourceProperties", {}),
                    request.hookContext.targetLogicalId,
                    request.hookContext.targetName,
                )

                progress = self.__run_checks(template, type_configuration)
            else:
                progress.status = OperationStatus.FAILED
                progress.errorCode = HandlerErrorCode.NonCompliant
                progress.message = "No reosurce properties were supplied"
        # pylint: disable=broad-except
        except Exception as err:
            LOG.error(err)
            progress.status = OperationStatus.FAILED
            progress.errorCode = HandlerErrorCode.NonCompliant
            progress.message = str(err)

        return progress

    def __make_cloudformation(
        self, props: dict, resource_name: str, resource_type: str
    ) -> dict:
        """
        Converts hook properties into CloudFormation template

        To keep rules consistent we are converting a hook resource
        properties into a valid CloudFormation template

        Parameters
        ----------
        props : dict
            The properties for the resource from the hook
        targetLogicalId : str
            A string representing the name of the resource
        targetName : str
            The type of the resource

        Returns
        -------
        dict
            A valid CloudFormation template
        """
        return {
            "Resources": {resource_name: {"Type": resource_type, "Properties": props}}
        }

    # pylint: disable=too-many-nested-blocks
    def __run_checks(self, template: dict, type_configuration: Any) -> ProgressEvent:
        """
        Runs checks agains Guard

        Runs the actual checks and converts the result to a
        hook ProgressEvent

        Parameters
        ----------
        template : dict
            A valid CloudFormation template

        Returns
        -------
        ProgressEvent
            A hook output that is a translation of
            running Guard into hook output format
        """
        progress = ProgressEvent(status=OperationStatus.SUCCESS)
        LOG.debug("Template: %s", json.dumps(template))

        for rule_file in self.jinja.list_templates():
            if rule_file in ["__init__.py", "__pycache__"]:
                continue
            if rule_file.startswith("__pycache__"):
                continue
            rules_jinja = self.jinja.get_template(rule_file)
            rules = rules_jinja.render(
                asdict(type_configuration) if type_configuration is not None else {}
            )
            LOG.debug("Rules from %s: %s", rule_file, rules)
            guard_result = cfn_guard_rs.run_checks(template, rules)
            LOG.debug("Raw Guard results: %s", guard_result)

            if guard_result.not_compliant:
                progress.status = OperationStatus.FAILED
                progress.errorCode = HandlerErrorCode.NonCompliant
                progress.message = ""
                for name, errs in guard_result.not_compliant.items():
                    for err in errs:
                        path = err.path
                        if err.message:
                            progress.message += (
                                f"Rule [{name}] failed on "
                                f"property [{path}] and got error [{err.message}]. "
                            )
                        else:
                            if err.comparison:
                                progress.message += (
                                    f"Rule [{name}] failed on "
                                    f"property [{path}] failed comparison operator "
                                    f"[{err.comparison.operator}] and not exists "
                                    f"of [{err.comparison.not_operator_exists}]. "
                                )
                            else:
                                progress.message += (
                                    f"Rule [{name}] failed on "
                                    f"property [{path}] failed. "
                                )
        progress.message = progress.message.strip()
        LOG.debug("Progress Event: %s", progress)
        return progress
