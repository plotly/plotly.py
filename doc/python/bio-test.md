---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.3.1
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
    version: 3.6.8
  plotly:
    description: Bio test description
    display_as: bio
    language: python
    layout: base
    name: Bio Test
    order: 1
    page_type: u-guide
    permalink: python/bio-test/
    thumbnail: thumbnail/hist2dcontour.png
---

## 2D Histogram Contours or Density Contours

A 2D histogram contour plot, also known as a density contour plot, is a 2-dimensional generalization of a 

```python
import plotly.express as px
df = px.data.tips()

fig = px.density_contour(df, x="total_bill", y="tip")
fig.show()
```
