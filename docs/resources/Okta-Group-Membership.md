
## Okta::Group::Membership

## Adds Okta users to groups

- [Source](https:&#x2F;&#x2F;github.com&#x2F;aws-ia&#x2F;cloudformation-okta-resource-providers&#x2F;tree&#x2F;main&#x2F;Okta-Group-Membership) 
- [Documentation]()

Published by AWS Community

## Schema
{% highlight json %}
{
    "typeName": "Okta::Group::Membership",
    "description": "Adds Okta users to groups",
    "sourceUrl": "https://github.com/aws-ia/cloudformation-okta-resource-providers/tree/main/Okta-Group-Membership",
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
        }
    },
    "properties": {
        "GroupId": {
            "type": "string"
        },
        "UserId": {
            "type": "string"
        }
    },
    "additionalProperties": false,
    "required": [
        "GroupId",
        "UserId"
    ],
    "primaryIdentifier": [
        "/properties/GroupId",
        "/properties/UserId"
    ],
    "createOnlyProperties": [
        "/properties/GroupId",
        "/properties/UserId"
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
