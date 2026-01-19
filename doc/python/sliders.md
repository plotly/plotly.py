---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.14.5
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
    version: 3.8.16
  plotly:
    description: How to add slider controls to your plots in Python with Plotly.
    display_as: controls
    language: python
    layout: base
    name: Sliders
    order: 1.5
    page_type: example_index
    permalink: python/sliders/
    thumbnail: thumbnail/slider2017.gif
---

### Simple Slider Control
Sliders can be used in Plotly to change the data displayed or style of a plot.

```python
import plotly.graph_objects as go
import numpy as np

# Create figure
fig = go.Figure()

# Add traces, one for each slider step
for step in np.arange(0, 5, 0.1):
    fig.add_trace(
        go.Scatter(
            visible=False,
            line=dict(color="#00CED1", width=6),
            name="𝜈 = " + str(step),
            x=np.arange(0, 10, 0.01),
            y=np.sin(step * np.arange(0, 10, 0.01))))

# Make 10th trace visible
fig.data[10].visible = True

# Create and add slider
steps = []
for i in range(len(fig.data)):
    step = dict(
        method="update",
        args=[{"visible": [False] * len(fig.data)},
              {"title": "Slider switched to step: " + str(i)}],  # layout attribute
    )
    step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
    steps.append(step)

sliders = [dict(
    active=10,
    currentvalue={"prefix": "Frequency: "},
    pad={"t": 50},
    steps=steps
)]

fig.update_layout(
    sliders=sliders
)

fig.show()
```

