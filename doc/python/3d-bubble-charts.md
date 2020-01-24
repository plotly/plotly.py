---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: "1.1"
      jupytext_version: 1.2.3
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
    description:
      How to make 3D Bubble Charts in Python with Plotly. Three examples
      of 3D Bubble Charts.
    display_as: 3d_charts
    language: python
    layout: base
    name: 3D Bubble Charts
    order: 7
    page_type: u-guide
    permalink: python/3d-bubble-charts/
    thumbnail: thumbnail/3dbubble.jpg
---

### 3d Bubble chart with Plotly Express

```python
import plotly.express as px
import numpy as np
df = px.data.gapminder()
fig = px.scatter_3d(df, x='year', y='continent', z='pop', size='gdpPercap', color='lifeExp',
                    hover_data=['country'])
fig.update_layout(scene_zaxis_type="log")
fig.show()
```

#### Simple Bubble Chart

```python
import plotly.graph_objects as go

import pandas as pd

# Get Data: this ex will only use part of it (i.e. rows 750-1500)
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

start, end = 750, 1500

fig = go.Figure(data=go.Scatter3d(
    x=df['year'][start:end],
    y=df['continent'][start:end],
    z=df['pop'][start:end],
    text=df['country'][start:end],
    mode='markers',
    marker=dict(
        sizemode='diameter',
        sizeref=750,
        size=df['gdpPercap'][start:end],
        color = df['lifeExp'][start:end],
        colorscale = 'Viridis',
        colorbar_title = 'Life<br>Expectancy',
        line_color='rgb(140, 140, 170)'
    )
))


fig.update_layout(height=800, width=800,
                  title='Examining Population and Life Expectancy Over Time')

fig.show()
```

#### Bubble Chart Sized by a Variable

Plot planets' distance from sun, density, and gravity with bubble size based on planet size

```python
import plotly.graph_objects as go

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
planet_colors = ['rgb(135, 135, 125)', 'rgb(210, 50, 0)', 'rgb(50, 90, 255)',
                 'rgb(178, 0, 0)', 'rgb(235, 235, 210)', 'rgb(235, 205, 130)',
                 'rgb(55, 255, 217)', 'rgb(38, 0, 171)', 'rgb(255, 255, 255)']
distance_from_sun = [57.9, 108.2, 149.6, 227.9, 778.6, 1433.5, 2872.5, 4495.1, 5906.4]
density = [5427, 5243, 5514, 3933, 1326, 687, 1271, 1638, 2095]
gravity = [3.7, 8.9, 9.8, 3.7, 23.1, 9.0, 8.7, 11.0, 0.7]
planet_diameter = [4879, 12104, 12756, 6792, 142984, 120536, 51118, 49528, 2370]

# Create trace, sizing bubbles by planet diameter
fig = go.Figure(data=go.Scatter3d(
    x = distance_from_sun,
    y = density,
    z = gravity,
    text = planets,
    mode = 'markers',
    marker = dict(
        sizemode = 'diameter',
        sizeref = 750, # info on sizeref: https://plot.ly/python/reference/#scatter-marker-sizeref
        size = planet_diameter,
        color = planet_colors,
        )
))

fig.update_layout(width=800, height=800, title = 'Planets!',
                  scene = dict(xaxis=dict(title='Distance from Sun', titlefont_color='white'),
                               yaxis=dict(title='Density', titlefont_color='white'),
                               zaxis=dict(title='Gravity', titlefont_color='white'),
                               bgcolor = 'rgb(20, 24, 54)'
                           ))

fig.show()
```

#### Edit the Colorbar

Plot planets' distance from sun, density, and gravity with bubble size based on planet size

```python
import plotly.graph_objects as go

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
temperatures = [167, 464, 15, -20, -65, -110, -140, -195, -200, -225]
distance_from_sun = [57.9, 108.2, 149.6, 227.9, 778.6, 1433.5, 2872.5, 4495.1, 5906.4]
density = [5427, 5243, 5514, 3933, 1326, 687, 1271, 1638, 2095]
gravity = [3.7, 8.9, 9.8, 3.7, 23.1, 9.0, 8.7, 11.0, 0.7]
planet_diameter = [4879, 12104, 12756, 6792, 142984, 120536, 51118, 49528, 2370]

# Create trace, sizing bubbles by planet diameter
fig = go.Figure(go.Scatter3d(
    x = distance_from_sun,
    y = density,
    z = gravity,
    text = planets,
    mode = 'markers',
    marker = dict(
        sizemode = 'diameter',
        sizeref = 750, # info on sizeref: https://plot.ly/python/reference/#scatter-marker-sizeref
        size = planet_diameter,
        color = temperatures,
        colorbar_title = 'Mean<br>Temperature',
        colorscale=[[0, 'rgb(5, 10, 172)'], [.3, 'rgb(255, 255, 255)'], [1, 'rgb(178, 10, 28)']]
        )
))

fig.update_layout(width=800, height=800, title = 'Planets!',
                  scene = dict(xaxis=dict(title='Distance from Sun', titlefont_color='white'),
                               yaxis=dict(title='Density', titlefont_color='white'),
                               zaxis=dict(title='Gravity', titlefont_color='white'),
                               bgcolor = 'rgb(20, 24, 54)'
                           ))

fig.show()
```

#### Reference

See https://plot.ly/python/reference/#scatter3d and https://plot.ly/python/reference/#scatter-marker-sizeref <br>for more information and chart attribute options!
