
## Okta::Group::Group

An example resource schema demonstrating some basic constructs and validation rules.

- [Source](https:&#x2F;&#x2F;github.com&#x2F;aws-cloudformation&#x2F;aws-cloudformation-rpdk.git) 
- [Documentation]()

Published by AWS Community

## Schema
{% highlight json %}
{
    "typeName": "Okta::Group::Group",
    "description": "An example resource schema demonstrating some basic constructs and validation rules.",
    "sourceUrl": "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
    "typeConfiguration": {
        "properties": {
            "OktaAccess": {
                "$ref": "#/definitions/OktaAccess"
            }
        },
        "additionalProperties": false
    },
    "definitions": {
        "OktaAccess": {
            "type": "object",
            "properties": {
                "Url": {
                    "type": "string",
                    "description": "Okta URL, including organization identifier"
                },
                "ApiKey": {
                    "type": "string",
                    "description": "Okta API tokens are used to authenticate requests to Okta APIs."
                }
            },
            "additionalProperties": false
        },
        "Profile": {
            "type": "object",
            "properties": {
                "Name": {
                    "type": "string",
                    "description": "Name of the Group"
                },
                "Description": {
                    "type": "string",
                    "description": "Description of the Group"
                }
            },
            "additionalProperties": false,
            "required": [
                "Name"
            ]
        },
        "Group": {
            "type": "object",
            "properties": {
                "Id": {
                    "type": "string",
                    "description": "Unique key for Group"
                },
                "Profile": {
                    "$ref": "#/definitions/Profile"
                }
            },
            "additionalProperties": false
        }
    },
    "properties": {
        "Id": {
            "type": "string",
            "description": "Unique key for Group"
        },
        "Profile": {
            "$ref": "#/definitions/Profile"
        },
        "Group": {
            "$ref": "#/definitions/Group"
        }
    },
    "additionalProperties": false,
    "required": [
        "Profile"
    ],
    "readOnlyProperties": [
        "/properties/Id",
        "/properties/Group"
    ],
    "primaryIdentifier": [
        "/properties/Id"
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
