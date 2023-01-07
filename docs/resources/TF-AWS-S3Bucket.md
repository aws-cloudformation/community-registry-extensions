
## TF::AWS::S3Bucket

Provides a S3 bucket resource.

-&gt; This functionality is for managing S3 in an AWS Partition. To manage [S3 on Outposts](https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonS3&#x2F;latest&#x2F;dev&#x2F;S3onOutposts.html), see the [&#x60;aws_s3control_bucket&#x60;](&#x2F;docs&#x2F;providers&#x2F;aws&#x2F;r&#x2F;s3control_bucket.html) resource.

- [Source](https:&#x2F;&#x2F;github.com&#x2F;iann0036&#x2F;cfn-tf-custom-types.git) 
- [Documentation]()

Published by Ian Mckay

## Schema
{% highlight json %}
{
    "typeName": "TF::AWS::S3Bucket",
    "description": "Provides a S3 bucket resource.\n\n-> This functionality is for managing S3 in an AWS Partition. To manage [S3 on Outposts](https://docs.aws.amazon.com/AmazonS3/latest/dev/S3onOutposts.html), see the [`aws_s3control_bucket`](/docs/providers/aws/r/s3control_bucket.html) resource.",
    "sourceUrl": "https://github.com/iann0036/cfn-tf-custom-types.git",
    "documentationUrl": "https://github.com/iann0036/cfn-tf-custom-types/blob/docs/resources/aws/TF-AWS-S3Bucket/docs/README.md",
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
        },
        "CorsRuleDefinition": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "AllowedHeaders": {
                    "type": "array",
                    "insertionOrder": false,
                    "items": {
                        "type": "string"
                    }
                },
                "AllowedMethods": {
                    "type": "array",
                    "insertionOrder": false,
                    "items": {
                        "type": "string"
                    }
                },
                "AllowedOrigins": {
                    "type": "array",
                    "insertionOrder": false,
                    "items": {
                        "type": "string"
                    }
                },
                "ExposeHeaders": {
                    "type": "array",
                    "insertionOrder": false,
                    "items": {
                        "type": "string"
                    }
                },
                "MaxAgeSeconds": {
                    "type": "number"
                }
            },
            "required": [
                "AllowedMethods",
                "AllowedOrigins"
            ]
        },
        "GrantDefinition": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "Id": {
                    "type": "string",
                    "description": "Canonical user id to grant for. Used only when `type` is `CanonicalUser`."
                },
                "Permissions": {
                    "type": "array",
                    "insertionOrder": true,
                    "items": {
                        "type": "string"
                    },
                    "description": "List of permissions to apply for grantee. Valid values are `READ`, `WRITE`, `READ_ACP`, `WRITE_ACP`, `FULL_CONTROL`."
                },
                "Type": {
                    "type": "string",
                    "description": "- Type of grantee to apply for. Valid values are `CanonicalUser` and `Group`. `AmazonCustomerByEmail` is not supported."
                },
                "Uri": {
                    "type": "string",
                    "description": "Uri address to grant for. Used only when `type` is `Group`."
                }
            },
            "required": [
                "Permissions",
                "Type"
            ]
        },
        "LifecycleRuleDefinition": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "AbortIncompleteMultipartUploadDays": {
                    "type": "number"
                },
                "Enabled": {
                    "type": "boolean",
                    "description": "Specifies lifecycle rule status."
                },
                "Id": {
                    "type": "string",
                    "description": "Unique identifier for the rule. Must be less than or equal to 255 characters in length."
                },
                "Prefix": {
                    "type": "string",
                    "description": "Object key prefix identifying one or more objects to which the rule applies."
                },
                "Tags": {
                    "type": "array",
                    "insertionOrder": true,
                    "items": {
                        "$ref": "#/definitions/TagsDefinition2"
                    },
                    "description": "Specifies object tags key and value."
                },
                "Expiration": {
                    "type": "array",
                    "insertionOrder": true,
                    "items": {
                        "$ref": "#/definitions/ExpirationDefinition"
                    },
                    "maxItems": 1
                },
                "NoncurrentVersionExpiration": {
                    "type": "array",
                    "insertionOrder": true,
                    "items": {
                        "$ref": "#/definitions/NoncurrentVersionExpirationDefinition"
                    },
                    "maxItems": 1
                },
                "NoncurrentVersionTransition": {
                    "type": "array",
                    "insertionOrder": false,
                    "items": {
                        "$ref": "#/definitions/NoncurrentVersionTransitionDefinition"
                    }
                },
                "Transition": {
                    "type": "array",
                    "insertionOrder": false,
                    "items": {
                        "$ref": "#/definitions/TransitionDefinition"
                    }
                }
            },
            "required": [
                "Enabled"
            ]
        },
        "TagsDefinition2": {
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
        "LoggingDefinition": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "TargetBucket": {
                    "type": "string",
                    "description": "The name of the bucket that will receive the log objects."
                },
                "TargetPrefix": {
                    "type": "string",
                    "description": "To specify a key prefix for log objects."
                }
            },
            "required": [
                "TargetBucket"
            ]
        },
        "ObjectLockConfigurationDefinition": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "ObjectLockEnabled": {
                    "type": "string",
                    "description": "Indicates whether this bucket has an Object Lock configuration enabled. Valid value is `Enabled`."
                },
                "Rule": {
                    "type": "array",
                    "insertionOrder": true,
                    "items": {
                        "$ref": "#/definitions/RuleDefinition"
                    },
                    "maxItems": 1
                }
            },
            "required": [
                "ObjectLockEnabled"
            ]
        },
        "ReplicationConfigurationDefinition": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "Role": {
                    "type": "string",
                    "description": "The ARN of the IAM role for Amazon S3 to assume when replicating the objects."
                },
                "Rules": {
                    "type": "array",
                    "insertionOrder": false,
                    "items": {
                        "$ref": "#/definitions/RulesDefinition"
                    },
                    "minItems": 1
                }
            },
            "required": [
                "Role"
            ]
        },
        "ServerSideEncryptionConfigurationDefinition": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "Rule": {
                    "type": "array",
                    "insertionOrder": true,
                    "items": {
                        "$ref": "#/definitions/RuleDefinition"
                    },
                    "maxItems": 1,
                    "minItems": 1
                }
            },
            "required": []
        },
        "VersioningDefinition": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "Enabled": {
                    "type": "boolean",
                    "description": "Enable versioning. Once you version-enable a bucket, it can never return to an unversioned state. You can, however, suspend versioning on that bucket."
                },
                "MfaDelete": {
                    "type": "boolean",
                    "description": "Enable MFA delete for either `Change the versioning state of your bucket` or `Permanently delete an object version`. Default is `false`. This cannot be used to toggle this setting but is available to allow managed buckets to reflect the state in AWS."
                }
            },
            "required": []
        },
        "WebsiteDefinition": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "ErrorDocument": {
                    "type": "string",
                    "description": "An absolute path to the document to return in case of a 4XX error."
                },
                "IndexDocument": {
                    "type": "string",
                    "description": "Amazon S3 returns this index document when requests are made to the root domain or any of the subfolders."
                },
                "RedirectAllRequestsTo": {
                    "type": "string",
                    "description": "A hostname to redirect all website requests for this bucket to. Hostname can optionally be prefixed with a protocol (`http://` or `https://`) to use when redirecting requests. The default is the protocol that is used in the original request."
                },
                "RoutingRules": {
                    "type": "string",
                    "description": "A json array containing [routing rules](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-websiteconfiguration-routingrules.html)\ndescribing redirect behavior and when redirects are applied."
                }
            },
            "required": []
        },
        "ExpirationDefinition": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "Date": {
                    "type": "string"
                },
                "Days": {
                    "type": "number"
                },
                "ExpiredObjectDeleteMarker": {
                    "type": "boolean"
                }
            },
            "required": []
        },
        "NoncurrentVersionExpirationDefinition": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "Days": {
                    "type": "number"
                }
            },
            "required": []
        },
        "NoncurrentVersionTransitionDefinition": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "Days": {
                    "type": "number"
                },
                "StorageClass": {
                    "type": "string"
                }
            },
            "required": [
                "StorageClass"
            ]
        },
        "TransitionDefinition": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "Date": {
                    "type": "string"
                },
                "Days": {
                    "type": "number"
                },
                "StorageClass": {
                    "type": "string"
                }
            },
            "required": [
                "StorageClass"
            ]
        },
        "RuleDefinition": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "BucketKeyEnabled": {
                    "type": "boolean",
                    "description": "Whether or not to use [Amazon S3 Bucket Keys](https://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-key.html) for SSE-KMS."
                },
                "ApplyServerSideEncryptionByDefault": {
                    "type": "array",
                    "insertionOrder": true,
                    "items": {
                        "$ref": "#/definitions/ApplyServerSideEncryptionByDefaultDefinition"
                    },
                    "maxItems": 1,
                    "minItems": 1
                }
            },
            "required": []
        },
        "RulesDefinition": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "Id": {
                    "type": "string",
                    "description": "Unique identifier for the rule. Must be less than or equal to 255 characters in length."
                },
                "Prefix": {
                    "type": "string",
                    "description": "Object keyname prefix identifying one or more objects to which the rule applies. Must be less than or equal to 1024 characters in length."
                },
                "Priority": {
                    "type": "number",
                    "description": "The priority associated with the rule."
                },
                "Status": {
                    "type": "string",
                    "description": "The status of the rule. Either `Enabled` or `Disabled`. The rule is ignored if status is not Enabled."
                },
                "Destination": {
                    "type": "array",
                    "insertionOrder": true,
                    "items": {
                        "$ref": "#/definitions/DestinationDefinition"
                    },
                    "maxItems": 1,
                    "minItems": 1
                },
                "Filter": {
                    "type": "array",
                    "insertionOrder": true,
                    "items": {
                        "$ref": "#/definitions/FilterDefinition"
                    },
                    "maxItems": 1
                },
                "SourceSelectionCriteria": {
                    "type": "array",
                    "insertionOrder": true,
                    "items": {
                        "$ref": "#/definitions/SourceSelectionCriteriaDefinition"
                    },
                    "maxItems": 1
                }
            },
            "required": [
                "Status"
            ]
        },
        "ApplyServerSideEncryptionByDefaultDefinition": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "KmsMasterKeyId": {
                    "type": "string",
                    "description": "The AWS KMS master key ID used for the SSE-KMS encryption. This can only be used when you set the value of `sse_algorithm` as `aws:kms`. The default `aws/s3` AWS KMS master key is used if this element is absent while the `sse_algorithm` is `aws:kms`."
                },
                "SseAlgorithm": {
                    "type": "string",
                    "description": "The server-side encryption algorithm to use. Valid values are `AES256` and `aws:kms`."
                }
            },
            "required": [
                "SseAlgorithm"
            ]
        },
        "DestinationDefinition": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "AccountId": {
                    "type": "string",
                    "description": "The Account ID to use for overriding the object owner on replication. Must be used in conjunction with `access_control_translation` override configuration."
                },
                "Bucket": {
                    "type": "string",
                    "description": "The ARN of the S3 bucket where you want Amazon S3 to store replicas of the object identified by the rule."
                },
                "ReplicaKmsKeyId": {
                    "type": "string",
                    "description": "Destination KMS encryption key ARN for SSE-KMS replication. Must be used in conjunction with\n`sse_kms_encrypted_objects` source selection criteria."
                },
                "StorageClass": {
                    "type": "string",
                    "description": "The class of storage used to store the object. Can be `STANDARD`, `REDUCED_REDUNDANCY`, `STANDARD_IA`, `ONEZONE_IA`, `INTELLIGENT_TIERING`, `GLACIER`, or `DEEP_ARCHIVE`."
                },
                "AccessControlTranslation": {
                    "type": "array",
                    "insertionOrder": true,
                    "items": {
                        "$ref": "#/definitions/AccessControlTranslationDefinition"
                    },
                    "maxItems": 1
                }
            },
            "required": [
                "Bucket"
            ]
        },
        "FilterDefinition": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "Prefix": {
                    "type": "string",
                    "description": "Object keyname prefix that identifies subset of objects to which the rule applies. Must be less than or equal to 1024 characters in length."
                },
                "Tags": {
                    "type": "array",
                    "insertionOrder": true,
                    "items": {
                        "$ref": "#/definitions/TagsDefinition3"
                    },
                    "description": "A map of tags that identifies subset of objects to which the rule applies.\nThe rule applies only to objects having all the tags in its tagset."
                }
            },
            "required": []
        },
        "TagsDefinition3": {
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
        "SourceSelectionCriteriaDefinition": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "SseKmsEncryptedObjects": {
                    "type": "array",
                    "insertionOrder": true,
                    "items": {
                        "$ref": "#/definitions/SseKmsEncryptedObjectsDefinition"
                    },
                    "maxItems": 1
                }
            },
            "required": []
        },
        "AccessControlTranslationDefinition": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "Owner": {
                    "type": "string",
                    "description": "The override value for the owner on replicated objects. Currently only `Destination` is supported."
                }
            },
            "required": [
                "Owner"
            ]
        },
        "SseKmsEncryptedObjectsDefinition": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "Enabled": {
                    "type": "boolean",
                    "description": "Boolean which indicates if this criteria is enabled."
                }
            },
            "required": [
                "Enabled"
            ]
        }
    },
    "properties": {
        "tfcfnid": {
            "description": "Internal identifier for tracking resource changes. Do not use.",
            "type": "string"
        },
        "AccelerationStatus": {
            "type": "string",
            "description": "Sets the accelerate configuration of an existing bucket. Can be `Enabled` or `Suspended`."
        },
        "Acl": {
            "type": "string",
            "description": "The [canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl) to apply. Valid values are `private`, `public-read`, `public-read-write`, `aws-exec-read`, `authenticated-read`, and `log-delivery-write`. Defaults to `private`.  Conflicts with `grant`."
        },
        "Arn": {
            "type": "string"
        },
        "Bucket": {
            "type": "string",
            "description": "The name of the bucket. If omitted, Terraform will assign a random, unique name. Must be less than or equal to 63 characters in length."
        },
        "BucketDomainName": {
            "type": "string"
        },
        "BucketPrefix": {
            "type": "string",
            "description": "Creates a unique bucket name beginning with the specified prefix. Conflicts with `bucket`. Must be less than or equal to 37 characters in length."
        },
        "BucketRegionalDomainName": {
            "type": "string"
        },
        "ForceDestroy": {
            "type": "boolean",
            "description": "A boolean that indicates all objects (including any [locked objects](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock-overview.html)) should be deleted from the bucket so that the bucket can be destroyed without error. These objects are *not* recoverable."
        },
        "HostedZoneId": {
            "type": "string"
        },
        "Id": {
            "type": "string"
        },
        "Policy": {
            "type": "string",
            "description": "A valid [bucket policy](https://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies.html) JSON document. Note that if the policy document is not specific enough (but still valid), Terraform may view the policy as constantly changing in a `terraform plan`. In this case, please make sure you use the verbose/specific version of the policy. For more information about building AWS IAM policy documents with Terraform, see the [AWS IAM Policy Document Guide](https://learn.hashicorp.com/terraform/aws/iam-policy)."
        },
        "Region": {
            "type": "string"
        },
        "RequestPayer": {
            "type": "string",
            "description": "Specifies who should bear the cost of Amazon S3 data transfer.\nCan be either `BucketOwner` or `Requester`. By default, the owner of the S3 bucket would incur\nthe costs of any data transfer. See [Requester Pays Buckets](http://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html)\ndeveloper guide for more information."
        },
        "Tags": {
            "type": "array",
            "insertionOrder": true,
            "items": {
                "$ref": "#/definitions/TagsDefinition"
            },
            "description": "A map of tags to assign to the bucket. If configured with a provider [`default_tags` configuration block](/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level."
        },
        "TagsAll": {
            "type": "array",
            "insertionOrder": true,
            "items": {
                "$ref": "#/definitions/TagsAllDefinition"
            }
        },
        "WebsiteDomain": {
            "type": "string"
        },
        "WebsiteEndpoint": {
            "type": "string"
        },
        "CorsRule": {
            "type": "array",
            "insertionOrder": false,
            "items": {
                "$ref": "#/definitions/CorsRuleDefinition"
            }
        },
        "Grant": {
            "type": "array",
            "insertionOrder": true,
            "items": {
                "$ref": "#/definitions/GrantDefinition"
            }
        },
        "LifecycleRule": {
            "type": "array",
            "insertionOrder": false,
            "items": {
                "$ref": "#/definitions/LifecycleRuleDefinition"
            }
        },
        "Logging": {
            "type": "array",
            "insertionOrder": true,
            "items": {
                "$ref": "#/definitions/LoggingDefinition"
            }
        },
        "ObjectLockConfiguration": {
            "type": "array",
            "insertionOrder": false,
            "items": {
                "$ref": "#/definitions/ObjectLockConfigurationDefinition"
            },
            "maxItems": 1
        },
        "ReplicationConfiguration": {
            "type": "array",
            "insertionOrder": false,
            "items": {
                "$ref": "#/definitions/ReplicationConfigurationDefinition"
            },
            "maxItems": 1
        },
        "ServerSideEncryptionConfiguration": {
            "type": "array",
            "insertionOrder": false,
            "items": {
                "$ref": "#/definitions/ServerSideEncryptionConfigurationDefinition"
            },
            "maxItems": 1
        },
        "Versioning": {
            "type": "array",
            "insertionOrder": false,
            "items": {
                "$ref": "#/definitions/VersioningDefinition"
            },
            "maxItems": 1
        },
        "Website": {
            "type": "array",
            "insertionOrder": false,
            "items": {
                "$ref": "#/definitions/WebsiteDefinition"
            },
            "maxItems": 1
        }
    },
    "additionalProperties": false,
    "required": [],
    "readOnlyProperties": [
        "/properties/tfcfnid",
        "/properties/BucketDomainName",
        "/properties/BucketRegionalDomainName",
        "/properties/Id",
        "/properties/Region"
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
