
## TF::AWS::KeyPair

Provides an [EC2 key pair](https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSEC2&#x2F;latest&#x2F;UserGuide&#x2F;ec2-key-pairs.html) resource. A key pair is used to control login access to EC2 instances.

Currently this resource requires an existing user-supplied key pair. This key pair&#39;s public key will be registered with AWS to allow logging-in to EC2 instances.

When importing an existing key pair the public key material may be in any format supported by AWS. Supported formats (per the [AWS documentation](https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSEC2&#x2F;latest&#x2F;UserGuide&#x2F;ec2-key-pairs.html#how-to-generate-your-own-key-and-import-it-to-aws)) are:

* OpenSSH public key format (the format in ~&#x2F;.ssh&#x2F;authorized_keys)
* Base64 encoded DER format
* SSH public key file format as specified in RFC4716

- [Source](https:&#x2F;&#x2F;github.com&#x2F;iann0036&#x2F;cfn-tf-custom-types.git) 
- [Documentation]()

Published by Ian Mckay

## Schema
{% highlight json %}
{
    "typeName": "TF::AWS::KeyPair",
    "description": "Provides an [EC2 key pair](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html) resource. A key pair is used to control login access to EC2 instances.\n\nCurrently this resource requires an existing user-supplied key pair. This key pair's public key will be registered with AWS to allow logging-in to EC2 instances.\n\nWhen importing an existing key pair the public key material may be in any format supported by AWS. Supported formats (per the [AWS documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html#how-to-generate-your-own-key-and-import-it-to-aws)) are:\n\n* OpenSSH public key format (the format in ~/.ssh/authorized_keys)\n* Base64 encoded DER format\n* SSH public key file format as specified in RFC4716",
    "sourceUrl": "https://github.com/iann0036/cfn-tf-custom-types.git",
    "documentationUrl": "https://github.com/iann0036/cfn-tf-custom-types/blob/docs/resources/aws/TF-AWS-KeyPair/docs/README.md",
    "definitions": {
        "TagsDefinition": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "MapKey": {
                    "type": "string"
                },
                "MapValue": {
                    "type": "string"
                }
            },
            "required": [
                "MapKey",
                "MapValue"
            ]
        },
        "TagsAllDefinition": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "MapKey": {
                    "type": "string"
                },
                "MapValue": {
                    "type": "string"
                }
            },
            "required": [
                "MapKey",
                "MapValue"
            ]
        }
    },
    "properties": {
        "tfcfnid": {
            "description": "Internal identifier for tracking resource changes. Do not use.",
            "type": "string"
        },
        "Arn": {
            "type": "string"
        },
        "Fingerprint": {
            "type": "string"
        },
        "Id": {
            "type": "string"
        },
        "KeyName": {
            "type": "string",
            "description": "The name for the key pair."
        },
        "KeyNamePrefix": {
            "type": "string",
            "description": "Creates a unique name beginning with the specified prefix. Conflicts with `key_name`."
        },
        "KeyPairId": {
            "type": "string"
        },
        "PublicKey": {
            "type": "string",
            "description": "The public key material."
        },
        "Tags": {
            "type": "array",
            "insertionOrder": true,
            "items": {
                "$ref": "#/definitions/TagsDefinition"
            },
            "description": "Key-value map of resource tags. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level."
        },
        "TagsAll": {
            "type": "array",
            "insertionOrder": true,
            "items": {
                "$ref": "#/definitions/TagsAllDefinition"
            }
        }
    },
    "additionalProperties": false,
    "required": [
        "PublicKey"
    ],
    "readOnlyProperties": [
        "/properties/tfcfnid",
        "/properties/Arn",
        "/properties/Fingerprint",
        "/properties/Id",
        "/properties/KeyPairId"
    ],
    "primaryIdentifier": [
        "/properties/tfcfnid"
    ],
    "handlers": {
        "create": {
            "permissions": [
                "s3:GetObject",
                "s3:DeleteObject",
                "lambda:InvokeFunction"
            ]
        },
        "read": {
            "permissions": [
                "s3:GetObject"
            ]
        },
        "update": {
            "permissions": [
                "s3:GetObject",
                "s3:DeleteObject",
                "lambda:InvokeFunction"
            ]
        },
        "delete": {
            "permissions": [
                "s3:GetObject",
                "s3:DeleteObject",
                "lambda:InvokeFunction"
            ]
        },
        "list": {
            "permissions": [
                "s3:GetObject",
                "s3:ListBucket"
            ]
        }
    }
}
{% endhighlight %}
