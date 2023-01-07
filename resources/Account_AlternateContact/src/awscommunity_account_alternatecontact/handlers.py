"""Main entrypoints."""
import logging
from typing import Any, MutableMapping, Optional
from cloudformation_cli_python_lib import (
    Action,
    OperationStatus,
    ProgressEvent,
    Resource,
    SessionProxy,
)
from cloudformation_cli_python_lib.exceptions import InternalFailure, InvalidRequest

from .actions import create, update, delete, get_identifier, read
from .constants import TYPE_NAME
from .models import ResourceHandlerRequest, ResourceModel

# Use this logger to forward log messages to CloudWatch Logs.
LOG = logging.getLogger(__name__)

resource = Resource(TYPE_NAME, ResourceModel)
test_entrypoint = resource.test_entrypoint


@resource.handler(Action.CREATE)
def create_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],  # pylint:disable=unused-argument
) -> ProgressEvent:
    """Create handler."""
    if not isinstance(session, SessionProxy):
        raise InternalFailure("Session is not a SessionProxy")

    model = request.desiredResourceState
    create(
        session, model, request.awsAccountId
    )  # api is different depending on the current aws account
    return ProgressEvent(
        status=OperationStatus.SUCCESS,
        resourceModel=model,
    )


@resource.handler(Action.UPDATE)
def update_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],  # pylint:disable=unused-argument
) -> ProgressEvent:
    """Update handler."""
    if not isinstance(session, SessionProxy):
        raise InternalFailure("Session is not a SessionProxy")

    if get_identifier(request.previousResourceState) != get_identifier(
        request.desiredResourceState
    ):
        raise InvalidRequest("Identifier changed between previous and desired state")

    # We can overwrite everything that is not the identifier, so we don't have
    # to look at the previous state
    model = request.desiredResourceState
    update(
        session, model, request.awsAccountId
    )  # api is different depending on the current aws account
    return ProgressEvent(
        status=OperationStatus.SUCCESS,
        resourceModel=model,
    )


@resource.handler(Action.DELETE)
def delete_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],  # pylint:disable=unused-argument
) -> ProgressEvent:
    """Delete handler."""
    if not isinstance(session, SessionProxy):
        raise InternalFailure("Session is not a SessionProxy")

    model = request.desiredResourceState
    delete(
        session, model, request.awsAccountId
    )  # api is different depending on the current aws account
    return ProgressEvent(
        status=OperationStatus.SUCCESS,
        resourceModel=None,
    )


@resource.handler(Action.READ)
def read_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],  # pylint:disable=unused-argument
) -> ProgressEvent:
    """Read handler."""
    if not isinstance(session, SessionProxy):
        raise InternalFailure("Session is not a SessionProxy")

    model = request.desiredResourceState
    model = read(
        session, model, request.awsAccountId
    )  # api is different depending on the current aws account
    return ProgressEvent(
        status=OperationStatus.SUCCESS,
        resourceModel=model,
    )
