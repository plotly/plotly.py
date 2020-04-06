---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.1'
      jupytext_version: 1.1.1
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
    version: 3.7.0
  plotly:
    description: How to set the configuration options of figures using the Plotly
      Python graphing library.
    display_as: file_settings
    language: python
    layout: base
    name: Configuration
    order: 9
    page_type: u-guide
    permalink: python/configuration-options/
    thumbnail: thumbnail/modebar-icons.png
---

# Configuration Options

The `.show()` method that you use to display your figures also accepts a `config` parameter.

You can set the configuration options for your figure by passing a dictionary to this parameter which contains the options you want to set.

If you don't set an option's value, it will be automatically be set to the default value for that option.

For the complete list of configuration options and their defaults see: https://github.com/plotly/plotly.js/blob/master/src/plot_api/plot_config.js

##### Enabling Scroll Zoom

This option allows users to zoom in and out of figures using the scroll wheel on their mouse and/or a two-finger scroll.

```python
import plotly.graph_objects as go

fig = go.Figure()

config = dict({'scrollZoom': True})

fig.add_trace(
    go.Scatter(
        x=[1, 2, 3],
        y=[1, 3, 1]))

fig.show(config=config)
```

##### Forcing The Modebar to Always Be Visible

When users hover over a figure generated with plotly.py, a modebar appears in the top-right of the figure. This presents users with several options for interacting with the figure.

By default, the modebar is only visible while the user is hovering over the chart. If you would like the modebar to always be visible regardless of whether or not the user is currently hovering over the figure, set the displayModeBar attribute in the configuration of your figure to true.

```python
import plotly.graph_objects as go

fig = go.Figure()

config = {'displayModeBar': True}

fig.add_trace(
    go.Scatter(
        x=[1, 2, 3],
        y=[1, 3, 1]))

fig.show(config=config)
```

##### Preventing the Modebar from Appearing

When users hover over a figure generated with `plotly.py`, a modebar appears in the top-right of the figure. This presents users with several options for interacting with the figure.

By default, the modebar is only visible while the user is hovering over the chart. If you would like the modebar to never be visible, then set the `displayModeBar` attribute in the config of your figure to false.

```python
import plotly.graph_objects as go

fig = go.Figure()

config = {'displayModeBar': False}

fig.add_trace(
    go.Scatter(
        x=[1, 2, 3],
        y=[1, 3, 1]))

fig.show(config=config)
```


##### Hiding the Plotly Logo on the Modebar

```python
import plotly.graph_objects as go

fig = go.Figure()

config = {'displaylogo': False}

fig.add_trace(
    go.Scatter(
        x=[1, 2, 3],
        y=[1, 3, 1]))

fig.show(config=config)
```

##### Turning Off Responsiveness

By default, figures you create with the `plotly.py` package are [responsive](https://en.wikipedia.org/wiki/Responsive_web_design). Responsive figures automatically change their height and width when the size of the window they are displayed in changes. This is true for figures which are displayed in web browsers on desktops and mobile, Jupyter Notebooks, and other [rendering](https://plot.ly/python/renderers/) environments.

Try resizing your browser window to see this behavior in effect on this page.

If you would like to disable this default behavior and force your figures to always have the same height and width regardless of the window size, set the value of the `responsive` key to `False` in your figure's configuration dictionary.

```python
import plotly.graph_objects as go

fig = go.Figure()

config = {'responsive': False}

fig.add_trace(
    go.Scatter(
        x=[1, 2, 3],
        y=[1, 3, 1]))

fig.show(config=config)
```

##### Making A Static Chart

```python
import plotly.graph_objects as go

fig = go.Figure()

config = {'staticPlot': True}

fig.add_trace(
    go.Scatter(
        x=[1, 2, 3],
        y=[1, 3, 1]))

fig.show(config=config)
```

##### Customizing Download Plot Options

```python
import plotly.graph_objects as go

fig = go.Figure()

config = {
  'toImageButtonOptions': {
    'format': 'svg', # one of png, svg, jpeg, webp
    'filename': 'custom_image',
    'height': 500,
    'width': 700,
    'scale': 1 # Multiply title/legend/axis/canvas sizes by this factor
  }
}

fig.add_trace(
    go.Scatter(
        x=[1, 2, 3],
        y=[1, 3, 1]))

fig.show(config=config)
```

##### Specifying Multiple Configuration Options Simultaneously

The dictionary that you use to specify configuration options for your figures can contain more than one configuration key/value pair.

```python
import plotly.graph_objects as go

fig = go.Figure()

config = dict({
    'scrollZoom': True,
    'displayModeBar': True,
    'editable': True
})

fig.add_trace(
    go.Scatter(
        x=[1, 2, 3],
        y=[1, 3, 1]))

fig.show(config=config)
```

##### Removing Modebar Buttons

To delete buttons from the modebar, pass an array of strings containing the names of the buttons you want to remove to the `modeBarButtonsToRemove` attribute in the figure's configuration dictionary. Note that different chart types have different default modebars. The following is a list of all the modebar buttons and the chart types they are associated with:

-'2D': `zoom2d`, `pan2d`, `select2d`, `lasso2d`, `zoomIn2d`, `zoomOut2d`, `autoScale2d`, `resetScale2d`
-'3D': `zoom3d`, `pan3d`, `rbitRotation`, `tableRotation`, `handleDrag3d`, `resetCameraDefault3d`, `resetCameraLastSave3d`, `hoverClosest3d`
-'Cartesian': `hoverClosestCartesian`, `hoverCompareCartesian`
-'Geo': `zoomInGeo`, `zoomOutGeo`, `resetGeo`, `hoverClosestGeo`
-'Other': `hoverClosestGl2d`, `hoverClosestPie`, `toggleHover`, `resetViews`, `toImage: sendDataToCloud`, `toggleSpikelines`, `resetViewMapbox`

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

### Double-Click Delay
Sets the maximum delay between two consecutive clicks to be interpreted as a double-click in milliseconds. This is the time interval between first mousedown and second mouseup. The default timing is 300 ms (less than half a second).
This setting propagates to all on-subplot double clicks (except for `geo` and `mapbox`).

```python
import plotly.graph_objects as go

config = {'doubleClickDelay': 1000}

fig = go.Figure(go.Bar(
    y = [3, 5, 3, 2],
    x = ["2019-09-02", "2019-10-10", "2019-11-12", "2019-12-22"],
    texttemplate = "%{label}",
    textposition = "inside"))

fig.update_layout(xaxis = {'type': 'date'})

fig.show(config=config)
```

#### Configuring Figures in Dash Apps

The same configuration dictionary that you pass to the `config` parameter of the `show()` method can also be passed to the [`config` property of a `dcc.Graph` component](https://dash.plotly.com/dash-core-components/graph).

#### Reference

See config options at https://github.com/plotly/plotly.js/blob/master/src/plot_api/plot_config.js#L6
