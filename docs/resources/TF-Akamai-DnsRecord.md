
## TF::Akamai::DnsRecord

## Use the &#x60;akamai_dns_record&#x60; resource to configure a DNS record that can integrate with your existing DNS infrastructure.

- [Source](https:&#x2F;&#x2F;github.com&#x2F;iann0036&#x2F;cfn-tf-custom-types.git) 
- [Documentation]()

Published by Ian Mckay

## Schema
{% highlight json %}
{
    "typeName": "TF::Akamai::DnsRecord",
    "description": "Use the `akamai_dns_record` resource to configure a DNS record that can integrate with your existing DNS infrastructure.",
    "sourceUrl": "https://github.com/iann0036/cfn-tf-custom-types.git",
    "documentationUrl": "https://github.com/iann0036/cfn-tf-custom-types/blob/docs/resources/akamai/TF-Akamai-DnsRecord/docs/README.md",
    "definitions": {},
    "properties": {
        "tfcfnid": {
            "description": "Internal identifier for tracking resource changes. Do not use.",
            "type": "string"
        },
        "Active": {
            "type": "boolean"
        },
        "Algorithm": {
            "type": "number"
        },
        "AnswerType": {
            "type": "string"
        },
        "Certificate": {
            "type": "string"
        },
        "Digest": {
            "type": "string"
        },
        "DigestType": {
            "type": "number"
        },
        "DnsName": {
            "type": "string"
        },
        "EmailAddress": {
            "type": "string"
        },
        "Expiration": {
            "type": "string"
        },
        "Expiry": {
            "type": "number"
        },
        "Fingerprint": {
            "type": "string"
        },
        "FingerprintType": {
            "type": "number"
        },
        "Flags": {
            "type": "number"
        },
        "Flagsnaptr": {
            "type": "string"
        },
        "Hardware": {
            "type": "string"
        },
        "Id": {
            "type": "string"
        },
        "Inception": {
            "type": "string"
        },
        "Iterations": {
            "type": "number"
        },
        "Key": {
            "type": "string"
        },
        "Keytag": {
            "type": "number"
        },
        "Labels": {
            "type": "number"
        },
        "Mailbox": {
            "type": "string"
        },
        "MatchType": {
            "type": "number"
        },
        "Name": {
            "type": "string"
        },
        "NameServer": {
            "type": "string"
        },
        "NextHashedOwnerName": {
            "type": "string"
        },
        "NxdomainTtl": {
            "type": "number"
        },
        "Order": {
            "type": "number"
        },
        "OriginalTtl": {
            "type": "number"
        },
        "Port": {
            "type": "number"
        },
        "Preference": {
            "type": "number"
        },
        "Priority": {
            "type": "number"
        },
        "PriorityIncrement": {
            "type": "number"
        },
        "Protocol": {
            "type": "number"
        },
        "RecordSha": {
            "type": "string"
        },
        "Recordtype": {
            "type": "string"
        },
        "Refresh": {
            "type": "number"
        },
        "Regexp": {
            "type": "string"
        },
        "Replacement": {
            "type": "string"
        },
        "Retry": {
            "type": "number"
        },
        "Salt": {
            "type": "string"
        },
        "Selector": {
            "type": "number"
        },
        "Serial": {
            "type": "number"
        },
        "Service": {
            "type": "string"
        },
        "Signature": {
            "type": "string"
        },
        "Signer": {
            "type": "string"
        },
        "Software": {
            "type": "string"
        },
        "Subtype": {
            "type": "number"
        },
        "SvcParams": {
            "type": "string"
        },
        "SvcPriority": {
            "type": "number"
        },
        "Target": {
            "type": "array",
            "insertionOrder": false,
            "items": {
                "type": "string"
            }
        },
        "TargetName": {
            "type": "string"
        },
        "Ttl": {
            "type": "number"
        },
        "Txt": {
            "type": "string"
        },
        "TypeBitmaps": {
            "type": "string"
        },
        "TypeCovered": {
            "type": "string"
        },
        "TypeMnemonic": {
            "type": "string"
        },
        "TypeValue": {
            "type": "number"
        },
        "Usage": {
            "type": "number"
        },
        "Weight": {
            "type": "number"
        },
        "Zone": {
            "type": "string"
        }
    },
    "additionalProperties": false,
    "required": [
        "Name",
        "Recordtype",
        "Ttl",
        "Zone"
    ],
    "readOnlyProperties": [
        "/properties/tfcfnid",
        "/properties/AnswerType",
        "/properties/DnsName",
        "/properties/Id",
        "/properties/RecordSha",
        "/properties/Serial"
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
