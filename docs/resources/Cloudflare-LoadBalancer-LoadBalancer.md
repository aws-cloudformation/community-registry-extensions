
## Cloudflare::LoadBalancer::LoadBalancer

A Cloudflare resource for managing load-balancing across pools

- [Source](https:&#x2F;&#x2F;github.com&#x2F;aws-ia&#x2F;cloudformation-cloudflare-resource-providers.git) 
- [Documentation]()

Published by AWS Community

## Schema
{% highlight json %}
{
    "typeName": "Cloudflare::LoadBalancer::LoadBalancer",
    "description": "A Cloudflare resource for managing load-balancing across pools",
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
            "description": "ID of the load balancer"
        },
        "ZoneId": {
            "type": "string",
            "description": "The zone ID to add the load balancer to."
        },
        "Name": {
            "type": "string",
            "description": "The DNS name (FQDN, including the zone) to associate with the load balancer."
        },
        "FallbackPool": {
            "type": "string",
            "description": "he pool ID to use when all other pools are detected as unhealthy."
        },
        "Description": {
            "type": "string",
            "description": "Free text description."
        },
        "Ttl": {
            "type": "number",
            "description": "Time to live (TTL) of this load balancer's DNS name. Conflicts with proxied - this cannot be set for proxied load balancers. Default is 30."
        },
        "SteeringPolicy": {
            "type": "string",
            "description": "Determine which method the load balancer uses to determine the fastest route to your origin"
        },
        "Proxied": {
            "type": "boolean",
            "description": "Whether the hostname gets Cloudflare's origin protection. Defaults to false."
        },
        "Enabled": {
            "type": "boolean",
            "description": "Enable or disable the load balancer. Defaults to true (enabled)."
        },
        "DefaultPools": {
            "description": "A list of pool IDs ordered by their failover priority. Pools defined here are used by default, or when region_pools are not configured for a given region",
            "uniqueItems": true,
            "type": "array",
            "insertionOrder": false,
            "items": {
                "type": "string"
            }
        },
        "RegionPools": {
            "description": "A set containing mappings of region codes to a list of pool IDs (ordered by their failover priority) for the given region",
            "type": "object"
        },
        "CountryPools": {
            "description": "A set containing mappings of country codes to a list of pool IDs (ordered by their failover priority) for the given country",
            "type": "object"
        },
        "PopPools": {
            "description": "A set containing mappings of Cloudflare Point-of-Presence (PoP) identifiers to a list of pool IDs (ordered by their failover priority) for the PoP (datacenter). This feature is only available to enterprise customers",
            "type": "object"
        },
        "RandomSteering": {
            "description": "Configures pool weights for random steering. When steering_policy is 'random', a random pool is selected with probability proportional to these pool weights",
            "type": "object",
            "properties": {
                "DefaultWeight": {
                    "type": "number"
                }
            },
            "additionalProperties": false
        },
        "SessionAffinity": {
            "type": "string",
            "description": "Associates all requests coming from an end-user with a single origin. Cloudflare will set a cookie on the initial response to the client, such that consequent requests with the cookie in the request will go to the same origin, so long as it is available"
        },
        "SessionAffinityTtl": {
            "type": "number",
            "description": "Time, in seconds, until this load balancers session affinity cookie expires after being created. This parameter is ignored unless a supported session affinity policy is set. The current default of 23 hours will be used unless session_affinity_ttl is explicitly set. Once the expiry time has been reached, subsequent requests may get sent to a different origin server. Valid values are between 1800 and 604800."
        },
        "SessionAffinityAttributes": {
            "type": "object",
            "description": "Configure cookie attributes for session affinity cookie"
        },
        "Rules": {
            "description": "A list of conditions and overrides for each load balancer operation",
            "type": "array",
            "insertionOrder": false,
            "items": {
                "type": "object"
            }
        },
        "ModifiedOn": {
            "type": "string",
            "description": "When the record was last modified"
        },
        "CreatedOn": {
            "type": "string",
            "description": "When the record was created"
        }
    },
    "additionalProperties": false,
    "required": [
        "ZoneId"
    ],
    "createOnlyProperties": [
        "/properties/ZoneId"
    ],
    "readOnlyProperties": [
        "/properties/Id",
        "/properties/ModifiedOn",
        "/properties/CreatedOn"
    ],
    "primaryIdentifier": [
        "/properties/Id",
        "/properties/ZoneId"
    ],
    "writeOnlyProperties": [
        "/properties/SessionAffinityAttributes"
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
