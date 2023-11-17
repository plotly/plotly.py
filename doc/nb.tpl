{%- extends 'basic.tpl' -%}
{%- block header -%}
---
{% for k in nb.metadata.get("plotly") -%}
{{ k }}: {{ nb.metadata.get("plotly")[k] }}
{% endfor -%}
---
{{ super() }}
{{ '{% raw %}' }}
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.2/require.js"></script>

{%- endblock header-%}

{% block input_group %}
    {%- if not cell.metadata.get('hide_code', False) -%}
        {{ super() }}
    {%- endif -%}
{% endblock input_group %}

{% block markdowncell %}
{{ cell.id }}
{%- if 'What About Dash?' in cell.source or
    'Sign up for Dash Club' in cell.source or
    'best way to build analytical apps in Python using Plotly figures' in cell.source -%}
    <div class="chatbot-exclude">
    {{ super() }}
    </div>
{% else %}
    {{ super() }}
{%- endif -%}
{% endblock markdowncell %}

{%- block footer %}
{{ super() }}
{{ '{% endraw %}' }}
{%- endblock footer-%}
