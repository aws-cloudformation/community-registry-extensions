/*
 * Generate documentation files.
 *
 * This script populates _data, which is used by Jekyll to render pages.
 *
 * It also creates individual pages for resources. TODO
 */
const aws = require("aws-sdk");
const fs = require("fs-extra");
const mustache = require("mustache")

const getAllResources = require("./get-all-resources");
const getTypeDescription = require("./get-type-description");

const cfn = new aws.CloudFormation();

(async function main() {
    try {
        const resources = await getAllResources()
        const publishers = {}
        for (const resource of resources) {
            const publisherName = resource.PublisherName
            const publisherId = resource.PublisherId
            if (!(publisherName in publishers)) {
                publishers[publisherName] = {}
                publishers[publisherName].PublisherName = publisherName
                publishers[publisherName].PublisherId = publisherId
                publishers[publisherName].Resources = []
            }
            publishers[publisherName].Resources.push(resource)
        }
        const siteData = {
            publishers: []
        }
        for (const key in publishers) {
            const pd = await cfn.describePublisher({
                PublisherId: publishers[key].PublisherId
            }).promise()
            publishers[key].PublisherProfile = pd.PublisherProfile
            console.log("Looked up profile for", key)
            siteData.publishers.push(publishers[key])
        }
        fs.writeFileSync("_data/resources.json", JSON.stringify(siteData))
        for (const t of resources) {
            console.log(t.TypeName)

            let desc
            try {
                desc = await getTypeDescription(t.TypeName)
            } catch (ex) {
                console.error(ex)
                break
            }
            if (!desc) {
                console.error("Unable to get type description for", t.TypeName)
                break
            }
            desc.PublisherName = t.PublisherName
            desc.Schema = JSON.parse(desc.Schema)
            desc.SchemaString = JSON.stringify(desc.Schema, null, 4)

            // Create a page for this type
            const fn = "resources/" + t.TypeName.replace(/::/g, "-") + ".md"
            const template = `
## {{TypeName}}

{{Description}}

- [Source]({{SourceUrl}}) 
- [Documentation]({{DocumenationUrl}})

Published by {{PublisherName}}

## Schema
{% highlight json %}
{{{SchemaString}}}
{% endhighlight %}
`
            const content = mustache.render(template, desc)

            fs.writeFileSync(fn, content)
            console.log("Wrote", fn)
        }
    }
    catch (ex) {
        console.error(ex)
    }
})()
