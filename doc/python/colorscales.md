---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: "1.2"
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
    description:
      How to set, create and control continous color scales and color bars
      in scatter, bar, map and heatmap figures.
    display_as: file_settings
    has_thumbnail: true
    ipynb: ~notebook_demo/187
    language: python
    layout: base
    name: Continuous Color Scales and Color Bars
    order: 20
    permalink: python/colorscales/
    redirect_from: python/logarithmic-color-scale/
    thumbnail: thumbnail/heatmap_colorscale.jpg
    v4upgrade: true
---

### Continuous vs Discrete Color

In the same way as the X or Y position of a mark in cartesian coordinates can be used to represent continuous values (i.e. amounts or moments in time) or categories (i.e. labels), color can be used to represent continuous or categorical data. This page is about using color to represent **continuous** data, but Plotly can also [represent categorical values with color](/python/discrete-color/).

### Continuous Color Concepts

This document explains the following four continuous-color-related concepts:

- **color scales** represent a mapping between the range 0 to 1 and some color domain within which colors are to be interpolated (unlike [discrete color sequences](/python/discrete-color/) which are never interpolated). Color scale defaults depend on the `layout.colorscales` attributes of the active [template](/python/templates/), and can be explicitly specified using the `color_continuous_scale` argument for many [Plotly Express](/python/plotly-express/) functions or the `colorscale` argument in various `graph_objects` such as `layout.coloraxis` or `marker.colorscale` in `go.Scatter` traces or `colorscale` in `go.Heatmap` traces. For example `[(0,"blue"), (1,"red")]` is a simple color scale that interpolated between blue and red via purple, which can also be implicitly represented as `["blue", "red"]` and happens to be one of the [built-in color scales](/python/builtin-colorscales) and therefore referred to as `"bluered"` or `plotly.colors.sequential.Bluered`.
- **color ranges** represent the minimum to maximum range of data to be mapped onto the 0 to 1 input range of the color scale. Color ranges default to the range of the input data and can be explicitly specified using either the `range_color` or `color_continous_midpoint` arguments for many Plotly Express functions, or `cmin`/`cmid`/`cmax` or `zmin`/`zmid`/`zmax` for various `graph_objects` such as `layout.coloraxis.cmin` or `marker.cmin` in `go.Scatter` traces or `cmin` in `go.Heatmap` traces. For example, if a color range of `[100, 200]` is used with the color scale above, then any mark with a color value of 100 or less will be blue, and 200 or more will be red. Marks with values in between will be various shades of purple.
- **color bars** are legend-like visible representations of the color range and color scale with optional tick labels and tick marks. Color bars can be configured with attributes inside `layout.coloraxis.colorbar` or in places like `marker.colorbar` in `go.Scatter` traces or `colorbar` in `go.Heatmap` traces.
- **color axes** connect color scales, color ranges and color bars to a trace's data. By default, any colorable attribute in a trace is attached to its own local color axis, but color axes may also be shared across attributes and traces by setting e.g. `marker.coloraxis` in `go.Scatter` traces or `coloraxis` in `go.Heatmap` traces. Local color axis attributes are configured within traces e.g. `marker.showscale` whereas shared color axis attributes are configured within the Layout e.g. `layout.coloraxis.showscale`.

### Continuous Color with Plotly Express

Most Plotly Express functions accept a `color` argument which automatically assigns data values to continuous color **if the data is numeric**. If the data contains strings, the color will automatically be considered [discrete (also known as categorical or qualitative)](/python/discrete-color/). This means that numeric strings must be parsed to be used for continuous color, and conversely, numbers used as category codes must be converted to strings.

For example, in the `tips` dataset, the `size` column contains numbers:

```python
import plotly.express as px
df = px.data.tips()
fig = px.scatter(df, x="total_bill", y="tip", color="size",
                 title="Numeric 'size' values mean continous color")

fig.show()
```

Converting this column to strings is very straightforward:

```python
import plotly.express as px
df = px.data.tips()
df["size"] = df["size"].astype(str)
fig = px.scatter(df, x="total_bill", y="tip", color="size",
                 title="String 'size' values mean discrete colors")

fig.show()
```

If you have stringified numbers you can convert back just as easily:

```python
import plotly.express as px
df = px.data.tips()
df["size"] = df["size"].astype(str)
df["size"] = df["size"].astype(float)
fig = px.scatter(df, x="total_bill", y="tip", color="size",
                 title="Numeric 'size' values mean continous color")

fig.show()
```

### Color Scales in Plotly Express

By default, Plotly Express will use the color scale from the active [template](/python/templates/)'s `layout.colorscales.sequential` attribute, and the default active template is `plotly` which uses the `Plasma` color scale. You can choose any of the [built-in color scales](/python/builtin-colorscales/), however, or define your own.

