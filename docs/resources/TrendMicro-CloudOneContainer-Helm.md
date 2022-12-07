
## TrendMicro::CloudOneContainer::Helm

## Deploys Trend Micro Cloud One Container Security into EKS clusters using helm.

- [Source](https:&#x2F;&#x2F;github.com&#x2F;aws-quickstart&#x2F;quickstart-trend-micro-cloudone-helm-resource-provider.git) 
- [Documentation]()

Published by aws-quickstart

## Schema
{% highlight json %}
{
    "typeName": "TrendMicro::CloudOneContainer::Helm",
    "description": "Deploys Trend Micro Cloud One Container Security into EKS clusters using helm.",
    "sourceUrl": "https://github.com/aws-quickstart/quickstart-trend-micro-cloudone-helm-resource-provider.git",
    "documentationUrl": "https://github.com/trendmicro/cloudone-container-security-helm/blob/master/README.md",
    "definitions": {
        "Arn": {
            "type": "string",
            "pattern": "^arn:aws(-(cn|us-gov))?:[a-z-]+:(([a-z]+-)+[0-9])?:([0-9]{12})?:[^.]+$"
        }
    },
    "properties": {
        "ClusterID": {
            "description": "EKS cluster name",
            "type": "string"
        },
        "KubeConfig": {
            "description": "Secrets Manager ARN for kubeconfig file",
            "$ref": "#/definitions/Arn"
        },
        "RoleArn": {
            "description": "IAM to use with EKS cluster authentication, if not resource execution role will be used",
            "$ref": "#/definitions/Arn"
        },
        "Chart": {
            "description": "Chart name",
            "type": "string"
        },
        "Namespace": {
            "description": "Namespace to use with helm. Created if doesn't exist and default will be used if not provided",
            "type": "string"
        },
        "Name": {
            "description": "Name for the helm release",
            "type": "string"
        },
        "Values": {
            "description": "Values to provide to the helm chart, note that an API key is required. For supported values and documentation see: https://github.com/trendmicro/cloudone-container-security-helm/blob/master/values.yaml",
            "type": "object",
            "additionalProperties": false,
            "patternProperties": {
                "^.+$": {
                    "type": "string"
                }
            }
        },
        "ValueYaml": {
            "description": "String representation of a values.yaml file",
            "type": "string"
        },
        "Version": {
            "description": "Version can be specified, if not latest will be used",
            "type": "string"
        },
        "ValueOverrideURL": {
            "description": "Custom Value Yaml file can optionally be specified",
            "type": "string",
            "pattern": "^[sS]3://[0-9a-zA-Z]([-.\\w]*[0-9a-zA-Z])(:[0-9]*)*([?/#].*)?$"
        },
        "ID": {
            "description": "Primary identifier for Cloudformation",
            "type": "string"
        },
        "TimeOut": {
            "description": "Timeout for resource provider. Default 60 mins",
            "type": "integer"
        },
        "VPCConfiguration": {
            "type": "object",
            "description": "For network connectivity to Cluster inside VPC",
            "additionalProperties": false,
            "properties": {
                "SecurityGroupIds": {
                    "description": "Specify one or more security groups",
                    "type": "array",
                    "items": {
                        "type": "string"
                    }
                },
                "SubnetIds": {
                    "description": "Specify one or more subnets",
                    "type": "array",
                    "items": {
                        "type": "string"
                    }
                }
            }
        }
    },
    "additionalProperties": false,
    "readOnlyProperties": [
        "/properties/Resources",
        "/properties/ID"
    ],
    "primaryIdentifier": [
        "/properties/ID"
    ],
    "createOnlyProperties": [
        "/properties/Name",
        "/properties/Namespace",
        "/properties/ClusterID"
    ],
    "handlers": {
        "create": {
            "permissions": [
                "secretsmanager:GetSecretValue",
                "kms:Decrypt",
                "eks:DescribeCluster",
                "s3:GetObject",
                "sts:AssumeRole",
                "iam:PassRole",
                "ec2:CreateNetworkInterface",
                "ec2:DescribeNetworkInterfaces",
                "ec2:DeleteNetworkInterface",
                "ec2:DescribeVpcs",
                "ec2:DescribeSubnets",
                "ec2:DescribeRouteTables",
                "ec2:DescribeSecurityGroups",
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents",
                "lambda:UpdateFunctionConfiguration",
                "lambda:DeleteFunction",
                "lambda:GetFunction",
                "lambda:InvokeFunction",
                "lambda:CreateFunction",
                "lambda:UpdateFunctionCode"
            ]
        },
        "read": {
            "permissions": [
                "secretsmanager:GetSecretValue",
                "kms:Decrypt",
                "eks:DescribeCluster",
                "s3:GetObject",
                "sts:AssumeRole",
                "iam:PassRole",
                "ec2:CreateNetworkInterface",
                "ec2:DescribeNetworkInterfaces",
                "ec2:DeleteNetworkInterface",
                "ec2:DescribeVpcs",
                "ec2:DescribeSubnets",
                "ec2:DescribeRouteTables",
                "ec2:DescribeSecurityGroups",
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents",
                "lambda:UpdateFunctionConfiguration",
                "lambda:DeleteFunction",
                "lambda:GetFunction",
                "lambda:InvokeFunction",
                "lambda:CreateFunction",
                "lambda:UpdateFunctionCode"
            ]
        },
        "update": {
            "permissions": [
                "secretsmanager:GetSecretValue",
                "kms:Decrypt",
                "eks:DescribeCluster",
                "s3:GetObject",
                "sts:AssumeRole",
                "iam:PassRole",
                "ec2:CreateNetworkInterface",
                "ec2:DescribeNetworkInterfaces",
                "ec2:DeleteNetworkInterface",
                "ec2:DescribeVpcs",
                "ec2:DescribeSubnets",
                "ec2:DescribeRouteTables",
                "ec2:DescribeSecurityGroups",
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents",
                "lambda:UpdateFunctionConfiguration",
                "lambda:DeleteFunction",
                "lambda:GetFunction",
                "lambda:InvokeFunction",
                "lambda:CreateFunction",
                "lambda:UpdateFunctionCode"
            ]
        },
        "delete": {
            "permissions": [
                "secretsmanager:GetSecretValue",
                "kms:Decrypt",
                "eks:DescribeCluster",
                "s3:GetObject",
                "sts:AssumeRole",
                "iam:PassRole",
                "ec2:CreateNetworkInterface",
                "ec2:DescribeNetworkInterfaces",
                "ec2:DeleteNetworkInterface",
                "ec2:DescribeVpcs",
                "ec2:DescribeSubnets",
                "ec2:DescribeRouteTables",
                "ec2:DescribeSecurityGroups",
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents",
                "lambda:UpdateFunctionConfiguration",
                "lambda:DeleteFunction",
                "lambda:GetFunction",
                "lambda:InvokeFunction",
                "lambda:CreateFunction",
                "lambda:UpdateFunctionCode"
            ]
        }
    }
}
{% endhighlight %}
