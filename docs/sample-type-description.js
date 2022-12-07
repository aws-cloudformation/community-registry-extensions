{
  ResponseMetadata: { RequestId: '1a8c7bce-a2c2-455c-a24c-6bad7129c343' },
  Arn: 'arn:aws:cloudformation:us-east-1:755952356119:type/resource/AWSQS-EKS-Cluster',
  Type: 'RESOURCE',
  TypeName: 'AWSQS::EKS::Cluster',
  Description: 'A resource that creates Amazon Elastic Kubernetes Service (Amazon EKS) clusters.',
  Schema: '{\n' +
    '    "typeName": "AWSQS::EKS::Cluster",\n' +
    '    "description": "A resource that creates Amazon Elastic Kubernetes Service (Amazon EKS) clusters.",\n' +
    '    "sourceUrl": "https://github.com/aws-quickstart/quickstart-amazon-eks-cluster-resource-provider.git",\n' +
    '    "documentationUrl": "https://github.com/aws-quickstart/quickstart-amazon-eks-cluster-resource-provider/blob/main/README.md",\n' +
    '    "definitions": {\n' +
    '        "KubernetesApiAccessEntry": {\n' +
    '            "type": "object",\n' +
    '            "additionalProperties": false,\n' +
    '            "properties": {\n' +
    '                "Arn": {"type": "string"},\n' +
    '                "Username": {"type": "string"},\n' +
    '                "Groups": {"type": "array", "items": {"type": "string"}}\n' +
    '            }\n' +
    '        },\n' +
    '        "Provider": {\n' +
    '            "description": "AWS Key Management Service (AWS KMS) customer master key (CMK). Either the ARN or the alias can be used.",\n' +
    '            "type": "object",\n' +
    '            "additionalProperties": false,\n' +
    '            "properties": {\n' +
    '                "KeyArn": {\n' +
    '                    "description": "Amazon Resource Name (ARN) or alias of the customer master key (CMK). The CMK must be symmetric, created in the same region as the cluster, and if the CMK was created in a different account, the user must have access to the CMK.",\n' +
    '                    "type": "string"\n' +
    '                }\n' +
    '            }\n' +
    '        },\n' +
    '        "EncryptionConfigEntry": {\n' +
    '            "description": "The encryption configuration for the cluster.",\n' +
    '            "type": "object",\n' +
    '            "additionalProperties": false,\n' +
    '            "properties": {\n' +
    '                "Resources": {\n' +
    '                    "type": "array",\n' +
    '                    "description": "Specifies the resources to be encrypted. The only supported value is \\"secrets\\".",\n' +
    '                    "items": {\n' +
    '                        "description": "Specifies the resources to be encrypted. The only supported value is \\"secrets\\".",\n' +
    '                        "type": "string"\n' +
    '                    }\n' +
    '                },\n' +
    '                "Provider": {\n' +
    '                    "$ref": "#/definitions/Provider"\n' +
    '                }\n' +
    '            }\n' +
    '        }\n' +
    '    },\n' +
    '    "properties": {\n' +
    '        "Name": {\n' +
    '            "description": "A unique name for your cluster.",\n' +
    '            "type": "string",\n' +
    '            "minLength": 1\n' +
    '        },\n' +
    '        "RoleArn": {\n' +
    '            "description": "Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role. This provides permissions for Amazon EKS to call other AWS APIs.",\n' +
    '            "type": "string"\n' +
    '        },\n' +
    '        "LambdaRoleName": {\n' +
    '            "description": "Name of the AWS Identity and Access Management (IAM) role used for clusters that have the public endpoint disabled. this provides permissions for Lambda to be invoked and attach to the cluster VPC",\n' +
    '            "type": "string",\n' +
    '            "default": "CloudFormation-Kubernetes-VPC"\n' +
    '        },\n' +
    '        "Version": {\n' +
    `            "description": "Desired Kubernetes version for your cluster. If you don't specify this value, the cluster uses the latest version from Amazon EKS.",\n` +
    '            "type": "string",\n' +
    '            "default": "1.21"\n' +
    '        },\n' +
    '        "KubernetesNetworkConfig": {\n' +
    '            "description": "Network configuration for Amazon EKS cluster.\\n\\n",\n' +
    '            "type": "object",\n' +
    '            "additionalProperties": false,\n' +
    '            "properties": {\n' +
    '                "ServiceIpv4Cidr": {\n' +
    '                    "description": "Specify the range from which cluster services will receive IPv4 addresses.",\n' +
    '                    "type": "string"\n' +
    '                }\n' +
    '            }\n' +
    '        },\n' +
    '        "ResourcesVpcConfig": {\n' +
    '            "description": "An object that represents the virtual private cloud (VPC) configuration to use for an Amazon EKS cluster.",\n' +
    '            "type": "object",\n' +
    '            "properties": {\n' +
    '                "SecurityGroupIds": {\n' +
    `                    "description": "Specify one or more security groups for the cross-account elastic network interfaces that Amazon EKS creates to use to allow communication between your worker nodes and the Kubernetes control plane. If you don't specify a security group, the default security group for your VPC is used.",\n` +
    '                    "type": "array",\n' +
    '                    "items": {"type": "string"}\n' +
    '                },\n' +
    '                "SubnetIds": {\n' +
    '                    "description": "Specify subnets for your Amazon EKS worker nodes. Amazon EKS creates cross-account elastic network interfaces in these subnets to allow communication between your worker nodes and the Kubernetes control plane.",\n' +
    '                    "type": "array",\n' +
    '                    "items": {"type": "string"}\n' +
    '                },\n' +
    '                "EndpointPublicAccess": {\n' +
    `                    "description": "Set this value to false to disable public access to your cluster's Kubernetes API server endpoint. If you disable public access, your cluster's Kubernetes API server can only receive requests from within the cluster VPC. The default value for this parameter is true , which enables public access for your Kubernetes API server.",\n` +
    '                    "type": "boolean"\n' +
    '                },\n' +
    '                "EndpointPrivateAccess": {\n' +
    `                    "description": "Set this value to true to enable private access for your cluster's Kubernetes API server endpoint. If you enable private access, Kubernetes API requests from within your cluster's VPC use the private VPC endpoint. The default value for this parameter is false , which disables private access for your Kubernetes API server. If you disable private access and you have worker nodes or AWS Fargate pods in the cluster, then ensure that publicAccessCidrs includes the necessary CIDR blocks for communication with the worker nodes or Fargate pods.",\n` +
    '                    "type": "boolean"\n' +
    '                },\n' +
    '                "PublicAccessCidrs": {\n' +
    `                    "description": "The CIDR blocks that are allowed access to your cluster's public Kubernetes API server endpoint. Communication to the endpoint from addresses outside of the CIDR blocks that you specify is denied. The default value is 0.0.0.0/0 . If you've disabled private endpoint access and you have worker nodes or AWS Fargate pods in the cluster, then ensure that you specify the necessary CIDR blocks.",\n` +
    '                    "type": "array",\n' +
    '                    "items": {"type": "string"}\n' +
    '                }\n' +
    '            },\n' +
    '            "required": ["SubnetIds"],\n' +
    '            "additionalProperties": false\n' +
    '        },\n' +
    '        "EnabledClusterLoggingTypes": {\n' +
    '            "description": "Enables exporting of logs from the Kubernetes control plane to Amazon CloudWatch Logs. By default, logs from the cluster control plane are not exported to CloudWatch Logs. The valid log types are api, audit, authenticator, controllerManager, and scheduler.",\n' +
    '            "type": "array",\n' +
    '            "items": {"type": "string", "pattern": "^api$|^audit$|^authenticator$|^controllerManager$|^scheduler$"}\n' +
    '        },\n' +
    '        "EncryptionConfig": {\n' +
    '            "description": "Encryption configuration for the cluster.",\n' +
    '            "type": "array",\n' +
    '            "items": {\n' +
    '                "$ref": "#/definitions/EncryptionConfigEntry"\n' +
    '            }\n' +
    '        },\n' +
    '        "KubernetesApiAccess": {\n' +
    '            "type": "object",\n' +
    '            "additionalProperties": false,\n' +
    '            "properties": {\n' +
    '                "Roles": {\n' +
    '                    "type": "array",\n' +
    '                    "items": {\n' +
    '                        "$ref": "#/definitions/KubernetesApiAccessEntry"\n' +
    '                    }\n' +
    '                },\n' +
    '                "Users": {\n' +
    '                    "type": "array",\n' +
    '                    "items": {\n' +
    '                        "$ref": "#/definitions/KubernetesApiAccessEntry"\n' +
    '                    }\n' +
    '                }\n' +
    '            }\n' +
    '        },\n' +
    '        "Arn": {\n' +
    '            "description": "ARN of the cluster (e.g., `arn:aws:eks:us-west-2:666666666666:cluster/prod`).",\n' +
    '            "type": "string"\n' +
    '        },\n' +
    '        "CertificateAuthorityData": {\n' +
    '            "description": "Certificate authority data for your cluster.",\n' +
    '            "type": "string"\n' +
    '        },\n' +
    '        "ClusterSecurityGroupId": {\n' +
    '            "description": "Security group that was created by Amazon EKS for your cluster. Managed-node groups use this security group for control-plane-to-data-plane communications.",\n' +
    '            "type": "string"\n' +
    '        },\n' +
    '        "Endpoint": {\n' +
    '            "description": "Endpoint for your Kubernetes API server (e.g., https://5E1D0CEXAMPLEA591B746AFC5AB30262.yl4.us-west-2.eks.amazonaws.com).",\n' +
    '            "type": "string"\n' +
    '        },\n' +
    '        "EncryptionConfigKeyArn": {\n' +
    '            "description": "ARN or alias of the customer master key (CMK).",\n' +
    '            "type": "string"\n' +
    '        },\n' +
    '        "OIDCIssuerURL": {\n' +
    '            "description": "Issuer URL for the OpenID Connect identity provider.",\n' +
    '            "type": "string"\n' +
    '        },\n' +
    '        "Tags": {\n' +
    '            "type": "array",\n' +
    '            "uniqueItems": false,\n' +
    '            "items": {\n' +
    '                "type": "object",\n' +
    '                "additionalProperties": false,\n' +
    '                "properties": {\n' +
    '                    "Value": {\n' +
    '                        "type": "string"\n' +
    '                    },\n' +
    '                    "Key": {\n' +
    '                        "type": "string"\n' +
    '                    }\n' +
    '                },\n' +
    '                "required": [\n' +
    '                    "Value",\n' +
    '                    "Key"\n' +
    '                ]\n' +
    '            }\n' +
    '        }\n' +
    '    },\n' +
    '    "additionalProperties": false,\n' +
    '    "required": [\n' +
    '        "RoleArn",\n' +
    '        "ResourcesVpcConfig"\n' +
    '    ],\n' +
    '    "readOnlyProperties": [\n' +
    '        "/properties/Arn",\n' +
    '        "/properties/Endpoint",\n' +
    '        "/properties/ClusterSecurityGroupId",\n' +
    '        "/properties/CertificateAuthorityData",\n' +
    '        "/properties/EncryptionConfigKeyArn",\n' +
    '        "/properties/OIDCIssuerURL"\n' +
    '    ],\n' +
    '    "createOnlyProperties": [\n' +
    '        "/properties/Name",\n' +
    '        "/properties/KubernetesNetworkConfig/ServiceIpv4Cidr",\n' +
    '        "/properties/RoleArn",\n' +
    '        "/properties/ResourcesVpcConfig/SubnetIds",\n' +
    '        "/properties/ResourcesVpcConfig/SecurityGroupIds"\n' +
    '    ],\n' +
    '    "primaryIdentifier": [\n' +
    '        "/properties/Name"\n' +
    '    ],\n' +
    '    "handlers": {\n' +
    '        "create": {\n' +
    '            "permissions": [\n' +
    '                "sts:GetCallerIdentity",\n' +
    '                "eks:CreateCluster",\n' +
    '                "eks:DescribeCluster",\n' +
    '                "eks:ListTagsForResource",\n' +
    '                "eks:TagResource",\n' +
    '                "iam:PassRole",\n' +
    '                "sts:AssumeRole",\n' +
    '                "lambda:UpdateFunctionConfiguration",\n' +
    '                "lambda:DeleteFunction",\n' +
    '                "lambda:GetFunction",\n' +
    '                "lambda:InvokeFunction",\n' +
    '                "lambda:CreateFunction",\n' +
    '                "lambda:UpdateFunctionCode",\n' +
    '                "ec2:DescribeVpcs",\n' +
    '                "ec2:DescribeSubnets",\n' +
    '                "ec2:DescribeSecurityGroups",\n' +
    '                "iam:PassRole",\n' +
    '                "cloudformation:ListExports",\n' +
    '                "kms:DescribeKey",\n' +
    '                "kms:CreateGrant"\n' +
    '            ]\n' +
    '        },\n' +
    '        "read": {\n' +
    '            "permissions": [\n' +
    '                "sts:GetCallerIdentity",\n' +
    '                "eks:DescribeCluster",\n' +
    '                "eks:ListTagsForResource",\n' +
    '                "lambda:UpdateFunctionConfiguration",\n' +
    '                "lambda:DeleteFunction",\n' +
    '                "lambda:GetFunction",\n' +
    '                "lambda:InvokeFunction",\n' +
    '                "lambda:CreateFunction",\n' +
    '                "lambda:UpdateFunctionCode",\n' +
    '                "ec2:DescribeVpcs",\n' +
    '                "ec2:DescribeSubnets",\n' +
    '                "ec2:DescribeSecurityGroups",\n' +
    '                "iam:PassRole",\n' +
    '                "cloudformation:ListExports",\n' +
    '                "kms:DescribeKey",\n' +
    '                "kms:CreateGrant"\n' +
    '            ]\n' +
    '        },\n' +
    '        "update": {\n' +
    '            "permissions": [\n' +
    '                "sts:GetCallerIdentity",\n' +
    '                "eks:DescribeCluster",\n' +
    '                "eks:UpdateClusterVersion",\n' +
    '                "eks:UpdateClusterConfig",\n' +
    '                "eks:ListTagsForResource",\n' +
    '                "eks:TagResource",\n' +
    '                "eks:UntagResource",\n' +
    '                "iam:PassRole",\n' +
    '                "lambda:UpdateFunctionConfiguration",\n' +
    '                "lambda:DeleteFunction",\n' +
    '                "lambda:GetFunction",\n' +
    '                "lambda:InvokeFunction",\n' +
    '                "lambda:CreateFunction",\n' +
    '                "lambda:UpdateFunctionCode",\n' +
    '                "ec2:DescribeVpcs",\n' +
    '                "ec2:DescribeSubnets",\n' +
    '                "ec2:DescribeSecurityGroups",\n' +
    '                "cloudformation:ListExports",\n' +
    '                "kms:DescribeKey",\n' +
    '                "kms:CreateGrant"\n' +
    '            ]\n' +
    '        },\n' +
    '        "delete": {\n' +
    '            "permissions": [\n' +
    '                "sts:GetCallerIdentity",\n' +
    '                "eks:DescribeCluster",\n' +
    '                "eks:ListTagsForResource",\n' +
    '                "eks:DeleteCluster",\n' +
    '                "lambda:UpdateFunctionConfiguration",\n' +
    '                "lambda:DeleteFunction",\n' +
    '                "lambda:GetFunction",\n' +
    '                "lambda:InvokeFunction",\n' +
    '                "lambda:CreateFunction",\n' +
    '                "lambda:UpdateFunctionCode",\n' +
    '                "ec2:DescribeVpcs",\n' +
    '                "ec2:DescribeSubnets",\n' +
    '                "ec2:DescribeSecurityGroups",\n' +
    '                "iam:PassRole",\n' +
    '                "cloudformation:ListExports",\n' +
    '                "kms:DescribeKey",\n' +
    '                "kms:CreateGrant"\n' +
    '            ]\n' +
    '        }\n' +
    '    }\n' +
    '}\n',
  ProvisioningType: 'FULLY_MUTABLE',
  DeprecatedStatus: 'LIVE',
  RequiredActivatedTypes: [],
  ExecutionRoleArn: 'arn:aws:iam::755952356119:role/registry-extension-activation',
  Visibility: 'PRIVATE',
  SourceUrl: 'https://github.com/aws-quickstart/quickstart-amazon-eks-cluster-resource-provider.git',
  DocumentationUrl: 'https://github.com/aws-quickstart/quickstart-amazon-eks-cluster-resource-provider/blob/main/README.md',
  LastUpdated: 2021-03-10T00:54:18.981Z,
  TimeCreated: 2022-12-07T17:08:04.944Z,
  PublisherId: '408988dff9e863704bcc72e7e13f8d645cee8311',
  OriginalTypeName: 'AWSQS::EKS::Cluster',
  OriginalTypeArn: 'arn:aws:cloudformation:us-east-1::type/resource/408988dff9e863704bcc72e7e13f8d645cee8311/AWSQS-EKS-Cluster',
  PublicVersionNumber: '1.12.0',
  AutoUpdate: true
}
