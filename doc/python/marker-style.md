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
    display_name: Python 3 (ipykernel)
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
    version: 3.8.0
  plotly:
    description: How to style markers in Python with Plotly.
    display_as: file_settings
    language: python
    layout: base
    name: Styling Markers
    order: 20
    permalink: python/marker-style/
    thumbnail: thumbnail/marker-style.gif
---

### Add Marker Border

In order to make markers look more distinct, you can add a border to the markers. This can be achieved by adding the line property to the marker object.

Here is an example of adding a marker border to a faceted scatter plot created using Plotly Express.

```python
import plotly.express as px

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")

fig.update_traces(marker=dict(size=12,
                              line=dict(width=2,
                                        color='DarkSlateGrey')),
                  selector=dict(mode='markers'))
fig.show()
```

Here is an example that creates an empty graph object figure, and then adds two scatter traces with a marker border.

```python
import plotly.graph_objects as go

# Generate example data
import numpy as np
np.random.seed(1)

x = np.random.uniform(low=3, high=6, size=(500,))
y = np.random.uniform(low=3, high=6, size=(500,))

# Build figure
fig = go.Figure()

# Add scatter trace with medium sized markers
fig.add_trace(
    go.Scatter(
        mode='markers',
        x=x,
        y=y,
        marker=dict(
            color='LightSkyBlue',
            size=20,
            line=dict(
                color='MediumPurple',
                width=2
            )
        ),
        showlegend=False
    )
)

# Add trace with large marker
fig.add_trace(
    go.Scatter(
        mode='markers',
        x=[2],
        y=[4.5],
        marker=dict(
            color='LightSkyBlue',
            size=120,
            line=dict(
                color='MediumPurple',
                width=12
            )
        ),
        showlegend=False
    )
)

fig.show()
```

Fully opaque, the default setting, is useful for non-overlapping markers. When many points overlap it can be hard to observe density.


### Control Marker Border with Dash

