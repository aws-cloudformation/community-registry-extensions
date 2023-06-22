#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk.cdk_stack import CdkStack


app = cdk.App()

#TODO - Replace with the name of the table you created separately
table_name = "cep-lambda-invoker-reg-alpha-us-east-1-755952356119"

CdkStack(app, "CdkStack",
    env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),
    table_name=table_name
    )

app.synth()
