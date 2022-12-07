
## AWSQS::Kubernetes::Get

## Fetches data from a kubernetes cluster using jsonpath expressions.

- [Source](https:&#x2F;&#x2F;github.com&#x2F;aws-quickstart&#x2F;quickstart-amazon-eks.git) 
- [Documentation]()

Published by aws-quickstart

## Schema
{% highlight json %}
{
    "typeName": "AWSQS::Kubernetes::Get",
    "description": "Fetches data from a kubernetes cluster using jsonpath expressions.",
    "sourceUrl": "https://github.com/aws-quickstart/quickstart-amazon-eks.git",
    "documentationUrl": "https://github.com/aws-quickstart/quickstart-kubernetes-resource-provider/blob/main/README.md",
    "properties": {
        "ClusterName": {
            "description": "Name of the EKS cluster to query",
            "type": "string"
        },
        "Name": {
            "description": "Name of the kubernetes resource to query, should contain kind. Eg.: pod/nginx",
            "type": "string"
        },
        "Namespace": {
            "description": "Kubernetes namespace containing the resource",
            "type": "string"
        },
        "JsonPath": {
            "description": "Jsonpath expression to filter the output",
            "type": "string"
        },
        "Response": {
            "description": "query response",
            "type": "string"
        },
        "Id": {
            "description": "Response from the kubernetes api represented as a string, will be a hash representation if the response is > 1000 characters.",
            "type": "string"
        },
        "Retries": {
            "description": "How many times to retry a request. This provides a mechanism to wait for resources to be created before proceeding. Interval between retries is 60 seconds.",
            "type": "integer"
        }
    },
    "additionalProperties": false,
    "required": [
        "ClusterName",
        "Namespace",
        "Name",
        "JsonPath"
    ],
    "readOnlyProperties": [
        "/properties/Response",
        "/properties/Id"
    ],
    "createOnlyProperties": [
        "/properties/ClusterName",
        "/properties/Namespace",
        "/properties/Name",
        "/properties/JsonPath"
    ],
    "primaryIdentifier": [
        "/properties/Id"
    ],
    "handlers": {
        "create": {
            "permissions": [
                "ssm:GetParameter",
                "ssm:PutParameter",
                "eks:DescribeCluster",
                "ec2:DescribeSubnets",
                "ec2:DescribeSecurityGroups",
                "ec2:DescribeVpcs",
                "ec2:CreateNetworkInterface",
                "ec2:DeleteNetworkInterface",
                "sts:GetCallerIdentity",
                "s3:GetObject",
                "lambda:CreateFunction",
                "lambda:UpdateFunctionConfiguration",
                "lambda:UpdateFunctionCode",
                "lambda:InvokeFunction",
                "iam:PassRole"
            ]
        },
        "read": {
            "permissions": [
                "ssm:GetParameter",
                "ssm:PutParameter",
                "eks:DescribeCluster",
                "ec2:DescribeSubnets",
                "ec2:DescribeSecurityGroups",
                "ec2:DescribeVpcs",
                "ec2:CreateNetworkInterface",
                "ec2:DeleteNetworkInterface",
                "sts:GetCallerIdentity",
                "s3:GetObject",
                "lambda:CreateFunction",
                "lambda:UpdateFunctionConfiguration",
                "lambda:UpdateFunctionCode",
                "lambda:InvokeFunction",
                "iam:PassRole"
            ]
        },
        "delete": {
            "permissions": [
                "ssm:GetParameter",
                "ssm:DeleteParameter",
                "eks:DescribeCluster",
                "ec2:DescribeSubnets",
                "ec2:DescribeSecurityGroups",
                "ec2:DescribeVpcs",
                "ec2:CreateNetworkInterface",
                "ec2:DeleteNetworkInterface",
                "sts:GetCallerIdentity",
                "s3:GetObject",
                "lambda:CreateFunction",
                "lambda:UpdateFunctionConfiguration",
                "lambda:UpdateFunctionCode",
                "lambda:InvokeFunction",
                "iam:PassRole"
            ]
        }
    }
}
{% endhighlight %}