Here is an example that creates a scatter plot using Plotly Express, with points colored using the Viridis color scale.

```python
import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length",
                 color="sepal_length", color_continuous_scale=px.colors.sequential.Viridis)

fig.show()
```

It is also possible to specify color scales by name. Here is an example that specifies the `Inferno` color scale by name, as a string

```python
import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length",
                 color="sepal_length", color_continuous_scale='Inferno')

fig.show()
```

### Reversing a built-in color scale

You can reverse a [built-in color scale](/python/builtin-colorscales/) by appending `_r` to its name, for color scales given either as a string or a `plotly` object.

```python
import plotly.express as px
df = px.data.gapminder().query("year == 2007").sort_values(by="lifeExp")
fig = px.bar(df, y="continent", x="pop", color="lifeExp", orientation="h",
             color_continuous_scale='Bluered_r', hover_name="country")

fig.show()
```

```python
import plotly.express as px
data = [[1, .3, .5, .9],
        [.3, .1, .4, 1],
        [.2, .8, .9, .3]]
fig = px.imshow(data, color_continuous_scale=px.colors.sequential.Cividis_r)
fig.show()
```

### Explicity Constructing a Color scale

The Plotly Express `color_continuous_scale` argument accepts explicitly-constructed color scales as well:

```python
import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="sepal_length",
                 color_continuous_scale=["red", "green", "blue"])

fig.show()
```

The example above provided a list of CSS colors to construct a scale, which inferred the reference points to be evenly spaced, but specific reference points can be provided as well. The following example has the same result:

```python
import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="sepal_length",
                 color_continuous_scale=[(0, "red"), (0.5, "green"), (1, "blue")])

fig.show()
```

### Constructing a Discrete or Discontinuous Color Scale

You can create a discrete color scale, with discontinuous color, by setting the same reference point twice in a row. This is useful for example with chart types that don't support discrete colors, like [Parallel Coordinates plots](/python/parallel-coordinates-plot/). See below for how to customize tick text.

```python
import plotly.express as px
df = px.data.iris()
fig = px.parallel_coordinates(df, color="species_id",
                             color_continuous_scale=[(0.00, "red"),   (0.33, "red"),
                                                     (0.33, "green"), (0.66, "green"),
                                                     (0.66, "blue"),  (1.00, "blue")])
fig.show()
```

### Explicitly setting a Color Range

When using the range of the input data as the color range is inappropriate, for example when producing many figures which must have comparable color ranges, or to clip the color range to account for outliers, the Plotly Express `range_color` argument can be used. Here we clip the top of the color range above the lower range of the data and extend it below the lower range of the data:

```python
import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="sepal_length", range_color=[5,8])

fig.show()
```

### Setting the Midpoint of a Color Range for a Diverging Color scale

Diverging color scales have a well-defined midpoint color, and are best-used when that midpoint is mapped to a meaningful data value. The `color_continuous_midpoint` argument to most Plotly Express functions is used for this. It cannot be used with `range_color` because setting it forces the color range to be centered on the midpoint while including the entire dataset. This means that for asymmetric data distributions, not all colors in the color scale will appear in the figure.

For example, a diverging color scale could be used to highlight points with a higher and lower value than the median in a choropleth map like this:

```python
import plotly.express as px

df = px.data.gapminder().query("year == 2007")
avg_lifeExp = (df['lifeExp']*df['pop']).sum()/df['pop'].sum()

fig = px.choropleth(df, locations="iso_alpha", color="lifeExp",
                    color_continuous_scale=px.colors.diverging.BrBG,
                    color_continuous_midpoint=avg_lifeExp,
                    title="World Average Life Expectancy in 2007 in years was %.1f" % avg_lifeExp)
fig.show()
```

### Hiding or Customizing the Plotly Express Color Bar

