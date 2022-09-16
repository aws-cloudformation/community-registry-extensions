"""
Handler functions for the CloudFormation Hook:
AwsCommunity::CloudFront::LoggingEnabled
"""
import logging

from cloudformation_cli_python_lib import (
    HandlerErrorCode,
    Hook,
    HookInvocationPoint,
    OperationStatus,
    ProgressEvent,
)

from .models import HookHandlerRequest, TypeConfigurationModel

# Use this logger to forward log messages to CloudWatch Logs.
LOG = logging.getLogger(__name__)
TYPE_NAME = "AwsCommunity::CloudFront::LoggingEnabled"
SUPPORTED_TYPES = ["AWS::CloudFront::Distribution"]

# Set the logging level
LOG.setLevel(logging.DEBUG)


hook = Hook(TYPE_NAME, TypeConfigurationModel)
test_entrypoint = hook.test_entrypoint


def _validate_cloudfront_logging(progress, target_name, resource_properties):
    """
    Function to validate if `DistributionConfig.Logging` attribute exists
    """
    try:
        LOG.debug(f"Details of resource_properties: {resource_properties}")
        logging_config = resource_properties.get("DistributionConfig", {}).get(
            "Logging"
        )
        LOG.debug(f"Logging Configuration: {logging_config}")
        if bool(logging_config):
            LOG.debug(f"CloudFront logging enabled: {logging_config}")
            progress.status = OperationStatus.SUCCESS
            progress.message = (
                f"Successfully invoked HookHandler for {target_name}. "
                "Resource logging enabled"
            )
        else:
            LOG.debug(
                "Noncompliant resource due to access logging disabled "
                f"{logging_config}"
            )
            progress.status = OperationStatus.FAILED
            progress.message = (
                "Failed Hook due to access logs disabled "
                f"{target_name}:{logging_config}"
            )
            progress.errorCode = HandlerErrorCode.NonCompliant

    except TypeError as e:
        # catch all exception and mark Hook status as failure
        progress.status = OperationStatus.FAILED
        progress.message = f"Not expecting type {e}."
        progress.errorCode = HandlerErrorCode.InternalFailure

    LOG.info(f"Results Message: {progress.message}")
    return progress


@hook.handler(HookInvocationPoint.CREATE_PRE_PROVISION)
@hook.handler(HookInvocationPoint.UPDATE_PRE_PROVISION)
def pre_handler(
    _s,
    request: HookHandlerRequest,
    _c,
    type_configuration: TypeConfigurationModel,
) -> ProgressEvent:
    """
    Handler for creation and update of CloudFormation stack
    """
    target_model = request.hookContext.targetModel
    target_name = request.hookContext.targetName
    progress: ProgressEvent = ProgressEvent(status=OperationStatus.IN_PROGRESS)
    LOG.debug(f"request: {request.__dict__}")
    LOG.debug(
        "type_configuration: "
        f"{type_configuration.__dict__ if type_configuration else dict()}"
    )

    if target_name in SUPPORTED_TYPES:
        LOG.info(f"Triggered PreHookHandler for target {target_name}")
        return _validate_cloudfront_logging(
            progress, target_name, target_model.get("resourceProperties")
        )
    LOG.error(
        f"Unknown target type: {target_name}, support types: {SUPPORTED_TYPES}"
    )
    return ProgressEvent(
        status=OperationStatus.FAILED,
        errorCode=HandlerErrorCode.InvalidRequest,
        message=(
            f"Invalid type: {target_name}, "
            f"This hook only supports: {SUPPORTED_TYPES}",
        ),
    )
