"""Resources Handler """
import logging
import copy
from typing import Any, MutableMapping, Optional, Tuple, Sequence, Dict

from botocore.exceptions import ClientError
from cloudformation_cli_python_lib import (
    Action,
    HandlerErrorCode,
    OperationStatus,
    ProgressEvent,
    Resource,
    SessionProxy,
)

from .models import ResourceHandlerRequest, ResourceModel, _AttributeValue, _Key

# Use this logger to forward log messages to CloudWatch Logs.
LOG = logging.getLogger(__name__)
TYPE_NAME = "AwsCommunity::DynamoDB::Item"

resource = Resource(TYPE_NAME, ResourceModel)
test_entrypoint = resource.test_entrypoint


def _get_composite_key(keys: Sequence["_Key"]) -> str:
    # it can only be string, number, or binary
    composite_key = ""
    for key in keys:
        if composite_key:
            composite_key = f"{composite_key}-{key.AttributeValue}"
        else:
            composite_key = key.AttributeValue
    return composite_key


def _keys_to_dynamodb(keys: Sequence["_Key"]) -> Dict[str, Dict[str, Any]]:
    attributes = {}
    for key in keys:
        attributes[key.AttributeName] = {
            key.AttributeType: key.AttributeValue,
        }
    return attributes


def _build_condition(
    keys: Sequence["_Key"],
    item: MutableMapping[str, _AttributeValue],
    exists: bool,
) -> Tuple[str, MutableMapping[str, _AttributeValue]]:
    """Build a condition for validating if the record should or shouldn't exist.
    If we are doing a create it shouldn't exist.
    If we are doing an update/delete/read it should exist
    """
    attribute = "attribute_exists" if exists else "attribute_not_exists"

    condition = ""
    for key in keys:
        item[key.AttributeName] = {key.AttributeType: key.AttributeValue}
        if condition:
            condition = f"{condition} AND {attribute}({key.AttributeName})"
        else:
            condition = f"{attribute}({key.AttributeName})"
    return (condition, item)


@resource.handler(Action.CREATE)
def create_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    """Create Handler"""
    model = request.desiredResourceState
    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
        resourceModel=model,
    )

    try:
        if model is not None:
            # Item could be none if we are just adding a PK or PK&SK
            # We need to empty it out for API purposes
            item = copy.deepcopy(model.Item)
            if item is None:
                item = {}
            condition, item = _build_condition(model.Keys, item, False)
            if isinstance(session, SessionProxy):
                client = session.client("dynamodb")
                client.put_item(
                    TableName=model.TableName, Item=item, ConditionExpression=condition
                )
            progress.resourceModel.CompositeKey = _get_composite_key(model.Keys)
        # Setting Status to success will signal to cfn that the operation is complete
        progress.status = OperationStatus.SUCCESS
    except ClientError as err:
        if err.response["Error"]["Code"] == "ConditionalCheckFailedException":
            return ProgressEvent.failed(
                HandlerErrorCode.AlreadyExists, "item already exists"
            )
        return ProgressEvent.failed(
            HandlerErrorCode.InternalFailure, f"got error {err}"
        )
    except Exception as err:
        return ProgressEvent.failed(
            HandlerErrorCode.InternalFailure, f"got error {err}"
        )

    return read_handler(session, request, callback_context)


# pylint: disable=unused-argument
@resource.handler(Action.UPDATE)
def update_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    """Update Handler"""
    model = request.desiredResourceState
    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
        resourceModel=model,
    )
    try:
        if model is not None:
            item = copy.deepcopy(model.Item)
            # Item could be none if we are just adding a PK or PK&SK
            # We need to empty it out for API purposes
            if item is None:
                item = {}

            condition, item = _build_condition(model.Keys, item, True)
            if isinstance(session, SessionProxy):

                client = session.client("dynamodb")
                client.put_item(
                    TableName=model.TableName, Item=item, ConditionExpression=condition
                )
            progress.resourceModel.CompositeKey = _get_composite_key(model.Keys)
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
    """Delete Handler"""
    model = request.desiredResourceState
    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
        resourceModel=None,
    )
    try:
        if model is not None:
            if isinstance(session, SessionProxy):

                condition, _ = _build_condition(model.Keys, {}, True)
                client = session.client("dynamodb")
                keys = _keys_to_dynamodb(model.Keys)
                client.delete_item(
                    TableName=model.TableName,
                    Key=keys,
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
    """Read Handler"""
    model = request.desiredResourceState
    output_model: ResourceModel

    #pylint: disable=too-many-nested-blocks
    try:
        if model is not None:
            if isinstance(session, SessionProxy):
                client = session.client("dynamodb")
                get_keys = _keys_to_dynamodb(model.Keys)
                result = client.get_item(
                    TableName=model.TableName,
                    Key=get_keys,
                    ConsistentRead=True,
                )
                if result.get("Item", None) is not None:
                    keys: Sequence[_Key] = []
                    attributes = {}
                    for key in model.Keys:
                        keys.append(
                            _Key(
                                AttributeName=key.AttributeName,
                                AttributeType=key.AttributeType,
                                AttributeValue=result["Item"][key.AttributeName][
                                    key.AttributeType
                                ],
                            )
                        )
                    for attributeName in model.Item.keys():
                        for key in model.Keys:
                            if attributeName == key.AttributeName:
                                break
                        attributes[attributeName] = result["Item"][attributeName]
                    output_model = ResourceModel(
                        TableName=model.TableName,
                        Keys=keys,
                        Item=attributes,
                        CompositeKey=_get_composite_key(keys),
                    )
                    return ProgressEvent(
                        status=OperationStatus.SUCCESS,
                        resourceModel=output_model,
                    )

                return ProgressEvent.failed(
                    HandlerErrorCode.NotFound, "resource not found"
                )
    except ClientError as err:
        return ProgressEvent.failed(
            HandlerErrorCode.InternalFailure, f"got error {err}"
        )
    except Exception as err:
        return ProgressEvent.failed(
            HandlerErrorCode.InternalFailure, f"got error {err}"
        )

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
    """List Handler"""
    # TODO: put code here
    return ProgressEvent(
        status=OperationStatus.SUCCESS,
        resourceModels=[],
    )
