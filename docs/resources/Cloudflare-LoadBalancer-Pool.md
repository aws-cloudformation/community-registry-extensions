
## Cloudflare::LoadBalancer::Pool

A resource to manage a pool of origin servers

- [Source](https:&#x2F;&#x2F;github.com&#x2F;aws-ia&#x2F;cloudformation-cloudflare-resource-providers.git) 
- [Documentation]()

Published by AWS Community

## Schema
{% highlight json %}
{
    "typeName": "Cloudflare::LoadBalancer::Pool",
    "description": "A resource to manage a pool of origin servers",
    "sourceUrl": "https://github.com/aws-ia/cloudformation-cloudflare-resource-providers.git",
    "documentationUrl": "https://github.com/aws-ia/cloudformation-cloudflare-resource-providers",
    "typeConfiguration": {
        "properties": {
            "CloudflareAccess": {
                "$ref": "#/definitions/CloudflareAccess"
            }
        },
        "additionalProperties": false
    },
    "definitions": {
        "CloudflareAccess": {
            "type": "object",
            "properties": {
                "Url": {
                    "type": "string",
                    "description": "Cloudflare API endpoint"
                },
                "ApiKey": {
                    "type": "string",
                    "description": "Cloudflare API tokens are used to authenticate requests to Cloudflare APIs."
                }
            },
            "additionalProperties": false
        },
        "Origin": {
            "type": "object",
            "properties": {
                "Name": {
                    "type": "string"
                },
                "Address": {
                    "type": "string"
                },
                "Enabled": {
                    "type": "boolean"
                },
                "Weight": {
                    "type": "number"
                }
            },
            "additionalProperties": false
        },
        "Filter": {
            "description": "Filter pool and origin health notifications by resource type or health status. Use null to reset",
            "type": "object",
            "properties": {
                "Pool": {
                    "type": "object",
                    "properties": {
                        "Healthy": {
                            "type": "boolean"
                        }
                    },
                    "additionalProperties": false
                }
            },
            "additionalProperties": false
        },
        "LoadShedding": {
            "description": "Configures load shedding policies and percentages for the pool",
            "type": "object",
            "properties": {
                "DefaultPercent": {
                    "type": "integer",
                    "description": "The percent of traffic to shed from the pool, according to the default policy. Applies to new sessions and traffic without session affinity."
                },
                "DefaultPolicy": {
                    "type": "string",
                    "description": "The default policy to use when load shedding. A random policy randomly sheds a given percent of requests. A hash policy computes a hash over the CF-Connecting-IP address and sheds all requests originating from a percent of IPs.",
                    "enum": [
                        "hash",
                        "random"
                    ]
                },
                "SessionPercent": {
                    "type": "integer",
                    "description": "The percent of existing sessions to shed from the pool, according to the session policy."
                },
                "SessionPolicy": {
                    "type": "string",
                    "description": "Session Policy",
                    "enum": [
                        "hash"
                    ]
                }
            },
            "additionalProperties": false
        }
    },
    "properties": {
        "Name": {
            "type": "string",
            "description": "A short name (tag) for the pool. Only alphanumeric characters, hyphens, and underscores are allowed.",
            "pattern": "^[a-zA-Z0-9\\-\\_]+$"
        },
        "AccountIdentifier": {
            "type": "string",
            "description": "The account identifier"
        },
        "Id": {
            "type": "string",
            "description": "The pool id"
        },
        "Origins": {
            "description": "The list of origins within this pool. Traffic directed at this pool is balanced across all currently healthy origins, provided the pool itself is healthy",
            "type": "array",
            "insertionOrder": false,
            "items": {
                "$ref": "#/definitions/Origin"
            }
        },
        "NotificationFilter": {
            "description": "Filter pool and origin health notifications by resource type or health status. Use null to reset",
            "$ref": "#/definitions/Filter"
        },
        "CheckRegions": {
            "description": "A list of regions (specified by region code) from which to run health checks. Empty means every Cloudflare data center (the default), but requires an Enterprise plan",
            "type": "array",
            "insertionOrder": false,
            "items": {
                "type": "string"
            }
        },
        "Description": {
            "type": "string",
            "description": "Free text description."
        },
        "Enabled": {
            "type": "boolean",
            "description": "Whether to enable (the default) this pool. Disabled pools will not receive traffic and are excluded from health checks. Disabling a pool will cause any load balancers using it to failover to the next pool (if any)."
        },
        "Latitude": {
            "type": "number",
            "description": "The latitude this pool is physically located at; used for proximity steering. Values should be between -90 and 90."
        },
        "Longitude": {
            "type": "number",
            "description": "The longitude this pool is physically located at; used for proximity steering. Values should be between -180 and 180."
        },
        "LoadShedding": {
            "$ref": "#/definitions/LoadShedding"
        },
        "MinimumOrigins": {
            "type": "number",
            "description": "The minimum number of origins that must be healthy for this pool to serve traffic. If the number of healthy origins falls below this number, the pool will be marked unhealthy and we will failover to the next available pool. Default: 1."
        },
        "Monitor": {
            "type": "string",
            "description": "The ID of the Monitor to use for health checking origins within this pool."
        },
        "NotificationEmail": {
            "type": "string",
            "description": "he email address to send health status notifications to. This can be an individual mailbox or a mailing list. Multiple emails can be supplied as a comma delimited list."
        },
        "OriginSteering": {
            "type": "object",
            "description": "Set an origin steering policy to control origin selection within a pool.",
            "properties": {
                "Policy": {
                    "type": "string",
                    "description": "The type of origin steering policy to use, either random or hash (based on CF-Connecting-IP).",
                    "enum": [
                        "hash",
                        "random"
                    ]
                }
            },
            "additionalProperties": false
        },
        "CreatedOn": {
            "type": "string",
            "description": "When the record was last modified"
        },
        "ModifiedOn": {
            "type": "string",
            "description": "When the record was last modified"
        }
    },
    "additionalProperties": false,
    "tagging": {
        "taggable": false
    },
    "required": [
        "Name",
        "Origins"
    ],
    "createOnlyProperties": [
        "/properties/AccountIdentifier"
    ],
    "readOnlyProperties": [
        "/properties/Id",
        "/properties/CreatedOn",
        "/properties/ModifiedOn"
    ],
    "primaryIdentifier": [
        "/properties/Id",
        "/properties/AccountIdentifier"
    ],
    "handlers": {
        "create": {
            "permissions": []
        },
        "read": {
            "permissions": []
        },
        "update": {
            "permissions": []
        },
        "delete": {
            "permissions": []
        },
        "list": {
            "permissions": []
        }
    }
}
{% endhighlight %}
