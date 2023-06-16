"""
This AWS Lambda-backed custom resource is used from setup.yaml 
to register a sample Lambda function.
"""

#pylint:disable=W0613
import boto3
from crhelper import CfnResource

helper = CfnResource()

@helper.create
@helper.update
def create_reg(event, context):
    "Create the registration entry in the table"
    print("create_reg called")
    print(event)
    props = event["ResourceProperties"]
    table_arn = props["RegistrationTableArn"]
    print("table_arn", table_arn)
    function_arn = props["FunctionArn"]
    print("function_arn", function_arn)
    table_name = table_arn.split(":table/")[1]
    print("table_name", table_name)
    ddb = boto3.client("dynamodb")
    ddb.put_item(TableName=table_name, 
                 Item={
                     "lambda_arn": {"S": function_arn}
                 })
    print(f"Put {function_arn} into {table_name}")


@helper.delete
def delete_reg(event, context):
    "Delete the registration entry from the table"
    print("delete_reg called")
    print(event)
    props = event["ResourceProperties"]
    table_arn = props["RegistrationTableArn"]
    print("table_arn", table_arn)
    function_arn = props["FunctionArn"]
    print("function_arn", function_arn)
    table_name = table_arn.split(":table/")[1]
    print("table_name", table_name)
    ddb = boto3.client("dynamodb")
    ddb.delete_item(TableName=table_name, 
                 Key={
                     "lambda_arn": {"S": function_arn}
                 })

def handler(event, context):
    "Handle the invocation from the CloudFormation custom resource"
    helper(event, context)



