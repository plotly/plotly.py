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
    description:
      How to make scatterplot matrices or sploms natively in Python with
      Plotly.
    display_as: statistical
    language: python
    layout: base
    name: Scatterplot Matrix
    order: 7
    page_type: u-guide
    permalink: python/splom/
    redirect_from: python/scatterplot-matrix/
    thumbnail: thumbnail/splom_image.jpg
---

### Scatter matrix with Plotly Express

A scatterplot matrix is a matrix associated to n numerical arrays (data variables), $X_1,X_2,…,X_n$ , of the same length. The cell (i,j) of such a matrix displays the scatter plot of the variable Xi versus Xj.

Here we show the Plotly Express function `px.scatter_matrix` to plot the scatter matrix for the columns of the dataframe. By default, all columns are considered.

[Plotly Express](/python/plotly-express/) is the easy-to-use, high-level interface to Plotly, which [operates on "tidy" data](/python/px-arguments/) and produces [easy-to-style figures](/python/styling-plotly-express/).

```python
import plotly.express as px
df = px.data.iris()
fig = px.scatter_matrix(df)
fig.show()
```

Specify the columns to be represented with the `dimensions` argument, and set colors using a column of the dataframe:

```python
import plotly.express as px
df = px.data.iris()
fig = px.scatter_matrix(df,
    dimensions=["sepal_width", "sepal_length", "petal_width", "petal_length"],
    color="species")
fig.show()
```

#### Styled Scatter Matrix with Plotly Express

The scatter matrix plot can be configured thanks to the parameters of `px.scatter_matrix`, but also thanks to `fig.update_traces` for fine tuning (see the next section to learn more about the options).

```python
import plotly.express as px
df = px.data.iris()
fig = px.scatter_matrix(df,
    dimensions=["sepal_width", "sepal_length", "petal_width", "petal_length"],
    color="species", symbol="species",
    title="Scatter matrix of iris data set",
    labels={col:col.replace('_', ' ') for col in df.columns}) # remove underscore
fig.update_traces(diagonal_visible=False)
fig.show()
```

<!-- #region -->

### Scatter matrix (splom) with go.Splom

If Plotly Express does not provide a good starting point, it is possible to use the more generic `go.Splom` function. All its parameters are documented in the reference page https://plot.ly/python/reference/#splom.

The Plotly splom trace implementation for the scatterplot matrix does not require to set $x=Xi$ , and $y=Xj$, for each scatter plot. All arrays, $X_1,X_2,…,X_n$ , are passed once, through a list of dicts called dimensions, i.e. each array/variable represents a dimension.

A trace of type `splom` is defined as follows:

```
trace=go.Splom(dimensions=[dict(label='string-1',
                                values=X1),
                           dict(label='string-2',
                                values=X2),
                           .
                           .
                           .
                           dict(label='string-n',
                                values=Xn)],
                           ....
               )
```

The label in each dimension is assigned to the axes titles of the corresponding matrix cell.

<!-- #endregion -->

#### Splom of the Iris data set

```python
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/iris-data.csv')

# The Iris dataset contains four data variables, sepal length, sepal width, petal length,
# petal width, for 150 iris flowers. The flowers are labeled as `Iris-setosa`,
# `Iris-versicolor`, `Iris-virginica`.

# Define indices corresponding to flower categories, using pandas label encoding
index_vals = df['class'].astype('category').cat.codes

fig = go.Figure(data=go.Splom(
                dimensions=[dict(label='sepal length',
                                 values=df['sepal length']),
                            dict(label='sepal width',
                                 values=df['sepal width']),
                            dict(label='petal length',
                                 values=df['petal length']),
                            dict(label='petal width',
                                 values=df['petal width'])],
                text=df['class'],
                marker=dict(color=index_vals,
                            showscale=False, # colors encode categorical variables
                            line_color='white', line_width=0.5)
                ))


fig.update_layout(
    title='Iris Data set',
    dragmode='select',
    width=600,
    height=600,
    hovermode='closest',
)

fig.show()
```

The scatter plots on the principal diagonal can be removed by setting `diagonal_visible=False`:

