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
    description: Plotly allows you to save interactive HTML versions of your figures
      to your local disk.
    display_as: file_settings
    language: python
    layout: base
    name: Interactive HTML Export
    order: 31
    page_type: u-guide
    permalink: python/interactive-html-export/
    thumbnail: thumbnail/static-image-export.png
---

### Interactive vs Static Export

Plotly figures are interactive when viewed in a web browser: you can hover over data points, pan and zoom axes, and show and hide traces by clicking or double-clicking on the legend. You can export figures either to [static image file formats like PNG, JEPG, SVG or PDF](/python/static-image-export/) or you can export them to HTML files which can be opened in a browser. This page explains how to do the latter.

<!-- #region -->
### Saving to an HTML file

Any figure can be saved an HTML file using the `write_html` method. These HTML files can be opened in any web browser to access the fully interactive figure.

```python
import plotly.express as px

fig =px.scatter(x=range(10), y=range(10))
fig.write_html("path/to/file.html")
```
<!-- #endregion -->

### Controlling the size of the HTML file

By default, the resulting HTML file is a fully self-contained HTML file which can be uploaded to a web server or shared via email or other file-sharing mechanisms. The downside to this approach is that the file is very large (5Mb+) because it contains an inlined copy of the Plotly.js library required to make the figure interactive. This can be controlled via the `include_plotlyjs` argument (see below).


### Full Parameter Documentation

```python
import plotly.graph_objects as go

help(go.Figure.write_html)
```