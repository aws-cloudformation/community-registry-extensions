"This custom resource lambda is used from setup.yaml to register a sample Lambda"

import boto3
from crhelper import CfnResource

helper = CfnResource()

@helper.create
@helper.update
def create_reg(event, _):
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
                     "pk": {"S": function_arn}, 
                     "sk": {"S": "001"}
                 })
    print(f"Put {function_arn} into {table_name}")


@helper.delete
def delete_reg(_, __):
    "Delete the registration entry from the table"
    print("delete_reg called")

def handler(event, context):
    "Handle the invocation from the CloudFormation custom resource"
    helper(event, context)



