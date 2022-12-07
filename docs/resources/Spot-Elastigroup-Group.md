
## Spot::Elastigroup::Group

The Spot Elastigroup Resource allows you to create, update, manage, and delete Spot Elastigroups easily with CloudFormation

- [Source]() 
- [Documentation]()

Published by 

## Schema
{% highlight json %}
{
    "typeName": "Spot::Elastigroup::Group",
    "description": "The Spot Elastigroup Resource allows you to create, update, manage, and delete Spot Elastigroups easily with CloudFormation",
    "definitions": {
        "Tag": {
            "type": "object",
            "properties": {
                "tagKey": {
                    "type": "string"
                },
                "tagValue": {
                    "type": "string"
                }
            },
            "additionalProperties": false
        },
        "ScalingPolicy": {
            "type": "object",
            "properties": {
                "policyName": {
                    "type": "string"
                },
                "metricName": {
                    "type": "string"
                },
                "statistic": {
                    "type": "string"
                },
                "unit": {
                    "type": "string"
                },
                "threshold": {
                    "type": "number"
                },
                "namespace": {
                    "type": "string"
                },
                "period": {
                    "type": "integer"
                },
                "evaluationPeriods": {
                    "type": "integer"
                },
                "cooldown": {
                    "type": "integer"
                },
                "dimension": {
                    "type": "array",
                    "title": "dimensions",
                    "items": {
                        "type": "object",
                        "properties": {
                            "name": {
                                "type": "string"
                            },
                            "value": {
                                "type": "string"
                            }
                        },
                        "additionalProperties": false
                    }
                },
                "action": {
                    "type": "object",
                    "properties": {
                        "type": {
                            "type": "string"
                        },
                        "adjustment": {
                            "type": "string"
                        },
                        "minTargetCapacity": {
                            "type": "string"
                        },
                        "target": {
                            "type": "string"
                        },
                        "minimum": {
                            "type": "string"
                        },
                        "maximum": {
                            "type": "string"
                        }
                    },
                    "additionalProperties": false
                }
            },
            "additionalProperties": false
        },
        "BlockDeviceMapping": {
            "type": "object",
            "properties": {
                "deviceName": {
                    "type": "string"
                },
                "noDevice": {
                    "type": "string"
                },
                "virtualName": {
                    "type": "string"
                },
                "ebs": {
                    "type": "object",
                    "properties": {
                        "deleteOnTermination": {
                            "type": "boolean"
                        },
                        "encrypted": {
                            "type": "boolean"
                        },
                        "iops": {
                            "type": "integer"
                        },
                        "snapshotId": {
                            "type": "string"
                        },
                        "volumeSize": {
                            "type": "integer"
                        },
                        "volumeType": {
                            "type": "string",
                            "enum": [
                                "standard",
                                "io1",
                                "gp2"
                            ]
                        }
                    },
                    "additionalProperties": false
                }
            },
            "additionalProperties": false
        },
        "Attribute": {
            "type": "object",
            "properties": {
                "key": {
                    "type": "string"
                },
                "value": {
                    "type": "string"
                }
            },
            "additionalProperties": false
        },
        "ecs": {
            "type": "object",
            "properties": {
                "clusterName": {
                    "type": "string"
                },
                "autoScale": {
                    "type": "object",
                    "properties": {
                        "isEnabled": {
                            "type": "boolean"
                        },
                        "cooldown": {
                            "type": "integer"
                        },
                        "isAutoConfig": {
                            "type": "boolean"
                        },
                        "shouldScaleDownNonServiceTasks": {
                            "type": "boolean"
                        },
                        "headroom": {
                            "type": "object",
                            "properties": {
                                "cpuPerUnit": {
                                    "type": "integer"
                                },
                                "memoryPerUnit": {
                                    "type": "integer"
                                },
                                "numOfUnits": {
                                    "type": "integer"
                                }
                            },
                            "additionalProperties": false
                        },
                        "down": {
                            "type": "object",
                            "properties": {
                                "evaluationPeriods": {
                                    "type": "integer"
                                },
                                "maxScaleDownPercentage": {
                                    "type": "integer"
                                }
                            },
                            "additionalProperties": false
                        },
                        "attributes": {
                            "type": "array",
                            "items": {
                                "$ref": "#/definitions/Attribute"
                            }
                        }
                    },
                    "additionalProperties": false
                },
                "batch": {
                    "type": "object",
                    "properties": {
                        "jobQueueNames": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            }
                        }
                    },
                    "additionalProperties": false
                },
                "optimizeImages": {
                    "type": "object",
                    "properties": {
                        "shouldOptimizeEcsAmi": {
                            "type": "boolean"
                        },
                        "performAt": {
                            "type": "string"
                        },
                        "timeWindows": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            }
                        }
                    },
                    "additionalProperties": false
                }
            },
            "additionalProperties": false
        },
        "Task": {
            "type": "object",
            "properties": {
                "isEnabled": {
                    "type": "boolean"
                },
                "taskType": {
                    "type": "string"
                },
                "cronExpression": {
                    "type": "string"
                },
                "scaleTargetCapacity": {
                    "type": "integer"
                },
                "scaleMinCapacity": {
                    "type": "integer"
                },
                "scaleMaxCapacity": {
                    "type": "integer"
                },
                "batchSizePercentage": {
                    "type": "integer"
                },
                "gracePeriod": {
                    "type": "integer"
                },
                "frequency": {
                    "type": "string"
                },
                "startTime": {
                    "type": "string"
                },
                "adjustment": {
                    "type": "integer"
                }
            },
            "additionalProperties": false
        }
    },
    "properties": {
        "credentials": {
            "type": "object",
            "properties": {
                "accountId": {
                    "type": "string"
                },
                "accessToken": {
                    "type": "string"
                }
            },
            "additionalProperties": false
        },
        "group": {
            "type": "object",
            "properties": {
                "groupId": {
                    "type": "string"
                },
                "name": {
                    "description": "The name of the elastigroup",
                    "type": "string"
                },
                "description": {
                    "description": "The description of the elastigroup",
                    "type": "string"
                },
                "region": {
                    "type": "string"
                },
                "strategy": {
                    "type": "object",
                    "properties": {
                        "risk": {
                            "type": "integer"
                        },
                        "onDemandCount": {
                            "type": "integer"
                        },
                        "availabilityVsCost": {
                            "type": "string"
                        },
                        "drainingTimeout": {
                            "type": "integer"
                        },
                        "fallbackToOd": {
                            "type": "boolean"
                        },
                        "lifetimePeriod": {
                            "type": "string"
                        },
                        "revertToSpot": {
                            "type": "object",
                            "properties": {
                                "performAt": {
                                    "type": "string"
                                },
                                "timeWindows": {
                                    "type": "array",
                                    "items": {
                                        "type": "string"
                                    }
                                }
                            },
                            "additionalProperties": false
                        }
                    },
                    "additionalProperties": false
                },
                "compute": {
                    "type": "object",
                    "properties": {
                        "instanceTypes": {
                            "type": "object",
                            "properties": {
                                "onDemand": {
                                    "type": "string"
                                },
                                "spot": {
                                    "type": "array",
                                    "items": {
                                        "type": "string"
                                    }
                                }
                            },
                            "additionalProperties": false
                        },
                        "availabilityZones": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "name": {
                                        "type": "string"
                                    },
                                    "subnetIds": {
                                        "type": "array",
                                        "items": {
                                            "type": "string"
                                        }
                                    }
                                },
                                "additionalProperties": false
                            }
                        },
                        "product": {
                            "type": "string"
                        },
                        "launchSpecification": {
                            "type": "object",
                            "properties": {
                                "securityGroupIds": {
                                    "type": "array",
                                    "items": {
                                        "type": "string"
                                    }
                                },
                                "loadBalancersConfig": {
                                    "type": "object",
                                    "properties": {
                                        "loadBalancers": {
                                            "type": "array",
                                            "items": {
                                                "type": "object",
                                                "properties": {
                                                    "name": {
                                                        "type": "string"
                                                    },
                                                    "arn": {
                                                        "type": "string"
                                                    },
                                                    "type": {
                                                        "type": "string"
                                                    },
                                                    "balancerId": {
                                                        "type": "string"
                                                    },
                                                    "targetSetId": {
                                                        "type": "string"
                                                    },
                                                    "azAwareness": {
                                                        "type": "boolean"
                                                    },
                                                    "autoWeight": {
                                                        "type": "boolean"
                                                    }
                                                },
                                                "additionalProperties": false
                                            }
                                        }
                                    },
                                    "additionalProperties": false
                                },
                                "healthCheckUnhealthyDurationBeforeReplacement": {
                                    "type": "integer"
                                },
                                "monitoring": {
                                    "type": "boolean"
                                },
                                "ebsOptimized": {
                                    "type": "boolean"
                                },
                                "imageId": {
                                    "type": "string"
                                },
                                "keyPair": {
                                    "type": "string"
                                },
                                "userData": {
                                    "type": "string"
                                },
                                "shutdownScript": {
                                    "type": "string"
                                },
                                "tags": {
                                    "type": "array",
                                    "items": {
                                        "$ref": "#/definitions/Tag"
                                    }
                                },
                                "healthCheckType": {
                                    "type": "string"
                                },
                                "healthCheckGracePeriod": {
                                    "type": "integer"
                                },
                                "tenancy": {
                                    "type": "string"
                                },
                                "blockDeviceMappings": {
                                    "type": "array",
                                    "items": {
                                        "$ref": "#/definitions/BlockDeviceMapping"
                                    }
                                },
                                "iamRole": {
                                    "type": "object",
                                    "properties": {
                                        "name": {
                                            "type": "string"
                                        },
                                        "arn": {
                                            "type": "string"
                                        }
                                    },
                                    "additionalProperties": false
                                }
                            },
                            "additionalProperties": false
                        }
                    },
                    "additionalProperties": false
                },
                "capacity": {
                    "type": "object",
                    "properties": {
                        "minimum": {
                            "type": "integer"
                        },
                        "maximum": {
                            "type": "integer"
                        },
                        "target": {
                            "type": "integer"
                        },
                        "unit": {
                            "type": "string"
                        }
                    },
                    "additionalProperties": false
                },
                "scaling": {
                    "type": "object",
                    "properties": {
                        "up": {
                            "type": "array",
                            "items": {
                                "$ref": "#/definitions/ScalingPolicy"
                            }
                        },
                        "down": {
                            "type": "array",
                            "items": {
                                "$ref": "#/definitions/ScalingPolicy"
                            }
                        }
                    },
                    "additionalProperties": false
                },
                "thirdPartiesIntegration": {
                    "type": "object",
                    "properties": {
                        "ecs": {
                            "type": "object",
                            "$ref": "#/definitions/ecs"
                        },
                        "codeDeploy": {
                            "type": "object",
                            "properties": {
                                "cleanUpOnFailure": {
                                    "type": "boolean"
                                },
                                "terminateInstanceOnFailure": {
                                    "type": "boolean"
                                },
                                "deploymentGroups": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "properties": {
                                            "applicationName": {
                                                "type": "string"
                                            },
                                            "deploymentGroupName": {
                                                "type": "string"
                                            }
                                        },
                                        "additionalProperties": false
                                    }
                                }
                            },
                            "additionalProperties": false
                        }
                    },
                    "additionalProperties": false
                },
                "scheduling": {
                    "type": "object",
                    "properties": {
                        "tasks": {
                            "type": "array",
                            "items": {
                                "$ref": "#/definitions/Task"
                            }
                        }
                    },
                    "additionalProperties": false
                }
            },
            "additionalProperties": false
        }
    },
    "primaryIdentifier": [
        "/properties/group/groupId"
    ],
    "readOnlyProperties": [
        "/properties/group/groupId"
    ],
    "createOnlyProperties": [
        "/properties/group/compute/product",
        "/properties/group/capacity/unit"
    ],
    "required": [
        "credentials"
    ],
    "handlers": {
        "create": {
            "permissions": [
                ""
            ]
        },
        "update": {
            "permissions": [
                ""
            ]
        },
        "delete": {
            "permissions": [
                ""
            ]
        },
        "read": {
            "permissions": [
                ""
            ]
        }
    },
    "additionalProperties": false
}
{% endhighlight %}
