---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
---

This is a list of all Public Third Party registry resource types available in us-east-1, grouped by publisher.

{% for publisher in site.data.resources.publishers %}
## ⭐ [{{publisher.PublisherName}}]({{publisher.PublisherProfile}}) 

{% for resource in publisher.Resources %}
### [{{ resource.TypeName }}](./resources/{{resource.TypeNameDashes}})

{{ resource.Description }}

{% endfor %}
{% endfor %}

