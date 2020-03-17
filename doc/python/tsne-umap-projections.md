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
    description: Visualize scikit-learn's k-Nearest Neighbors (kNN) classification
      in Python with Plotly.
    display_as: ai_ml
    language: python
    layout: base
    name: t-SNE and UMAP projections
    order: 1
    page_type: example_index
    permalink: python/t-sne-and-umap-projections/
    thumbnail: thumbnail/tsne-umap-projections.png
---

## Basic t-SNE projections


### Visualizing high-dimensional data with `px.scatter_matrix`

```python
import plotly.express as px

df = px.data.iris()
features = ["sepal_width", "sepal_length", "petal_width", "petal_length"]
fig = px.scatter_matrix(df, dimensions=features, color="species")
fig.show()
```

### Project data into 2D with t-SNE and `px.scatter`

```python
from sklearn.manifold import TSNE
import plotly.express as px

df = px.data.iris()

features = df.loc[:, :'petal_width']

tsne = TSNE(n_components=2, random_state=0)
projections = tsne.fit_transform(features)

fig = px.scatter(
    projections, x=0, y=1, 
    color=df.species, labels={'color': 'species'}
)
fig.show()
```

### Project data into 3D with t-SNE and `px.scatter_3d`

```python
from sklearn.manifold import TSNE
import plotly.express as px

df = px.data.iris()

features = df.loc[:, :'petal_width']

tsne = TSNE(n_components=3, random_state=0)
projections = tsne.fit_transform(features, )

fig = px.scatter_3d(
    projections, x=0, y=1, z=2, 
    color=df.species, labels={'color': 'species'}
)
fig.update_traces(marker_size=8)
fig.show()
```

## Projections with UMAP

Just like t-SNE, [UMAP](https://umap-learn.readthedocs.io/en/latest/index.html) is a dimensionality reduction specifically designed for visualizing complex data in low dimensions (2D or 3D). As the number of data points increase, [UMAP becomes more time efficient](https://umap-learn.readthedocs.io/en/latest/benchmarking.html) compared to TSNE.

In the example below, we see how easy it is to use UMAP as a drop-in replacement for scikit-learn's `manifold.TSNE`.

```python
from umap import UMAP
import plotly.express as px

df = px.data.iris()

features = df.loc[:, :'petal_width']

umap_2d = UMAP(n_components=2, init='random', random_state=0)
umap_3d = UMAP(n_components=3, init='random', random_state=0)

proj_2d = umap_2d.fit_transform(features)
proj_3d = umap_3d.fit_transform(features)

fig_2d = px.scatter(
    proj_2d, x=0, y=1,
    color=df.species, labels={'color': 'species'}
)
fig_3d = px.scatter_3d(
    proj_3d, x=0, y=1, z=2, 
    color=df.species, labels={'color': 'species'}
)
fig_3d.update_traces(marker_size=5)

fig_2d.show()
fig_3d.show()
```

## Visualizing image datasets

In the following example, we show how to visualize large image datasets using UMAP. Here, we use [`load_digits`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html), a subset of the famous MNIST dataset that was downsized to 8x8 and flattened to 64 dimensions.

```python
import plotly.express as px
from sklearn.datasets import load_digits
from umap import UMAP

digits = load_digits()

umap_2d = UMAP(random_state=0)
umap_2d.fit(digits.data)

projections = umap_2d.transform(digits.data)

fig = px.scatter(
    projections, x=0, y=1, 
    color=digits.target.astype(str), labels={'color': 'digit'}
)
fig.show()
```

### Reference
