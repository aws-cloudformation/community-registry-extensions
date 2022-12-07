
## TF::DigitalOcean::Droplet

## Provides a DigitalOcean Droplet resource. This can be used to create,
modify, and delete Droplets. Droplets also support
[provisioning](https:&#x2F;&#x2F;www.terraform.io&#x2F;docs&#x2F;language&#x2F;resources&#x2F;provisioners&#x2F;syntax.html).

- [Source](https:&#x2F;&#x2F;github.com&#x2F;iann0036&#x2F;cfn-tf-custom-types.git) 
- [Documentation]()

Published by Ian Mckay

## Schema
{% highlight json %}
{
    "typeName": "TF::DigitalOcean::Droplet",
    "description": "Provides a DigitalOcean Droplet resource. This can be used to create,\nmodify, and delete Droplets. Droplets also support\n[provisioning](https://www.terraform.io/docs/language/resources/provisioners/syntax.html).",
    "sourceUrl": "https://github.com/iann0036/cfn-tf-custom-types.git",
    "documentationUrl": "https://github.com/iann0036/cfn-tf-custom-types/blob/docs/resources/digitalocean/TF-DigitalOcean-Droplet/docs/README.md",
    "definitions": {},
    "properties": {
        "tfcfnid": {
            "description": "Internal identifier for tracking resource changes. Do not use.",
            "type": "string"
        },
        "Backups": {
            "type": "boolean",
            "description": "Boolean controlling if backups are made. Defaults to\nfalse."
        },
        "CreatedAt": {
            "type": "string"
        },
        "Disk": {
            "type": "number"
        },
        "Id": {
            "type": "string"
        },
        "Image": {
            "type": "string",
            "description": "The Droplet image ID or slug."
        },
        "Ipv4Address": {
            "type": "string"
        },
        "Ipv4AddressPrivate": {
            "type": "string"
        },
        "Ipv6": {
            "type": "boolean",
            "description": "Boolean controlling if IPv6 is enabled. Defaults to false."
        },
        "Ipv6Address": {
            "type": "string"
        },
        "Locked": {
            "type": "boolean"
        },
        "Memory": {
            "type": "number"
        },
        "Monitoring": {
            "type": "boolean",
            "description": "Boolean controlling whether monitoring agent is installed.\nDefaults to false."
        },
        "Name": {
            "type": "string",
            "description": "The Droplet name."
        },
        "PriceHourly": {
            "type": "number"
        },
        "PriceMonthly": {
            "type": "number"
        },
        "PrivateNetworking": {
            "type": "boolean",
            "description": "Boolean controlling if private networking\nis enabled. When VPC is enabled on an account, this will provision the\nDroplet inside of your account's default VPC for the region. Use the\n`vpc_uuid` attribute to specify a different VPC."
        },
        "Region": {
            "type": "string",
            "description": "The region to start in."
        },
        "ResizeDisk": {
            "type": "boolean",
            "description": "Boolean controlling whether to increase the disk\nsize when resizing a Droplet. It defaults to `true`. When set to `false`,\nonly the Droplet's RAM and CPU will be resized. **Increasing a Droplet's disk\nsize is a permanent change**. Increasing only RAM and CPU is reversible."
        },
        "Size": {
            "type": "string",
            "description": "The unique slug that indentifies the type of Droplet. You can find a list of available slugs on [DigitalOcean API documentation](https://developers.digitalocean.com/documentation/v2/#list-all-sizes)."
        },
        "SshKeys": {
            "type": "array",
            "insertionOrder": true,
            "items": {
                "type": "string"
            },
            "description": "A list of SSH key IDs or fingerprints to enable in\nthe format `[12345, 123456]`. To retrieve this info, use the\n[DigitalOcean API](https://docs.digitalocean.com/reference/api/api-reference/#tag/SSH-Keys)\nor CLI (`doctl compute ssh-key list`). Once a Droplet is created keys can not\nbe added or removed via this provider. Modifying this field will prompt you\nto destroy and recreate the Droplet."
        },
        "Status": {
            "type": "string"
        },
        "Tags": {
            "type": "array",
            "insertionOrder": true,
            "items": {
                "type": "string"
            },
            "description": "A list of the tags to be applied to this Droplet."
        },
        "Urn": {
            "type": "string"
        },
        "UserData": {
            "type": "string"
        },
        "Vcpus": {
            "type": "number"
        },
        "VolumeIds": {
            "type": "array",
            "insertionOrder": true,
            "items": {
                "type": "string"
            }
        },
        "VpcUuid": {
            "type": "string",
            "description": "The ID of the VPC where the Droplet will be located."
        }
    },
    "additionalProperties": false,
    "required": [
        "Image",
        "Name",
        "Region",
        "Size"
    ],
    "readOnlyProperties": [
        "/properties/tfcfnid",
        "/properties/CreatedAt",
        "/properties/Disk",
        "/properties/Id",
        "/properties/Ipv4Address",
        "/properties/Ipv4AddressPrivate",
        "/properties/Ipv6Address",
        "/properties/Locked",
        "/properties/Memory",
        "/properties/PriceHourly",
        "/properties/PriceMonthly",
        "/properties/Status",
        "/properties/Urn",
        "/properties/Vcpus"
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
