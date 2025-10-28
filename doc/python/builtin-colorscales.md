---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.14.1
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
    version: 3.8.8
  plotly:
    description: A reference for the built-in named continuous (sequential, diverging
      and cyclical) color scales in Plotly.
    display_as: file_settings
    has_thumbnail: true
    ipynb: ~notebook_demo/187
    language: python
    layout: base
    name: Built-in Continuous Color Scales
    order: 28
    permalink: python/builtin-colorscales/
    thumbnail: thumbnail/heatmap_colorscale.jpg
    v4upgrade: true
---

### Using Built-In Continuous Color Scales

Many Plotly Express functions accept a `color_continuous_scale` argument and many trace
types have a `colorscale` attribute in their schema. Plotly comes with a large number of
built-in continuous color scales, which can be referred to in Python code when setting the above arguments,
either by name in a case-insensitive string e.g. `px.scatter(color_continuous_scale="Viridis"`) or by reference e.g.
`go.Scatter(marker_colorscale=plotly.colors.sequential.Viridis)`. They can also be reversed by adding `_r` at the end
e.g. `"Viridis_r"` or `plotly.colors.sequential.Viridis_r`.

The `plotly.colours` module is also available under `plotly.express.colors` so you can refer to it as `px.colors`.

When using continuous color scales, you will often want to [configure various aspects of its range and colorbar](/python/colorscales/).

### Discrete Color Sequences

Plotly also comes with some built-in [discrete color sequences](/python/discrete-color/) which are _not intended_ to be used with the `color_continuous_scale` argument as they are not designed for interpolation to occur between adjacent colors.

### Named Built-In Continuous Color Scales

You can use any of the following names as string values to set `continuous_color_scale` or `colorscale` arguments.
These strings are case-insensitive and you can append `_r` to them to reverse the order of the scale.

```python
import plotly.express as px
from textwrap import wrap

named_colorscales = px.colors.named_colorscales()
print("\n".join(wrap("".join('{:<12}'.format(c) for c in named_colorscales), 96)))
```

Built-in color scales are stored as lists of CSS colors:

```python
import plotly.express as px

print(px.colors.sequential.Plasma)
```

### Continuous Color Scales in Dash

[Dash](https://plotly.com/dash/) is the best way to build analytical apps in Python using Plotly figures. To run the app below, run `pip install dash`, click "Download" to get the code and run `python app.py`.

Get started  with [the official Dash docs](https://dash.plotly.com/installation) and **learn how to effortlessly [style](https://plotly.com/dash/design-kit/) & publish apps like this with <a class="plotly-red" href="https://plotly.com/dash/">Dash Enterprise</a> or <a class="plotly-red" href="https://plotly.com/cloud/">Plotly Cloud</a>.**


```python hide_code=true
from IPython.display import IFrame
snippet_url = 'https://python-docs-dash-snippets.herokuapp.com/python-docs-dash-snippets/'
IFrame(snippet_url + 'builtin-colorscales', width='100%', height=1200)
```

<div style="font-size: 0.9em;"><div style="width: calc(100% - 30px); box-shadow: none; border: thin solid rgb(229, 229, 229);"><div style="padding: 5px;"><div><p><strong>Sign up for Dash Club</strong> → Free cheat sheets plus updates from Chris Parmer and Adam Schroeder delivered to your inbox every two months. Includes tips and tricks, community apps, and deep dives into the Dash architecture.
<u><a href="https://go.plotly.com/dash-club?utm_source=Dash+Club+2022&utm_medium=graphing_libraries&utm_content=inline">Join now</a></u>.</p></div></div></div></div>


### Built-In Sequential Color scales

A collection of predefined sequential colorscales is provided in the `plotly.colors.sequential` module. Sequential color scales are appropriate for most continuous data, but in some cases it can be helpful to use a diverging or cyclical color scale (see below).

Here are all the built-in scales in the `plotly.colors.sequential` module:

```python
import plotly.express as px

fig = px.colors.sequential.swatches_continuous()
fig.show()
```

Note: `RdBu` was included in the `sequential` module by mistake, even though it is a diverging color scale.
It is intentionally left in for backwards-compatibility reasons.

### Built-In Diverging Color scales

A collection of predefined diverging color scales is provided in the `plotly.colors.diverging` module.
Diverging color scales are appropriate for continuous data that has a natural midpoint
other otherwise informative special value, such as 0 altitude, or the boiling point
of a liquid. These scales are intended to be used when [explicitly setting the midpoint of the scale](/python/colorscales/#setting-the-midpoint-of-a-color-range-for-a-diverging-color-scale).

Here are all the built-in scales in the `plotly.colors.diverging` module:

```python
import plotly.express as px

fig = px.colors.diverging.swatches_continuous()
fig.show()
```

### Built-In Cyclical Color scales

A collection of predefined cyclical color scales is provided in the `plotly.colors.cyclical` module.
Cyclical color scales are appropriate for continuous data that has a natural cyclical
structure, such as temporal data (hour of day, day of week, day of year, seasons) or
complex numbers or other phase or angular data.

Here are all the built-in scales in the `plotly.colors.cyclical` module:

```python
import plotly.express as px

fig = px.colors.cyclical.swatches_cyclical()
fig.show()

fig = px.colors.cyclical.swatches_continuous()
fig.show()
```
