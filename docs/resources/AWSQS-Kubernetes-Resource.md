
## AWSQS::Kubernetes::Resource

## Applys a YAML manifest to the specified Kubernetes cluster

- [Source](https:&#x2F;&#x2F;github.com&#x2F;aws-quickstart&#x2F;quickstart-amazon-eks.git) 
- [Documentation]()

Published by aws-quickstart

## Schema
{% highlight json %}
{
    "typeName": "AWSQS::Kubernetes::Resource",
    "description": "Applys a YAML manifest to the specified Kubernetes cluster",
    "sourceUrl": "https://github.com/aws-quickstart/quickstart-amazon-eks.git",
    "documentationUrl": "https://github.com/aws-quickstart/quickstart-kubernetes-resource-provider/blob/main/README.md",
    "properties": {
        "ClusterName": {
            "description": "Name of the EKS cluster",
            "type": "string"
        },
        "Namespace": {
            "description": "Kubernetes namespace",
            "type": "string"
        },
        "Manifest": {
            "description": "Text representation of the kubernetes yaml manifests to apply to the cluster.",
            "type": "string"
        },
        "Url": {
            "type": "string",
            "description": "Url to the kubernetes yaml manifests to apply to the cluster. Urls starting with s3:// will be fetched using an authenticated S3 read."
        },
        "Name": {
            "type": "string",
            "description": "Name of the resource."
        },
        "ResourceVersion": {
            "type": "string",
            "description": "Resource version."
        },
        "SelfLink": {
            "type": "string",
            "description": "Link returned by the kubernetes api. Deprecated and removed in kubernetes 1.20+"
        },
        "Uid": {
            "type": "string",
            "description": "Resource unique ID."
        },
        "CfnId": {
            "type": "string",
            "description": "CloudFormation Physical ID."
        }
    },
    "additionalProperties": false,
    "required": [
        "ClusterName"
    ],
    "readOnlyProperties": [
        "/properties/Name",
        "/properties/ResourceVersion",
        "/properties/SelfLink",
        "/properties/Uid",
        "/properties/CfnId"
    ],
    "createOnlyProperties": [
        "/properties/Namespace",
        "/properties/ClusterName"
    ],
    "primaryIdentifier": [
        "/properties/ClusterName",
        "/properties/CfnId"
    ],
    "handlers": {
        "create": {
            "permissions": [
                "ssm:GetParameter",
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
                "eks:DescribeCluster",
                "ec2:DescribeSubnets",
                "ec2:DescribeVpcs",
                "ec2:DescribeSecurityGroups",
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
        "update": {
            "permissions": [
                "ssm:GetParameter",
                "eks:DescribeCluster",
                "ec2:DescribeSubnets",
                "ec2:DescribeSecurityGroups",
                "ec2:DescribeVpcs",
                "ec2:CreateNetworkInterface",
                "ec2:DeleteNetworkInterface",
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
                "eks:DescribeCluster",
                "ec2:DescribeSecurityGroups",
                "ec2:DescribeSubnets",
                "ec2:DescribeVpcs",
                "ec2:CreateNetworkInterface",
                "ec2:DeleteNetworkInterface",
                "sts:GetCallerIdentity",
                "s3:GetObject",
                "lambda:CreateFunction",
                "lambda:UpdateFunctionConfiguration",
                "lambda:UpdateFunctionCode",
                "lambda:InvokeFunction",
                "lambda:DeleteFunction",
                "iam:PassRole"
            ]
        }
    }
}
{% endhighlight %}
