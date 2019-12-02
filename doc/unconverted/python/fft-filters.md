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
    display_name: Python 2
    language: python
    name: python2
  plotly:
    description: Learn how filter out the frequencies of a signal by using low-pass,
      high-pass and band-pass FFT filtering.
    display_as: signal-analysis
    has_thumbnail: false
    language: python
    layout: base
    name: FFT Filters
    order: 2
    page_type: example_index
    permalink: python/fft-filters/
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
import plotly.figure_factory as ff

import numpy as np
import pandas as pd
import scipy

from scipy import signal
```

#### Import Data
An `FFT Filter` is a process that involves mapping a time signal from time-space to frequency-space in which frequency becomes an axis. By mapping to this space, we can get a better picture for how much of which frequency is in the original time signal and we can ultimately cut some of these frequencies out to remap back into time-space. Such filter types include `low-pass`, where lower frequencies are allowed to pass and higher ones get cut off -, `high-pass`, where higher frequencies pass, and `band-pass`, which selects only a narrow range or "band" of frequencies to pass through.

Let us import some stock data to apply FFT Filtering:

```python
data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/wind_speed_laurel_nebraska.csv')
df = data[0:10]

table = ff.create_table(df)
py.iplot(table, filename='wind-data-sample')
```

#### Plot the Data
Let's look at our data in its raw form before doing any filtering.

```python
trace1 = go.Scatter(
    x=list(range(len(list(data['10 Min Std Dev'])))),
    y=list(data['10 Min Std Dev']),
    mode='lines',
    name='Wind Data'
)

layout = go.Layout(
    showlegend=True
)

trace_data = [trace1]
fig = go.Figure(data=trace_data, layout=layout)
py.iplot(fig, filename='wind-raw-data-plot')
```

#### Low-Pass Filter
A `Low-Pass Filter` is used to remove the higher frequencies in a signal of data.

`fc` is the cutoff frequency as a fraction of the sampling rate, and `b` is the transition band also as a function of the sampling rate. `N` must be an odd number in our calculation as well.

```python
fc = 0.1
b = 0.08
N = int(np.ceil((4 / b)))
if not N % 2: N += 1
n = np.arange(N)

sinc_func = np.sinc(2 * fc * (n - (N - 1) / 2.))
window = 0.42 - 0.5 * np.cos(2 * np.pi * n / (N - 1)) + 0.08 * np.cos(4 * np.pi * n / (N - 1))
sinc_func = sinc_func * window
sinc_func = sinc_func / np.sum(sinc_func)

s = list(data['10 Min Std Dev'])
new_signal = np.convolve(s, sinc_func)

trace1 = go.Scatter(
    x=list(range(len(new_signal))),
    y=new_signal,
    mode='lines',
    name='Low-Pass Filter',
    marker=dict(
        color='#C54C82'
    )
)

layout = go.Layout(
    title='Low-Pass Filter',
    showlegend=True
)

trace_data = [trace1]
fig = go.Figure(data=trace_data, layout=layout)
py.iplot(fig, filename='fft-low-pass-filter')
```

#### High-Pass Filter
Similarly a `High-Pass Filter` will remove the lower frequencies from a signal of data.

Again, `fc` is the cutoff frequency as a fraction of the sampling rate, and `b` is the transition band also as a function of the sampling rate. `N` must be an odd number.

Only by performing a spectral inversion afterwards after setting up our Low-Pass Filter will we get the High-Pass Filter.

```python
fc = 0.1
b = 0.08
N = int(np.ceil((4 / b)))
if not N % 2: N += 1
n = np.arange(N)

sinc_func = np.sinc(2 * fc * (n - (N - 1) / 2.))
window = np.blackman(N)
sinc_func = sinc_func * window
sinc_func = sinc_func / np.sum(sinc_func)

# reverse function
sinc_func = -sinc_func
sinc_func[int((N - 1) / 2)] += 1

s = list(data['10 Min Std Dev'])
new_signal = np.convolve(s, sinc_func)

trace1 = go.Scatter(
    x=list(range(len(new_signal))),
    y=new_signal,
    mode='lines',
    name='High-Pass Filter',
    marker=dict(
        color='#424242'
    )
)

layout = go.Layout(
    title='High-Pass Filter',
    showlegend=True
)

trace_data = [trace1]
fig = go.Figure(data=trace_data, layout=layout)
py.iplot(fig, filename='fft-high-pass-filter')
```

#### Band-Pass Filter
The `Band-Pass Filter` will allow you to reduce the frequencies outside of a defined range of frequencies. We can think of it as low-passing and high-passing at the same time.

In the example below, `fL` and `fH` are the low and high cutoff frequencies respectively as a fraction of the sampling rate.

```python
fL = 0.1
fH = 0.3
b = 0.08
N = int(np.ceil((4 / b)))
if not N % 2: N += 1  # Make sure that N is odd.
n = np.arange(N)

# low-pass filter
hlpf = np.sinc(2 * fH * (n - (N - 1) / 2.))
hlpf *= np.blackman(N)
hlpf = hlpf / np.sum(hlpf)

# high-pass filter
hhpf = np.sinc(2 * fL * (n - (N - 1) / 2.))
hhpf *= np.blackman(N)
hhpf = hhpf / np.sum(hhpf)
hhpf = -hhpf
hhpf[int((N - 1) / 2)] += 1

h = np.convolve(hlpf, hhpf)
s = list(data['10 Min Std Dev'])
new_signal = np.convolve(s, h)

trace1 = go.Scatter(
    x=list(range(len(new_signal))),
    y=new_signal,
    mode='lines',
    name='Band-Pass Filter',
    marker=dict(
        color='#BB47BE'
    )
)

layout = go.Layout(
    title='Band-Pass Filter',
    showlegend=True
)

trace_data = [trace1]
fig = go.Figure(data=trace_data, layout=layout)
py.iplot(fig, filename='fft-band-pass-filter')
```

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'python-FFT-Filters.ipynb', 'python/fft-filters/', 'FFT Filters | plotly',
    'Learn how filter out the frequencies of a signal by using low-pass, high-pass and band-pass FFT filtering.',
    title='FFT Filters in Python | plotly',
    name='FFT Filters',
    language='python',
    page_type='example_index', has_thumbnail='false', display_as='signal-analysis', order=2)
```

```python

```
