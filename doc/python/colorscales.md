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
    description: How to set colorscales and heatmap colorscales in Python and Plotly.
      Divergent, sequential, and qualitative colorscales.
    display_as: file_settings
    has_thumbnail: true
    ipynb: ~notebook_demo/187
    language: python
    layout: base
    name: Colorscales
    order: 20
    permalink: python/colorscales/
    redirect_from: python/logarithmic-color-scale/
    thumbnail: thumbnail/heatmap_colorscale.jpg
    v4upgrade: true
---

### Predefined colorscales in Plotly Express
A collection of predefined sequential colorscales is provided in the `plotly.express.colors.sequential` module.

Here is an example that creates a scatter plot using Plotly Express, with points colored using the Viridis colorscale.

```python
import plotly.express as px
iris = px.data.iris()
fig = px.scatter(iris, x="sepal_width", y="sepal_length",
                 color="sepal_length", color_continuous_scale=px.colors.sequential.Viridis)

fig.show()
```

It is also possible to specify colorscales by name. Here is an example that specifies the Magma colorscale by name, as a string

```python
import plotly.express as px
iris = px.data.iris()
fig = px.scatter(iris, x="sepal_width", y="sepal_length",
                 color="sepal_length", color_continuous_scale='Magma')

fig.show()
```

### Custom Discretized Heatmap Colorscale

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

### Colorscale for Scatter Plots

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

### Colorscale for Contour Plot

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

### Custom Heatmap Colorscale

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

### Setting the Midpoint of a Diverging Colorscale
The following example uses [marker.cmid](https://plot.ly/python/reference/#scatter-marker-cmid) attribute to set the mid-point of the color domain by scaling 'cmin' and/or 'cmax' to be equidistant to this point. It only has impact when [marker.color](https://plot.ly/python/reference/#scattercarpet-marker-line-color) sets to a numerical array, and 'marker.cauto' is `True`. 

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

### Custom Contour Plot Colorscale

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

### Custom Colorbar Title, Labels, and Ticks

Like axes, you can customize the colorbar ticks, labels, and values with `ticks`, `ticktext`, and `tickvals`.

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

### Share Color Axis
This example shows how traces can share colorbars. To share colorscale information in multiple subplots, you can use [coloraxis](https://plot.ly/javascript/reference/#scatter-marker-line-coloraxis).

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


### Logarithmic Colorscale

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
