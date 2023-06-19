"""
This stack deploys a compliance check lambda function that
is called by the AwsCommunity::Lambda::Invoker hook
"""
from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
from constructs import Construct
from .compliance_construct import ComplianceConstruct 

class CdkStack(Stack):
    "Sample stack"

    def __init__(self, scope: Construct, construct_id: str, 
                 table_name, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create instances of ComplianceConstruct to validate stack operations
        code = """
import boto3
def handler(event, context):
    print(event)
    if event["type_name"] != "AWS::S3::Bucket":
        return
    if event["operation"] not in ["create", "update"]:
        return
    if "BucketEncryption" not in event["resource_properties"]:
        raise Exception("Expected BucketEncryption")
"""
        ComplianceConstruct(self, "check1", table_name, code)

