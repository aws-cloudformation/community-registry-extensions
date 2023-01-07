const aws = require("aws-sdk");

const cfn = new aws.CloudFormation()

/**
 * Get the detailed description for an activated type.
 */
async function getTypeDescription(typeName) {
    const params = {
        Type: "RESOURCE", 
        TypeName: typeName
    }
    try {
        const result = await cfn.describeType(params).promise()
        return result
    } catch (ex) {
        if (ex.code === "TypeNotFoundException") {
            return false
        }
        console.error("Failed to describe type:", ex)
        return undefined
    }
}
module.exports = getTypeDescription

