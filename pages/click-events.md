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
    description: Click Events With FigureWidget
    display_as: chart_events
    language: python
    layout: base
    name: Click Events
    order: 4
    page_type: example_index
    permalink: python/click-events/
    thumbnail: thumbnail/figurewidget-click-events.gif
---

#### Update Points Using a Click Callback

```python
import plotly.graph_objects as go

import numpy as np
np.random.seed(1)

x = np.random.rand(100)
y = np.random.rand(100)

f = go.FigureWidget([go.Scatter(x=x, y=y, mode='markers')])

scatter = f.data[0]
colors = ['#a3a7e4'] * 100
scatter.marker.color = colors
scatter.marker.size = [10] * 100
f.layout.hovermode = 'closest'


# create our callback function
def update_point(trace, points, selector):
    c = list(scatter.marker.color)
    s = list(scatter.marker.size)
    for i in points.point_inds:
        c[i] = '#bae2be'
        s[i] = 20
        with f.batch_update():
            scatter.marker.color = c
            scatter.marker.size = s


scatter.on_click(update_point)

f
```

<img src='https://raw.githubusercontent.com/michaelbabyn/plot_data/master/figurewidget-click-event.gif'>


#### Reference


See [these Jupyter notebooks](https://github.com/jonmmease/plotly_ipywidget_notebooks) for even more FigureWidget examples.

```python
import plotly.graph_objects as go
f = go.FigureWidget([go.Scatter()])
help(f.data[0].on_click)
```

**Output:**
```
Help on method on_click in module plotly.basedatatypes:

on_click(callback, append=False) method of plotly.graph_objects._scatter.Scatter instance
    Register function to be called when the user clicks on one or more
    points in this trace.

    Note: Callbacks will only be triggered when the trace belongs to a
    instance of plotly.graph_objects.FigureWidget and it is displayed in an
    ipywidget context. Callbacks will not be triggered on figures
    that are displayed using plot/iplot.

    Parameters
    ----------
    callback
        Callable function that accepts 3 arguments

        - this trace
        - plotly.callbacks.Points object
        - plotly.callbacks.InputDeviceState object

    append : bool
        If False (the default), this callback replaces any previously
        defined on_click callbacks for this trace. If True,
        this callback is appended to the list of any previously defined
        callbacks.

    Returns
    -------
    None

    Examples
    --------

    >>> import plotly.graph_objs as go
    >>> from plotly.callbacks import Points, InputDeviceState
    >>> points, state = Points(), InputDeviceState()

    >>> def click_fn(trace, points, state):
    ...     inds = points.point_inds
    ...     # Do something

    >>> trace = go.Scatter(x=[1, 2], y=[3, 0])
    >>> trace.on_click(click_fn)

    Note: The creation of the `points` and `state` objects is optional,
    it's simply a convenience to help the text editor perform completion
    on the arguments inside `click_fn`
```
