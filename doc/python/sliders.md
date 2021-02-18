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
    version: 3.7.2
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