#### Methods
The method determines which [plotly.js function](https://plot.ly/javascript/plotlyjs-function-reference/) will be used to update the chart. Plotly can use several [updatemenu](https://plot.ly/python/reference/layout/updatemenus/#layout-updatemenus-items-updatemenu-buttons-items-button-method) methods to add the slider:
- `"update"`: modify **data and layout** attributes (as above)
- `"restyle"`: modify **data** attributes
- `"relayout"`: modify **layout** attributes
- `"animate"`: start or pause an animation


#### Update Method
The `"update"` method should be used when modifying the data and layout sections of the graph.
This example demonstrates how to update the data displayed while simultaneously updating layout attributes such as the annotations.

```python
import plotly.graph_objects as go
import numpy as np

# Create figure
fig = go.Figure()

min_val = 0
max_val = 0

# Add traces, one for each slider step
start = -1
for step in np.arange(start, 5, 0.1):
    x_vec=np.arange(0, 10, 0.01) #np.arange(start, 1, 0.1)
    y_vec=np.cos(step * np.arange(0, 10, 0.01))
    fig.add_trace(
        go.Scatter(
            visible=False,
            line=dict(color="#00CED1", width=4),
            name="𝜈 = " + str(step),
            x=x_vec,
            y=y_vec))
    if step == start:
        min_val = np.min(y_vec)
        max_val = np.max(y_vec)
    else:
        tmp_min = np.min(y_vec)
        tmp_max = np.max(y_vec)
        min_val = min(min_val, tmp_min)
        max_val = max(max_val, tmp_max)
    
# Make 10th trace visible
fig.data[10].visible = True

# Add Annotations
annotation_info = [dict(x=1,
                       y=0,
                       xref="paper", yref="paper",
                       text="Min value:<br> %.4f" % min_val,
                       ax=0, ay=40,
                       showarrow=False,
                       xanchor="left", yanchor="bottom"),
                  dict(x=1,
                       y=1,
                       xref="paper", yref="paper",
                       text="Max value:<br> %.4f" % max_val,
                       ax=0, ay=-40,
                       showarrow=False,
                       xanchor="left", yanchor="top")
                 ]
# Create and add slider
steps = []
for i in range(len(fig.data)):
    step = dict(
        method="update",
        label=str(i),
        args=[{"visible": [False] * len(fig.data)},
              {"title": "Slider switched to step: " + str(i), # layout attribute
              "annotations": annotation_info}],  # layout attribute
    )
    step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
    steps.append(step)

sliders = [dict(
    active=10,
    currentvalue={"prefix": "Slider value: "},
    pad={"t": 30},
    steps=steps
)]

fig.update_layout(
    sliders=sliders
)

fig.show()
```

This example demonstrates how sliders can be employed to data filtering. Here we show companies, represented with bars, when values of the outcome variable are above the threshold. The change in trace attributes is associated with the change in layout attribute. The title is updated when the value of the threshold is more than zero.

```python
import plotly.graph_objects as go
import numpy as np
import math

companies = ['Company A','Company B','Company C','Company D','Company E','Company F','Company G','Company H']
outcomes = [7.8, 12.3, 20.4, 8.9, -5.7, -16.3, 10.2, -1.5]

# Create figure
fig = go.Figure()

# Add trace
fig.add_trace(go.Bar(
    x=companies,
    y=outcomes,
    marker=dict(color = "green")
))

min_outcome = math.ceil(min(outcomes))
max_outcome = math.ceil(max(outcomes))

titles = ["Companies and outcomes", "Companies with positive outcomes"]
steps = [dict(method="update",
              args=[{'x': [[c for c, o in zip(companies,outcomes) if o>k]], #trace attributes that are updated by each slider step
                     'y': [[y for y in outcomes if y>k]]}, #trace attributes that are updated by each slider step
                    {'title': titles[1] if k>0 else titles[0]}], #layout attributes that are updated
              label=f"{k}") for k in range(min_outcome, max_outcome)]

sliders = [dict(
           active=0,
           currentvalue={"prefix": "threshold: "},
           steps=steps
)]

fig.update_layout(title=titles[0],
                  yaxis_title="outcome [mil.]",
                  sliders=sliders)

fig.show()
```

#### Relayout Method
The `"relayout"` method should be used when modifying layout attributes.
This example demonstrates how to update which groups are in clusters.

```python
import plotly.graph_objects as go
import numpy as np

# Create figure
fig = go.Figure()

x0 = np.random.normal(2, 0.2, 400)
y0 = np.random.normal(2, 0.3, 400)
x1 = np.random.normal(3, 0.1, 600)
y1 = np.random.normal(6, 0.3, 400)
x2 = np.random.normal(4, 0.4, 200)
y2 = np.random.normal(4, 0.5, 200)

# Add traces
fig.add_trace(
    go.Scatter(
        x=x0,
        y=y0,
        mode="markers",
        marker=dict(color="DarkOrange")
    )
)

fig.add_trace(
    go.Scatter(
        x=x1,
        y=y1,
        mode="markers",
        marker=dict(color="Crimson")
    )
)

fig.add_trace(
    go.Scatter(
        x=x2,
        y=y2,
        mode="markers",
        marker=dict(color="RebeccaPurple")
    )
)

initial_cluster = [dict(type="circle",
                            xref="x", yref="y",
                            x0=min(x0), y0=min(y0),
                            x1=max(x0), y1=max(y0),
                            line=dict(color="DarkOrange"))]
cluster2 = [dict(type="circle",
                            xref="x", yref="y",
                            x0=min(x0), y0=min(y0),
                            x1=max(x1), y1=max(y1),
                            line=dict(color="Crimson"))]
cluster3 = [dict(type="circle",
                            xref="x", yref="y",
                            x0=min(x0), y0=min(y0),
                            x1=max(x2), y1=max(y1),
                            line=dict(color="RebeccaPurple"))]

clusters = [[], initial_cluster, cluster2, cluster3]

# Create and add slider
steps = [dict(method="relayout",
              args=["shapes", clusters[k]], 
              label=f"{k}") for k in range(len(clusters))]

sliders = [dict(
    active=0,
    currentvalue={"prefix": "Groups in cluster: "},
    pad={"t": 50},
    steps=steps
)]

fig.update_layout(
    title_text="Groups",
    showlegend=False,
    sliders=sliders
)

fig.show()
```

### Sliders in Plotly Express
Plotly Express provide sliders, but with implicit animation using the `"animate"` method described above. The animation play button can be omitted by removing `updatemenus` in the `layout`:

```python
import plotly.express as px

df = px.data.gapminder()
fig = px.scatter(df, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
           size="pop", color="continent", hover_name="country",
           log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90])

fig["layout"].pop("updatemenus") # optional, drop animation buttons
fig.show()
```

#### Reference
Check out https://plotly.com/python/reference/layout/updatemenus/ for more information!
