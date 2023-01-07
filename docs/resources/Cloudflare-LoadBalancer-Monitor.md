
## Cloudflare::LoadBalancer::Monitor

A Monitor policy to configure monitoring of endpoint health

- [Source](https:&#x2F;&#x2F;github.com&#x2F;aws-ia&#x2F;cloudformation-cloudflare-resource-providers.git) 
- [Documentation]()

Published by AWS Community

## Schema
{% highlight json %}
{
    "typeName": "Cloudflare::LoadBalancer::Monitor",
    "description": "A Monitor policy to configure monitoring of endpoint health",
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
        }
    },
    "properties": {
        "Id": {
            "type": "string",
            "description": "Load balancer monitor ID"
        },
        "AccountIdentifier": {
            "type": "string",
            "description": "The account identifier"
        },
        "ExpectedBody": {
            "type": "string",
            "description": "A case-insensitive sub-string to look for in the response body. If this string is not found, the origin will be marked as unhealthy. Only valid if type is \"http\" or \"https\". Default: \"\"."
        },
        "ExpectedCodes": {
            "type": "string",
            "description": "The expected HTTP response code or code range of the health check. Eg 2xx. Only valid and required if type is \"http\" or \"https\"."
        },
        "Method": {
            "type": "string",
            "description": "The method to use for the health check. Valid values are any valid HTTP verb if type is \"http\" or \"https\", or connection_established if type is \"tcp\". Default: \"GET\" if type is \"http\" or \"https\", \"connection_established\" if type is \"tcp\", and empty otherwise."
        },
        "Timeout": {
            "type": "number",
            "description": "The timeout (in seconds) before marking the health check as failed. Default: 5."
        },
        "Path": {
            "type": "string",
            "description": "The endpoint path to health check against. Default: \"/\". Only valid if type is \"http\" or \"https\"."
        },
        "Interval": {
            "type": "number",
            "description": "The interval between each health check. Shorter intervals may improve failover time, but will increase load on the origins as we check from multiple locations. Default: 60."
        },
        "Retries": {
            "type": "number",
            "description": "The number of retries to attempt in case of a timeout before marking the origin as unhealthy. Retries are attempted immediately. Default: 2."
        },
        "Header": {
            "type": "object",
            "description": "The HTTP request headers to send in the health check. It is recommended you set a Host header by default. The User-Agent header cannot be overridden. Fields documented below. Only valid if type is \"http\" or \"https\"."
        },
        "Type": {
            "type": "string",
            "description": "The protocol to use for the healthcheck. Currently supported protocols are 'HTTP', 'HTTPS', 'TCP', 'UDP-ICMP', 'ICMP-PING', and 'SMTP'. Default: \"http\"."
        },
        "Port": {
            "type": "number",
            "description": "The port number to use for the healthcheck, required when creating a TCP monitor. Valid values are in the range 0-65535."
        },
        "Description": {
            "type": "string",
            "description": "Free text description."
        },
        "AllowInsecure": {
            "type": "boolean",
            "description": "Do not validate the certificate when monitor use HTTPS. Only valid if type is \"http\" or \"https\"."
        },
        "FollowRedirects": {
            "type": "boolean",
            "description": "Follow redirects if returned by the origin. Only valid if type is \"http\" or \"https\"."
        },
        "ProbeZone": {
            "type": "string",
            "description": "Assign this monitor to emulate the specified zone while probing. Only valid if type is \"http\" or \"https\"."
        },
        "CreatedOn": {
            "type": "string",
            "description": "When the record was created"
        },
        "ModifiedOn": {
            "type": "string",
            "description": "When the record was last modified"
        }
    },
    "additionalProperties": false,
    "required": [
        "ExpectedCodes"
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
