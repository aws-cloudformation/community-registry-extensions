"Compliance Construct"
from aws_cdk import aws_lambda as lambda_

from constructs import Construct
from .awscommunity_dynamodb_item import CfnItem

class ComplianceConstruct(Construct):
    """
    This construct creates a Lambda function to validate stack operations
    and also registers the ARN of that function into the DynamoDB table 
    that you created separately. You must also have activated or 
    privately registered the AwsCommunity::DynamoDB::Item extension 
    from the public registry.
    """

    def __init__(self, scope, construct_id, table_name, code, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        # Create a Lambda function to validate resources
        func = lambda_.Function(self, 
            'compliance-func',
            runtime=lambda_.Runtime.PYTHON_3_8,
            code=lambda_.Code.from_inline(code),
            handler='index.handler', 
            )
        
        # Enter the ARN of the function into the registration table
        CfnItem(scope=self, 
            id='compliance-item', 
            keys=[
                {
                    "attributeName": "lambda_arn",
                    "attributeType": "S",
                    "attributeValue": func.function_arn
                }], 
            table_name=table_name, 
            item={
                "lambda_arn": {
                    "S": func.function_arn
                }})