Plotly Express binds all traces to [`layout.coloraxis`](/python/reference/#layout-coloraxis), rather than using trace-specific color axes. This means that the color bar can configured there, for example it can be hidden:

```python
import plotly.express as px
df = px.data.tips()
fig = px.density_heatmap(df, x="total_bill", y="tip", title="No color bar on this density plot")

fig.update_layout(coloraxis_showscale=False)

fig.show()
```

You can also configure the title, size, placement and tick marks and labels on a color bar:

```python
import plotly.express as px
df = px.data.tips()
fig = px.density_heatmap(df, x="total_bill", y="tip", title="Customized color bar on this density plot")

fig.update_layout(coloraxis_colorbar=dict(
    title="Number of Bills per Cell",
    thicknessmode="pixels", thickness=50,
    lenmode="pixels", len=200,
    yanchor="top", y=1,
    ticks="outside", ticksuffix=" bills",
    dtick=5
))

fig.show()
```

### Customizing Tick Text on Discrete Color Bars

This is the same example as the Parallel Coordinates plot above, with customized tick text for species:

```python
import plotly.express as px
df = px.data.iris()
fig = px.parallel_coordinates(df, dimensions=["sepal_length", "sepal_width", "petal_length", "petal_width"],
                             color="species_id", range_color=[0.5, 3.5],
                             color_continuous_scale=[(0.00, "red"),   (0.33, "red"),
                                                     (0.33, "green"), (0.66, "green"),
                                                     (0.66, "blue"),  (1.00, "blue")])

fig.update_layout(coloraxis_colorbar=dict(
    title="Species",
    tickvals=[1,2,3],
    ticktext=["setosa","versicolor","virginica"],
    lenmode="pixels", len=100,
))
fig.show()
```

### Customizing Tick Text on Logarithmic Color Bars

You can customize text on a logarithmic color bar to make it more readable:

```python
import plotly.express as px
import numpy as np

df = px.data.gapminder().query("year == 2007")
fig = px.scatter(df, y="lifeExp", x="pop", color=np.log10(df["pop"]), hover_name="country", log_x=True)

fig.update_layout(coloraxis_colorbar=dict(
    title="Population",
    tickvals=[6,7,8,9],
    ticktext=["1M", "10M", "100M", "1B"],
))
fig.show()
```

### Custom Discretized Heatmap Color scale with Graph Objects

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Heatmap(
    z=[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]],
    colorscale=[
        # Let first 10% (0.1) of the values have color rgb(0, 0, 0)
        [0, "rgb(0, 0, 0)"],
        [0.1, "rgb(0, 0, 0)"],

        # Let values between 10-20% of the min and max of z
        # have color rgb(20, 20, 20)
        [0.1, "rgb(20, 20, 20)"],
        [0.2, "rgb(20, 20, 20)"],

        # Values between 20-30% of the min and max of z
        # have color rgb(40, 40, 40)
        [0.2, "rgb(40, 40, 40)"],
        [0.3, "rgb(40, 40, 40)"],

        [0.3, "rgb(60, 60, 60)"],
        [0.4, "rgb(60, 60, 60)"],

        [0.4, "rgb(80, 80, 80)"],
        [0.5, "rgb(80, 80, 80)"],

        [0.5, "rgb(100, 100, 100)"],
        [0.6, "rgb(100, 100, 100)"],

        [0.6, "rgb(120, 120, 120)"],
        [0.7, "rgb(120, 120, 120)"],

        [0.7, "rgb(140, 140, 140)"],
        [0.8, "rgb(140, 140, 140)"],

        [0.8, "rgb(160, 160, 160)"],
        [0.9, "rgb(160, 160, 160)"],

        [0.9, "rgb(180, 180, 180)"],
        [1.0, "rgb(180, 180, 180)"]
    ],
    colorbar=dict(
        tick0=0,
        dtick=1
    )
))

fig.show()
```

### Color scale for Scatter Plots with Graph Objects

```python
import plotly.graph_objects as go

fig = go.Figure()

# Create list from 0 to 39 to use as x, y, and color
values = list(range(40))

fig.add_trace(go.Scatter(
    x=values,
    y=values,
    marker=dict(
        size=16,
        cmax=39,
        cmin=0,
        color=values,
        colorbar=dict(
            title="Colorbar"
        ),
        colorscale="Viridis"
    ),
    mode="markers"))

fig.show()
```

### Color scale for Contour Plot with Graph Objects

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Contour(
    z=[[10, 10.625, 12.5, 15.625, 20],
       [5.625, 6.25, 8.125, 11.25, 15.625],
       [2.5, 3.125, 5., 8.125, 12.5],
       [0.625, 1.25, 3.125, 6.25, 10.625],
       [0, 0.625, 2.5, 5.625, 10]],
    colorscale="Cividis",
))

fig.show()
```

### Custom Heatmap Color scale with Graph Objects

```python
import plotly.graph_objects as go

import six.moves.urllib
import json

response = six.moves.urllib.request.urlopen(
    "https://raw.githubusercontent.com/plotly/datasets/master/custom_heatmap_colorscale.json"
)

dataset = json.load(response)

fig = go.Figure()

fig.add_trace(go.Heatmap(
    z=dataset["z"],
    colorscale=[[0.0, "rgb(165,0,38)"],
                [0.1111111111111111, "rgb(215,48,39)"],
                [0.2222222222222222, "rgb(244,109,67)"],
                [0.3333333333333333, "rgb(253,174,97)"],
                [0.4444444444444444, "rgb(254,224,144)"],
                [0.5555555555555556, "rgb(224,243,248)"],
                [0.6666666666666666, "rgb(171,217,233)"],
                [0.7777777777777778, "rgb(116,173,209)"],
                [0.8888888888888888, "rgb(69,117,180)"],
                [1.0, "rgb(49,54,149)"]]
))

fig.show()
```

