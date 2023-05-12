---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.1'
      jupytext_version: 1.2.3
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
    version: 3.7.3
  plotly:
    description: How to make an UpSet plot in Python, which can be used to display counts of 
arbitrarily complex set intersections.
    display_as: scientific
    language: python
    layout: base
    name: UpSet Plots
    order: 10
    permalink: python/upset-plots/
---

[UpSet plots](https://en.wikipedia.org/wiki/UpSet_Plot) allow you to visualize data that counts different intersections
subsets inside a set. This could arise by actual intersections, or counting tag occurrences on data which need not be 
disjoint. Data used in this method must be in one of two forms: wide or condensed. If the latter is provided, then the
data will be transformed into the wide format before proceeding with the plot generation. 

#### A Simple UpSet Plot
```python
import plotly.express as px
import plotly.figure_factory as ff

df = px.data.iris()

# Create categorical non-disjoint tags for "large" features
df['SL'] = df['sepal_length'].apply(lambda x: int(x > 6))
df['SW'] = df['sepal_width'].apply(lambda x: int(x > 3))
df['PL'] = df['petal_length'].apply(lambda x: int(x > 3))
df['PW'] = df['petal_width'].apply(lambda x: int(x > 1))

df = df[['SL', 'SW', 'PL', 'PW']]    # data in "wide" form
fig = ff.create_upset(df, color_discrete_sequence=['#000000'])
fig.show()
```


#### Using Condensed Format

Sometimes it's more convenient to have data where one column is given as a list of (possibly) overlapping tags that data
point has. This can be thought of as dividing our dataset into a family of subsets, one for each tag. UpSet plots can help
analyze how different combinations of these tags are distributed in the data. 

As long as the entries in this column are a list/tuple, this method can handle the preprocessing step of getting the 
data into the "wide" format like above. We simulate this below.

```python
import plotly.express as px
import plotly.figure_factory as ff

df = px.data.iris()

# Create categorical non-disjoint tags for "large" features
df['SL'] = df['sepal_length'].apply(lambda x: int(x > 6))
df['SW'] = df['sepal_width'].apply(lambda x: int(x > 3))
df['PL'] = df['petal_length'].apply(lambda x: int(x > 3))
df['PW'] = df['petal_width'].apply(lambda x: int(x > 1))

# Simulate "tags" column
df['tags'] = df['sepal_length'].apply(lambda x: ['SL'] if x > 6 else ['']) + df['sepal_width'].apply(lambda x: ['SW'] if x > 3 else ['']) + \
            df['petal_length'].apply(lambda x: ['PL'] if x > 3 else ['']) + df['petal_width'].apply(lambda x: ['PW'] if x > 1 else [''])
df['tags'] = df['tags'].apply(lambda x: [y for y in x if y != ''])

# Note we can (optionally) choose the order for how the method unpacks the tags
fig = ff.create_upset(df, subset_column='tags', subset_order=['PW', 'SW', 'PL', 'SL'], color_discrete_sequence=['#000000'])
fig.show()
```

#### Grouping Data by Color

This method supports two ways of grouping data to visualize counts of subset intersections. The first, shown here, 
allows you to see how these counts vary by subset in parallel across categories described by another column.

```python
import plotly.express as px
import plotly.figure_factory as ff

df = px.data.iris()

# Create categorical non-disjoint tags for "large" features
df['SL'] = df['sepal_length'].apply(lambda x: int(x > 6))
df['SW'] = df['sepal_width'].apply(lambda x: int(x > 3))
df['PL'] = df['petal_length'].apply(lambda x: int(x > 3))
df['PW'] = df['petal_width'].apply(lambda x: int(x > 1))

df = df[['species', 'SL', 'SW', 'PL', 'PW']]    # data in "wide" form, with extra "species" column
# Note: ONLY the extra color column was kept, as rest of columns are inferred to make "wide" format subset data
fig = ff.create_upset(df, color='species', asc=True)    # Can toggle in "asc" order
fig.show()
```

#### Visualizing Distributions of Counts by Subset

The other way to group data is to provide a column which provides label for different clusters of observations. This
could be e.g. the day of the observation, different samples in biology, or any other way of dividing up the same 
observations in different situations. This technique lets you see how the different subset counts vary across this 
dimension.

```python
import plotly.express as px
import plotly.figure_factory as ff
import numpy as np

df = px.data.iris()

# Create categorical non-disjoint tags for "large" features
df['SL'] = df['sepal_length'].apply(lambda x: int(x > 6))
df['SW'] = df['sepal_width'].apply(lambda x: int(x > 3))
df['PL'] = df['petal_length'].apply(lambda x: int(x > 3))
df['PW'] = df['petal_width'].apply(lambda x: int(x > 1))
df = df[['SL', 'SW', 'PL', 'PW']]

# Simulate random "day" of observation
np.random.seed(100)
df['day'] = np.random.randint(0, 5, len(df))

fig = ff.create_upset(df, x='day', plot_type='box', show_yaxis=True, title='Variation of Tags by Day')
fig.update_layout(yaxis_side="right")
fig.show()
```

