---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.1'
      jupytext_version: 1.1.7
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
    version: 3.6.5
  plotly:
    description: How to use filters in Python with Plotly.
    display_as: transforms
    language: python
    layout: base
    name: Filter
    order: 1
    page_type: example_index
    permalink: python/filter/
    thumbnail: thumbnail/filter.jpg
---

#### Basic Example

```python
import plotly.io as pio

subject = ['Moe','Larry','Curly','Moe','Larry','Curly','Moe','Larry','Curly','Moe','Larry','Curly']
score = [1,6,2,8,2,9,4,5,1,5,2,8]

data = [dict(
  type = 'scatter',
  x = subject,
  y = score,
  mode = 'markers',
  transforms = [dict(
    type = 'filter',
    target = 'y',
    operation = '>',
    value = 4
  )]
)]

layout = dict(
    title = 'Scores > 4'
)

fig_dict = dict(data=data, layout=layout)

pio.show(fig_dict, validate=False)
```

#### Reference
See https://plot.ly/python/reference/ for more information and chart attribute options!
