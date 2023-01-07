/*
 * Activates all public extensions, if they have not already been activated.
 *
 * You can't call describeType on a public type that you haven't activated, 
 * and we need that for detailed information about each type.
 *
 * Creates a role called registry-extension-activation if it doesn't already exist.
 */
const aws = require("aws-sdk");
const fs = require("fs-extra");
const getAllResources = require("./get-all-resources");
const getTypeDescription = require("./get-type-description")

const cfn = new aws.CloudFormation()
const iam = new aws.IAM()
const ROLE_NAME = "registry-extension-activation"

/**
 * Create the execution role that we will use to activate the extensions.
 *
 * Returns the role arn
 */
async function createExecutionRole() {
    try {
        const existingRole = await iam.getRole({
            RoleName: ROLE_NAME 
        }).promise()
        console.log("Execution role", ROLE_NAME, "exists")
        return existingRole.Role.Arn
    }
    catch (ex) {
        if (ex.code === "NoSuchEntity") {
            const role = await iam.CreateRole({
                RoleName: ROLE_NAME,
                Description: "This role is used to activate extensions as part of the activate-all.js script for creating community registry extension docs",
                AssumeRolePolicyDocument: JSON.stringify({
                    "Version": "2012-10-17",
                    "Statement": [
                        {
                            "Effect": "Allow",
                            "Principal": {
                                "Service": [
                                    "resources.cloudformation.amazonaws.com",
                                    "hooks.cloudformation.amazonaws.com"
                                ]
                            },
                            "Action": "sts:AssumeRole"
                        }
                    ]
                }),
            }).promise()
            return role.Role.Arn
        } else {
            console.error(ex)
            return false
        }
    }
}

(async function main() {
    try {
        const roleArn = await createExecutionRole()
        if (!roleArn) {
            console.error("Unable to create execution role")
            return
        }

        const resources = await getAllResources()
        for (const t of resources) {
            console.log(t.TypeName)
            const d = await getTypeDescription(t.TypeName)
            if (d === false) {
                // Type was not found
                console.log("About to activate", t.TypeName)
                try {
                    const activationResult = await cfn.activateType({
                        Type: "RESOURCE",
                        TypeName: t.TypeName,
                        ExecutionRoleArn: roleArn,
                        PublisherId: t.PublisherId
                    }).promise()
                    console.log(t.TypeName, "activated")
                } catch (activationEx) {
                    console.error(activationEx)
                    break
                }
            } else if (d === undefined) {
                break
            } else {
                console.log(t.TypeName, "is already activated")
            }
        }
    }
    catch (ex) {
        console.error(ex)
    }

})()
