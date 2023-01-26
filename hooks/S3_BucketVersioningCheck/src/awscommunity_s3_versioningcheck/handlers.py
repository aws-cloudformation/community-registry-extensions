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
TYPE_NAME = "AwsCommunity::S3::VersioningCheck"

hook = Hook(TYPE_NAME, TypeConfigurationModel)
test_entrypoint = hook.test_entrypoint

def _validate_s3_bucket_versioning(bucket: MutableMapping[str, Any]) -> ProgressEvent:
    status = None
    message = ""
    error_code = None

    if bucket:
        bucket_name = bucket.get("BucketName")
        bucket_versioning = bucket.get("VersioningConfiguration")
        if bucket_versioning:
            if bucket_versioning.get("Status") == "Enabled":
                status = OperationStatus.SUCCESS
                message = f"Successfully invoked S3 Bucket Versioning Check Handler for AWS::S3::Bucket with name: {bucket_name}"
            else:
                status = OperationStatus.FAILED
                message = f"S3 Bucket Versioning not enabled for bucket with name: {bucket_name}"
        else:
            status = OperationStatus.FAILED
            message = f"S3 Bucket Versioning not enabled for bucket with name: {bucket_name}"
    else:
        status = OperationStatus.FAILED
        message = "Resource properties for S3 Bucket target model are empty"
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
    # TODO: put code here

    # Example:
    try:
        target_name = request.hookContext.targetName
        if "AWS::S3::Bucket" == target_name:
            return _validate_s3_bucket_versioning(request.hookContext.targetModel.get("resourceProperties"))
        else:
            raise exceptions.InvalidRequest(f"Unknown target type: {target_name}")

        # Reading the Resource Hook's target properties
        resource_properties = target_model.get("resourceProperties")

        if isinstance(session, SessionProxy):
            client = session.client("s3")
        # Setting Status to success will signal to cfn that the hook operation is complete
        progress.status = OperationStatus.SUCCESS
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
    # TODO: put code here

    # Example:
    try:
        # A Hook that checks to see that S3 bucket's versioning is enabled
        target_name = request.hookContext.targetName
        if "AWS::S3::Bucket" == target_name:
            return _validate_s3_bucket_versioning(request.hookContext.targetModel.get("resourceProperties"))
        else:
            raise exceptions.InvalidRequest(f"Unknown target type: {target_name}")

        # Reading the Resource Hook's target current properties and previous properties
        resource_properties = target_model.get("resourceProperties")
        previous_properties = target_model.get("previousResourceProperties")

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
    # TODO: put code here
    return ProgressEvent(
        status=OperationStatus.SUCCESS
    )
