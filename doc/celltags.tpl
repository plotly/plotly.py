{%- macro celltags(cell) -%}
    {% if cell.metadata.tags | length > 0 -%}
        {% for tag in cell.metadata.tags -%}
            {{ ' celltag_' ~ tag -}}
        {%- endfor -%}
    {%- endif %}
{%- endmacro %}
