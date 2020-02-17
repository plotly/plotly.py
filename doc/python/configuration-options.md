---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.3.2
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
    description: How to set the configuration options of figures using Plotly Python graphing library.
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

The `show()` method that you use to display your figures also accepts a `config` parameter.

You can set the configuration options for your figure by passing a dictionary to this parameter which contains the options you want to set. 

If you don't set an option's value, it will be automatically be set to the default value for that option. 

For the complete list of configuration options and their defaults see: https://github.com/plotly/plotly.js/blob/master/src/plot_api/plot_config.js

##### Enable Scroll Zoom

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

##### Force The Modebar to Always Be Visible

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

##### Never Display The Modebar

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

##### Display the `Edit Chart` Link

Set `showLink` to `True` in order to make your figure editable on [Chart Studio](https://plot.ly/online-chart-maker). 

```python
import plotly.graph_objects as go

fig = go.Figure()

config = {'showLink': True}

fig.add_trace(
    go.Scatter(
        x=[1, 2, 3],
        y=[1, 3, 1]))

fig.show(config=config)
```

### Display The `Edit In Chart Studio` Modebar Button

```python
import plotly.graph_objects as go

fig = go.Figure()

config = {'showEditInChartStudio': True}

fig.add_trace(
    go.Scatter(
        x=[1, 2, 3],
        y=[1, 3, 1]))

fig.show(config=config)
```

##### Hide the Plotly Logo on the Modebar

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

##### Making A Responsive Chart

```python
import plotly.graph_objects as go

fig = go.Figure()

config = {'responsive': True}

fig.add_trace(
    go.Scatter(
        x=[1, 2, 3],
        y=[1, 3, 1]))

fig.show(config=config)
```

##### Editable Mode

In editable mode, users can edit the chart title, axis labels and trace names in the legend.

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=[1, 2, 3],
        y=[1, 3, 1]))

fig.show(config={'editable': True})
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

##### Customize Download Plot Options

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

##### Specifying Multiple Configuration Options Simultaneously!

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

##### Remove Modebar Buttons

To delete buttons from the modebar, pass an array of strings containing the names of the buttons you want to remove to the modeBarButtonsToRemove attribute in the figure's configuration dictionary. Note that different chart types have different default modebars. The following is a list of all the modebar buttons and the chart types they are associated with:

-'2D': `zoom2d`, `pan2d`, `select2d`, `lasso2d`, `zoomIn2d`, `zoomOut2d`, `autoScale2d`, `resetScale2d`
-'3D': `zoom3d`, `pan3d`, `rbitRotation`, `tableRotation`, `handleDrag3d`, resetCameraDefault3d, resetCameraLastSave3d, `hoverClosest3d`
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

### Double Click Delay
Sets the maximum delay between two consecutive clicks to be interpreted as a double-click in `ms`. This is the time interval between first mousedown and second mouseup. The default timing is 300 ms (less than half a second).
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

The same configuration dictionary that you pass to the `config` parameter of the `show()` method can also be passed to the `config` parameter of a `dcc.Graph` component.

```python
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

config = dict({
    'scrollZoom': True,
    'displayModeBar': True,
    'editable': True
})

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        },
        config=config
    )
])

# if __name__ == '__main__':
    # app.run_server(debug=True)
```

#### Reference


See config options at https://github.com/plotly/plotly.js/blob/master/src/plot_api/plot_config.js#L6