### Setting the Midpoint of a Diverging Color scale with Graph Objects

The following example uses the [marker.cmid](https://plot.ly/python/reference/#scatter-marker-cmid) attribute to set the mid-point of the color domain by scaling 'cmin' and/or 'cmax' to be equidistant to this point. It only has impact when [marker.color](https://plot.ly/python/reference/#scattercarpet-marker-line-color) sets to a numerical array, and 'marker.cauto' is `True`.

```python
import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Scatter(
    y=list(range(-5,15)),
    mode="markers",
    marker={"size": 25, "color": list(range(-3,10)), "cmid": 0}))

fig.show()
```

The heatmap chart uses [marker.zmid](https://plot.ly/python/reference/#scatter-marker-zmid) attribute to set the mid-point of the color domain.

```python
import plotly.graph_objects as go

a = list(range(-10,5))
b = list(range(-5,10))
c = list(range(-5,15))

fig = go.Figure(go.Heatmap(
    z=[a, b, c],
    colorscale='RdBu',
    zmid=0))

fig.show()
```

### Custom Contour Plot Color scale with Graph Objects

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Contour(
    z=[[10, 10.625, 12.5, 15.625, 20],
       [5.625, 6.25, 8.125, 11.25, 15.625],
       [2.5, 3.125, 5., 8.125, 12.5],
       [0.625, 1.25, 3.125, 6.25, 10.625],
       [0, 0.625, 2.5, 5.625, 10]],
    colorscale=[[0, "rgb(166,206,227)"],
                [0.25, "rgb(31,120,180)"],
                [0.45, "rgb(178,223,138)"],
                [0.65, "rgb(51,160,44)"],
                [0.85, "rgb(251,154,153)"],
                [1, "rgb(227,26,28)"]],
))

fig.show()
```

### Custom Color bar Title, Labels, and Ticks with Graph Objects

Like axes, you can customize the color bar ticks, labels, and values with `ticks`, `ticktext`, and `tickvals`.

```python
import plotly.graph_objects as go

import six.moves.urllib
import json

# Load heatmap data
response = six.moves.urllib.request.urlopen(
    "https://raw.githubusercontent.com/plotly/datasets/master/custom_heatmap_colorscale.json")
dataset = json.load(response)

# Create and show figure
fig = go.Figure()

fig.add_trace(go.Heatmap(
    z=dataset["z"],
    colorbar=dict(
        title="Surface Heat",
        titleside="top",
        tickmode="array",
        tickvals=[2, 50, 100],
        ticktext=["Cool", "Mild", "Hot"],
        ticks="outside"
    )
))

fig.show()
```

### Sharing a Color Axis with Graph Objects

To share colorscale information in multiple subplots, you can use [coloraxis](https://plot.ly/javascript/reference/#scatter-marker-line-coloraxis).

```python
import plotly.graph_objects as go
from plotly.subplots import make_subplots

fig = make_subplots(1,2)

fig.add_trace(
 go.Heatmap(x = [1, 2, 3, 4], z = [[1, 2, 3, 4], [4, -3, -1, 1]], coloraxis = "coloraxis"), 1,1)

fig.add_trace(
 go.Heatmap(x = [3, 4, 5, 6], z = [[10, 2, 1, 0], [4, 3, 5, 6]], coloraxis = "coloraxis"),1,2)
fig.update_layout(coloraxis = {'colorscale':'viridis'})

fig.show()
```

### Logarithmic Color scale with Graph Objects

```python
import plotly.graph_objects as go

fig = go.Figure(go.Heatmap(
    z= [[10, 100.625, 1200.5, 150.625, 2000],
       [5000.625, 60.25, 8.125, 100000, 150.625],
       [2000.5, 300.125, 50., 8.125, 12.5],
       [10.625, 1.25, 3.125, 6000.25, 100.625],
       [0, 0.625, 2.5, 50000.625, 10]],
    colorscale= [
        [0, 'rgb(250, 250, 250)'],        #0
        [1./10000, 'rgb(200, 200, 200)'], #10
        [1./1000, 'rgb(150, 150, 150)'],  #100
        [1./100, 'rgb(100, 100, 100)'],   #1000
        [1./10, 'rgb(50, 50, 50)'],       #10000
        [1., 'rgb(0, 0, 0)'],             #100000

    ],
    colorbar= dict(
        tick0= 0,
        tickmode= 'array',
        tickvals= [0, 1000, 10000, 100000]
    )
))

fig.show()
```

### Reference

See https://plot.ly/python/reference/ for more information and chart attribute options!
