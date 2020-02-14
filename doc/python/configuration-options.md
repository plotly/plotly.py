---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.1'
      jupytext_version: 1.2.1
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
    description: How to set configuration options of plotly graphs in python.
    display_as: file_settings
    language: python
    layout: base
    name: Configuration
    order: 9
    page_type: u-guide
    permalink: python/configuration-options/
    thumbnail: thumbnail/modebar-icons.png
---


You can pass a `config` dictionary with all configurations options such as `scrollZoom`, `editable`, and `displayModeBar`. For the complete list of config options check out: https://github.com/plotly/plotly.js/blob/master/src/plot_api/plot_config.js

##### Enable Scroll Zoom

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=[1, 2, 3],
        y=[1, 3, 1]))

fig.show(config={'scrollZoom': True})
```

##### Display ModeBar

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=[1, 2, 3],
        y=[1, 3, 1]))

fig.show(config={'displayModeBar': True})
```

##### Edit Mode - change the title and axis titles

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=[1, 2, 3],
        y=[1, 3, 1]))

fig.show(config={'editable': True})
```

##### Multiple Config Options at Once!

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=[1, 2, 3],
        y=[1, 3, 1]))

fig.show(config={
    'scrollZoom': True,
    'displayModeBar': True,
    'editable': True
})
```

##### Remove Modebar Buttons

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=[1, 2, 3],
        y=[1, 3, 1]))

fig.show(config={
    'modeBarButtonsToRemove': ['toggleSpikelines','hoverCompareCartesian']
})
```

### Double-click Delay
Sets the maximum delay between two consecutive clicks to be interpreted as a double-click in ms. This is the time interval between first mousedown, and' second mouseup. The default timing is 300 ms (less than half a second).
This setting propagates to all on-subplot double clicks (except for geo and mapbox). 

```python
import plotly.graph_objects as go

fig = go.Figure(go.Bar(
    y = [3, 5, 3, 2],
    x = ["2019-09-02", "2019-10-10", "2019-11-12", "2019-12-22"],
    texttemplate = "%{label}",
    textposition = "inside"))

fig.update_layout(xaxis = {'type': 'date'})

fig.show(config = {'doubleClickDelay': 1000})
```

#### Reference


See config options at https://github.com/plotly/plotly.js/blob/master/src/plot_api/plot_config.js#L6
