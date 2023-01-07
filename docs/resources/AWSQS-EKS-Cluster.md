
## AWSQS::EKS::Cluster

A resource that creates Amazon Elastic Kubernetes Service (Amazon EKS) clusters.

- [Source](https:&#x2F;&#x2F;github.com&#x2F;aws-quickstart&#x2F;quickstart-amazon-eks-cluster-resource-provider.git) 
- [Documentation]()

Published by aws-quickstart

## Schema
{% highlight json %}
{
    "typeName": "AWSQS::EKS::Cluster",
    "description": "A resource that creates Amazon Elastic Kubernetes Service (Amazon EKS) clusters.",
    "sourceUrl": "https://github.com/aws-quickstart/quickstart-amazon-eks-cluster-resource-provider.git",
    "documentationUrl": "https://github.com/aws-quickstart/quickstart-amazon-eks-cluster-resource-provider/blob/main/README.md",
    "definitions": {
        "KubernetesApiAccessEntry": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "Arn": {
                    "type": "string"
                },
                "Username": {
                    "type": "string"
                },
                "Groups": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    }
                }
            }
        },
        "Provider": {
            "description": "AWS Key Management Service (AWS KMS) customer master key (CMK). Either the ARN or the alias can be used.",
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "KeyArn": {
                    "description": "Amazon Resource Name (ARN) or alias of the customer master key (CMK). The CMK must be symmetric, created in the same region as the cluster, and if the CMK was created in a different account, the user must have access to the CMK.",
                    "type": "string"
                }
            }
        },
        "EncryptionConfigEntry": {
            "description": "The encryption configuration for the cluster.",
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "Resources": {
                    "type": "array",
                    "description": "Specifies the resources to be encrypted. The only supported value is \"secrets\".",
                    "items": {
                        "description": "Specifies the resources to be encrypted. The only supported value is \"secrets\".",
                        "type": "string"
                    }
                },
                "Provider": {
                    "$ref": "#/definitions/Provider"
                }
            }
        }
    },
    "properties": {
        "Name": {
            "description": "A unique name for your cluster.",
            "type": "string",
            "minLength": 1
        },
        "RoleArn": {
            "description": "Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role. This provides permissions for Amazon EKS to call other AWS APIs.",
            "type": "string"
        },
        "LambdaRoleName": {
            "description": "Name of the AWS Identity and Access Management (IAM) role used for clusters that have the public endpoint disabled. this provides permissions for Lambda to be invoked and attach to the cluster VPC",
            "type": "string",
            "default": "CloudFormation-Kubernetes-VPC"
        },
        "Version": {
            "description": "Desired Kubernetes version for your cluster. If you don't specify this value, the cluster uses the latest version from Amazon EKS.",
            "type": "string",
            "default": "1.21"
        },
        "KubernetesNetworkConfig": {
            "description": "Network configuration for Amazon EKS cluster.\n\n",
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "ServiceIpv4Cidr": {
                    "description": "Specify the range from which cluster services will receive IPv4 addresses.",
                    "type": "string"
                }
            }
        },
        "ResourcesVpcConfig": {
            "description": "An object that represents the virtual private cloud (VPC) configuration to use for an Amazon EKS cluster.",
            "type": "object",
            "properties": {
                "SecurityGroupIds": {
                    "description": "Specify one or more security groups for the cross-account elastic network interfaces that Amazon EKS creates to use to allow communication between your worker nodes and the Kubernetes control plane. If you don't specify a security group, the default security group for your VPC is used.",
                    "type": "array",
                    "items": {
                        "type": "string"
                    }
                },
                "SubnetIds": {
                    "description": "Specify subnets for your Amazon EKS worker nodes. Amazon EKS creates cross-account elastic network interfaces in these subnets to allow communication between your worker nodes and the Kubernetes control plane.",
                    "type": "array",
                    "items": {
                        "type": "string"
                    }
                },
                "EndpointPublicAccess": {
                    "description": "Set this value to false to disable public access to your cluster's Kubernetes API server endpoint. If you disable public access, your cluster's Kubernetes API server can only receive requests from within the cluster VPC. The default value for this parameter is true , which enables public access for your Kubernetes API server.",
                    "type": "boolean"
                },
                "EndpointPrivateAccess": {
                    "description": "Set this value to true to enable private access for your cluster's Kubernetes API server endpoint. If you enable private access, Kubernetes API requests from within your cluster's VPC use the private VPC endpoint. The default value for this parameter is false , which disables private access for your Kubernetes API server. If you disable private access and you have worker nodes or AWS Fargate pods in the cluster, then ensure that publicAccessCidrs includes the necessary CIDR blocks for communication with the worker nodes or Fargate pods.",
                    "type": "boolean"
                },
                "PublicAccessCidrs": {
                    "description": "The CIDR blocks that are allowed access to your cluster's public Kubernetes API server endpoint. Communication to the endpoint from addresses outside of the CIDR blocks that you specify is denied. The default value is 0.0.0.0/0 . If you've disabled private endpoint access and you have worker nodes or AWS Fargate pods in the cluster, then ensure that you specify the necessary CIDR blocks.",
                    "type": "array",
                    "items": {
                        "type": "string"
                    }
                }
            },
            "required": [
                "SubnetIds"
            ],
            "additionalProperties": false
        },
        "EnabledClusterLoggingTypes": {
            "description": "Enables exporting of logs from the Kubernetes control plane to Amazon CloudWatch Logs. By default, logs from the cluster control plane are not exported to CloudWatch Logs. The valid log types are api, audit, authenticator, controllerManager, and scheduler.",
            "type": "array",
            "items": {
                "type": "string",
                "pattern": "^api$|^audit$|^authenticator$|^controllerManager$|^scheduler$"
            }
        },
        "EncryptionConfig": {
            "description": "Encryption configuration for the cluster.",
            "type": "array",
            "items": {
                "$ref": "#/definitions/EncryptionConfigEntry"
            }
        },
        "KubernetesApiAccess": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "Roles": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/KubernetesApiAccessEntry"
                    }
                },
                "Users": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/KubernetesApiAccessEntry"
                    }
                }
            }
        },
        "Arn": {
            "description": "ARN of the cluster (e.g., `arn:aws:eks:us-west-2:666666666666:cluster/prod`).",
            "type": "string"
        },
        "CertificateAuthorityData": {
            "description": "Certificate authority data for your cluster.",
            "type": "string"
        },
        "ClusterSecurityGroupId": {
            "description": "Security group that was created by Amazon EKS for your cluster. Managed-node groups use this security group for control-plane-to-data-plane communications.",
            "type": "string"
        },
        "Endpoint": {
            "description": "Endpoint for your Kubernetes API server (e.g., https://5E1D0CEXAMPLEA591B746AFC5AB30262.yl4.us-west-2.eks.amazonaws.com).",
            "type": "string"
        },
        "EncryptionConfigKeyArn": {
            "description": "ARN or alias of the customer master key (CMK).",
            "type": "string"
        },
        "OIDCIssuerURL": {
            "description": "Issuer URL for the OpenID Connect identity provider.",
            "type": "string"
        },
        "Tags": {
            "type": "array",
            "uniqueItems": false,
            "items": {
                "type": "object",
                "additionalProperties": false,
                "properties": {
                    "Value": {
                        "type": "string"
                    },
                    "Key": {
                        "type": "string"
                    }
                },
                "required": [
                    "Value",
                    "Key"
                ]
            }
        }
    },
    "additionalProperties": false,
    "required": [
        "RoleArn",
        "ResourcesVpcConfig"
    ],
    "readOnlyProperties": [
        "/properties/Arn",
        "/properties/Endpoint",
        "/properties/ClusterSecurityGroupId",
        "/properties/CertificateAuthorityData",
        "/properties/EncryptionConfigKeyArn",
        "/properties/OIDCIssuerURL"
    ],
    "createOnlyProperties": [
        "/properties/Name",
        "/properties/KubernetesNetworkConfig/ServiceIpv4Cidr",
        "/properties/RoleArn",
        "/properties/ResourcesVpcConfig/SubnetIds",
        "/properties/ResourcesVpcConfig/SecurityGroupIds"
    ],
    "primaryIdentifier": [
        "/properties/Name"
    ],
    "handlers": {
        "create": {
            "permissions": [
                "sts:GetCallerIdentity",
                "eks:CreateCluster",
                "eks:DescribeCluster",
                "eks:ListTagsForResource",
                "eks:TagResource",
                "iam:PassRole",
                "sts:AssumeRole",
                "lambda:UpdateFunctionConfiguration",
                "lambda:DeleteFunction",
                "lambda:GetFunction",
                "lambda:InvokeFunction",
                "lambda:CreateFunction",
                "lambda:UpdateFunctionCode",
                "ec2:DescribeVpcs",
                "ec2:DescribeSubnets",
                "ec2:DescribeSecurityGroups",
                "iam:PassRole",
                "cloudformation:ListExports",
                "kms:DescribeKey",
                "kms:CreateGrant"
            ]
        },
        "read": {
            "permissions": [
                "sts:GetCallerIdentity",
                "eks:DescribeCluster",
                "eks:ListTagsForResource",
                "lambda:UpdateFunctionConfiguration",
                "lambda:DeleteFunction",
                "lambda:GetFunction",
                "lambda:InvokeFunction",
                "lambda:CreateFunction",
                "lambda:UpdateFunctionCode",
                "ec2:DescribeVpcs",
                "ec2:DescribeSubnets",
                "ec2:DescribeSecurityGroups",
                "iam:PassRole",
                "cloudformation:ListExports",
                "kms:DescribeKey",
                "kms:CreateGrant"
            ]
        },
        "update": {
            "permissions": [
                "sts:GetCallerIdentity",
                "eks:DescribeCluster",
                "eks:UpdateClusterVersion",
                "eks:UpdateClusterConfig",
                "eks:ListTagsForResource",
                "eks:TagResource",
                "eks:UntagResource",
                "iam:PassRole",
                "lambda:UpdateFunctionConfiguration",
                "lambda:DeleteFunction",
                "lambda:GetFunction",
                "lambda:InvokeFunction",
                "lambda:CreateFunction",
                "lambda:UpdateFunctionCode",
                "ec2:DescribeVpcs",
                "ec2:DescribeSubnets",
                "ec2:DescribeSecurityGroups",
                "cloudformation:ListExports",
                "kms:DescribeKey",
                "kms:CreateGrant"
            ]
        },
        "delete": {
            "permissions": [
                "sts:GetCallerIdentity",
                "eks:DescribeCluster",
                "eks:ListTagsForResource",
                "eks:DeleteCluster",
                "lambda:UpdateFunctionConfiguration",
                "lambda:DeleteFunction",
                "lambda:GetFunction",
                "lambda:InvokeFunction",
                "lambda:CreateFunction",
                "lambda:UpdateFunctionCode",
                "ec2:DescribeVpcs",
                "ec2:DescribeSubnets",
                "ec2:DescribeSecurityGroups",
                "iam:PassRole",
                "cloudformation:ListExports",
                "kms:DescribeKey",
                "kms:CreateGrant"
            ]
        }
    }
}
{% endhighlight %}
