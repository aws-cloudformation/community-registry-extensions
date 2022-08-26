"""
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
"""

from typing import Type, Optional, MutableMapping, Any
import json
import logging
from cloudformation_cli_python_lib import (
    Hook,
    BaseHookHandlerRequest,
    ProgressEvent,
    SessionProxy,
    HookInvocationPoint,
    OperationStatus,
    HandlerErrorCode,
)
import importlib.resources as pkg_resources
from cloudformation_cli_python_lib.interface import BaseModel
import cfn_guard_rs

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.DEBUG)


class GuardHook(Hook):
    def __init__(
        self,
        type_name: str,
        type_configuration_model_cls: Type[BaseModel],
        rules: pkg_resources.Package,
    ) -> None:
        super().__init__(type_name, type_configuration_model_cls)
        self._handlers = {
            HookInvocationPoint.CREATE_PRE_PROVISION: self.pre_create_handler,
            HookInvocationPoint.UPDATE_PRE_PROVISION: self.pre_update_handler,
            HookInvocationPoint.DELETE_PRE_PROVISION: self.pre_delete_handler,
        }
        self.rules = rules

    def pre_create_handler(
        self,
        session: Optional[SessionProxy],
        request: BaseHookHandlerRequest,
        callback_context: MutableMapping[str, Any],
        type_configuration: Type[BaseModel],
    ) -> ProgressEvent:
        return self.__generic_handler(request=request)

    def pre_update_handler(
        self,
        session: Optional[SessionProxy],
        request: BaseHookHandlerRequest,
        callback_context: MutableMapping[str, Any],
        type_configuration: Type[BaseModel],
    ) -> ProgressEvent:
        return self.__generic_handler(request=request)

    def pre_delete_handler(
        self,
        session: Optional[SessionProxy],
        request: BaseHookHandlerRequest,
        callback_context: MutableMapping[str, Any],
        type_configuration: Type[BaseModel],
    ) -> ProgressEvent:
        return self.__generic_handler(request=request)

    def __generic_handler(self, request: BaseHookHandlerRequest):
        target_model = request.hookContext.targetModel
        progress: ProgressEvent = ProgressEvent(status=OperationStatus.FAILED)
        LOG.debug(f"Request: {request}")
        try:
            template = self.__make_cloudformation(
                target_model.get("resourceProperties", {}),
                request.hookContext.targetLogicalId,
                request.hookContext.targetName,
            )

            progress = self.__run_checks(template)
        except Exception as err:
            LOG.error(err)

        return progress

    def __make_cloudformation(
        self, props: dict, targetLogicalId: str, targetName: str
    ) -> dict:
        return {
            "Resources": {targetLogicalId: {"Type": targetName, "Properties": props}}
        }

    def __run_checks(self, template: dict) -> ProgressEvent:
        progress = ProgressEvent(status=OperationStatus.SUCCESS)
        LOG.debug(f"Template: {json.dumps(template)}")

        for c in pkg_resources.contents(self.rules):
            if c in ["__init__.py", "__pycache__"]:
                continue
            rules = pkg_resources.read_text(self.rules, c)
            LOG.debug(f"Rules from {c}: {rules}")

            guard_result = cfn_guard_rs.run_checks(template, rules, False)
            LOG.debug(f"Raw Guard results: {guard_result}")

            if guard_result.not_compliant:
                progress.status = OperationStatus.FAILED
                progress.errorCode = HandlerErrorCode.NonCompliant
                progress.message = ""
                for name, errs in guard_result.not_compliant.items():
                    for err in errs:
                        path = err.path
                        if err.message:
                            progress.message += f"Rule [{name}] failed on property [{path}] and got error [{err.message}]. "
                        else:
                            progress.message += f"Rule [{name}] failed on property [{path}] failed comparison operator [{err.comparison.operator}] and not exists of [{err.comparison.not_operator_exists}]. "

        progress.message = progress.message.strip()
        LOG.debug(progress)
        return progress
