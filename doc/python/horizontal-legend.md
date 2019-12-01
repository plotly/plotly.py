---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.1'
      jupytext_version: 1.1.6
  kernelspec:
    display_name: Python 3
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
    version: 3.7.3
  plotly:
    description: How to add images to charts as background images or logos.
    display_as: advanced_opt
    language: python
    layout: base
    name: Horizontal Legends
    order: 12
    page_type: example_index
    permalink: python/horizontal-legend/
    thumbnail: thumbnail/your-tutorial-chart.jpg
---

###  Horizontal Legend

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    name="First",
    y=[1, 2, 3],
    mode="markers",
    marker=dict(
        size=16,
        color="Crimson"
    ))
)

fig.add_trace(go.Bar(
    name="Second",
    y=[1, 3, 2],
    marker=dict(
        color="LightSeaGreen"
    ))
)

fig.add_trace(go.Scatter(
    name="Third",
    y=[4, 3, 1],
    mode="lines",
    line=dict(
        width=4,
        color="MediumPurple"
    ))
)

fig.update_layout(legend_orientation="h")

fig.show()
```

#### Reference
See https://plot.ly/python/reference/#layout-legend-orientation for more information and chart attribute options!
