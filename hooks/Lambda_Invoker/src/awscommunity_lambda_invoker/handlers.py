"Handler functions for the Lambda Invoker hook"
# pylint:disable=W0613

import logging
import traceback

from cloudformation_cli_python_lib import (
    HandlerErrorCode,
    Hook,
    HookInvocationPoint,
    OperationStatus,
    ProgressEvent,
    SessionProxy,
    exceptions,
)

from .models import TypeConfigurationModel
from .invoker import invoke_lambdas

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

TYPE_NAME = "AwsCommunity::Lambda::Invoker"

SUPPORTED_PREFIXES = ["AWS::"]

hook = Hook(TYPE_NAME, TypeConfigurationModel)
test_entrypoint = hook.test_entrypoint


def _handler(session, request, type_configuration, op):
    "Handle creates, updates, and deletes"
    target_model = request.hookContext.targetModel
    target_name = request.hookContext.targetName
    progress = ProgressEvent(status=OperationStatus.IN_PROGRESS)

    logger.debug("_handler")
    logger.debug(target_name)
    logger.debug(target_model)

    # Check to make sure we support this type
    supported = False
    for s in SUPPORTED_PREFIXES:
        if target_name.startswith(s):
            supported = True
            break
    if not supported:
        return ProgressEvent(
            status=OperationStatus.FAILED,
            errorCode=HandlerErrorCode.UnsupportedTarget,
            message=f"Invalid type: {target_name}, ",
        )

    try:
        # Read the Resource Hook's target properties
        resource_properties = target_model.get("resourceProperties")
        logger.debug(resource_properties)

        if isinstance(session, SessionProxy):
            ddb = session.client("dynamodb")
            lam = session.client("lambda")

            logger.debug("About to query DDB for all Lambda Arns")
            table_arn = type_configuration.RegistrationTableArn
            logger.debug("table_arn: %s", table_arn)
            table_name = table_arn.split(":table/")[1]
            logger.debug("table_name: %s", table_name)
            target = {
                "type_name": target_name,
                "resource_properties": resource_properties,
                "operation": op,
            }
            logger.debug("target: %s", target)

            errs = invoke_lambdas(ddb, lam, target, logger, table_name)

            # If anything failed, append all error messages to the progress event message
            if errs:
                logger.debug("invoke_lambdas returned errors")
                progress.status = OperationStatus.FAILED
                progress.errorCode = HandlerErrorCode.NonCompliant
                progress.message = ""
                for err in errs:
                    progress.message += err + "\n"
                logger.debug("message: %s", progress.message)
                return progress

        else:
            raise exceptions.InternalFailure("No SessionProxy")

        progress.status = OperationStatus.SUCCESS

    except Exception as e:
        logger.debug("Uncaught exception")
        return failure(HandlerErrorCode.InternalFailure, str(e), traceback.format_exc())

    return progress


@hook.handler(HookInvocationPoint.CREATE_PRE_PROVISION)
def pre_create_handler(session, request, callback_context, type_configuration):
    "Called before creating a resource"
    logger.debug("In pre_create_handler")
    return _handler(session, request, type_configuration, "create")


@hook.handler(HookInvocationPoint.UPDATE_PRE_PROVISION)
def pre_update_handler(session, request, callback_context, type_configuration):
    "Called before updating a resource"
    return _handler(session, request, type_configuration, "update")


@hook.handler(HookInvocationPoint.DELETE_PRE_PROVISION)
def pre_delete_handler(session, request, callback_context, type_configuration):
    "Called before deleting a resource"
    return _handler(session, request, type_configuration, "delete")


def failure(handler_error_code, error_message, traceback_content):
    "Log an error, and return a ProgressEvent indicating a failure."
    logger.debug("%s\n%s", error_message, traceback_content)
    return ProgressEvent.failed(
        handler_error_code,
        f"Error: {error_message}",
    )
