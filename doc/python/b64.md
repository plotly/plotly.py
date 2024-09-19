---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.16.3
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
    version: 3.10.0
  plotly:
    description: How to use typed arrays in Plotly.py
    display_as: file_settings
    language: python
    layout: base
    name: Improving Performance with Typed Arrays
    order: 39
    permalink: python/b64/
    thumbnail: thumbnail/b64.png
---

*New in Plotly.py 6.0**

Improve the performance of generating Plotly figures that use a large number of data points by using NumPy arrays and other objects that can be converted to NumPy arrays, such as Pandas Series and Index objects. 

Plotly.py uses Plotly.js for rendering, which supports base64-encoded typed arrays. In Plotly.py, NumPy array and NumPy-convertible arrays are base64 encoded before being passed to Plotly.js for rendering.


## Arrays and Data Types Supported

The following types of array objects in Python are supported:

- Numpy `numpy.ndarray` objects.
- Pandas Index, `pandas.Index`, or Series, `pandas.Series`, objects.
- Array objects that can be converted to `numpy.ndarray` objects. i.e., they implement `"__array__"` or `"__array_interface__"` and return a `numpy.ndarray`.

The following array data types are supported:

- int8
- uint8
- int16
- uint16
- int32
- uint32
- float32
- float64
- int64*
- uint64*
    
*If the array dtype is **int64** and **uint64**, often the default dtype for arrays in NumPy when no dtype is specified, those dtypes will be changed to other types internally by Plotly.py where possible. 



## Unsupported Attributes

Arrays passsed to attributes with the following names do not use the Plotly.js base64 typed arrays functionality:

`geojson`, `layers`, and `range`.


## Example with NumPy Arrays

Here, we use NumPy arrays with a `go.Scatter3d` figure.

```python
import plotly.graph_objects as go
import numpy as np

np.random.seed(1)

# Number of data points
N = 10000

# Generate random data
x = np.random.randn(N)
y = np.random.randn(N).astype('float32')
z = np.random.randint(size=N, low=0, high=256, dtype='uint8')
c = np.random.randint(size=N, low=-10, high=10, dtype='int8')

fig = go.Figure(data=[go.Scatter3d(
    x=x,
    y=y,
    z=z,
    marker=dict(color=c),
    mode='markers',
    opacity=0.2
)])

fig.show()
```

### Example with Multi-Dimensional Array

Here, we use a multi dimensional array with a `go.Surface` figure.


```python
import plotly.graph_objects as go
import numpy as np

np.random.seed(1)

# Define the dimensions
M = 100
N = 200

x = np.arange(0, M, 1, dtype='int32')
y = np.arange(0, N, 1, dtype='uint8')

z = np.random.random([N, M])

fig = go.Figure(data=[go.Surface(
    x=x,
    y=y,
    z=z
)])

fig.show()
```
