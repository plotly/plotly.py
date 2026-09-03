---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.1'
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
    description: How to make a quiver plot in Python. A quiver plot displays a 2D vector
      field as an array of arrows.
    display_as: scientific
    language: python
    layout: base
    name: Quiver Plots
    order: 10
    permalink: python/quiver-plots/
    thumbnail: thumbnail/quiver-plot.jpg
---

A quiver plot displays a 2D vector field as an array of arrows. Since version 7.0, Plotly has a `Quiver` trace type, which is the recommended way to make quiver plots. Earlier versions relied on the `create_quiver` [figure factory](/python/figure-factories/), which is still available and is described at the end of this page.

A `Quiver` trace takes four arrays of the same length: `x` and `y` give the position of each arrow, and `u` and `v` give the vector components at that position. Arrow direction and length come from `(u, v)`.

#### Basic Quiver Plot

```python
import plotly.graph_objects as go
import numpy as np

x, y = np.meshgrid(np.arange(0, 2, .2), np.arange(0, 2, .2))
u = np.cos(x) * y
v = np.sin(x) * y

fig = go.Figure(go.Quiver(x=x.flatten(), y=y.flatten(),
                          u=u.flatten(), v=v.flatten()))

fig.show()
```

#### Arrow Anchor and Length

`anchor` sets which part of the arrow sits at its `(x, y)` position: `"tail"` (the default), `"tip"`, or `"center"`.

Arrow length is controlled by `lengthmode` and `lengthfactor`. With `lengthmode="scaled"` (the default), lengths are normalized against the longest vector in the field and the density of points, so a dense grid stays readable whatever the underlying values are. `lengthmode="raw"` draws each arrow at its specified magnitude determined by `u` and `v`. `lengthfactor` is a multiplier applied on top: values below 1 shorten every arrow, above 1 lengthen them.

```python
import plotly.graph_objects as go
import numpy as np

x, y = np.meshgrid(np.arange(-2, 3), np.arange(-2, 3))
u, v = -y, x  # rotational field

fig = go.Figure(go.Quiver(x=x.flatten(), y=y.flatten(),
                          u=u.flatten(), v=v.flatten(),
                          anchor="center", lengthfactor=0.8))

fig.update_layout(title_text="Rotational field, arrows centered on each point",
                  yaxis_scaleanchor="x")
fig.show()
```

#### Setting Arrow Reference

The `arrowref` property controls how the `u` and `v` vector components are interpreted, and how the vector arrows respond to zooming along a single axis.

By default, `arrowref="data"`, meaning that `u` and `v` are interpreted as data values. This means that the angle of the vectors depends on the relative scale of the two axes, and the apparent angle will change when zooming along one axis. This is the appropriate behavior when `u` and `v` represent data-space values, such as when illustrating a magnetic field.

To instead interpret `u` and `v` in pixel values, set `arrowref="paper"`, which will always draw vectors at the same angle regardless of the axis scales. This is the correct behavior when the vectors correspond to abstract values which are not linked to the data space.

Note that `arrowref="paper"` always scales arrow lengths, so `lengthmode="raw"` is ignored when you set it.

The difference is clearest on axes with different scales. Both panels below plot the same vectors, `u=1` and `v=0.1`, on a grid where x spans 10 units and y spans 1.

```python
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

x = np.linspace(0, 10, 6)
y = np.full_like(x, 0.5)
u = np.ones_like(x)
v = np.full_like(x, 0.1)

fig = make_subplots(rows=1, cols=2,
                    subplot_titles=['arrowref="data"', 'arrowref="paper"'])
fig.add_trace(go.Quiver(x=x, y=y, u=u, v=v, arrowref="data"), row=1, col=1)
fig.add_trace(go.Quiver(x=x, y=y, u=u, v=v, arrowref="paper"), row=1, col=2)

fig.update_xaxes(range=[-1, 11])
fig.update_yaxes(range=[0, 1])
fig.update_layout(showlegend=False)
fig.show()
```

With `"data"`, `v=0.1` covers a tenth of the y-axis while `u=1` covers a tenth of the x-axis, so the arrows tilt noticeably. With `"paper"`, the same components are 1 pixel across and 0.1 pixels up, so the arrows stay nearly flat whatever the axis ranges are.

