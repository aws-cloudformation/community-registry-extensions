# AwsCommunity::Config::ProactiveEval

- [Overview](#overview)

- [Deployment](#deployment)

- [Usage](#usage)

## Overview
[AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) is a service that allows you to continually assess, audit, and evaluate the configuration of your resources. 

One of the ways Config helps you to evaluate resources is through the use of **Config rules**. A Config rule evaluates your resource against a desired configuration and lets you know if the resource meets the configuration requirements. 

Config rules can be run in two [evaluation modes](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config-rules.html#aws-config-rules-evaluation-modes): **Detective mode** which evaluates resources that are already deployed, and [**Proactive mode**](https://aws.amazon.com/blogs/aws/new-aws-config-rules-now-support-proactive-compliance/) which evaluates resource properties before a resource is deployed. 

[AWS CloudFormation hooks](https://aws.amazon.com/blogs/mt/proactively-keep-resources-secure-and-compliant-with-aws-cloudformation-hooks/) allow customers to run code before creating, updating, or deleting resources with CloudFormation and can be used to provide automatic and proactive enforcement of requirements. Business requirement logic can be written directly in the hook, but hooks are also capable of calling external services. 

This CloudFormation hook calls the AWS Config proactive evaluation endpoint to check resources against Config rules that are enabled in the account. This allows customers to manage their resource configuration requirements directly in AWS Config rather than writing the business requirements in the code for the hook.

## Deployment

### Prerequisites
1. Building and registering this hook requires:
  
    a. A version of the Java JDK of 8 or higher, such as [Amazon Corretto](https://aws.amazon.com/corretto).

    b. [Maven](https://maven.apache.org/)

    c. The [CloudFormation CLI](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html)

2. Evaluating resource with this hook requires:
  
    a. AWS Config enabled in the AWS Account and Region where you will be registering the hook and deploying resources. A sample CloudFormation template to enable Config can be found at [cloudformation-samples/cfn-config-sample.json](./cloudformation-samples/cfn-config-sample.json)

    b. AWS Config rules enabled in **proactive mode** in the AWS Account and Region where you enabled Config. A sample CloudFormation template to enable a subset of Config rules can be found at [cloudformation-samples/cfn-config-rules-sample.json](./cloudformation-samples/cfn-config-rules-sample.json)


### Register the hook
The hook registration process is described in full detail in the [Registering hooks](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/registering-hooks.html) section of the CloudFormation CLI developer guide. 

When you reach the **Configure hooks** section of the registration process, use the following commands to configure the hook (instead of the one listed in the documentation).

1. Create a typeConfiguration.json file. 

In this case we are configuring the hook to return a success state and have CloudFormation continue with resource creation in the event that AWS Config returns Insufficient Data when evaluation the resource.

To change this behavior modify the OutcomeForComplianceTypeInsufficientData property to FAIL
```
cat <<EOF > typeConfiguration.json
{
    "CloudFormationConfiguration": {
        "HookConfiguration": {
            "TargetStacks": "ALL",
            "FailureMode": "FAIL",
            "Properties": {
                "OutcomeForComplianceTypeInsufficientData": "PASS"
            }
        }
    }
}
EOF
```

**Note:** The hook is currently configured to run when the following resource types are deployed. These resource types correspond with all resource types that currently have [rules to support proactive evaluation](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-evaluation-mode.html#heading:r1d:) in AWS Config.
```
"AWS::ApiGateway::Stage",
"AWS::AutoScaling::AutoScalingGroup",
"AWS::EC2::EIP",
"AWS::EC2::Instance",
"AWS::EC2::Subnet",
"AWS::Elasticsearch::Domain",
"AWS::Lambda::Function",
"AWS::RDS::DBInstance",
"AWS::Redshift::Cluster",
"AWS::S3::Bucket",
"AWS::SNS::Topic"
```

To configure the hook to only run for a specific subset of this list you can configure a `targetFilter` in the typeConfiguration. See [targetFilter](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hooks-structure.html#hooks-targetfilters) in the Hook configuration schema user guide for details.

2. Specify the hook configuration
```
$ aws cloudformation set-type-configuration --configuration file://typeConfiguration.json --type-arn $HOOK_TYPE_ARN
```

## Usage 

### Testing
The hook can be tested by provisioning CloudFormation stacks. Sample CloudFormation templates have been provided to test the hook once it is deployed. These can be found in the [cloudformation-samples](./cloudformation-samples/) directory. When using the provided sample Config rules template, these resource will all fail to create. 

Note that there is a [prerequisite](#prerequisites) to enable AWS Config and proactive Config rules to properly test the hook.

### Clean up
For information on how to update, deactivate, or deregister your hook, see [Managing Hooks](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/managing-hooks-python.html) in the AWS CloudFormation Hooks User Guide.
