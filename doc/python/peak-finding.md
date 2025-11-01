---
description: Learn how to find peaks and valleys on datasets in Python
---

### Imports

The tutorial below imports [Pandas](https://pandas.pydata.org/docs/user_guide/10min.html), and [SciPy](https://www.scipy.org/).

```python
import pandas as pd
from scipy.signal import find_peaks
```

### Import Data

To start detecting peaks, we will import some data on milk production by month:

```python
import plotly.graph_objects as go
import pandas as pd

milk_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/monthly-milk-production-pounds.csv')
time_series = milk_data['Monthly milk production (pounds per cow)']

fig = go.Figure(data=go.Scatter(
    y = time_series,
    mode = 'lines'
))

fig.show()
```

### Peak Detection

We need to find the x-axis indices for the peaks in order to determine where the peaks are located.

```python
import plotly.graph_objects as go
import pandas as pd
from scipy.signal import find_peaks

milk_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/monthly-milk-production-pounds.csv')
time_series = milk_data['Monthly milk production (pounds per cow)']

indices = find_peaks(time_series)[0]

fig = go.Figure()
fig.add_trace(go.Scatter(
    y=time_series,
    mode='lines+markers',
    name='Original Plot'
))

fig.add_trace(go.Scatter(
    x=indices,
    y=[time_series[j] for j in indices],
    mode='markers',
    marker=dict(
        size=8,
        color='red',
        symbol='cross'
    ),
    name='Detected Peaks'
))

fig.show()
```

### Only Highest Peaks

We can attempt to set our threshold so that we identify as many of the _highest peaks_ that we can.

```python
import plotly.graph_objects as go
import numpy as np
import pandas as pd
from scipy.signal import find_peaks

milk_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/monthly-milk-production-pounds.csv')
time_series = milk_data['Monthly milk production (pounds per cow)']

indices = find_peaks(time_series, threshold=20)[0]

fig = go.Figure()
fig.add_trace(go.Scatter(
    y=time_series,
    mode='lines+markers',
    name='Original Plot'
))

fig.add_trace(go.Scatter(
    x=indices,
    y=[time_series[j] for j in indices],
    mode='markers',
    marker=dict(
        size=8,
        color='red',
        symbol='cross'
    ),
    name='Detected Peaks'
))

fig.show()
```
