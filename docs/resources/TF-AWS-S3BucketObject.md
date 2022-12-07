
## TF::AWS::S3BucketObject

## Provides a S3 bucket object resource.

- [Source](https:&#x2F;&#x2F;github.com&#x2F;iann0036&#x2F;cfn-tf-custom-types.git) 
- [Documentation]()

Published by Ian Mckay

## Schema
{% highlight json %}
{
    "typeName": "TF::AWS::S3BucketObject",
    "description": "Provides a S3 bucket object resource.",
    "sourceUrl": "https://github.com/iann0036/cfn-tf-custom-types.git",
    "documentationUrl": "https://github.com/iann0036/cfn-tf-custom-types/blob/docs/resources/aws/TF-AWS-S3BucketObject/docs/README.md",
    "definitions": {
        "MetadataDefinition": {
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
        "Acl": {
            "type": "string",
            "description": "The [canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl) to apply. Valid values are `private`, `public-read`, `public-read-write`, `aws-exec-read`, `authenticated-read`, `bucket-owner-read`, and `bucket-owner-full-control`. Defaults to `private`."
        },
        "Bucket": {
            "type": "string",
            "description": "The name of the bucket to put the file in. Alternatively, an [S3 access point](https://docs.aws.amazon.com/AmazonS3/latest/dev/using-access-points.html) ARN can be specified."
        },
        "BucketKeyEnabled": {
            "type": "boolean",
            "description": "Whether or not to use [Amazon S3 Bucket Keys](https://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-key.html) for SSE-KMS."
        },
        "CacheControl": {
            "type": "string",
            "description": "Specifies caching behavior along the request/reply chain Read [w3c cache_control](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9) for further details."
        },
        "Content": {
            "type": "string",
            "description": "Literal string value to use as the object content, which will be uploaded as UTF-8-encoded text."
        },
        "ContentBase64": {
            "type": "string",
            "description": "Base64-encoded data that will be decoded and uploaded as raw bytes for the object content. This allows safely uploading non-UTF8 binary data, but is recommended only for small content such as the result of the `gzipbase64` function with small text strings. For larger objects, use `source` to stream the content from a disk file."
        },
        "ContentDisposition": {
            "type": "string",
            "description": "Specifies presentational information for the object. Read [w3c content_disposition](http://www.w3.org/Protocols/rfc2616/rfc2616-sec19.html#sec19.5.1) for further information."
        },
        "ContentEncoding": {
            "type": "string",
            "description": "Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field. Read [w3c content encoding](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.11) for further information."
        },
        "ContentLanguage": {
            "type": "string",
            "description": "The language the content is in e.g. en-US or en-GB."
        },
        "ContentType": {
            "type": "string",
            "description": "A standard MIME type describing the format of the object data, e.g. application/octet-stream. All Valid MIME Types are valid for this input."
        },
        "Etag": {
            "type": "string",
            "description": "Used to trigger updates. The only meaningful value is `${filemd5(\"path/to/file\")}` (Terraform 0.11.12 or later) or `${md5(file(\"path/to/file\"))}` (Terraform 0.11.11 or earlier).\nThis attribute is not compatible with KMS encryption, `kms_key_id` or `server_side_encryption = \"aws:kms\"`."
        },
        "ForceDestroy": {
            "type": "boolean",
            "description": "Allow the object to be deleted by removing any legal hold on any object version.\nDefault is `false`. This value should be set to `true` only if the bucket has S3 object lock enabled."
        },
        "Id": {
            "type": "string"
        },
        "Key": {
            "type": "string",
            "description": "The name of the object once it is in the bucket."
        },
        "KmsKeyId": {
            "type": "string",
            "description": "Amazon Resource Name (ARN) of the KMS Key to use for object encryption. If the S3 Bucket has server-side encryption enabled, that value will automatically be used. If referencing the\n`aws_kms_key` resource, use the `arn` attribute. If referencing the `aws_kms_alias` data source or resource, use the `target_key_arn` attribute. Terraform will only perform drift detection if a configuration value\nis provided."
        },
        "Metadata": {
            "type": "array",
            "insertionOrder": true,
            "items": {
                "$ref": "#/definitions/MetadataDefinition"
            },
            "description": "A map of keys/values to provision metadata (will be automatically prefixed by `x-amz-meta-`, note that only lowercase label are currently supported by the AWS Go API)."
        },
        "ObjectLockLegalHoldStatus": {
            "type": "string",
            "description": "The [legal hold](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock-overview.html#object-lock-legal-holds) status that you want to apply to the specified object. Valid values are `ON` and `OFF`."
        },
        "ObjectLockMode": {
            "type": "string",
            "description": "The object lock [retention mode](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock-overview.html#object-lock-retention-modes) that you want to apply to this object. Valid values are `GOVERNANCE` and `COMPLIANCE`."
        },
        "ObjectLockRetainUntilDate": {
            "type": "string",
            "description": "The date and time, in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8), when this object's object lock will [expire](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock-overview.html#object-lock-retention-periods)."
        },
        "ServerSideEncryption": {
            "type": "string",
            "description": "Specifies server-side encryption of the object in S3. Valid values are \"`AES256`\" and \"`aws:kms`\"."
        },
        "Source": {
            "type": "string",
            "description": "The path to a file that will be read and uploaded as raw bytes for the object content."
        },
        "StorageClass": {
            "type": "string",
            "description": "Specifies the desired [Storage Class](http://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html)\nfor the object. Can be either \"`STANDARD`\", \"`REDUCED_REDUNDANCY`\", \"`ONEZONE_IA`\", \"`INTELLIGENT_TIERING`\", \"`GLACIER`\", \"`DEEP_ARCHIVE`\", or \"`STANDARD_IA`\". Defaults to \"`STANDARD`\"."
        },
        "Tags": {
            "type": "array",
            "insertionOrder": true,
            "items": {
                "$ref": "#/definitions/TagsDefinition"
            },
            "description": "A map of tags to assign to the object. If configured with a provider [`default_tags` configuration block](/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level."
        },
        "TagsAll": {
            "type": "array",
            "insertionOrder": true,
            "items": {
                "$ref": "#/definitions/TagsAllDefinition"
            }
        },
        "VersionId": {
            "type": "string"
        },
        "WebsiteRedirect": {
            "type": "string",
            "description": "Specifies a target URL for [website redirect](http://docs.aws.amazon.com/AmazonS3/latest/dev/how-to-page-redirect.html)."
        }
    },
    "additionalProperties": false,
    "required": [
        "Bucket",
        "Key"
    ],
    "readOnlyProperties": [
        "/properties/tfcfnid",
        "/properties/Id",
        "/properties/VersionId"
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