[Dash](https://plotly.com/dash/) is the best way to build analytical apps in Python using Plotly figures. To run the app below, run `pip install dash`, click "Download" to get the code and run `python app.py`.

Get started  with [the official Dash docs](https://dash.plotly.com/installation) and **learn how to effortlessly [style](https://plotly.com/dash/design-kit/) & [deploy](https://plotly.com/dash/app-manager/) apps like this with <a class="plotly-red" href="https://plotly.com/dash/">Dash Enterprise</a>.**

```python hide_code=true
from IPython.display import IFrame
snippet_url = 'https://python-docs-dash-snippets.herokuapp.com/python-docs-dash-snippets/'
IFrame(snippet_url + 'marker-style', width='100%', height=1200)
```

<div style="font-size: 0.9em;"><div style="width: calc(100% - 30px); box-shadow: none; border: thin solid rgb(229, 229, 229);"><div style="padding: 5px;"><div><p><strong>Sign up for Dash Club</strong> → Free cheat sheets plus updates from Chris Parmer and Adam Schroeder delivered to your inbox every two months. Includes tips and tricks, community apps, and deep dives into the Dash architecture.
<u><a href="https://go.plotly.com/dash-club?utm_source=Dash+Club+2022&utm_medium=graphing_libraries&utm_content=inline">Join now</a></u>.</p></div></div></div></div>


### Opacity

Setting opacity outside the marker will set the opacity of the trace. Thus, it will allow greater visibility of additional traces but like fully opaque it is hard to distinguish density.

```python
import plotly.graph_objects as go

# Generate example data
import numpy as np

x = np.random.uniform(low=3, high=6, size=(500,))
y = np.random.uniform(low=3, high=4.5, size=(500,))
x2 = np.random.uniform(low=3, high=6, size=(500,))
y2 = np.random.uniform(low=4.5, high=6, size=(500,))

# Build figure
fig = go.Figure()

# Add first scatter trace with medium sized markers
fig.add_trace(
    go.Scatter(
        mode='markers',
        x=x,
        y=y,
        opacity=0.5,
        marker=dict(
            color='LightSkyBlue',
            size=20,
            line=dict(
                color='MediumPurple',
                width=2
            )
        ),
        name='Opacity 0.5'
    )
)

# Add second scatter trace with medium sized markers
# and opacity 1.0
fig.add_trace(
    go.Scatter(
        mode='markers',
        x=x2,
        y=y2,
        marker=dict(
            color='LightSkyBlue',
            size=20,
            line=dict(
                color='MediumPurple',
                width=2
            )
        ),
        name='Opacity 1.0'
    )
)

# Add trace with large markers
fig.add_trace(
    go.Scatter(
        mode='markers',
        x=[2, 2],
        y=[4.25, 4.75],
        opacity=0.5,
        marker=dict(
            color='LightSkyBlue',
            size=80,
            line=dict(
                color='MediumPurple',
                width=8
            )
        ),
        showlegend=False
    )
)

fig.show()

```

### Marker Opacity

To maximise visibility of density, it is recommended to set the opacity inside the marker `marker:{opacity:0.5}`. If multiple traces exist with high density, consider using marker opacity in conjunction with trace opacity.

```python
import plotly.graph_objects as go

# Generate example data
import numpy as np

x = np.random.uniform(low=3, high=6, size=(500,))
y = np.random.uniform(low=3, high=6, size=(500,))

# Build figure
fig = go.Figure()

# Add scatter trace with medium sized markers
fig.add_trace(
    go.Scatter(
        mode='markers',
        x=x,
        y=y,
        marker=dict(
            color='LightSkyBlue',
            size=20,
            opacity=0.5,
            line=dict(
                color='MediumPurple',
                width=2
            )
        ),
        showlegend=False
    )
)


# Add trace with large markers
fig.add_trace(
    go.Scatter(
        mode='markers',
        x=[2, 2],
        y=[4.25, 4.75],
        marker=dict(
            color='LightSkyBlue',
            size=80,
            opacity=0.5,
            line=dict(
                color='MediumPurple',
                width=8
            )
        ),
        showlegend=False
    )
)

fig.show()

```

### Color Opacity

To maximise visibility of each point, set the color as an `rgba` string that includes an alpha value of 0.5.

This example sets the marker color to `'rgba(135, 206, 250, 0.5)'`. The rgb values of 135, 206, and 250 are from the definition of the `LightSkyBlue` named CSS color that is is used in the previous examples (See https://www.color-hex.com/color/87cefa). The marker line will remain opaque.

```python
import plotly.graph_objects as go

# Generate example data
import numpy as np

x = np.random.uniform(low=3, high=6, size=(500,))
y = np.random.uniform(low=3, high=6, size=(500,))


# Build figure
fig = go.Figure()

# Add scatter trace with medium sized markers
fig.add_trace(
    go.Scatter(
        mode='markers',
        x=x,
        y=y,
        marker=dict(
            color='rgba(135, 206, 250, 0.5)',
            size=20,
            line=dict(
                color='MediumPurple',
                width=2
            )
        ),
        showlegend=False
    )
)


# Add trace with large markers
fig.add_trace(
    go.Scatter(
        mode='markers',
        x=[2, 2],
        y=[4.25, 4.75],
        marker=dict(
            color='rgba(135, 206, 250, 0.5)',
            size=80,
            line=dict(
                color='MediumPurple',
                width=8
            )
        ),
        showlegend=False
    )
)

fig.show()

```

### Custom Marker Symbols

The `marker_symbol` attribute allows you to choose from a wide array of symbols to represent markers in your figures.

The basic symbols are: `circle`, `square`, `diamond`, `cross`, `x`, `triangle`, `pentagon`, `hexagram`, `star`, `hourglass`, `bowtie`, `asterisk`, `hash`, `y`, and `line`.

Each basic symbol is also represented by a number. Adding 100 to that number is equivalent to appending the suffix "-open" to a symbol name. Adding 200 is equivalent to appending "-dot" to a symbol name. Adding 300 is equivalent to appending "-open-dot" or "dot-open" to a symbol name.

In the following figure, hover over a symbol to see its name or number. Set the `marker_symbol` attribute equal to that name or number to change the marker symbol in your figure.

> The `arrow-wide` and `arrow` marker symbols are new in 5.11

```python
import plotly.graph_objects as go
from plotly.validators.scatter.marker import SymbolValidator

raw_symbols = SymbolValidator().values
namestems = []
namevariants = []
symbols = []
for i in range(0,len(raw_symbols),3):
    name = raw_symbols[i+2]
    symbols.append(raw_symbols[i])
    namestems.append(name.replace("-open", "").replace("-dot", ""))
    namevariants.append(name[len(namestems[-1]):])

fig = go.Figure(go.Scatter(mode="markers", x=namevariants, y=namestems, marker_symbol=symbols,
                           marker_line_color="midnightblue", marker_color="lightskyblue",
                           marker_line_width=2, marker_size=15,
                           hovertemplate="name: %{y}%{x}<br>number: %{marker.symbol}<extra></extra>"))
fig.update_layout(title="Mouse over symbols for name & number!",
                  xaxis_range=[-1,4], yaxis_range=[len(set(namestems)),-1],
                  margin=dict(b=0,r=0), xaxis_side="top", height=1400, width=400)
fig.show()
```


### Using a Custom Marker

To use a custom marker, set the `symbol` on the `marker`. Here we set it to `diamond`.


```python
import plotly.express as px

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")

fig.update_traces(
    marker=dict(size=8, symbol="diamond", line=dict(width=2, color="DarkSlateGrey")),
    selector=dict(mode="markers"),
)
fig.show()

```

### Setting Marker Angles


*New in 5.11*

Change the angle of markers by setting `angle`. Here we set the angle on the `arrow` markers to `45`.

```python
import plotly.express as px

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")

fig.update_traces(
    marker=dict(
        size=12, symbol="arrow", angle=45, line=dict(width=2, color="DarkSlateGrey")
    ),
    selector=dict(mode="markers"),
)
fig.show()

```

### Setting Angle Reference

*New in 5.11*

In the previous example the angle reference is the default `up`, which
means all makers start at the angle reference point of 0. Set `angleref` to `previous` and a marker will take its angle reference from the previous data point.

```python
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = px.data.gapminder()

fig = go.Figure()

for x in df.loc[df.continent.isin(["Europe"])].country.unique()[:5]:
    fil = df.loc[(df.country.str.contains(x))]
    fig.add_trace(
        go.Scatter(
            x=fil["year"],
            y=fil["pop"],
            mode="lines+markers",
            marker=dict(
                symbol="arrow",
                size=15,
                angleref="previous",
            ),
            name=x,
        )
    )
fig.show()

```

### Using Standoff to Position a Marker

*New in 5.11*

When you have multiple markers at one location, you can use `standoff` on a marker to move it away from the other marker in the direction of the `angle`. 
In this example, we set `standoff=8` on the `arrow` marker, which is half the size of the other `circle` marker, meaning it points exactly at the `circle`.

```python
import pandas as pd
import plotly.graph_objects as go
from plotly import data

df = data.gapminder()
df = df.loc[(df.continent == "Americas") & (df.year.isin([1987, 2007]))]

countries = (
    df.loc[(df.continent == "Americas") & (df.year.isin([2007]))]
    .sort_values(by=["pop"], ascending=True)["country"]
    .unique()
)[5:-10]

data = {"x": [], "y": [], "colors": [], "years": []}

for country in countries:
    data["x"].extend(
        [
            df.loc[(df.year == 1987) & (df.country == country)]["pop"].values[0],
            df.loc[(df.year == 2007) & (df.country == country)]["pop"].values[0],
            None,
        ]
    )
    data["y"].extend([country, country, None]),
    data["colors"].extend(["cyan", "darkblue", "white"]),
    data["years"].extend(["1987", "2007", None])

fig = go.Figure(
    data=[
        go.Scatter(
            x=data["x"],
            y=data["y"],
            mode="markers+lines",
            marker=dict(
                symbol="arrow",
                color="royalblue",
                size=16,
                angleref="previous",
                standoff=8,
            ),
        ),
        go.Scatter(
            x=data["x"],
            y=data["y"],
            text=data["years"],
            mode="markers",
            marker=dict(
                color=data["colors"],
                size=16,
            ),
            hovertemplate="""Country: %{y} <br> Population: %{x} <br> Year: %{text} <br><extra></extra>""",
        ),
    ]
)

fig.update_layout(
    title="Population changes 1987 to 2007",
    width=1000,
    height=1000,
    showlegend=False,
)


fig.show()

```

### Reference

See https://plotly.com/python/reference/ for more information and chart attribute options!
