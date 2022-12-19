from __future__ import annotations

import logging
from typing import Any, MutableMapping, Optional, Union

from cloudformation_cli_python_lib import (
    Action,
    HandlerErrorCode,
    OperationStatus,
    ProgressEvent,
    Resource,
    SessionProxy,
    exceptions,
    identifier_utils,
)
from dateutil import parser
from dateutil.parser import ParserError

from .models import ResourceHandlerRequest, ResourceModel

# Use this logger to forward log messages to CloudWatch Logs.
LOG = logging.getLogger(__name__)
LOG.setLevel(logging.DEBUG)
TYPE_NAME = "EWS::ApplicationAutoscaling::ScheduledAction"

resource = Resource(TYPE_NAME, ResourceModel)
test_entrypoint = resource.test_entrypoint


def rule_exists(session: SessionProxy, model) -> Union[dict, None]:
    if not model:
        return None
    exists_query_r = session.client(
        "application-autoscaling"
    ).describe_scheduled_actions(
        ServiceNamespace=model.ServiceNamespace,
        ResourceId=model.ResourceId,
        ScalableDimension=model.ScalableDimension,
        ScheduledActionNames=[model.ScheduledActionName],
        MaxResults=1,
    )
    if exists_query_r["ScheduledActions"]:
        return exists_query_r["ScheduledActions"][0]
    return None


def define_scalable_target_action(model) -> dict:
    action: dict = {
        "ScheduledActionName": model.ScheduledActionName,
        "ServiceNamespace": model.ServiceNamespace,
        "ResourceId": model.ResourceId,
        "ScalableDimension": model.ScalableDimension,
        "Schedule": model.Schedule,
    }
    target_action: dict = {}
    if model.ScalableTargetAction.MinCapacity:
        target_action["MinCapacity"] = int(model.ScalableTargetAction.MinCapacity)
    if model.ScalableTargetAction.MaxCapacity:
        target_action["MaxCapacity"] = int(model.ScalableTargetAction.MaxCapacity)
    try:
        if model.EndTime and isinstance(model.EndTime, str):
            action["EndTime"] = parser.parse(model.EndTime).isoformat()
    except ParserError as error:
        LOG.exception(error)
        LOG.error("EndTime")
    try:
        if model.StartTime and isinstance(model.StartTime, str):
            action["StartTime"] = parser.parse(model.StartTime).isoformat()
    except ParserError as error:
        LOG.exception(error)
    if model.Timezone:
        action["Timezone"] = model.Timezone
    action["ScalableTargetAction"] = target_action
    return action


def must_exist(
    session: SessionProxy, model, progress: ProgressEvent, context: str
) -> Union[ProgressEvent, None]:
    if not model:
        return None
    try:
        if not rule_exists(session, model):
            progress.status = OperationStatus.FAILED
            progress.errorCode = HandlerErrorCode.NotFound
            progress.message = (
                f"Scheduled Action {model.ScheduledActionName} not found for"
                f" {model.ServiceNamespace}|{model.ResourceId}"
            )
            return progress
    except Exception as error:
        LOG.error(f"{context} pre-validation error")
        LOG.exception(error)
        return ProgressEvent(
            status=OperationStatus.FAILED,
            errorCode=HandlerErrorCode.InternalFailure,
            message=f"{context} - Validation - {repr(error)}",
        )
    return None


@resource.handler(Action.CREATE)
def create_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    model = request.desiredResourceState
    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
        resourceModel=model,
    )
    application_autoscaling_client = session.client("application-autoscaling")
    try:
        if rule_exists(session, model):
            progress.status = OperationStatus.FAILED
            progress.errorCode = HandlerErrorCode.AlreadyExists
            progress.message = (
                f"Scheduled Action {model.ScheduledActionName} already exists for"
                f" {model.ServiceNamespace}|{model.ResourceId}"
            )
            return progress
    except Exception as error:
        LOG.error("pre-create validation error")
        LOG.exception(error)
        return ProgressEvent(
            status=OperationStatus.FAILED,
            errorCode=HandlerErrorCode.InternalFailure,
            message=f"Create - {repr(error)}",
        )
    try:
        kwargs = define_scalable_target_action(model)
        application_autoscaling_client.put_scheduled_action(**kwargs)
        resource_r = rule_exists(session, model)
        primary_identifier = resource_r["ScheduledActionARN"]
        model.ScheduledActionARN = primary_identifier
        progress.status = OperationStatus.SUCCESS
        progress.message = (
            "Successfully created Scheduled Action for"
            f" {model.ServiceNamespace}|{model.ResourceId}"
        )
        return progress
    except application_autoscaling_client.exceptions.ObjectNotFoundException:
        return ProgressEvent(
            status=OperationStatus.FAILED,
            errorCode=HandlerErrorCode.NotFound,
            message=(
                f"Scalable target {model.ServiceNamespace}|{model.ResourceId} not found"
            ),
        )
    except Exception as error:
        LOG.error("CREATE ERROR")
        LOG.exception(error)
        return ProgressEvent(
            status=OperationStatus.FAILED,
            errorCode=HandlerErrorCode.InternalFailure,
            message=f"Create error - {repr(error)}",
        )


@resource.handler(Action.UPDATE)
def update_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    model = request.desiredResourceState
    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
        resourceModel=model,
    )
    cannot_proceed = must_exist(session, model, progress, "Update")
    if cannot_proceed and isinstance(cannot_proceed, ProgressEvent):
        return cannot_proceed
    application_autoscaling_client = session.client("application-autoscaling")
    try:
        kwargs = define_scalable_target_action(model)
        application_autoscaling_client.put_scheduled_action(**kwargs)
        progress.status = OperationStatus.SUCCESS
        progress.message = f"Successfully updated {model.ScheduledActionName}"
        return progress
    except Exception as error:
        LOG.error("UPDATE ERROR")
        LOG.exception(error)
        return ProgressEvent(
            status=OperationStatus.FAILED,
            errorCode=HandlerErrorCode.InternalFailure,
            message=f"Update handler - {repr(error)}",
        )


@resource.handler(Action.DELETE)
def delete_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    model = request.desiredResourceState
    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
        resourceModel=None,
    )
    cannot_proceed = must_exist(session, model, progress, "Delete")
    if cannot_proceed and isinstance(cannot_proceed, ProgressEvent):
        return cannot_proceed
    application_autoscaling_client = session.client("application-autoscaling")
    try:
        application_autoscaling_client.delete_scheduled_action(
            ScheduledActionName=model.ScheduledActionName,
            ServiceNamespace=model.ServiceNamespace,
            ResourceId=model.ResourceId,
            ScalableDimension=model.ScalableDimension,
        )
        progress.status = OperationStatus.SUCCESS
        progress.message = "Successfully delete scheduled action"
        return progress
    except Exception as error:
        LOG.error("DELETE ERROR")
        LOG.exception(error)
        return ProgressEvent(
            status=OperationStatus.FAILED,
            errorCode=HandlerErrorCode.InternalFailure,
            message=f"Update handler - {repr(error)}",
        )


@resource.handler(Action.READ)
def read_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    model = request.desiredResourceState
    progress = ProgressEvent(status=OperationStatus.IN_PROGRESS, resourceModel=model)
    cannot_proceed = must_exist(session, model, progress, "Read")
    if cannot_proceed and isinstance(cannot_proceed, ProgressEvent):
        return cannot_proceed
    return ProgressEvent(
        status=OperationStatus.SUCCESS,
        resourceModel=model,
    )


@resource.handler(Action.LIST)
def list_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    return ProgressEvent(
        status=OperationStatus.SUCCESS,
        resourceModels=[],
    )
