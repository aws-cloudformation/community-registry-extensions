"Implementation for the Lambda function invoker"

import json
import logging
import os
import boto3


def invoke_lambdas(ddb, lam, target, logger, table_name):
    """
    Read the lambda arns from the Dynamo table and invoke them all.
    Returns an array of error messages from the lambdas called.
    """
    # Query the DDB table for all Lambda Arns
    lambda_arns = []
    resp = ddb.scan(TableName=table_name)
    items = resp["Items"]
    for item in items:
        lambda_arn = item["pk"]["S"]
        logger.debug(lambda_arn)
        lambda_arns.append(lambda_arn)

    logger.debug("Found %s lambda arns", len(lambda_arns))

    # Invoke each Lambda Arn and send in the resource properties
    logger.debug(target)
    errs = []
    for arn in lambda_arns:
        try:
            lam.invoke(
                FunctionName=arn.split(":function:")[1],
                Payload=json.dumps(target),
            )
        except Exception as lamex:
            errs.append(str(lamex))
    return errs


def main():
    "Main, used for integ testing"
    ddb = boto3.client("dynamodb")
    lam = boto3.client("lambda")
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logging.basicConfig()
    logger.debug("Logger initialized")
    targets = {}
    with open("../../inputs/inputs_1_pre_create.json", "r", encoding="UTF-8") as f:
        targets = json.load(f)
    name = "AWS::S3::AccessPoint"
    target_props = targets[name]["resourceProperties"]
    target = {
        "resource_name": name,
        "resource_properties": target_props
    }
    errs = invoke_lambdas(ddb, lam, target, logger, os.environ["DDB_TABLE_NAME"])
    if errs:
        for err in errs:
            print(err)
    else:
        print("Success")


if __name__ == "__main__":
    main()
