
## AWSQS::Kubernetes::Helm

A resource provider for managing helm. Version: 1.2.1

- [Source](https:&#x2F;&#x2F;github.com&#x2F;aws-quickstart&#x2F;quickstart-helm-resource-provider.git) 
- [Documentation]()

Published by aws-quickstart

## Schema
{% highlight json %}
{
    "typeName": "AWSQS::Kubernetes::Helm",
    "description": "A resource provider for managing helm. Version: 1.2.1",
    "sourceUrl": "https://github.com/aws-quickstart/quickstart-helm-resource-provider.git",
    "documentationUrl": "https://github.com/aws-quickstart/quickstart-helm-resource-provider/blob/main/README.md",
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
        "Repository": {
            "description": "Repository url. Defaults to kubernetes-charts.storage.googleapis.com",
            "type": "string"
        },
        "RepositoryOptions": {
            "description": "Extra options for repository",
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "Username": {
                    "description": "Chart repository username",
                    "type": "string"
                },
                "Password": {
                    "description": "Chart repository password",
                    "type": "string"
                },
                "CAFile": {
                    "description": "Verify certificates of HTTPS-enabled servers using this CA bundle from S3",
                    "type": "string"
                },
                "InsecureSkipTLSVerify": {
                    "description": "Skip TLS certificate checks for the repository",
                    "type": "boolean"
                }
            }
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
            "description": "Custom Values can optionally be specified",
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
        "Resources": {
            "description": "Resources from the helm charts",
            "type": "object"
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
    "required": [
        "Chart"
    ],
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
    "writeOnlyProperties": [
        "/properties/RepositoryOptions"
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
                "lambda:UpdateFunctionCode",
                "ecr:GetAuthorizationToken",
                "ecr:BatchCheckLayerAvailability",
                "ecr:GetDownloadUrlForLayer",
                "ecr:BatchGetImage"
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
                "lambda:UpdateFunctionCode",
                "ecr:GetAuthorizationToken",
                "ecr:BatchCheckLayerAvailability",
                "ecr:GetDownloadUrlForLayer",
                "ecr:BatchGetImage"
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
                "lambda:UpdateFunctionCode",
                "ecr:GetAuthorizationToken",
                "ecr:BatchCheckLayerAvailability",
                "ecr:GetDownloadUrlForLayer",
                "ecr:BatchGetImage"
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
                "lambda:UpdateFunctionCode",
                "ecr:GetAuthorizationToken",
                "ecr:BatchCheckLayerAvailability",
                "ecr:GetDownloadUrlForLayer",
                "ecr:BatchGetImage"
            ]
        }
    }
}
{% endhighlight %}
