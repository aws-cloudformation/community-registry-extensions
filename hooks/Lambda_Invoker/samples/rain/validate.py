"""
This module is a 'shift left' effort to allow a developer to directly invoke
the compliance lambda functions, to make sure their code is valid before 
trying an actual CloudFormation deployment. It scans the registration table 
to get the list of Lambda function ARNs, decomposes the template into 
resources, and submits each of them separately, to mimic the behavior of 
CloudFormation when it invokes the hook.

This is one of the main reasons for this solution to exist, since CloudFormation 
hooks do not have an API that can be called to validate templates. By delegating 
the hook logic out to Lambda functions, we can now call them from anywhere.

One shortcoming of this technique is that we can't know all of the runtime 
values for functions like GetAtt, for example if you GetAtt a resource Arn, we
won't know the arn yet, and if your compliance lambda validates a specific arn, 
this script will give a false negative.

"""

import json
import sys
import yaml
import boto3


def main(args):
    """
    args[0]: path to the template
    args[1]: Arn of the registration table
    """

    template_path = args[0]
    table_arn = args[1]
    table_name = table_arn.split(":table/")[1]

    # Scan the DDB table to get the Lambda Arns
    ddb = boto3.client("dynamodb")
    lambda_arns = []
    resp = ddb.scan(TableName=table_name)
    items = resp["Items"]
    for item in items:
        lambda_arn = item["lambda_arn"]["S"]
        print(lambda_arn)
        lambda_arns.append(lambda_arn)

    if len(lambda_arns) == 0:
        print("No lambda arns found in the table")
        return

    # TODO - Parse the template and create inputs for the functions
    targets = []
    with open(template_path, "r", encoding="utf8") as t:
        y = yaml.safe_load(t)
        print(y)
        resources = y["Resources"]
        for logical_id in resources:
            r = resources[logical_id]
            props = {}
            if "Properties" in r:
                props = r["Properties"]
            targets.append({
                "type_name": r["Type"],
                "resource_properties": props,
                "operation": "create"
                })

    # Invoke each function and print out any errors found
    errs = []
    # Invoke each Lambda Arn and send in the resource properties
    lam = boto3.client("lambda")
    for target in targets:
        print("Checking target:", target)
        for arn in lambda_arns:
            function_name = arn.split(":function:")[1]
            print("Invoking lambda:", function_name)
            resp = lam.invoke(
                FunctionName=function_name,
                Payload=json.dumps(target),
            )
            # The invoke function returns 200 if the code raises an exception
            if "FunctionError" in resp and resp["FunctionError"]:
                payload = resp["Payload"]
                j = json.loads(payload.read().decode("utf-8"))
                errs.append(j["errorMessage"])

    if errs:
        print("Template failed validation checks")
        for err in errs:
            print(err)
        sys.exit(1)
    else:
        print("All validation checks passed")


if __name__ == "__main__":
    main(sys.argv[1:])
