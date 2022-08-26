"""
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
"""

from cfn_guard_rs_hook import __version__, GuardHook
import pytest
from cloudformation_cli_python_lib import (
    HookInvocationPoint,
    ProgressEvent,
    OperationStatus,
    HandlerErrorCode,
)

from .helpers import TypeConfigurationModel, create_request
from .fixtures import rules


def test_version():
    assert __version__ == "0.1.0"


@pytest.mark.parametrize(
    "TYPE_NAME,model,invocationPoint,expected",
    [
        (
            "Community::S3Bucket::Encryption",
            {
                "resourceProperties": {
                    "PublicAccessBlockConfiguration": {
                        "BlockPublicAcls": "true",
                        "BlockPublicPolicy": "true",
                        "IgnorePublicAcls": "true",
                        "RestrictPublicBuckets": "true",
                    }
                }
            },
            HookInvocationPoint.CREATE_PRE_PROVISION,
            ProgressEvent(
                status=OperationStatus.SUCCESS,
                errorCode=None,
                message="",
                result=None,
                callbackContext=None,
                callbackDelaySeconds=0,
                resourceModel=None,
                resourceModels=None,
                nextToken=None,
            ),
        ),
        (
            "Community::S3Bucket::Encryption",
            {
                "resourceProperties": {
                    "PublicAccessBlockConfiguration": {
                        "BlockPublicAcls": "false",
                        "BlockPublicPolicy": "true",
                        "IgnorePublicAcls": "true",
                        "RestrictPublicBuckets": "true",
                    }
                }
            },
            HookInvocationPoint.CREATE_PRE_PROVISION,
            ProgressEvent(
                status=OperationStatus.FAILED,
                errorCode=HandlerErrorCode.NonCompliant,
                message="Rule [S3_BUCKET_LEVEL_PUBLIC_ACCESS_PROHIBITED] failed on property [/Resources/Bucket/Properties/PublicAccessBlockConfiguration/BlockPublicAcls] failed comparison operator [Eq] and not exists of [False].",
                result=None,
                callbackContext=None,
                callbackDelaySeconds=0,
                resourceModel=None,
                resourceModels=None,
                nextToken=None,
            ),
        ),
    ],
)
def test_transactions(TYPE_NAME, model, invocationPoint, expected):
    req = create_request(invocationPoint, model)
    hook = GuardHook(TYPE_NAME, TypeConfigurationModel, rules)

    result = hook._invoke_handler(
        session=None,
        request=req,
        invocation_point=invocationPoint,
        callback_context={},
        type_configuration=TypeConfigurationModel(),
    )

    assert result == expected
