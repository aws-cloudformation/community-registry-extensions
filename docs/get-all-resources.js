const aws = require("aws-sdk");

/**
 * Get a list of all public third party resource types.
 *
 * Returns [
 *   {
 *     TypeName,
 *     Description,
 *     PublisherName,
 *     PublisherId
 *   }
 * ]
 */
async function getAllResources() {
    const cfn = new aws.CloudFormation()
    let nextToken = undefined
    const params = {
        Filters: {
            Category: "THIRD_PARTY",
        },
        Type: "RESOURCE",
        Visibility: "PUBLIC",
    }
    const resources = []
    try {
        do {
            if (nextToken) params.NextToken = nextToken
            const result = await cfn.listTypes(params).promise()
            nextToken = result.NextToken
            for (const t of result.TypeSummaries) {
                resources.push({
                    TypeName: t.TypeName,
                    Description: t.Description,
                    PublisherName: t.PublisherName,
                    PublisherId: t.PublisherId,
                    TypeNameDashes: t.TypeName.replace(/::/g, "-")
                })
            }
        } while (nextToken)
        return resources
    }
    catch (ex) {
        console.error(ex)
        return undefined
    }
}

module.exports = getAllResources
