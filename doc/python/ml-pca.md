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
  language_info:
    codemirror_mode:
      name: ipython
      version: 3
    file_extension: .py
    mimetype: text/x-python
    name: python
    nbconvert_exporter: python
    pygments_lexer: ipython3
    version: 3.7.6
  plotly:
    description: Visualize Principle Component Analysis (PCA) of your high-dimensional
      data with Plotly on Python.
    display_as: ai_ml
    language: python
    layout: base
    name: PCA Visualization
    order: 4
    page_type: example_index
    permalink: python/pca-visualization/
    thumbnail: thumbnail/ml-pca.png
---

## Basic PCA Scatter Plot

This example shows you how to simply visualize the first two principal components of a PCA, by reducing a dataset of 4 dimensions to 2D. It uses scikit-learn's `PCA`.

```python
import plotly.express as px
from sklearn.decomposition import PCA

df = px.data.iris()
X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]

pca = PCA(n_components=2)
components = pca.fit_transform(X)

fig = px.scatter(x=components[:, 0], y=components[:, 1], color=df['species'])
fig.show()
```

## Visualize PCA with `px.scatter_3d`

Just like the basic PCA plot, this let you visualize the first 3 dimensions. This additionally displays the total variance explained by those components.

```python
import plotly.express as px
from sklearn.decomposition import PCA

df = px.data.iris()
X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]

pca = PCA(n_components=3)
components = pca.fit_transform(X)

total_var = pca.explained_variance_ratio_.sum() * 100

fig = px.scatter_3d(
    x=components[:, 0], y=components[:, 1], z=components[:, 2],
    color=df['species'], 
    title=f'Total Explained Variance: {total_var:.2f}%',
    labels={'x': 'PC 1', 'y': 'PC 2', 'z': 'PC 3'},
)
fig.show()
```

## Plot high-dimensional components with `px.scatter_matrix`

If you need to visualize more than 3 dimensions, you can use scatter plot matrices.

```python
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.datasets import load_boston

boston = load_boston()
df = pd.DataFrame(boston.data, columns=boston.feature_names)

pca = PCA(n_components=5)
components = pca.fit_transform(df)

total_var = pca.explained_variance_ratio_.sum() * 100

labels = {str(i): f"PC {i+1}" for i in range(5)}
labels['color'] = 'Median Price'

fig = px.scatter_matrix(
    components, 
    color=boston.target,
    dimensions=range(5),
    labels=labels,
    title=f'Total Explained Variance: {total_var:.2f}%',
)
fig.update_traces(diagonal_visible=False)
fig.show()
```

## Plotting explained variance

Often, you might be interested in seeing how much variance the PCA is able to explain as you increase the number of components, in order to decide how many dimensions to ultimately keep or analyze. This example shows you how to quickly plot the cumulative sum of explained variance for a high-dimensional dataset like [Diabetes](https://scikit-learn.org/stable/datasets/index.html#diabetes-dataset).

```python
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.datasets import load_diabetes

boston = load_diabetes()
df = pd.DataFrame(boston.data, columns=boston.feature_names)

pca = PCA()
pca.fit(df)
exp_var_cumul = np.cumsum(pca.explained_variance_ratio_)

px.area(
    x=range(1, exp_var_cumul.shape[0] + 1),
    y=exp_var_cumul, 
    labels={"x": "# Components", "y": "Explained Variance"}
)
```

## Visualize loadings
