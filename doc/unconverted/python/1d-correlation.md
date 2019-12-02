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
  plotly:
    description: Learn how to perform 1 dimensional correlation between two signals
      in Python.
    display_as: signal-analysis
    has_thumbnail: false
    language: python
    layout: base
    name: 1D Correlation
    order: 5
    page_type: example_index
    permalink: python/1d-correlation/
    thumbnail: /images/static-image
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


#### Imports
The tutorial below imports [NumPy](http://www.numpy.org/), [Pandas](https://plot.ly/pandas/intro-to-pandas-tutorial/), [SciPy](https://www.scipy.org/) and [Plotly](https://plot.ly/python/getting-started/).

```python
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np
import pandas as pd
import scipy

from scipy import signal
```

#### Correlation Between Saw and Square Wave
Similar to convolution, the 1D Cross-Correlation between two functions $f$ and $g$ is a measure of their similarity in terms of the lag of one to another ([source](https://en.wikipedia.org/wiki/Convolution)). Since we are dealing with arrays of data rather than continuous functions, the cross-correlation is mathematically defined as:

$$
\begin{align*}
(f*g)[n] = \sum_{m=-\infty}^{\infty} f^{*}[m]g[n+m]
\end{align*}
$$

where $f^*$ is the `complex conjugate` of $f$.

To give us an intuitive glance at what this does, let us look at the cross-correlation between a saw wave and a square wave.

```python
x = np.linspace(0, 20, 50)
saw_y = signal.sawtooth(t=x)
square_y = signal.square(t=x)
convolve_y = signal.convolve(saw_y, square_y)

trace_saw = go.Scatter(
    x = x,
    y = saw_y,
    mode = 'lines',
    name = 'Saw',
    marker=dict(
        color='#57D1C9'
    )
)

trace_square = go.Scatter(
    x = x,
    y = square_y,
    mode = 'lines',
    name = 'Square',
    marker=dict(
        color='#ED5485'
    )
)

trace_convolution = go.Scatter(
    x = x,
    y = convolve_y,
    mode = 'lines',
    name = 'Convolution',
    marker=dict(
        color='#FFE869'
    )
)

data = [trace_saw, trace_square, trace_convolution]
py.iplot(data, filename='1d-convolution-of-saw-and-square')
```

#### Correlation Between Saw and Shifted Saw Wave
To compare with the plot above, we can plot a saw wave, a phase shifted saw wave and the convolution between the two to see how they correlate along the axis.

```python
x = np.linspace(0, 20, 50)

saw_y = signal.sawtooth(t=x)
square_y = signal.square(t=x)
shifted_saw_y = signal.sawtooth(t=np.linspace(10, 30, 50))
convolve_y = signal.convolve(saw_y, shifted_saw_y)

trace_saw = go.Scatter(
    x = x,
    y = saw_y,
    mode = 'lines',
    name = 'Saw',
    marker = dict(
        color='#FF7844'
    ),
    opacity = 0.8
)

trace_shifted_saw = go.Scatter(
    x = x,
    y = shifted_saw_y,
    mode = 'lines',
    name = 'Shifted Saw',
    marker = dict(
        color='#A64942'
    ),
    opacity = 0.8
)

trace_convolution = go.Scatter(
    x = x,
    y = convolve_y,
    mode = 'lines',
    name = 'Convolution',
    marker = dict(
        color='#53354A'
    )
)

data = [trace_saw, trace_shifted_saw, trace_convolution]
py.iplot(data, filename='1d-convolution-of-saw-and-shifted-saw')
```

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'python-1D-Correlation.ipynb', 'python/1d-correlation/', '1D Correlation | plotly',
    'Learn how to perform 1 dimensional correlation between two signals in Python.',
    title='1D Correlation in Python | plotly',
    name='1D Correlation',
    language='python',
    page_type='example_index', has_thumbnail='false', display_as='signal-analysis', order=5)
```

```python

```
