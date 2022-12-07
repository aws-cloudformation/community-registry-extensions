
## Cloudflare::Dns::Record

## A Cloudflare resource for managing a single DNS record

- [Source](https:&#x2F;&#x2F;github.com&#x2F;aws-ia&#x2F;cloudformation-cloudflare-resource-providers.git) 
- [Documentation]()

Published by AWS Community

## Schema
{% highlight json %}
{
    "typeName": "Cloudflare::Dns::Record",
    "description": "A Cloudflare resource for managing a single DNS record",
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
            "description": "DNS record identifier tag"
        },
        "Type": {
            "type": "string",
            "description": "Record type",
            "enum": [
                "A",
                "AAAA",
                "CERT",
                "CNAME",
                "DNSKEY",
                "DS",
                "HTTPS",
                "LOC",
                "MX",
                "NAPTR",
                "NS",
                "SMIMEA",
                "SRV",
                "SSHFP",
                "SVCB",
                "TLSA",
                "TXT",
                "URI"
            ]
        },
        "Meta": {
            "type": "object",
            "description": "Extra Cloudflare-specific information about the record"
        },
        "Locked": {
            "type": "boolean",
            "description": "Whether this record can be modified/deleted (true means it's managed by Cloudflare)"
        },
        "Name": {
            "type": "string",
            "description": "DNS record name (or @ for the zone apex)"
        },
        "Ttl": {
            "type": "number",
            "description": "Time to live, in seconds, of the DNS record. Must be between 60 and 86400, or 1 for 'automatic'"
        },
        "ZoneId": {
            "type": "string",
            "description": "Zone identifier tag"
        },
        "ModifiedOn": {
            "type": "string",
            "description": "When the record was last modified"
        },
        "CreatedOn": {
            "type": "string",
            "description": "When the record was created"
        },
        "Proxiable": {
            "type": "boolean",
            "description": "Whether the record can be proxied by Cloudflare or not"
        },
        "Content": {
            "type": "string",
            "description": "A valid IPv4 address"
        },
        "Proxied": {
            "type": "boolean",
            "description": "Whether the record is receiving the performance and security benefits of Cloudflare"
        },
        "ZoneName": {
            "type": "string",
            "description": "The domain of the record"
        }
    },
    "additionalProperties": false,
    "required": [
        "ZoneId",
        "Name",
        "Type",
        "Content",
        "Ttl"
    ],
    "readOnlyProperties": [
        "/properties/Id",
        "/properties/Locked",
        "/properties/ModifiedOn",
        "/properties/CreatedOn",
        "/properties/Proxiable",
        "/properties/ZoneName"
    ],
    "primaryIdentifier": [
        "/properties/Id",
        "/properties/ZoneId"
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