```python
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/iris-data.csv')
index_vals = df['class'].astype('category').cat.codes

fig = go.Figure(data=go.Splom(
                dimensions=[dict(label='sepal length',
                                 values=df['sepal length']),
                            dict(label='sepal width',
                                 values=df['sepal width']),
                            dict(label='petal length',
                                 values=df['petal length']),
                            dict(label='petal width',
                                 values=df['petal width'])],
                diagonal_visible=False, # remove plots on diagonal
                text=df['class'],
                marker=dict(color=index_vals,
                            showscale=False, # colors encode categorical variables
                            line_color='white', line_width=0.5)
                ))


fig.update_layout(
    title='Iris Data set',
    width=600,
    height=600,
)

fig.show()
```

To plot only the lower/upper half of the splom we switch the default `showlowerhalf=True`/`showupperhalf=True` to `False`:

```python
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/iris-data.csv')
index_vals = df['class'].astype('category').cat.codes

fig = go.Figure(data=go.Splom(
                dimensions=[dict(label='sepal length',
                                 values=df['sepal length']),
                            dict(label='sepal width',
                                 values=df['sepal width']),
                            dict(label='petal length',
                                 values=df['petal length']),
                            dict(label='petal width',
                                 values=df['petal width'])],
                showupperhalf=False, # remove plots on diagonal
                text=df['class'],
                marker=dict(color=index_vals,
                            showscale=False, # colors encode categorical variables
                            line_color='white', line_width=0.5)
                ))


fig.update_layout(
    title='Iris Data set',
    width=600,
    height=600,
)

fig.show()
```

Each dict in the list dimensions has a key, visible, set by default on True. We can choose to remove a variable from splom, by setting `visible=False` in its corresponding dimension. In this case the default grid associated to the scatterplot matrix keeps its number of cells, but the cells in the row and column corresponding to the visible false dimension are empty:

```python
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/iris-data.csv')
index_vals = df['class'].astype('category').cat.codes

fig = go.Figure(data=go.Splom(
                dimensions=[dict(label='sepal length',
                                 values=df['sepal length']),
                            dict(label='sepal width',
                                 values=df['sepal width'],
                                 visible=False),
                            dict(label='petal length',
                                 values=df['petal length']),
                            dict(label='petal width',
                                 values=df['petal width'])],
                text=df['class'],
                marker=dict(color=index_vals,
                            showscale=False, # colors encode categorical variables
                            line_color='white', line_width=0.5)
                ))


fig.update_layout(
    title='Iris Data set',
    width=600,
    height=600,
)

fig.show()
```

#### Splom for the diabetes dataset

Diabetes dataset is downloaded from [kaggle](https://www.kaggle.com/uciml/pima-indians-diabetes-database/data). It is used to predict the onset of diabetes based on 8 diagnostic measures. The diabetes file contains the diagnostic measures for 768 patients, that are labeled as non-diabetic (Outcome=0), respectively diabetic (Outcome=1). The splom associated to the 8 variables can illustrate the strength of the relationship between pairs of measures for diabetic/nondiabetic patients.

```python
import plotly.graph_objs as go
import pandas as pd

dfd = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/diabetes.csv')
textd = ['non-diabetic' if cl==0 else 'diabetic' for cl in dfd['Outcome']]

fig = go.Figure(data=go.Splom(
                  dimensions=[dict(label='Pregnancies', values=dfd['Pregnancies']),
                              dict(label='Glucose', values=dfd['Glucose']),
                              dict(label='BloodPressure', values=dfd['BloodPressure']),
                              dict(label='SkinThickness', values=dfd['SkinThickness']),
                              dict(label='Insulin', values=dfd['Insulin']),
                              dict(label='BMI', values=dfd['BMI']),
                              dict(label='DiabPedigreeFun', values=dfd['DiabetesPedigreeFunction']),
                              dict(label='Age', values=dfd['Age'])],
                  marker=dict(color=dfd['Outcome'],
                              size=5,
                              colorscale='Bluered',
                              line=dict(width=0.5,
                                        color='rgb(230,230,230)')),
                  text=textd,
                  diagonal=dict(visible=False)))

title = "Scatterplot Matrix (SPLOM) for Diabetes Dataset<br>Data source:"+\
        " <a href='https://www.kaggle.com/uciml/pima-indians-diabetes-database/data'>[1]</a>"
fig.update_layout(title=title,
                  dragmode='select',
                  width=1000,
                  height=1000,
                  hovermode='closest')

fig.show()
```
