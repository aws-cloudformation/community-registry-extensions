# AwsCommunity::RDS::MultiAZCheck

Validates all RDS Instances created and updated with CloudFormation stacks to ensure that they have the multiAZ setting enabled. 
This is modeled after the Trusted Advisor MultiAZ check: https://docs.aws.amazon.com/awssupport/latest/user/fault-tolerance-checks.html#amazon-rds-multi-az


## Configuration

```bash


# enable the hook
aws cloudformation set-type-configuration 
  --configuration "{\"CloudFormationConfiguration\":{\"HookConfiguration\":{\"TargetStacks\":\"ALL\",\"FailureMode\":\"FAIL\",\"Properties\":{}}}}" \\n--type-arn <ARN of your hook>

```

## Example templates

The Hook will find this template to be non-compliant.
```json

{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
        "RDSInstance": {
            "Type": "AWS::RDS::DBInstance",
            "Properties": {
                "DBName"            : "CompliantDB" ,
                "Engine"            : "MySQL",
                "MultiAZ"           : false,
                "MasterUsername"    : "admin",
                "DBInstanceClass"   : "db.t2.small",
                "AllocatedStorage"  : "10",
                "MasterUserPassword": "password"
            }
        }
    }
}
```

This template will be found as compliant and deploy successfully.
```json
{
"AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
        "RDSInstance": {
            "Type": "AWS::RDS::DBInstance",
            "Properties": {
                "DBName"            : "CompliantDB" ,
                "Engine"            : "MySQL",
                "MultiAZ"           : true,
                "MasterUsername"    : "admin",
                "DBInstanceClass"   : "db.t2.small",
                "AllocatedStorage"  : "10",
                "MasterUserPassword": "password"
            }
        }
    }
}
```