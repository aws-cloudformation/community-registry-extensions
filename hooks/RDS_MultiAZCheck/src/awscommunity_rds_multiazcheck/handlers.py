import logging
from typing import Any, MutableMapping, Optional
from cloudformation_cli_python_lib import (
    BaseHookHandlerRequest,
    HandlerErrorCode,
    Hook,
    HookInvocationPoint,
    OperationStatus,
    ProgressEvent,
    SessionProxy,
    exceptions,
)

from .models import HookHandlerRequest, TypeConfigurationModel

# Use this logger to forward log messages to CloudWatch Logs.
LOG = logging.getLogger(__name__)
TYPE_NAME = "AwsCommunity::RDS::MultiAZCheck"

hook = Hook(TYPE_NAME, TypeConfigurationModel)
test_entrypoint = hook.test_entrypoint

def _validate_RDS_multiaz_setting(rds: MutableMapping[str, Any]) -> ProgressEvent:
    status = None
    message = ""
    error_code = None

    if rds:
        rds_name = rds.get("DBName")
        rds_multiAZ_setting = rds.get("MultiAZ")
        if rds_multiAZ_setting:
                status = OperationStatus.SUCCESS
                message = f"Successfully invoked RDS MultiAZ  Check Handler for AWS::RDS::DBInstance with name: {rds_name}"
        else:
                status = OperationStatus.FAILED
                message = f"RDS MultiAZ not enabled for AWS::RDS::DBInstance with name: {rds_name}"
    else:
        status = OperationStatus.FAILED
        message = "Resource properties for RDS target model are empty"
    if status == OperationStatus.FAILED:
        error_code = HandlerErrorCode.NonCompliant

    return ProgressEvent(
        status=status,
        message=message,
        errorCode=error_code
    )

@hook.handler(HookInvocationPoint.CREATE_PRE_PROVISION)
def pre_create_handler(
        session: Optional[SessionProxy],
        request: HookHandlerRequest,
        callback_context: MutableMapping[str, Any],
        type_configuration: TypeConfigurationModel
) -> ProgressEvent:
    target_model = request.hookContext.targetModel
    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS
    )
    try:
        # A Hook that checks if RDS has MultiAZ setting enabled
        target_name = request.hookContext.targetName
        if "AWS::RDS::DBInstance" == target_name:
            return _validate_RDS_multiaz_setting(request.hookContext.targetModel.get("resourceProperties"))
        else:
            raise exceptions.InvalidRequest(f"Unknown target type: {target_name}")

    except TypeError as e:
        # exceptions module lets CloudFormation know the type of failure that occurred
        raise exceptions.InternalFailure(f"was not expecting type {e}")
        # this can also be done by returning a failed progress event
        # return ProgressEvent.failed(HandlerErrorCode.InternalFailure, f"was not expecting type {e}")

    return progress


@hook.handler(HookInvocationPoint.UPDATE_PRE_PROVISION)
def pre_update_handler(
        session: Optional[SessionProxy],
        request: BaseHookHandlerRequest,
        callback_context: MutableMapping[str, Any],
        type_configuration: TypeConfigurationModel
) -> ProgressEvent:
    target_model = request.hookContext.targetModel
    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS
    )
    try:
        # A Hook that checks if RDS has MultiAZ setting enabled
        target_name = request.hookContext.targetName
        if "AWS::RDS::DBInstance" == target_name:
            return _validate_RDS_multiaz_setting(request.hookContext.targetModel.get("resourceProperties"))
        else:
            raise exceptions.InvalidRequest(f"Unknown target type: {target_name}")

    except TypeError as e:
        progress = ProgressEvent.failed(HandlerErrorCode.InternalFailure, f"was not expecting type {e}")

    return progress


@hook.handler(HookInvocationPoint.DELETE_PRE_PROVISION)
def pre_delete_handler(
        session: Optional[SessionProxy],
        request: BaseHookHandlerRequest,
        callback_context: MutableMapping[str, Any],
        type_configuration: TypeConfigurationModel
) -> ProgressEvent:
    return ProgressEvent(
        status=OperationStatus.SUCCESS
    )
