# AwsCommunity::Resource::Lookup

- [Overview](#Overview)
    - [Context](#Context)
- [Resource type reference](#Resource-type-reference)
- [Usage](#Usage)
    - [Upgrade path](#Upgrade-path)
    - [Constructing queries](#Constructing-queries)
        - [Using the AWS resource and property types reference](#Using-the-AWS-resource-and-property-types-reference)
        - [Using the AWS CLI and AWS Cloud Control API](#Using-the-AWS-CLI-and-AWS-Cloud-Control-API)
    - [The ResourceModel property](#The-ResourceModel-property)
    - [The ResourceLookupRoleArn property](#The-ResourceLookupRoleArn-property)
    - [The LookupSerialNumber property](#The-LookupSerialNumber-property)
    - [The Tags property](#The-Tags-property)
- [Usage walkthrough](#Usage-walkthrough)
    - [Cleanup](#Cleanup)
- [Resource type registry submission with StackSets](#Resource-type-registry-submission-with-StackSets)
- [Development notes](#Development-notes)
    - [Contract tests](#Contract-tests)
    - [Integration tests](#Integration-tests)
    - [Schema](#Schema)

## Overview
The `AwsCommunity::Resource::Lookup` AWS CloudFormation [resource type](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-types.html) uses `ListResources` and `GetResource` [actions](https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/API_Operations.html) of [AWS Cloud Control API](https://aws.amazon.com/cloudcontrolapi/) to perform a search for a resource of a given type (such as, `AWS::EC2::VPC`) in your AWS account -and current region if you are using a regional AWS service- based on a query you specify.  If only one match is found, `AwsCommunity::Resource::Lookup` returns the primary identifier of the resource (in the `AWS::EC2::VPC` example, the ID of the VPC) and the resource properties in JSON format, that you can then consume by referencing them in your template with the `Fn::GetAtt`[intrinsic function](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference.html).

Note: as this resource type uses Cloud Control API, you can specify resource type search targets -like `AWS::EC2::VPC`- that are supported by Cloud Control API; for more information, see [Determining if a resource type supports Cloud Control API](https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-types.html#resource-types-determine-support).

### Context
This section describes the context on when you should use the methods that CloudFormation already provides to correlate resources, and when you can choose to use this resource type.

When you use [AWS CloudFormation](https://aws.amazon.com/cloudformation/) to describe AWS or third-party resources in your templates, you'll likely need to have one resource depend on another.  For example, you describe an `AWS::EC2::SecurityGroup` [resource](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group.html), and you use the `VpcId` [property](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-security-group.html#cfn-ec2-securitygroup-vpcid) to specify, as a reference, the ID of the [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/) (Amazon VPC) resource to which the security group will refer.

CloudFormation provides already ways for you to create dependencies between resources:

- with [intrinsic functions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference.html) like `Ref`, `Fn::Sub`, and `Fn::GetAtt`, to reference values for resources you describe in the same template;
- if you are describing resources across templates, you can export values from one template(s) and consume them in others with the `Fn::ImportValue` [intrinsic function](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-importvalue.html), or use [nested stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html).

You can also lookup values you need to reference (for example, the ID of a VPC), and pass them in as template parameters.  Alternatively, you can store the value in an [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html) parameter, and consume the parameter from the other template.  For more information, see [Using dynamic references to specify template values](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html).

There are also use cases where you want to reference a resource that you chose to create outside the CloudFormation's purview.  For example, you created a VPC with the [AWS Management Console](https://aws.amazon.com/console/), or with the [AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli/).  In these cases, if you are planning to use CloudFormation to manage your resource, you have the option of importing a resource supported today, and then use one of the methods described earlier to establish resource dependencies.  For more information, see [Bringing existing resources into CloudFormation management](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import.html).

If you choose to manage the resource you want to reference outside CloudFormation -or if the resource is managed by another team with CloudFormation or with another service or tool- and you want to look it up to create a dependency against it in your template(s), you can perform the lookup yourself and provide the value as a template parameter, or use Parameter Store as mentioned earlier.  If you have use cases where a dynamic lookup is more desirable, this is where the `AwsCommunity::Resource::Lookup` resource type comes into play.

## Resource type reference
For reference information on properties for the `AwsCommunity::Resource::Lookup` resource type, including properties that are required or not, property types, property value constraints, and update behaviors, see [AwsCommunity::Resource::Lookup](docs/README.md) in the documentation page for this resource in the `docs` directory.

## Usage
Example: you want to search for one of your existing [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/) (Amazon VPC) resources, based on search criteria that include [tag](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html) key(s) and value(s); for more information, see [Constructing queries](#Constructing-queries) in this document.  The example CloudFormation template shown next declares the `AwsCommunity::Resource::Lookup` resource type, and shows how to consume its return value from the `VpcId` property of the `AWS::EC2::SecurityGroup` resource type.  Note also that the template shows the usage of the optional `Tags` property, that is not related to the VPC example use case: this property describes tags for the [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html) parameter resource(s) that `AwsCommunity::Resource::Lookup` creates in your account and current region to persist the lookup result(s) (`AwsCommunity::Resource::Lookup` needs this data, for example, when its `Read` handler is invoked):

```
AWSTemplateFormatVersion: "2010-09-09"

Description: This template describes an example resource type for an AWS::EC2::VPC resource lookup operation and consumption.

Parameters:
  JmesPathQuery:
    Description: Specify the query, in JMESPath format, that you wish to run to filter results.
    Type: String
    Default: Tags[?Key == 'Owner' && Value == 'contract-test-only-test-team']
    MinLength: "1"

  LookupSerialNumber:
    Description: Optional, numeric integer value (such as `1`, `2`), that you can specify to induce a new search on e.g., stack updates without modifying the value for `JmesPathQuery`.
    Type: String
    Default: "1"
    AllowedPattern: ^[0-9]*$

  ResourceLookupRoleArn:
    Description: The ARN of the IAM role to use for resource lookup operations.
    Type: String
    AllowedPattern: ^arn:aws(-[a-z]+)*:iam::[0-9]{12}:role\/[\w+=,.@-]{1,64}$

  TypeName:
    Description: Specify the type name you wish to use for the lookup operation.
    Type: String
    Default: AWS::EC2::VPC
    AllowedPattern: ^[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}$

Resources:
  ResourceLookup:
    Type: AwsCommunity::Resource::Lookup
    Properties:
      JmesPathQuery: !Ref 'JmesPathQuery'
      LookupSerialNumber: !Ref 'LookupSerialNumber'
      ResourceLookupRoleArn: !Ref 'ResourceLookupRoleArn'
      TypeName: !Ref 'TypeName'
      Tags:
        Env: DEV
        Name: Test-only

  InstanceSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Example security group.
      SecurityGroupEgress:
        - CidrIp: 0.0.0.0/0
          FromPort: 80
          IpProtocol: tcp
          ToPort: 80
      VpcId: !GetAtt ResourceLookup.ResourceIdentifier

Outputs:
  ResourceIdentifier:
    Description: The resource identifier result of the lookup operation.
    Value: !GetAtt ResourceLookup.ResourceIdentifier

  ResourceLookupId:
    Description: The ID of the resource lookup operation.
    Value: !Ref 'ResourceLookup'

  ResourceProperties:
    Description: The properties of the resource you looked up.
    Value: !GetAtt ResourceLookup.ResourceProperties
```

In the `Outputs` section for the example above, note the `ResourceIdentifier` and `ResourceProperties` outputs that use the `Fn::GetAtt` intrinsic function to reference, respectively, the `ResourceIdentifier` and `ResourceProperties` properties of the `AwsCommunity::Resource::Lookup` resource type: the former property returns, in the example above, the ID of the VPC you looked up (e.g., `vpc-111222333`), and the latter the resource properties of the VPC (e.g., `{"VpcId":"vpc-111222333","InstanceTenancy":"default",[...]`) in JSON format.

Note: the `AwsCommunity::Resource::Lookup` resource type also uses AWS Cloud Control API to get the properties of a resource (in this case, of the resource that has been found as part of your lookup operation).  For more information, see [Reading a resource's current state](https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations-read.html).

### Upgrade path
A new version of the `AwsCommunity::Resource::Lookup` resource type introduced the ability of consuming the properties of a resource type that is the target of the search (in the above examples, a VPC) with the `Fn::GetAtt` intrinsic function.  If you have an existing CloudFormation stack that uses a previous version of the `AwsCommunity::Resource::Lookup` resource type, for you to use a reference to the resource properties such as with `!GetAtt ResourceLookup.ResourceProperties`, first you'll need to:

- make sure you use the latest version of the `AwsCommunity::Resource::Lookup` resource type;
- update your existing stack: when you do so, pass a new parameter value to `LookupSerialNumber`: for example, pass `2` instead of `1`.  This will induce a change into the desired resource state, and a new lookup operation will start when the stack update operation begins.  Once the resource has been looked up again, due to how this resource type is designed a new Parameter Store resource will be created, and it will replace the existing one: the new parameter will contain additional information to support the retrieval of the resource properties (the ARN of the lookup role you already passed in as an input to the resource);
- next, on subsequent uses, you should be able to reference the resource properties of the target resource type with (for example): `!GetAtt ResourceLookup.ResourceProperties`.

### Constructing queries
This resource type uses [JMESPath](https://jmespath.org/) to search through `ResourceDescription` [properties](https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/API_ResourceDescription.html) returned by the [GetResource](https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/API_GetResource.html) API of [AWS Cloud Control API](https://aws.amazon.com/cloudcontrolapi/).  You specify your query in the `JmesPathQuery` property of the `AwsCommunity::Resource::Lookup` resource type.  To build a query that you'll pass in as an input to this resource type, you'd want to:

- familiarize with the [JMESPath Specification](https://jmespath.org/specification.html);
- determine the JSON data structure to use;
- build a strategy of the field(s) you wish to query;
- build a query that traverses the JSON structure.

#### Using the AWS resource and property types reference
A first-glance way to have an idea of which JSON data structure to use, is to open the [AWS resource and property types reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html) page, and then open the documentation for the resource type that is the target of your query.  For example, open the page for the `AWS::EC2::VPC` [resource](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpc.html), and locate the JSON [Syntax](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpc.html#aws-resource-ec2-vpc-syntax) section.  You can also navigate to the [Examples](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpc.html#aws-resource-ec2-vpc--examples) section further down in the page, to see sample template snippets.

Let's make an example: assume you want to query for the VPC, in your account and current region, whose resource tags are
`Key` set to `stack`, and `Value` set to `production`; the JSON data input to query would then be as the one shown in the following snippet, and looking at the structure underneath `Properties`:

```
    [...omitted...],
    "ExampleVpc" : {
      "Type" : "AWS::EC2::VPC",
        "Properties" : {
          [...omitted...],
          "Tags" : [
            {"Key" : "stack", "Value" : "production"}
          ]
```

A JMESPath example query for the above would be:

```
Tags[?Key == 'stack' && Value == 'production']
```

#### Using the AWS CLI and AWS Cloud Control API
You can also use the AWS CLI and AWS Cloud Control API to determine the JSON data structure to use as you build your query.  First, get a list of resources of a given type (the examples use the `us-east-1` region; adapt to the region you wish to use):

```
aws cloudcontrol list-resources \
  --region us-east-1 \
  --type-name "AWS::EC2::VPC"
```

This should yield a list of relevant resources in your account and region:

```
{
    "ResourceDescriptions": [
        {
            "Identifier": "vpc-aaaabbbbccccdddd0",
    [...omitted...]
```

Make a note of the `Identifier` value you need; e.g., `vpc-aaaabbbbccccdddd0`.

Next, install the [jq](https://stedolan.github.io/jq/) tool, that you'll use to format the JSON output you'll get from another API call you'll make next.

When ready, use the identifier you noted earlier, and get the structure and data as such:

```
aws cloudcontrol get-resource \
  --region us-east-1 \
  --type-name "AWS::EC2::VPC" \
  --identifier vpc-YOUR_VPC_ID \
  --query ResourceDescription.Properties --output text | jq
```

This should yield an output such as:

```
{
  "VpcId": "[...omitted...]",
  "InstanceTenancy": "default",
  "CidrBlockAssociations": [
    "[...omitted...]"
  ],
  "CidrBlock": "[...omitted...]",
  "DefaultNetworkAcl": "[...omitted...]",
  "EnableDnsSupport": true,
  "Ipv6CidrBlocks": [
    "[...omitted...]"
  ],
  "DefaultSecurityGroup": "[...omitted...]",
  "EnableDnsHostnames": false,
  "Tags": [
    {
      "Value": "stack",
      "Key": "production"
    }
  ]
}
```

Assuming you want to query for the VPC whose resource tags are `Key` set to `stack`, and `Value` set to `production`, a JMESPath example query for the above would be:

```
Tags[?Key == 'stack' && Value == 'production']
```

### The ResourceModel property
The `ResourceModel` property for the `AwsCommunity::Resource::Lookup` resource type is required if you're using a resource type shown in the [Resources that require additional information](https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations-list.html#resource-operations-list-containers) page.  Specify the required properties using the JSON format; for example, to specify `LoadBalancerArn` and its ARN value for the `AWS::ElasticLoadBalancingV2::Listener` resource type (that you specify in the `TypeName` property), use:

```
{"LoadBalancerArn": "REPLACE_WITH_YOUR_LOAD_BALANCER_ARN"}
```

### The ResourceLookupRoleArn property
`ResourceLookupRoleArn` is a required property for the `AwsCommunity::Resource::Lookup` resource type: the [Amazon Resource Name](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) (ARN) of the [AWS Identity and Access Management](https://aws.amazon.com/iam/) (IAM) role that you specify for this property is passed to Cloud Control API's `ListResources` and `GetResource` actions when this resource type calls them on your behalf against resource type targets (such as, `AWS::EC2::VPC`).

You need to create an IAM role with an IAM policy that you deem to be adequate to access resource type targets (such as, `AWS::EC2::VPC`).  The `examples/example-resource-lookup-role.template` template describes an IAM role that uses the `ReadOnlyAccess` AWS managed [policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html#awsmp_readonlyaccess): you can choose to create a stack with this template, and use the ARN of the newly-created role as an input value to `ResourceLookupRoleArn`; depending on your needs, you might want to use a different policy -or create your own- to describe which permissions you require.

### The LookupSerialNumber property
The `LookupSerialNumber` property for the `AwsCommunity::Resource::Lookup` resource type is an optional, numeric integer value (such as `1`, `2`), that you can specify to induce a new search on e.g., stack updates without modifying the value for `JmesPathQuery`.  Specify a value that is different from the previous one to induce the update; note that either adding this property to the resource if not present before an update, or removing it if previously added to the resource, will yield the same effect of changing the property value and will induce an update.

### The Tags property
The `Tags` property for the `AwsCommunity::Resource::Lookup` resource type is an optional key-value pairs object (such as, `Env: Dev`, `Name: Test`) to associate to the AWS Systems Manager Parameter Store parameter resource that the implementation of this resource type creates in your account and current region to persist the lookup result.

## Usage walkthrough
This section assumes you are using this resource type to submit it as a private extension to the CloudFormation registry, in the AWS region(s) of your choice.  To get started, follow the steps shown next:

- Install [Apache Maven](https://maven.apache.org/install.html), that you'll need to build this resource type that uses Java.  You'll also need to install the JDK 8 or JDK 11.
- Install the [CloudFormation CLI](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html).
- Install the `cloudformation-cli-java-plugin` by following instructions in the [Setting up your environment for developing extensions](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html#resource-type-setup) page.

When ready, create a stack with the `example-resource-lookup-role.template` example template for the IAM role, that you'll use for resource lookup operations.  You'll need to pass the Amazon Resource Name (ARN) of the created role as an input to the resource type later on (the examples use the `us-east-1` region; adapt to the region you wish to use):

```
aws cloudformation create-stack \
  --region us-east-1 \
  --stack-name example-resource-lookup-role \
  --template-body file://examples/example-resource-lookup-role.template \
  --capabilities CAPABILITY_IAM

aws cloudformation wait stack-create-complete \
  --region us-east-1 \
  --stack-name example-resource-lookup-role
```

Note: the IAM role above (that uses `cloudformation.amazonaws.com` service as a [Principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/intro-structure.html#intro-structure-principal)), uses the `ReadOnlyAccess` AWS managed [policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html#awsmp_readonlyaccess).  You might want to use a different policy or create a new one depending on your needs.

Describe the stack you just created, and query its `Outputs`; make a note of the `OutputValue` for `ResourceLookupRoleArn`, such as `arn:aws:iam::111122223333:role/example-resource-lookup-role-ResourceLookupRole-[OMITTED]`, that is the ARN of the role you created:

```
aws cloudformation describe-stacks \
  --region us-east-1 \
  --stack-name example-resource-lookup-role \
  --query "Stacks[].Outputs[]"
[
    {
        "OutputKey": "ResourceLookupRoleArn",
        "OutputValue": "arn:aws:iam::111122223333:role/example-resource-lookup-role-ResourceLookupRole-[OMITTED]"
    }
]
```

Next, create a VPC using, for example, the [AWS Command Line Interface](https://aws.amazon.com/cli/) (AWS CLI).  The scope of this exercise is to have an existing resource you can dynamically look up.  When you have completed the VPC creation using the command below, note the ID of the resulting VPC (e.g., `vpc-aaaabbbbccccdddd0`), as you'll need this information later on to delete the VPC when you are done:

```
aws ec2 create-vpc \
  --region us-east-1 \
  --cidr-block 10.0.0.0/16 \
  --amazon-provided-ipv6-cidr-block \
  --tag-specifications ResourceType=vpc,Tags='[{Key=Env,Value="dev"},{Key=Owner,Value="contract-test-only-test-team"}]' \
  --query Vpc.VpcId --output text
```

Build and submit the resource type to the [CloudFormation registry](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-register.html) as a private extension:

```
mvn clean verify
cfn submit --set-default --region us-east-1
```

Create a stack to consume the resource type; replace the IAM role placeholder text below with the ARN of the role you created earlier (such as, for example: `arn:aws:iam::111122223333:role/example-resource-lookup-role-ResourceLookupRole-[OMITTED]`):

```
aws cloudformation create-stack \
  --region us-east-1 \
  --stack-name resource-lookup-test-stack \
  --template-body file://examples/example-resource-lookup.template \
  --parameters ParameterKey=ResourceLookupRoleArn,ParameterValue=REPLACE_WITH_YOUR_IAM_ROLE_ARN

aws cloudformation wait stack-create-complete \
  --region us-east-1 \
  --stack-name resource-lookup-test-stack
```

When the stack creation is complete, describe the stack and note the ID of the VPC you created earlier in the `ResourceIdentifier` output:

```
aws cloudformation describe-stacks \
  --region us-east-1 \
  --stack-name resource-lookup-test-stack
```


### Cleanup
Delete the stack consuming the resource type:

```
aws cloudformation delete-stack \
  --region us-east-1 \
  --stack-name resource-lookup-test-stack

aws cloudformation wait stack-delete-complete \
  --region us-east-1 \
  --stack-name resource-lookup-test-stack
```

Delete the VPC you created above with the AWS CLI when done:

```
aws ec2 delete-vpc \
  --region us-east-1 \
  --vpc-id REPLACE_WITH_YOUR_VPC_ID
```

## Resource type registry submission with StackSets
This section will guide you through the process of submitting the resource type to the registry as a private extension using [AWS CloudFormation StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html), to multiple regions with one operation.

To get started, use the command below to build and package the resource type in an `awscommunity-resource-lookup.zip` ZIP archive:

```shell
mvn clean verify && cfn submit --dry-run
```

Upload the ZIP archive to a bucket you own; later on, you'll need to reference the object URL of this ZIP file you uploaded, so make a note of it.  You can also choose to use the `examples/private-registry-submit-s3-bucket.yaml` template to create a stack that, in turn, creates an S3 bucket to which you can upload the ZIP archive.

Following steps assume you'll choose to use the [self-managed permissions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-getting-started-create.html) to operate with StackSets.  To get started, prepare your account by following [Prerequisites for stack set operations](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs.html): follow steps in [Set up basic permissions for stack set operations](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.html#stacksets-prereqs-accountsetup), and create both the `AWSCloudFormationStackSetAdministrationRole` and `AWSCloudFormationStackSetExecutionRole` resources in your account.

Once ready, you'll use the AWS CloudFormation [console](https://console.aws.amazon.com/cloudformation/) to [Create a stack set](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-getting-started-create.html), for which you'll choose to use self-managed permissions:

- In the CloudFormation console, choose **StackSets**.
- Choose **Create StackSet**.
- In the **Choose a template** page, choose **Self-service permissions**.
- Specify the admin **IAM role name** you created earlier: `AWSCloudFormationStackSetAdministrationRole`.
- Specify the **IAM execution role name** you created earlier: `AWSCloudFormationStackSetExecutionRole`.
- Go to the **Prerequisite - Prepare template** section.
- Choose **Template is ready**.
- Specify the template to use in the **Specify template** section: choose to upload the `examples/private-registry-submit.yaml` template; alternatively, first upload the template to a bucket you own, and then provide the Amazon S3 template URL.  **Note that by using this template, if you choose to use [AWS Key Management Service](https://aws.amazon.com/kms/) (AWS KMS) to encrypt log data, you'll also create a KMS key for each region you'll choose**, and use each key with [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) log group resources that the template describes: you are not required to use KMS with log group resources, and if you choose not to use KMS, your Log group data will still be encrypted, because CloudWatch Logs uses server-side encryption by default to encrypt your log data at rest.
- Choose **Next**.
- In **Specify StackSet details**, specify the StackSet name and description.
- In **Parameters**, specify values you need.  In `SchemaHandlerPackage` parameter, specify the object URL of the ZIP archive you uploaded earlier.  Choose **Next**.
- In **Execution configuration**, choose the **Active** managed execution.  Choose **Next**.
- In **Accounts**, specify your [AWS account ID](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-identifiers.html#FindAccountId) in **Account numbers**.
- In the **Regions** section, specify the regions you need.
- In **Deployment options**, choose **Parallel** for **Region Concurrency**.  Choose **Next**.
- In the **Review** page, review your choices, and select **I acknowledge that AWS CloudFormation might create IAM resources**.
- Choose **Submit** to start the StackSet creation process.

## Development notes

### Contract tests
Contract tests help you validate that CloudFormation extensions (such as resource types and hooks) that you develop work as you'd expect.  Passing contract tests is required before an extension is published in the public registry; although not required for private extensions, it is highly recommended you implement contract test inputs for those as well, and to pass contract tests.  For more information, see [Testing resource types using contract tests](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-test.html).

To run contract tests, start with setting up a retry configuration in your `~/.aws/config` global AWS configuration file, should it be needed.  For more information, see [AWS CLI retries](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-retries.html).  Assuming you use a `default` profile, add this content to your file:

```
[default]
retry_mode = standard
max_attempts = 15
```

Next, open a new terminal window, and run:

```shell
sam local start-lambda
```

For more information, see [Testing resource types locally using AWS SAM](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-test.html#resource-type-develop-test).

Open another terminal window.  Create a stack using the `test/setup.yml` template, to create an `AWS::EC2::VPC` search target, and an IAM role to use for lookup operations; the template you are using will create an `Export` called `ResourceLookupRoleArn`, that contract test inputs in the `inputs` directory will reference using the `{{ResourceLookupRoleArn}}` syntax.  Run these commands to create the role and the output to export (the examples use the `us-east-1` region; adapt to the region you wish to use):

```
aws cloudformation create-stack \
  --region us-east-1 \
  --stack-name resource-lookup-setup \
  --template-body file://test/setup.yml \
  --capabilities CAPABILITY_NAMED_IAM

aws cloudformation wait stack-create-complete \
  --region us-east-1 \
  --stack-name resource-lookup-setup
```

Next, build this resource type, and run contract tests:

```shell
cfn generate && mvn clean verify && cfn test -v --enforce-timeout 90
```

Delete the stack when no longer needed:

```
aws cloudformation delete-stack \
  --region us-east-1 \
  --stack-name resource-lookup-setup

aws cloudformation wait stack-delete-complete \
  --region us-east-1 \
  --stack-name resource-lookup-setup
```

### Integration tests
The `test/integ.yml` template describes resources to perform an end-to-end testing of the resource (the examples use the `us-east-1` region; adapt to the region you wish to use):

```
aws cloudformation create-stack \
  --region us-east-1 \
  --stack-name resource-lookup-integ \
  --template-body file://test/integ.yml \
  --capabilities CAPABILITY_NAMED_IAM

aws cloudformation wait stack-create-complete \
  --region us-east-1 \
  --stack-name resource-lookup-integ
```

Delete the stack when no longer needed:

```
aws cloudformation delete-stack \
  --region us-east-1 \
  --stack-name resource-lookup-integ

aws cloudformation wait stack-delete-complete \
  --region us-east-1 \
  --stack-name resource-lookup-integ
```

### Schema
This resource type uses the `awscommunity-resource-lookup.json` JSON schema to describe its model.  The RPDK will automatically generate the correct resource model from the schema whenever the project is built via Maven.  You can also do this manually with the following command: `cfn generate`.

> Please don't modify files under `target/generated-sources/rpdk`, as they will be automatically overwritten.

The code uses [Lombok](https://projectlombok.org/), and [you may have to install IDE integrations](https://projectlombok.org/setup/overview) to enable auto-complete for Lombok-annotated classes.
