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
    description: How to create dumbbell plots in Python with Plotly.
    display_as: basic
    language: python
    layout: base
    name: Dumbbell Plots
    order: 19
    page_type: example_index
    permalink: python/dumbbell-plots/
    thumbnail: thumbnail/dumbbell-plot.jpg
---

## Basic Dumbbell Plot


Dumbbell plots are useful for demonstrating change between two sets of data points, for example, the population change for a selection of countries for two different years.

In this example, we compare life expectancy in 1952 with life expectancy in 2002 for countries in Europe.

```python
import plotly.graph_objects as go
from plotly import data

import pandas as pd

df = data.gapminder()
df = df.loc[(df.continent == "Europe") & (df.year.isin([1952, 2002]))]

countries = (
    df.loc[(df.continent == "Europe") & (df.year.isin([2002]))]
    .sort_values(by=["lifeExp"], ascending=True)["country"]
    .unique()
)

data = {"line_x": [], "line_y": [], "1952": [], "2002": [], "colors": [], "years": [], "countries": []}

for country in countries:
    data["1952"].extend([df.loc[(df.year == 1952) & (df.country == country)]["lifeExp"].values[0]])
    data["2002"].extend([df.loc[(df.year == 2002) & (df.country == country)]["lifeExp"].values[0]])
    data["line_x"].extend(
        [
            df.loc[(df.year == 1952) & (df.country == country)]["lifeExp"].values[0],
            df.loc[(df.year == 2002) & (df.country == country)]["lifeExp"].values[0],
            None,
        ]
    )
    data["line_y"].extend([country, country, None]),

fig = go.Figure(
    data=[
        go.Scatter(
            x=data["line_x"],
            y=data["line_y"],
            mode="lines",
            showlegend=False,
            marker=dict(
                color="grey"
            )
        ),
        go.Scatter(
            x=data["1952"],
            y=countries,
            mode="markers",
            name="1952",
            marker=dict(
                color="green",
                size=10
            )

        ),
        go.Scatter(
            x=data["2002"],
            y=countries,
            mode="markers",
            name="2002",
            marker=dict(
                color="blue",
                size=10
            )
        ),
    ]
)

fig.update_layout(
    title=dict(text="Life Expectancy in Europe: 1952 and 2002"),
    height=1000,
    legend_itemclick=False
)

fig.show()

```

## Dumbbell Plot with Arrow Markers

*Note: The `arrow`, `angleref`, and `standoff` properties used on the `marker` in this example are new in 5.11*

In this example, we add arrow markers to the plot. The first trace adds the lines connecting the data points and arrow markers.
The second trace adds circle markers. On the first trace, we use `standoff=8` to position the arrow marker back from the data point.
For the arrow marker to point directly at the circle marker, this value should be half the circle marker size, which is hardcoded to 16 here.

```python
import pandas as pd
import plotly.graph_objects as go
from plotly import data

df = data.gapminder()
df = df.loc[(df.continent == "Europe") & (df.year.isin([1952, 2002]))]

countries = (
    df.loc[(df.continent == "Europe") & (df.year.isin([2002]))]
    .sort_values(by=["lifeExp"], ascending=True)["country"]
    .unique()
)

data = {"line_x": [], "line_y": [], "1952": [], "2002": [], "colors": [], "years": [], "countries": []}

for country in countries:
    data["1952"].extend([df.loc[(df.year == 1952) & (df.country == country)]["lifeExp"].values[0]])
    data["2002"].extend([df.loc[(df.year == 2002) & (df.country == country)]["lifeExp"].values[0]])
    data["line_x"].extend(
        [
            df.loc[(df.year == 1952) & (df.country == country)]["lifeExp"].values[0],
            df.loc[(df.year == 2002) & (df.country == country)]["lifeExp"].values[0],
            None,
        ]
    )
    data["line_y"].extend([country, country, None]),

fig = go.Figure(
    data=[
        go.Scatter(
            x=data["line_x"],
            y=data["line_y"],
            mode="markers+lines",
            showlegend=False,
            marker=dict(
                symbol="arrow",
                color="black",
                size=16,
                angleref="previous",
                standoff=8
            )
        ),
        go.Scatter(
            x=data["1952"],
            y=countries,
            name="1952",
            mode="markers",
            marker=dict(
                color="silver",
                size=16,
            )
        ),
        go.Scatter(
            x=data["2002"],
            y=countries,
            name="2002",
            mode="markers",
            marker=dict(
                color="lightskyblue",
                size=16,
            ),
        ),
    ]
)

fig.update_layout(
    title=dict(text="Life Expectancy in Europe: 1952 and 2002"),
    height=1000,
    legend_itemclick=False
)


fig.show()

```
