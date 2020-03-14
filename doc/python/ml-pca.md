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

## High-dimensional PCA Analysis with  `px.scatter_matrix`


### Visualize all the original dimensions

First, let's plot all the features and see how the `species` in the Iris dataset are grouped. In a [splom](https://plot.ly/python/splom/), each subplot displays a feature against another, so if we have $N$ features we have a $N \times N$ matrix.

In our example, we are plotting all 4 features from the Iris dataset, thus we can see how `sepal_width` is compared against `sepal_length`, then against `petal_width`, and so forth. Keep in mind how some pairs of features can more easily separate different species.

```python
import plotly.express as px

df = px.data.iris()
features = ["sepal_width", "sepal_length", "petal_width", "petal_length"]

fig = px.scatter_matrix(
    df,
    dimensions=features,
    color="species"
)
fig.update_traces(diagonal_visible=False)
fig.show()
```

###  Visualize all the principal components

Now, we apply `PCA` the same dataset, and retrieve **all** the components. We use the same `px.scatter_matrix` trace to display our results, but this time our features are the resulting *principal components*, ordered by how much variance they are able to explain. 

The importance of explained variance is demonstrated in the example below. The subplot between PC3 and PC4 is clearly unable to separate each class, whereas the subplot between PC1 and PC2 shows a clear separation between each species.

```python
import plotly.express as px
from sklearn.decomposition import PCA

df = px.data.iris()
features = ["sepal_width", "sepal_length", "petal_width", "petal_length"]

pca = PCA()
components = pca.fit_transform(df[features])
labels = {
    str(i): f"PC {i+1} ({var:.1f}%)" 
    for i, var in enumerate(pca.explained_variance_ratio_ * 100)
}

fig = px.scatter_matrix(
    components,
    labels=labels,
    dimensions=range(4),
    color=df["species"]
)
fig.update_traces(diagonal_visible=False)
fig.show()
```

### Visualize a subset of the principal components

When you will have too many features to visualize, you might be interested in only visualizing the most relevant components. Those components often capture a majority of the [explained variance](https://en.wikipedia.org/wiki/Explained_variation), which is a good way to tell if those components are sufficient for modelling this dataset.

In the example below, our dataset contains 10 features, but we only select the first 4 components, since they explain over 99% of the total variance.

```python
import pandas as pd
import plotly.express as px
from sklearn.decomposition import PCA
from sklearn.datasets import load_boston

boston = load_boston()
df = pd.DataFrame(boston.data, columns=boston.feature_names)
n_components = 4

pca = PCA(n_components=n_components)
components = pca.fit_transform(df)

total_var = pca.explained_variance_ratio_.sum() * 100

labels = {str(i): f"PC {i+1}" for i in range(n_components)}
labels['color'] = 'Median Price'

fig = px.scatter_matrix(
    components, 
    color=boston.target,
    dimensions=range(n_components),
    labels=labels,
    title=f'Total Explained Variance: {total_var:.2f}%',
)
fig.update_traces(diagonal_visible=False)
fig.show()
```

## 2D PCA Scatter Plot

In the previous examples, you saw how to visualize high-dimensional PCs. In this example, we show you how to simply visualize the first two principal components of a PCA, by reducing a dataset of 4 dimensions to 2D.

```python
import plotly.express as px
from sklearn.decomposition import PCA

df = px.data.iris()
X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]

pca = PCA(n_components=2)
components = pca.fit_transform(X)

fig = px.scatter(components, x=0, y=1, color=df['species'])
fig.show()
```

## Visualize PCA with `px.scatter_3d`

With `px.scatter_3d`, you can visualize an additional dimension, which let you capture even more variance.

```python
import plotly.express as px
from sklearn.decomposition import PCA

df = px.data.iris()
X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]

pca = PCA(n_components=3)
components = pca.fit_transform(X)

total_var = pca.explained_variance_ratio_.sum() * 100

fig = px.scatter_3d(
    components, x=0, y=1, z=2, color=df['species'], 
    title=f'Total Explained Variance: {total_var:.2f}%',
    labels={'0': 'PC 1', '1': 'PC 2', '2': 'PC 3'}
)
fig.show()
```

## Plotting explained variance

Often, you might be interested in seeing how much variance PCA is able to explain as you increase the number of components, in order to decide how many dimensions to ultimately keep or analyze. This example shows you how to quickly plot the cumulative sum of explained variance for a high-dimensional dataset like [Diabetes](https://scikit-learn.org/stable/datasets/index.html#diabetes-dataset).

```python
import numpy as np
import pandas as pd
import plotly.express as px
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

## Visualize Loadings

It is also possible to visualize loadings using `shapes`, and use `annotations` to indicate which feature a certain loading original belong to. Here, we define loadings as:

$$
loadings = eigenvectors \cdot \sqrt{eigenvalues}
$$

```python
import plotly.express as px
from sklearn.decomposition import PCA
from sklearn import datasets
from sklearn.preprocessing import StandardScaler

df = px.data.iris()
features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
X = df[features]

pca = PCA(n_components=2)
components = pca.fit_transform(X)

loadings = pca.components_.T * np.sqrt(pca.explained_variance_)

fig = px.scatter(components, x=0, y=1, color=df['species'])

for i, feature in enumerate(features):
    fig.add_shape(
        type='line',
        x0=0, y0=0,
        x1=loadings[i, 0],
        y1=loadings[i, 1]
    )
    fig.add_annotation(
        x=loadings[i, 0],
        y=loadings[i, 1],
        ax=0, ay=0,
        xanchor="center",
        yanchor="bottom",
        text=feature,
    )
fig.show()
```

## References

Learn more about `px`, `px.scatter_3d`, and `px.scatter_matrix` here:
* https://plot.ly/python/plotly-express/
* https://plot.ly/python/3d-scatter-plots/
* https://plot.ly/python/splom/

The following resources offer an in-depth overview of PCA and explained variance:
* https://en.wikipedia.org/wiki/Explained_variation
* https://scikit-learn.org/stable/modules/decomposition.html#pca
* https://stats.stackexchange.com/questions/2691/making-sense-of-principal-component-analysis-eigenvectors-eigenvalues/140579#140579
