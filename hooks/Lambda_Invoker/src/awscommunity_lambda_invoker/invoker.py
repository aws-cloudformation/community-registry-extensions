"Implementation for the Lambda function invoker"

import json
import logging
import boto3


def invoke_lambdas(ddb, lam, target, logger, table_name):
    "Read the lambda arns from the Dynamo table and invoke them"

    # Query the DDB table for all Lambda Arns
    lambda_arns = []
    resp = ddb.scan(TableName=table_name)
    items = resp["Items"]
    for item in items:
        lambda_arns.append(item["pk"]["S"])

    # Invoke each Lambda Arn and send in the resource properties
    logger.debug(target_json)
    errs = []
    for arn in lambda_arns:
        try:
            lam.invoke(
                FunctionName=arn.split(":function:")[1], Payload={"target": target_json}
            )
        except Exception as lamex:
            errs.append(str(lamex))


if __name__ == "__main__":
    # Integ test

    ddb = boto3.client("dynamodb")
    lam = boto3.client("lambda")
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    targets = json.load("inputs/inputs_1_pre_create.json")
    target = targets["AWS::S3::AccessPoint"]
    errs = invoke_lambdas(ddb, lam, target, logger, os.environ["DDB_TABLE_NAME"])
    if errs:
        for err in errs:
            print(err)
    else:
        print("Success")
