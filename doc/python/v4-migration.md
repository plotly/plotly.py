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
    version: 3.6.7
  plotly:
    description: Migration guide for upgrading from version 3 to version 4
    display_as: file_settings
    language: python
    layout: base
    name: Version 4 Migration Guide
    order: 3
    page_type: example_index
    permalink: python/v4-migration/
    thumbnail: thumbnail/v4-migration.png
---

### Upgrading to Version 4

Upgrading to version 4 of `plotly` is a matter of following the instructions in the [Getting Started](/python/getting-started/) guide and reinstalling the packages, subject to the notices below.

### Getting Help

If you encounter issues in upgrading from version 3 to version 4, please reach out in our [Community Forum](https://community.plot.ly/c/api/python) or if you've found an issue or regression in version 4, please report a [Github Issue](https://github.com/plotly/plotly.py/issues/new)

<!-- #region -->
### Online features (`plotly.plotly`) moved to `chart-studio` package

Prior versions of plotly.py contained functionality for creating figures in both "online" and "offline" modes.  In "online" mode figures were uploaded to the Chart Studio cloud (or on-premise) service, whereas in "offline" mode figures were rendered locally.  **Version 4 of `plotly` is "offline"-only: all "online" functionality has been removed from the main `plotly` distribution package and moved to the new `chart-studio` distribution package.**

To migrate version 3 "online" functionality, first install the `chart-studio` package using pip...

```
$ pip install chart-studio
```

of conda.

```
$ conda install -c plotly chart-studio
```

Then, update your Python import statements to import "online" functionality from the top-level `chart_studio` package, rather than the top-level `plotly` package.  For example. replace

```python
from plotly.plotly import plot, iplot
```

with

```python
from chart_studio.plotly import plot, iplot
```

Similarly,
 - Replace **`plotly.api`** with **`chart_studio.api`**
 - Replace **`plotly.dashboard_objs`** with **`chart_studio.dashboard_objs`**
 - Replace **`plotly.grid_objs`** with **`chart_studio.grid_objs`**
 - Replace **`plotly.presentation_objs`** with **`chart_studio.presentation_objs`**
 - Replace **`plotly.widgets`** with **`chart_studio.widgets`**
<!-- #endregion -->

<!-- #region -->
### Offline features (`plotly.offline`) replaced by Renderers framework & HTML export

Version 4 introduces a new renderers framework that is a generalization of version 3's `plotly.offline.init_notebook_mode` and `plotly.offline.iplot` functions for displaying figures.  *This is a non-breaking change*: the `plotly.offline.iplot` function is still available and has been reimplemented on top of the renderers framework, so no changes are required when porting to version 4.  Going forward, we recommend using the renderers framework directly. See [Displaying plotly figures](/python/renderers) for more information.


In version 3, the `plotly.offline.plot` function was used to export figures to HTML files.  In version 4, this function has been reimplemented on top of the new `to_html` and `write_html` functions from the `plotly.io` module.  These functions have a slightly more consistent API (see docstrings for details), and going forward we recommend using them directly when performing HTML export. When working with a graph object figure, these functions are also available as the `.to_html` and `.write_html` figure methods.
<!-- #endregion -->

### New default theme
An updated `"plotly"` theme has been enabled by default in version 4.

```python
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

# Make figure with subplots
fig = make_subplots(rows=1, cols=2, specs=[[{"type": "bar"},
                                            {"type": "surface"}]])

# Add bar traces to subplot (1, 1)
fig.add_trace(go.Bar(y=[2, 1, 3]), row=1, col=1)
fig.add_trace(go.Bar(y=[3, 2, 1]), row=1, col=1)
fig.add_trace(go.Bar(y=[2.5, 2.5, 3.5]), row=1, col=1)

# Add surface trace to subplot (1, 2)
# Read data from a csv
z_data = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv")
fig.add_surface(z=z_data)

# Hide legend
fig.update_layout(
    showlegend=False,
    title_text="Default Theme",
    height=500,
    width=800,
)

fig.show()
```

You can revert to the version 3 figure appearance by disabling the default theme as follows:

```python
import plotly.io as pio
pio.templates.default = "none"

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

# Make figure with subplots
fig = make_subplots(rows=1, cols=2, specs=[[{"type": "bar"},
                                            {"type": "surface"}]])

# Add bar traces to subplot (1, 1)
fig.add_trace(go.Bar(y=[2, 1, 3]), row=1, col=1)
fig.add_trace(go.Bar(y=[3, 2, 1]), row=1, col=1)
fig.add_trace(go.Bar(y=[2.5, 2.5, 3.5]), row=1, col=1)

# Add surface trace to subplot (1, 2)
# Read data from a csv
z_data = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv")
fig.add_surface(z=z_data)

# Hide legend
fig.update_layout(
    showlegend=False,
    title_text="Default Theme Disabled",
    height=500,
    width=800,
)

fig.show()
```

```python
# Restore default theme
pio.templates.default = "plotly"
```

See [Theming and templates](/python/templates) for more information on theming in plotly.py version 4.

### Add trace return value
In version 3, the `add_trace` graph object figure method returned a reference to the newly created trace. This was also the case for the `add_{trace_type}` methods (e.g. `add_scatter`, `add_bar`, etc.).  In version 4, these methods return a reference to the calling figure.  This change was made to support method chaining of figure operations. For example

```python
from plotly.subplots import make_subplots
(make_subplots(rows=1, cols=2)
 .add_scatter(y=[2, 1, 3], row=1, col=1)
 .add_bar(y=[3, 2, 1], row=1, col=2)
 .update_layout(
     title_text="Figure title",
     showlegend=False,
     width=800,
     height=500,
 )
 .show())
```

<!-- #region -->
Code that relied on the `add_*` methods to return a reference to the newly created trace will need to be updated to access the trace from the returned figure.  This can be done by appending `.data[-1]` to the add trace expression.

Here is an example of a version 3 code snippet that adds a scatter trace to a figure, assigns the result to a variable named `scatter`, and then modifies the marker size of the scatter trace.

```python
import plotly.graph_objs as go
fig = go.Figure()
scatter = fig.add_trace(go.Scatter(y=[2, 3, 1]))
scatter.marker.size = 20
```
In version 4, this would be replaced with the following:

```python
import plotly.graph_objects as go
fig = go.Figure()
scatter = fig.add_trace(go.Scatter(y=[2, 3, 1])).data[-1]
scatter.marker.size = 20
```
<!-- #endregion -->

### `make_subplots` updates
The `make_subplots` function has been overhauled to support all trace types and to support the integration of Plotly Express.  Here are a few changes to be aware of when porting code that uses `make_subplots` to version 4.

#### New preferred import location
The preferred import location of the `make_subplots` function is now `plotly.subplots.make_subplots`.  For compatibility, this function is still available as `plotly.tools.make_subplots`.

#### Grid no longer printed by default
When the `print_grid` argument to `make_subplots` is set to `True`, a text representation of the subplot grid is printed by the `make_subplots` function.  In version 3, the default value of `print_grid` was `True`. In version 4, the default value of `print_grid` is `False`.

#### New `row_heights` argument to replace `row_width`
The legacy argument for specifying the relative height of subplot rows was called `row_width`. A new `row_heights` argument has been introduced for this purpose.

> Note: Although it is not mentioned in the docstring for `plotly.subplots.make_subplots`, the legacy `row_width` argument, with the legacy behavior, is still available in version 4.

In addition to having a more consistent name, values specified to the new `row_heights` argument properly honor the `start_cell` argument.  With the legacy `row_width` argument, the list of heights was always interpreted from the bottom row to the top row, even if `start_cell=="top-left"`. With the new `row_heights` argument, the list of heights is interpreted from top to bottom if `start_cell=="top-left"` and from bottom to top if `start_cell=="bottom-left"`.

When porting code from `row_width` to `row_heights`, the order of the heights list must be reversed if `start_cell=="top-left"` or `start_cell` was unspecified.

Here is a version 3 compatible example that uses the `row_width` argument to create a figure with subplots where the top row is twice as tall as the bottom row.

```python
from plotly.subplots import make_subplots

fig = make_subplots(
    rows=2, cols=1,
    row_width=[0.33, 0.67],
    start_cell="top-left")

fig.add_scatter(y=[2, 1, 3], row=1, col=1)
fig.add_bar(y=[2, 3, 1], row=2, col=1)
fig.show()
```

And here is the equivalent, version 4 example. Note how the order to the height list is reversed compared to the example above.

```python
from plotly.subplots import make_subplots

fig = make_subplots(
    rows=2, cols=1,
    row_heights=[0.67, 0.33],
    start_cell="top-left")

fig.add_scatter(y=[2, 1, 3], row=1, col=1)
fig.add_bar(y=[2, 3, 1], row=2, col=1)
fig.show()
```

#### Implementation of shared axes with `make_subplots`
The implementation of shared axis support in the `make_subplots` function has been simplified.  Prior to version 4, shared y-axes were implemented by associating a single `yaxis` object with multiple `xaxis` objects, and vica versa.

In version 4, every 2D Cartesian subplot has a dedicated x-axis and and a dedicated y-axis. Axes are now "shared" by being linked together using the `matches` axis property.

For legacy code that makes use of the `make_subplots` and add trace APIs, this change does not require any action on the user's part.  However, legacy code that uses `make_subplots` to create a figure with shared axes, and then manipulates the axes directly, may require updates.  The output of the `.print_grid` method on a figure created using `make_subplots` can be used to identify which axis objects are associated with each subplot.

```python
from plotly.subplots import make_subplots
fig = make_subplots(rows=1, cols=2, shared_yaxes=True)
fig.print_grid()
print(fig)
```

### Trace UIDs
In version 3, all trace graph objects were copied and assigned a new `uid` property when being added to a `Figure`. In version 4, these `uid` properties are only generated automatically when a trace is added to a `FigureWidget`.  When a trace is added to a standard `Figure` graph object the input `uid`, if provided, is accepted as is.

### Timezones
Prior to version 4, when plotly.py was passed a `datetime` that included a timezone, the `datetime` was automatically converted to UTC.  In version 4, this conversion is no longer performed, and `datetime` objects are accepted and displayed in local time.

<!-- #region -->
### Headless image export on Linux with Xvfb.
In version 4, the static image export logic attempts to automatically detect whether to call the orca image export utility using Xvfb.  Xvfb is needed for orca to work in a Linux environment if an X11 display server is not available. By default, Xvfb us used if plotly.py is running on Linux if no X11 display server is detected and `Xvfb` is available on the system `PATH`.

This new behavior can be disabled by setting the `use_xvfb` orca configuration option to `False` as follows:

```python
import plotly.io as pio
pio.orca.config.use_xvfb = False
```
<!-- #endregion -->

### Removals

#### fileopt argument removal
The `fileopt` argument to `chart_studio.plotly.plot` has been removed, so in-place modifications to previously published figures are no longer supported.

#### Legacy online `GraphWidget`
The legacy online-only `GraphWidget` class has been removed.  Please use the `plotly.graph_objects.FigureWidget` class instead. See the [Figure Widget Overview](/python/figurewidget/) for more information.

### Recommended style updates

#### Import from `graph_objects` instead of `graph_objs`
The legacy `plotly.graph_objs` package has been aliased as `plotly.graph_objects` because the latter is much easier to communicate verbally. The `plotly.graph_objs` package is still available for backward compatibility.

