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
    description: Learn how to perform several operations on matrices including inverse,
      eigenvalues, and determinents
    display_as: mathematics
    has_thumbnail: false
    language: python
    layout: base
    name: Linear Algebra
    order: 10
    page_type: example_index
    permalink: python/linear-algebra/
    thumbnail: /images/static-image
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by dowloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


#### Imports
The tutorial below imports [NumPy](http://www.numpy.org/), [Pandas](https://plot.ly/pandas/intro-to-pandas-tutorial/), and [SciPy](https://www.scipy.org/).

```python
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.tools import FigureFactory as FF

import numpy as np
import pandas as pd
import scipy
```

#### Add Two Matrices


A Matrix is a 2D array that stores real or complex numbers. A _Real Matrix_ is one such that all its elements $r$ belong to $\mathbb{R}$. Likewise, a _Complex Matrix_ has entries $c$ in $\mathbb{C}$.

```python
matrix1 = np.matrix(
    [[0, 4],
     [2, 0]]
)

matrix2 = np.matrix(
    [[-1, 2],
     [1, -2]]
)

matrix_sum = matrix1 + matrix2

colorscale = [[0, '#EAEFC4'], [1, '#9BDF46']]
font=['#000000', '#000000']

table = FF.create_annotated_heatmap(matrix_sum.tolist(), colorscale=colorscale, font_colors=font)
py.iplot(table, filename='matrix-sum')
```

#### Multiply Two Matrices
How to find the product of two matrices

```python
matrix1 = np.matrix(
    [[1, 4],
     [2, 0]]
)

matrix2 = np.matrix(
    [[-1, 2],
     [1, -2]]
)

matrix_prod = matrix1 * matrix2

colorscale = [[0, '#F1FFD9'], [1, '#8BDBF5']]
font=['#000000', '#000000']

table = FF.create_annotated_heatmap(matrix_prod.tolist(), colorscale=colorscale, font_colors=font)
py.iplot(table, filename='matrix-prod')
```

#### Solve Matrix Equation
How to find the solution of $AX=B$

```python
A = np.matrix(
    [[1, 4],
     [2, 0]]
)

B = np.matrix(
    [[-1, 2],
     [1, -2]]
)

X = np.linalg.solve(A, B)

colorscale = [[0, '#497285'], [1, '#DFEBED']]
font=['#000000', '#000000']

table = FF.create_annotated_heatmap(X.tolist(), colorscale=colorscale, font_colors=font)
py.iplot(table, filename='matrix-eq')
```

#### Find the Determinant

```python
matrix = np.matrix(
    [[1, 4],
     [2, 0]]
)

det = np.linalg.det(matrix)
det
```

#### Find the Inverse

```python
matrix = np.matrix(
    [[1, 4],
     [2, 0]]
)

inverse = np.linalg.inv(matrix)

colorscale = [[0, '#F1FAFB'], [1, '#A0E4F1']]
font=['#000000', '#000000']

table = FF.create_annotated_heatmap(inverse.tolist(), colorscale=colorscale, font_colors=font)
py.iplot(table, filename='inverse')
```

#### Find Eigenvalues

```python
matrix = np.matrix(
    [[1, 4],
     [2, 0]]
)

eigvals = np.linalg.eigvals(matrix)
print("The eignevalues are %f and %f") %(eigvals[0], eigvals[1])
```

#### Find SVD
How to find the Singular Value Decomposition of a matrix, i.e. break up a matrix into the product of three matrices: $U$, $\Sigma$, $V^*$

```python
matrix = np.matrix(
    [[1, 4],
     [2, 0]]
)

svd = np.linalg.svd(matrix)

u = svd[0]
sigma = svd[1]
v = svd[2]

u = u.tolist()
sigma = sigma.tolist()
v = v.tolist()

colorscale = [[0, '#111111'],[1, '#222222']]
font=['#ffffff', '#ffffff']

matrix_prod = [
    ['$U$', '', '$\Sigma$', '$V^*$', ''],
    [u[0][0], u[0][1], sigma[0], v[0][0], v[0][1]],
    [u[1][0], u[1][1], sigma[1], v[1][0], v[1][1]]
]

table = FF.create_table(matrix_prod)
py.iplot(table, filename='svd')
```

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'python_Linear_Algebra.ipynb', 'python/linear-algebra/', 'Linear Algebra | plotly',
    'Learn how to perform several operations on matrices including inverse, eigenvalues, and determinents',
    title='Linear Algebra in Python. | plotly',
    name='Linear Algebra',
    language='python',
    page_type='example_index', has_thumbnail='false', display_as='mathematics', order=10,
    ipynb= '~notebook_demo/104')
```

```python

```
