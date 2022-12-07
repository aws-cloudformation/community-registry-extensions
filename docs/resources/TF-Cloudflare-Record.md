
## TF::Cloudflare::Record

## Provides a Cloudflare record resource.

- [Source](https:&#x2F;&#x2F;github.com&#x2F;iann0036&#x2F;cfn-tf-custom-types.git) 
- [Documentation]()

Published by Ian Mckay

## Schema
{% highlight json %}
{
    "typeName": "TF::Cloudflare::Record",
    "description": "Provides a Cloudflare record resource.",
    "sourceUrl": "https://github.com/iann0036/cfn-tf-custom-types.git",
    "documentationUrl": "https://github.com/iann0036/cfn-tf-custom-types/blob/docs/resources/cloudflare/TF-Cloudflare-Record/docs/README.md",
    "definitions": {
        "DataDefinition": {
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
        "TimeoutsDefinition": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "Create": {
                    "type": "string"
                },
                "Update": {
                    "type": "string"
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
        "CreatedOn": {
            "type": "string"
        },
        "Data": {
            "type": "array",
            "insertionOrder": true,
            "items": {
                "$ref": "#/definitions/DataDefinition"
            },
            "description": "Map of attributes that constitute the record value. Primarily used for LOC and SRV record types. Either this or `value` must be specified."
        },
        "Hostname": {
            "type": "string"
        },
        "Id": {
            "type": "string"
        },
        "Metadata": {
            "type": "array",
            "insertionOrder": true,
            "items": {
                "$ref": "#/definitions/MetadataDefinition"
            }
        },
        "ModifiedOn": {
            "type": "string"
        },
        "Name": {
            "type": "string",
            "description": "The name of the record."
        },
        "Priority": {
            "type": "number",
            "description": "The priority of the record."
        },
        "Proxiable": {
            "type": "boolean"
        },
        "Proxied": {
            "type": "boolean",
            "description": "Whether the record gets Cloudflare's origin protection; defaults to `false`."
        },
        "Ttl": {
            "type": "number",
            "description": "The TTL of the record ([automatic: '1'](https://api.cloudflare.com/#dns-records-for-a-zone-create-dns-record))."
        },
        "Type": {
            "type": "string",
            "description": "The type of the record."
        },
        "Value": {
            "type": "string",
            "description": "The (string) value of the record. Either this or `data` must be specified."
        },
        "ZoneId": {
            "type": "string",
            "description": "The DNS zone ID to add the record to."
        },
        "Timeouts": {
            "$ref": "#/definitions/TimeoutsDefinition"
        }
    },
    "additionalProperties": false,
    "required": [
        "Name",
        "Type",
        "ZoneId"
    ],
    "readOnlyProperties": [
        "/properties/tfcfnid",
        "/properties/CreatedOn",
        "/properties/Hostname",
        "/properties/Id",
        "/properties/Metadata",
        "/properties/ModifiedOn",
        "/properties/Proxiable"
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
