
## TF::Google::StorageBucket

## Creates a new bucket in Google cloud storage service (GCS).
Once a bucket has been created, its location can&#39;t be changed.

For more information see
[the official documentation](https:&#x2F;&#x2F;cloud.google.com&#x2F;storage&#x2F;docs&#x2F;overview)
and
[API](https:&#x2F;&#x2F;cloud.google.com&#x2F;storage&#x2F;docs&#x2F;json_api&#x2F;v1&#x2F;buckets).

**Note**: If the project id is not set on the resource or in the provider block it will be dynamically
determined which will require enabling the compute api.

- [Source](https:&#x2F;&#x2F;github.com&#x2F;iann0036&#x2F;cfn-tf-custom-types.git) 
- [Documentation]()

Published by Ian Mckay

## Schema
{% highlight json %}
{
    "typeName": "TF::Google::StorageBucket",
    "description": "Creates a new bucket in Google cloud storage service (GCS).\nOnce a bucket has been created, its location can't be changed.\n\nFor more information see\n[the official documentation](https://cloud.google.com/storage/docs/overview)\nand\n[API](https://cloud.google.com/storage/docs/json_api/v1/buckets).\n\n**Note**: If the project id is not set on the resource or in the provider block it will be dynamically\ndetermined which will require enabling the compute api.",
    "sourceUrl": "https://github.com/iann0036/cfn-tf-custom-types.git",
    "documentationUrl": "https://github.com/iann0036/cfn-tf-custom-types/blob/docs/resources/google/TF-Google-StorageBucket/docs/README.md",
    "definitions": {
        "LabelsDefinition": {
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
        "CorsDefinition": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "MaxAgeSeconds": {
                    "type": "number",
                    "description": "The value, in seconds, to return in the [Access-Control-Max-Age header](https://www.w3.org/TR/cors/#access-control-max-age-response-header) used in preflight responses."
                },
                "Method": {
                    "type": "array",
                    "insertionOrder": false,
                    "items": {
                        "type": "string"
                    },
                    "description": "The list of HTTP methods on which to include CORS response headers, (GET, OPTIONS, POST, etc) Note: \"*\" is permitted in the list of methods, and means \"any method\"."
                },
                "Origin": {
                    "type": "array",
                    "insertionOrder": false,
                    "items": {
                        "type": "string"
                    },
                    "description": "The list of [Origins](https://tools.ietf.org/html/rfc6454) eligible to receive CORS response headers. Note: \"*\" is permitted in the list of origins, and means \"any Origin\"."
                },
                "ResponseHeader": {
                    "type": "array",
                    "insertionOrder": false,
                    "items": {
                        "type": "string"
                    },
                    "description": "The list of HTTP headers other than the [simple response headers](https://www.w3.org/TR/cors/#simple-response-header) to give permission for the user-agent to share across domains."
                }
            },
            "required": []
        },
        "EncryptionDefinition": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "DefaultKmsKeyName": {
                    "type": "string"
                }
            },
            "required": [
                "DefaultKmsKeyName"
            ]
        },
        "LifecycleRuleDefinition": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "Action": {
                    "type": "array",
                    "insertionOrder": false,
                    "items": {
                        "$ref": "#/definitions/ActionDefinition"
                    },
                    "maxItems": 1,
                    "minItems": 1
                },
                "Condition": {
                    "type": "array",
                    "insertionOrder": false,
                    "items": {
                        "$ref": "#/definitions/ConditionDefinition"
                    },
                    "maxItems": 1,
                    "minItems": 1
                }
            },
            "required": []
        },
        "LoggingDefinition": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "LogBucket": {
                    "type": "string",
                    "description": "The bucket that will receive log objects."
                },
                "LogObjectPrefix": {
                    "type": "string",
                    "description": "The object prefix for log objects. If it's not provided,\nby default GCS sets this to this bucket's name."
                }
            },
            "required": [
                "LogBucket"
            ]
        },
        "RetentionPolicyDefinition": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "IsLocked": {
                    "type": "boolean",
                    "description": "If set to `true`, the bucket will be [locked](https://cloud.google.com/storage/docs/using-bucket-lock#lock-bucket) and permanently restrict edits to the bucket's retention policy.  Caution: Locking a bucket is an irreversible action."
                },
                "RetentionPeriod": {
                    "type": "number",
                    "description": "The period of time, in seconds, that objects in the bucket must be retained and cannot be deleted, overwritten, or archived. The value must be less than 2,147,483,647 seconds."
                }
            },
            "required": [
                "RetentionPeriod"
            ]
        },
        "VersioningDefinition": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "Enabled": {
                    "type": "boolean",
                    "description": "While set to `true`, versioning is fully enabled for this bucket."
                }
            },
            "required": [
                "Enabled"
            ]
        },
        "WebsiteDefinition": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "MainPageSuffix": {
                    "type": "string",
                    "description": "Behaves as the bucket's directory index where\nmissing objects are treated as potential directories."
                },
                "NotFoundPage": {
                    "type": "string",
                    "description": "The custom object to return when a requested\nresource is not found."
                }
            },
            "required": []
        },
        "ActionDefinition": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "StorageClass": {
                    "type": "string",
                    "description": "The target [Storage Class](https://cloud.google.com/storage/docs/storage-classes) of objects affected by this Lifecycle Rule. Supported values include: `STANDARD`, `MULTI_REGIONAL`, `REGIONAL`, `NEARLINE`, `COLDLINE`, `ARCHIVE`."
                },
                "Type": {
                    "type": "string",
                    "description": "The type of the action of this Lifecycle Rule. Supported values include: `Delete` and `SetStorageClass`."
                }
            },
            "required": [
                "Type"
            ]
        },
        "ConditionDefinition": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "Age": {
                    "type": "number",
                    "description": "Minimum age of an object in days to satisfy this condition."
                },
                "CreatedBefore": {
                    "type": "string",
                    "description": "A date in the RFC 3339 format YYYY-MM-DD. This condition is satisfied when an object is created before midnight of the specified date in UTC."
                },
                "CustomTimeBefore": {
                    "type": "string",
                    "description": "A date in the RFC 3339 format YYYY-MM-DD. This condition is satisfied when the customTime metadata for the object is set to an earlier date than the date used in this lifecycle condition."
                },
                "DaysSinceCustomTime": {
                    "type": "number",
                    "description": "Days since the date set in the `customTime` metadata for the object. This condition is satisfied when the current date and time is at least the specified number of days after the `customTime`."
                },
                "DaysSinceNoncurrentTime": {
                    "type": "number",
                    "description": "Relevant only for versioned objects. Number of days elapsed since the noncurrent timestamp of an object."
                },
                "MatchesStorageClass": {
                    "type": "array",
                    "insertionOrder": false,
                    "items": {
                        "type": "string"
                    },
                    "description": "[Storage Class](https://cloud.google.com/storage/docs/storage-classes) of objects to satisfy this condition. Supported values include: `STANDARD`, `MULTI_REGIONAL`, `REGIONAL`, `NEARLINE`, `COLDLINE`, `ARCHIVE`, `DURABLE_REDUCED_AVAILABILITY`."
                },
                "NoncurrentTimeBefore": {
                    "type": "string",
                    "description": "Relevant only for versioned objects. The date in RFC 3339 (e.g. `2017-06-13`) when the object became nonconcurrent."
                },
                "NumNewerVersions": {
                    "type": "number",
                    "description": "Relevant only for versioned objects. The number of newer versions of an object to satisfy this condition."
                },
                "WithState": {
                    "type": "string",
                    "description": "Match to live and/or archived objects. Unversioned buckets have only live objects. Supported values include: `\"LIVE\"`, `\"ARCHIVED\"`, `\"ANY\"`."
                }
            },
            "required": []
        }
    },
    "properties": {
        "tfcfnid": {
            "description": "Internal identifier for tracking resource changes. Do not use.",
            "type": "string"
        },
        "BucketPolicyOnly": {
            "type": "boolean",
            "description": "Enables [Bucket Policy Only](https://cloud.google.com/storage/docs/bucket-policy-only) access to a bucket. This field will be removed in the next major release of the provider."
        },
        "DefaultEventBasedHold": {
            "type": "boolean"
        },
        "ForceDestroy": {
            "type": "boolean",
            "description": "When deleting a bucket, this\nboolean option will delete all contained objects. If you try to delete a\nbucket that contains objects, Terraform will fail that run."
        },
        "Id": {
            "type": "string"
        },
        "Labels": {
            "type": "array",
            "insertionOrder": true,
            "items": {
                "$ref": "#/definitions/LabelsDefinition"
            },
            "description": "A map of key/value label pairs to assign to the bucket."
        },
        "Location": {
            "type": "string",
            "description": "The [GCS location](https://cloud.google.com/storage/docs/bucket-locations)."
        },
        "Name": {
            "type": "string",
            "description": "The name of the bucket."
        },
        "Project": {
            "type": "string",
            "description": "The ID of the project in which the resource belongs. If it\nis not provided, the provider project is used."
        },
        "RequesterPays": {
            "type": "boolean",
            "description": "Enables [Requester Pays](https://cloud.google.com/storage/docs/requester-pays) on a storage bucket."
        },
        "SelfLink": {
            "type": "string"
        },
        "StorageClass": {
            "type": "string",
            "description": "The [Storage Class](https://cloud.google.com/storage/docs/storage-classes) of the new bucket. Supported values include: `STANDARD`, `MULTI_REGIONAL`, `REGIONAL`, `NEARLINE`, `COLDLINE`, `ARCHIVE`."
        },
        "UniformBucketLevelAccess": {
            "type": "boolean",
            "description": "Enables [Uniform bucket-level access](https://cloud.google.com/storage/docs/uniform-bucket-level-access) access to a bucket."
        },
        "Url": {
            "type": "string"
        },
        "Cors": {
            "type": "array",
            "insertionOrder": false,
            "items": {
                "$ref": "#/definitions/CorsDefinition"
            }
        },
        "Encryption": {
            "type": "array",
            "insertionOrder": false,
            "items": {
                "$ref": "#/definitions/EncryptionDefinition"
            },
            "maxItems": 1
        },
        "LifecycleRule": {
            "type": "array",
            "insertionOrder": false,
            "items": {
                "$ref": "#/definitions/LifecycleRuleDefinition"
            },
            "maxItems": 100
        },
        "Logging": {
            "type": "array",
            "insertionOrder": false,
            "items": {
                "$ref": "#/definitions/LoggingDefinition"
            },
            "maxItems": 1
        },
        "RetentionPolicy": {
            "type": "array",
            "insertionOrder": false,
            "items": {
                "$ref": "#/definitions/RetentionPolicyDefinition"
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
    "required": [
        "Name"
    ],
    "readOnlyProperties": [
        "/properties/tfcfnid",
        "/properties/Id",
        "/properties/SelfLink",
        "/properties/Url"
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
