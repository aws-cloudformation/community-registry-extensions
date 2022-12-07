---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
---

{% for item in site.data.resources %}
## {{ item.TypeName }}

{{ item.Description }}

Publisher: {{ item.PublisherName }}
{% endfor %}
