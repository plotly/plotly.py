---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.16.4
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
  language_info:
    codemirror_mode:
      name: ipython
      version: 3
    file_extension: .py
    mimetype: text/x-python
    name: python
    nbconvert_exporter: python
    pygments_lexer: ipython3
    version: 3.9.16
  plotly:
    description: Guide to changes in version 6 of Plotly.py and how to migrate from
      version 5
    display_as: file_settings
    language: python
    layout: base
    name: Changes in Version 6
    order: 8
    page_type: example_index
    permalink: python/v6-migration/
    thumbnail: thumbnail/v4-migration.png
---

This page outlines the changes in Plotly.py version 6 and cases where you may need to update your charts or tools that you use for working with Plotly.py

<!-- #region -->
## Jupyter Notebook Support

## Removed Attributes

The following attributes have been removed in Plotly.py 6.

### `layout.titlefont`

`layout.titlefont` as shown in the following example has been removed. 


```python
import plotly.graph_objects as go

trace = go.Bar(
    x=['A', 'B', 'C', 'D'],
    y=[10, 15, 13, 17]
)

layout = go.Layout(
    title=dict(
        text='Chart Title'
    ),
    titlefont=dict(
        size=40
    )
)

fig = go.Figure(data=[trace], layout=layout)

fig.show()
```

Replace it with `layout.title.font`:

```python
import plotly.graph_objects as go

trace = go.Bar(
    x=['A', 'B', 'C', 'D'],
    y=[10, 15, 13, 17]
)

layout = go.Layout(
    title=dict(
        text='Chart Title',
        font=dict(size=40)
    )
)

fig = go.Figure(data=[trace], layout=layout)

fig.show()
```

## Removed Traces




<!-- #endregion -->
