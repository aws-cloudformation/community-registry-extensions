"Handler functions for the Lambda Invoker hook"
#pylint:disable=W0613
import logging
import json
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

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.DEBUG)

TYPE_NAME = "AwsCommunity::Lambda::Invoker"

hook = Hook(TYPE_NAME, TypeConfigurationModel)
test_entrypoint = hook.test_entrypoint

@hook.handler(HookInvocationPoint.CREATE_PRE_PROVISION)
def pre_create_handler(session, request, callback_context, type_configuration):
    "Called before creating a resource"
    target_model = request.hookContext.targetModel
    progress = ProgressEvent(status=OperationStatus.IN_PROGRESS)

    try:
        # Read the Resource Hook's target properties
        resource_properties = target_model.get("resourceProperties")
        LOG.debug(resource_properties)

        if isinstance(session, SessionProxy):
            #ddb = session.client("dynamodb")
            #lam = session.client("lambda")

            # TODO

            LOG.debug("About to query DDB for all Lambda Arns")
            LOG.debug("DDB Arn: %s", type_configuration.RegistrationTableArn)
            # Query the DDB table for all Lambda Arns

            # Invoke each Lambda Arn and send in the resource properties
            target_json = json.dumps(dict(target_model))
            LOG.debug(target_json)
            
            # Store each failure message
            
            # If anything failed, append all error messages to the progress event message

        else:
            raise exceptions.InternalFailure("No SessionProxy")

        progress.status = OperationStatus.SUCCESS

    except Exception as e:
        return failure(HandlerErrorCode.InternalFailure, str(e), traceback.format_exc())

    return progress

@hook.handler(HookInvocationPoint.UPDATE_PRE_PROVISION)
def pre_update_handler(session, request, callback_context, type_configuration):
    "Called before updating a resource"
    target_model = request.hookContext.targetModel
    progress = ProgressEvent(status=OperationStatus.IN_PROGRESS)
    try:
        # Read the Resource Hook's target current properties and previous properties
        resource_properties = target_model.get("resourceProperties")
        LOG.debug(resource_properties)
        previous_properties = target_model.get("previousResourceProperties")
        LOG.debug(previous_properties)

        progress.status = OperationStatus.SUCCESS

    except Exception as e:
        return failure(HandlerErrorCode.InternalFailure, str(e), traceback.format_exc())

    return progress

@hook.handler(HookInvocationPoint.DELETE_PRE_PROVISION)
def pre_delete_handler(session, request, callback_context, type_configuration):
    "Called before deleting a resource"
    return ProgressEvent(status=OperationStatus.SUCCESS)

def failure(handler_error_code, error_message, traceback_content):
    "Log an error, and return a ProgressEvent indicating a failure."
    LOG.debug("%s\n%s", error_message, traceback_content)
    return ProgressEvent.failed(
        handler_error_code,
        f"Error: {error_message}",
    )
