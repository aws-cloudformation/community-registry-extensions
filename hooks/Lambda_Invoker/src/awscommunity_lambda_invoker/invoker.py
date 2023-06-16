"Implementation for the Lambda function invoker"

import json
import logging
import os
import boto3


def invoke_lambdas(ddb, lam, target, logger, table_name):
    """
    Read Lambda function ARNs from the DynamoDB table and invoke them all.
    Returns an array of error messages from the lambdas called.
    """
    # Query the DDB table for all Lambda Arns
    lambda_arns = []
    logger.debug("About to scan %s", table_name)
    resp = ddb.scan(TableName=table_name)
    items = resp["Items"]
    for item in items:
        lambda_arn = item["lambda_arn"]["S"]
        logger.debug(lambda_arn)
        lambda_arns.append(lambda_arn)

    logger.debug("Found %s lambda arns", len(lambda_arns))

    logger.debug(target)
    errs = []
    # Invoke each Lambda Arn and send in the resource properties
    for arn in lambda_arns:
        try:
            resp = lam.invoke(
                FunctionName=arn.split(":function:")[1],
                Payload=json.dumps(target),
            )
            logger.debug(resp)
            # The invoke function returns 200 if the code raises an exception
            if "FunctionError" in resp and resp["FunctionError"]:
                payload = resp["Payload"]
                j = json.loads(payload.read().decode("utf-8"))
                logger.debug(j)
                errs.append(j["errorMessage"])
        except Exception as lamex:
            # This indicates a system error, not a compliance check error
            logger.debug("Caught lamex: %s", str(lamex))
            errs.append(str(lamex))

    logger.debug("About to return errs: %s", errs)
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
    print("About to test ", name)
    target_props = targets[name]["resourceProperties"]
    target = {
        "type_name": name,
        "resource_properties": target_props
    }
    errs = invoke_lambdas(ddb, lam, target, logger, os.environ["DDB_TABLE_NAME"])
    if errs:
        for err in errs:
            print(err)
    else:
        print("Success for type:", name)

    print("About to test failure case")
    target = {
        "type_name": "TEST::TEST::FAIL",
        "resource_properties": {}
    }
    errs = invoke_lambdas(ddb, lam, target, logger, os.environ["DDB_TABLE_NAME"])
    if errs:
        for err in errs:
            print(err)
    else:
        print("Success for FAIL case")


if __name__ == "__main__":
    main()
