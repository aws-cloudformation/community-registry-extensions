"""
    Test cfn_guard_rs_hook
"""
import pytest
from cloudformation_cli_python_lib import (
    HookInvocationPoint,
    ProgressEvent,
    OperationStatus,
    HandlerErrorCode,
)
from cfn_guard_rs_hook import __version__, GuardHook


from .helpers import TypeConfigurationModel, create_request
from .fixtures import rules


def test_version():
    """
    Test version value
    """
    assert __version__ == "0.1.0"


@pytest.mark.parametrize(
    "type_name,model,invocation_point,expected",
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
                message="Rule [S3_BUCKET_LEVEL_PUBLIC_ACCESS_PROHIBITED] failed on "
                "property [/Resources/Bucket/Properties/"
                "PublicAccessBlockConfiguration/BlockPublicAcls"
                "] failed comparison operator [Eq] and not exists of [False].",
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
def test_transactions(type_name, model, invocation_point, expected):
    """
    Test a hook call
    """
    req = create_request(invocation_point, model)
    hook = GuardHook(type_name, TypeConfigurationModel, rules)

    # pylint: disable=protected-access
    result = hook._invoke_handler(
        session=None,
        request=req,
        invocation_point=invocation_point,
        callback_context={},
        type_configuration=TypeConfigurationModel(),
    )
    assert result == expected
