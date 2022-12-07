
## Okta::Group::GroupApplicationAssociation

Manage Groups assigned to an Application

- [Source](https:&#x2F;&#x2F;github.com&#x2F;aws-ia&#x2F;cloudformation-okta-resource-providers.git) 
- [Documentation]()

Published by AWS Community

## Schema
{% highlight json %}
{
    "typeName": "Okta::Group::GroupApplicationAssociation",
    "description": "Manage Groups assigned to an Application",
    "sourceUrl": "https://github.com/aws-ia/cloudformation-okta-resource-providers.git",
    "documentationUrl": "https://github.com/aws-ia/cloudformation-okta-resource-providers",
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
        "ApplicationId": {
            "type": "string",
            "description": "id of an app"
        },
        "GroupId": {
            "type": "string",
            "description": "unique key of a valid Group"
        }
    },
    "additionalProperties": false,
    "required": [
        "ApplicationId",
        "GroupId"
    ],
    "createOnlyProperties": [
        "/properties/ApplicationId",
        "/properties/GroupId"
    ],
    "primaryIdentifier": [
        "/properties/ApplicationId",
        "/properties/GroupId"
    ],
    "handlers": {
        "create": {
            "permissions": []
        },
        "read": {
            "permissions": []
        },
        "delete": {
            "permissions": []
        }
    }
}
{% endhighlight %}
