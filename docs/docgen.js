/*
 * Generate documentation files.
 *
 * This script populates _data, which is used by Jekyll to render pages.
 *
 * It also creates individual pages for resources. TODO
 */
const aws = require("aws-sdk");
const fs = require("fs-extra");

(async function main() {
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
                console.log(t.TypeName)
                resources.push({
                    TypeName: t.TypeName,
                    Description: t.Description,
                    PublisherName: t.PublisherName,
                })
            }
        } while (nextToken)

        fs.writeFileSync("_data/resources.json", JSON.stringify(resources))
    }
    catch (ex) {
        console.error(ex)
    }


})()
