---
description: How to make a quiver plot in Python. A quiver plot displays velocity
  vectors a arrows.
---
Quiver plots can be made using a [figure factory](figure-factories.md) as detailed in this page.

#### Basic Quiver Plot

```python
import plotly.figure_factory as ff

import numpy as np

x,y = np.meshgrid(np.arange(0, 2, .2), np.arange(0, 2, .2))
u = np.cos(x)*y
v = np.sin(x)*y

fig = ff.create_quiver(x, y, u, v)
fig.show()
```

#### Quiver Plot with Points

```python
import plotly.figure_factory as ff
import plotly.graph_objects as go

import numpy as np

x,y = np.meshgrid(np.arange(-2, 2, .2),
                  np.arange(-2, 2, .25))
z = x*np.exp(-x**2 - y**2)
v, u = np.gradient(z, .2, .2)

# Create quiver figure
fig = ff.create_quiver(x, y, u, v,
                       scale=.25,
                       arrow_scale=.4,
                       name='quiver',
                       line_width=1)

# Add points to figure
fig.add_trace(go.Scatter(x=[-.7, .75], y=[0,0],
                    mode='markers',
                    marker_size=12,
                    name='points'))

fig.show()
```

#### See also

[Cone plot](cone-plot.md) for the 3D equivalent of quiver plots.

#### Reference

For more info on `ff.create_quiver()`, see the [full function reference](reference/figure-factory.md#plotly.figure_factory.create_quiver)