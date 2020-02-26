---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: "1.1"
      jupytext_version: 1.1.1
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
    version: 3.6.7
  plotly:
    description: Learn how to perform smoothing using various methods in Python.
    display_as: advanced_opt
    has_thumbnail: false
    language: python
    layout: base
    name: Smoothing
    order: 1
    page_type: example_index
    permalink: python/smoothing/
    thumbnail: /images/static-image
---

#### Imports

The tutorial below imports [NumPy](http://www.numpy.org/), [Pandas](https://plot.ly/pandas/intro-to-pandas-tutorial/), [SciPy](https://www.scipy.org/) and [Plotly](https://plot.ly/python/getting-started/).

```python
import plotly.graph_objects as go

import numpy as np
import pandas as pd
import scipy

from scipy import signal
```

#### Savitzky-Golay Filter

`Smoothing` is a technique that is used to eliminate noise from a dataset. There are many algorithms and methods to accomplish this but all have the same general purpose of 'roughing out the edges' or 'smoothing' some data.

There is reason to smooth data if there is little to no small-scale structure in the data. The danger to this thinking is that one may skew the representation of the data enough to change its percieved meaning, so for the sake of scientific honesty it is an imperative to at the very minimum explain one's reason's for using a smoothing algorithm to their dataset.

In this example we use the [Savitzky-Golay Filter](https://en.wikipedia.org/wiki/Savitzky%E2%80%93Golay_filter), which fits subsequents windows of adjacent data with a low-order polynomial.

```python
import plotly.graph_objects as go

import numpy as np
import pandas as pd
import scipy

from scipy import signal

np.random.seed(1)

x = np.linspace(0, 10, 100)
y = np.sin(x)
noise = 2 * np.random.random(len(x)) - 1 # uniformly distributed between -1 and 1
y_noise = y + noise

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=x,
    y=y,
    mode='markers',
    marker=dict(size=2, color='black'),
    name='Sine'
))

fig.add_trace(go.Scatter(
    x=x,
    y=y_noise,
    mode='markers',
    marker=dict(
        size=6,
        color='royalblue',
        symbol='circle-open'
    ),
    name='Noisy Sine'
))

fig.add_trace(go.Scatter(
    x=x,
    y=signal.savgol_filter(y,
                           53, # window size used for filtering
                           3), # order of fitted polynomial
    mode='markers',
    marker=dict(
        size=6,
        color='mediumpurple',
        symbol='triangle-up'
    ),
    name='Savitzky-Golay'
))


fig.show()
```

#### Triangular Moving Average

Another method for smoothing is a moving average. There are various forms of this, but the idea is to take a window of points in your dataset, compute an average of the points, then shift the window over by one point and repeat. This will generate a bunch of points which will result in the `smoothed` data.

Let us look at the common `Simple Moving Average` first. In the 1D case we have a data set of $N$ points with y-values $y_1, y_2, ..., y_N$. Setting our window size to $n < N$, the new $i^{th}$ y-value after smoothing is computed as:

$$
\begin{align*}
SMA_i = \frac{y_i + ... + y_{i+n}}{n}
\end{align*}
$$

In the `Triangular Moving Average`, two simple moving averages are computed on top of each other, in order to give more weight to closer (adjacent) points. This means that our $SMA_i$ are computed then a Triangular Moving Average $TMA_i$ is computed as:

$$
\begin{align*}
TMA_i = \frac{SMA_i + ... + SMA_{i+n}}{n}
\end{align*}
$$

```python
def smoothTriangle(data, degree):
    triangle=np.concatenate((np.arange(degree + 1), np.arange(degree)[::-1])) # up then down
    smoothed=[]

    for i in range(degree, len(data) - degree * 2):
        point=data[i:i + len(triangle)] * triangle
        smoothed.append(np.sum(point)/np.sum(triangle))
    # Handle boundaries
    smoothed=[smoothed[0]]*int(degree + degree/2) + smoothed
    while len(smoothed) < len(data):
        smoothed.append(smoothed[-1])
    return smoothed

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=x,
    y=y,
    mode='markers',
    marker=dict(
        size=2,
        color='rgb(0, 0, 0)',
    ),
    name='Sine'
))

fig.add_trace(go.Scatter(
    x=x,
    y=y_noise,
    mode='markers',
    marker=dict(
        size=6,
        color='#5E88FC',
        symbol='circle-open'
    ),
    name='Noisy Sine'
))

fig.add_trace(go.Scatter(
    x=x,
    y=smoothTriangle(y_noise, 10),  # setting degree to 10
    mode='markers',
    marker=dict(
        size=6,
        color='#C190F0',
        symbol='triangle-up'
    ),
    name='Moving Triangle - Degree 10'
))

fig.show()
```
