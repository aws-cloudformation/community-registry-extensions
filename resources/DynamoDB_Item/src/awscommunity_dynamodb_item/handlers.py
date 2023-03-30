"""Resources Handler """
import logging
from typing import Any, MutableMapping, Optional, Tuple

from botocore.exceptions import ClientError
from cloudformation_cli_python_lib import (Action, HandlerErrorCode,
                                           OperationStatus, ProgressEvent,
                                           Resource, SessionProxy)

from .models import ResourceHandlerRequest, ResourceModel, _AttributeValue

# Use this logger to forward log messages to CloudWatch Logs.
LOG = logging.getLogger(__name__)
TYPE_NAME = "AwsCommunity::DynamoDB::Item"

resource = Resource(TYPE_NAME, ResourceModel)
test_entrypoint = resource.test_entrypoint


def _build_condition(
    key: Optional[MutableMapping[str, _AttributeValue]],
    item: MutableMapping[str, _AttributeValue],
    exists: bool,
) -> Tuple[str, MutableMapping[str, _AttributeValue]]:
    """Build a condition for validating if the record should or shouldn't exist.
    If we are doing a create it shouldn't exist.
    If we are doing an update/delete/read it should exist
    """
    attribute = "attribute_exists" if exists else "attribute_not_exists"

    condition = ""
    if key is not None:
        for k, v in key.items():
            item[k] = v
            if condition != "":
                condition = f"{condition} AND {attribute}({k})"
            else:
                condition = f"{attribute}({k})"
    return (condition, item)


@resource.handler(Action.CREATE)
def create_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    """Create Handler """
    model = request.desiredResourceState
    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
        resourceModel=model,
    )

    try:
        if model is not None:
            # Item could be none if we are just adding a PK or PK&SK
            # We need to empty it out for API purposes
            item = model.Item
            if item is None:
                item = {}
            condition, item = _build_condition(model.Key, item, False)
            if isinstance(session, SessionProxy):
                client = session.client("dynamodb")
                client.put_item(
                    TableName=model.TableName, Item=item, ConditionExpression=condition
                )
        # Setting Status to success will signal to cfn that the operation is complete
        progress.status = OperationStatus.SUCCESS
    except ClientError as err:
        if err.response["Error"]["Code"] == "ConditionalCheckFailedException":
            return ProgressEvent.failed(
                HandlerErrorCode.AlreadyExists, "item already exists"
            )
        return ProgressEvent.failed(HandlerErrorCode.InternalFailure, f"got error {err}")
    except Exception as err:
        return ProgressEvent.failed(HandlerErrorCode.InternalFailure, f"got error {err}")

    return read_handler(session, request, callback_context)


# pylint: disable=unused-argument
@resource.handler(Action.UPDATE)
def update_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    """Update Handler """
    model = request.desiredResourceState
    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
        resourceModel=model,
    )
    try:
        if model is not None:
            item = model.Item
            # Item could be none if we are just adding a PK or PK&SK
            # We need to empty it out for API purposes
            if item is None:
                item = {}

            condition, item = _build_condition(model.Key, item, True)
            if isinstance(session, SessionProxy):

                client = session.client("dynamodb")
                client.put_item(
                    TableName=model.TableName, Item=item, ConditionExpression=condition
                )
        # Setting Status to success will signal to cfn that the operation is complete
        progress.status = OperationStatus.SUCCESS
    except ClientError as e:
        if e.response["Error"]["Code"] == "ConditionalCheckFailedException":
            return ProgressEvent.failed(
                HandlerErrorCode.NotFound, "item does not exist"
            )
        return ProgressEvent.failed(HandlerErrorCode.InternalFailure, f"got error {e}")
    except Exception as e:
        return ProgressEvent.failed(HandlerErrorCode.InternalFailure, f"got error {e}")

    return read_handler(session, request, callback_context)


# pylint: disable=unused-argument
@resource.handler(Action.DELETE)
def delete_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    """Delete Handler """
    model = request.desiredResourceState
    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
        resourceModel=None,
    )
    try:
        if model is not None:
            if isinstance(session, SessionProxy):

                condition, _ = _build_condition(model.Key, {}, True)
                client = session.client("dynamodb")
                client.delete_item(
                    TableName=model.TableName,
                    Key=model.Key,
                    ConditionExpression=condition,
                )
        # Setting Status to success will signal to cfn that the operation is complete
        progress.status = OperationStatus.SUCCESS
    except ClientError as e:
        if e.response["Error"]["Code"] == "ConditionalCheckFailedException":
            return ProgressEvent.failed(
                HandlerErrorCode.NotFound, "item does not exist"
            )
        return ProgressEvent.failed(HandlerErrorCode.InternalFailure, f"got error {e}")
    except Exception as e:
        return ProgressEvent.failed(HandlerErrorCode.InternalFailure, f"got error {e}")

    return progress


# pylint: disable=unused-argument
@resource.handler(Action.READ)
def read_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    """Read Handler """
    model = request.desiredResourceState
    output_model: ResourceModel

    try:
        if model is not None:
            if isinstance(session, SessionProxy):
                client = session.client("dynamodb")
                result = client.get_item(
                    TableName=model.TableName,
                    Key=model.Key,
                    ConsistentRead=True,
                )
                if result.get("Item", None) is not None:
                    keys = {}
                    attributes = {}
                    for key in model.Key.keys():
                        keys[key] = result["Item"][key]
                    for key in model.Item.keys():
                        attributes[key] = result["Item"][key]
                    output_model = ResourceModel(
                        TableName=model.TableName, Key=keys, Item=attributes
                    )
                    return ProgressEvent(
                        status=OperationStatus.SUCCESS,
                        resourceModel=output_model,
                    )

                return ProgressEvent.failed(
                    HandlerErrorCode.NotFound, "resource not found"
                )
    except ClientError as err:
        return ProgressEvent.failed(HandlerErrorCode.InternalFailure, f"got error {err}")
    except Exception as err:
        return ProgressEvent.failed(HandlerErrorCode.InternalFailure, f"got error {err}")

    return ProgressEvent(
        status=OperationStatus.SUCCESS,
        resourceModel=output_model,
    )


# pylint: disable=unused-argument
@resource.handler(Action.LIST)
def list_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    """List Handler """
    # TODO: put code here
    return ProgressEvent(
        status=OperationStatus.SUCCESS,
        resourceModels=[],
    )