#### Coloring Arrows by a Scalar Field

Pass `marker.color` an array with one value per arrow, together with the usual colorscale attributes, to color each arrow by that value. If you enable a colorscale without supplying a `marker.color` array, arrows are colored by their vector magnitude. A single (non-array) `marker.color` paints the whole field one color.

```python
import plotly.graph_objects as go
import numpy as np

x, y = np.meshgrid(np.arange(-2, 2, .2), np.arange(-2, 2, .25))
z = x * np.exp(-x**2 - y**2)
v, u = np.gradient(z, .2, .2)
speed = np.sqrt(u**2 + v**2)

fig = go.Figure(go.Quiver(x=x.flatten(), y=y.flatten(),
                          u=u.flatten(), v=v.flatten(),
                          marker=dict(color=speed.flatten(),
                                      colorscale="Viridis",
                                      showscale=True,
                                      colorbar_title_text="speed")))

fig.show()
```

#### Styling Arrows

`marker.line.width` and `marker.line.dash` style the arrow shafts, and `marker.arrowsize` scales the arrowhead relative to the shaft width — the default of `1` draws a head about three times as wide as the shaft.

```python
import plotly.graph_objects as go
import numpy as np

x, y = np.meshgrid(np.arange(0, 6), np.arange(0, 6))
u_model = np.ones_like(x, dtype=float)
v_model = 0.15 * (y - 2.5)
u_measured = 0.9 * u_model
v_measured = v_model + 0.25 * np.cos(x)

fig = go.Figure([
    go.Quiver(x=x.flatten(), y=y.flatten(),
              u=u_model.flatten(), v=v_model.flatten(),
              name="model",
              marker=dict(color="#7f7f7f", arrowsize=0.8,
                          line=dict(width=2, dash="dot"))),
    go.Quiver(x=x.flatten(), y=y.flatten(),
              u=u_measured.flatten(), v=v_measured.flatten(),
              name="measured",
              marker=dict(color="#d62728", arrowsize=1.2,
                          line=dict(width=3))),
])

fig.update_layout(title_text="Modelled and measured fields", showlegend=True)
fig.show()
```

#### Quiver Plot with Points

A `Quiver` trace is a cartesian trace, so it can be combined with other cartesian traces in the same figure.

```python
import plotly.graph_objects as go
import numpy as np

x, y = np.meshgrid(np.arange(-2, 2, .2), np.arange(-2, 2, .25))
z = x * np.exp(-x**2 - y**2)
v, u = np.gradient(z, .2, .2)

fig = go.Figure(go.Quiver(x=x.flatten(), y=y.flatten(),
                          u=u.flatten(), v=v.flatten(),
                          name="quiver",
                          marker=dict(line_width=1)))

fig.add_trace(go.Scatter(x=[-.7, .75], y=[0, 0],
                         mode="markers",
                         marker_size=12,
                         name="points"))

fig.show()
```

#### Quiver Plots with Figure Factory

`create_quiver` builds a quiver plot out of `Scatter` traces rather than using the `Quiver` trace type. It remains available, and offers two options the trace type does not: `angle` sets the arrowhead angle in radians, and `scaleratio` fixes the ratio between the y-axis and x-axis scales.

```python
import plotly.figure_factory as ff
import numpy as np

x, y = np.meshgrid(np.arange(0, 2, .2), np.arange(0, 2, .2))
u = np.cos(x) * y
v = np.sin(x) * y

fig = ff.create_quiver(x, y, u, v)

fig.show()
```

Because the result is made of `Scatter` traces, the arrows cannot be colored individually by a scalar field, and the trace-level attributes described above (`anchor`, `lengthmode`, `marker.arrowsize`) do not apply.

#### See also

[Cone plot](/python/cone-plot) for the 3D equivalent of quiver plots.

#### Reference

See the [Quiver trace reference](https://plotly.com/python/reference/quiver/) for the full list of attributes, or the [`create_quiver` function reference](https://plotly.com/python-api-reference/generated/plotly.figure_factory.create_quiver.html) for the figure factory.
