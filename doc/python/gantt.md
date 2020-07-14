---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.4.2
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
    version: 3.7.7
  plotly:
    description: How to make Gantt Charts in Python with Plotly. Gantt Charts use
      horizontal bars to represent the start and end times of tasks.
    display_as: basic
    language: python
    layout: base
    name: Gantt Charts
    order: 9
    page_type: u-guide
    permalink: python/gantt/
    thumbnail: thumbnail/gantt.jpg
---

A [Gantt chart](https://en.wikipedia.org/wiki/Gantt_chart) is a type of bar chart that illustrates a project schedule. The chart lists the tasks to be performed on the vertical axis, and time intervals on the horizontal axis. The width of the horizontal bars in the graph shows the duration of each activity.


### Gantt Charts and Timelines with plotly.express

[Plotly Express](/python/plotly-express/) is the easy-to-use, high-level interface to Plotly, which [operates on a variety of types of data](/python/px-arguments/) and produces [easy-to-style figures](/python/styling-plotly-express/). With `px.timeline` (*introduced in version 4.9*) each data point is represented as a horizontal bar with a start and end point specified as dates. 

The `px.timeline` function by default sets the X-axis to be of `type=date`, so it can be configured like any [time-series chart](/python/time-series/).

Plotly Express also supports a [general-purpose `px.bar` function for bar charts](/python/bar-charts/).

```python
import plotly.express as px
import pandas as pd

df = pd.DataFrame([
    dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28'),
    dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15'),
    dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30')
])

fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task")
fig.update_yaxes(autorange="reversed") # otherwise tasks are listed from the bottom up
fig.show()
```

`px.timeline` supports [discrete color](/python/discrete-color/) as above, or [continuous color](/python/colorscales/) as follows.

```python
import plotly.express as px
import pandas as pd

df = pd.DataFrame([
    dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28', Resource="Alex"),
    dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15', Resource="Alex"),
    dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30', Resource="Max")
])

fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", color="Resource")
fig.update_yaxes(autorange="reversed")
fig.show()
```

```python
import plotly.express as px
import pandas as pd

df = pd.DataFrame([
    dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28', Completion_pct=50),
    dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15', Completion_pct=25),
    dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30', Completion_pct=75)
])

fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", color="Completion_pct")
fig.update_yaxes(autorange="reversed")
fig.show()
```

It is also possible to have multiple bars on the same horizontal line, say by resource:

*Note*: When setting `color` to the same value as `y`, `autorange` should not be set to `reverse`, so as to list the value of the Y axis in the same order as the legend entries.

```python
import plotly.express as px
import pandas as pd

df = pd.DataFrame([
    dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28', Resource="Alex"),
    dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15', Resource="Alex"),
    dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30', Resource="Max")
])

fig = px.timeline(df, x_start="Start", x_end="Finish", y="Resource", color="Resource")
fig.show()
```

#### Deprecated Figure Factory

Prior to the introduction of `plotly.express.timeline()` in version 4.9, the recommended way to make Gantt charts was to use the now-deprecated `create_gantt()` [figure factory](/python/figure-factories/), as follows:

```python
import plotly.figure_factory as ff

df = [dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28'),
      dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15'),
      dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30')]

fig = ff.create_gantt(df)
fig.show()
```

<!-- #region -->
#### Group Tasks Together


The following example shows how to use the now-deprecated `create_gantt()` [figure factory](/python/figure-factories/) to color tasks by a numeric variable.
<!-- #endregion -->

```python
import plotly.figure_factory as ff

df = [dict(Task="Job-1", Start='2017-01-01', Finish='2017-02-02', Resource='Complete'),
      dict(Task="Job-1", Start='2017-02-15', Finish='2017-03-15', Resource='Incomplete'),
      dict(Task="Job-2", Start='2017-01-17', Finish='2017-02-17', Resource='Not Started'),
      dict(Task="Job-2", Start='2017-01-17', Finish='2017-02-17', Resource='Complete'),
      dict(Task="Job-3", Start='2017-03-10', Finish='2017-03-20', Resource='Not Started'),
      dict(Task="Job-3", Start='2017-04-01', Finish='2017-04-20', Resource='Not Started'),
      dict(Task="Job-3", Start='2017-05-18', Finish='2017-06-18', Resource='Not Started'),
      dict(Task="Job-4", Start='2017-01-14', Finish='2017-03-14', Resource='Complete')]

colors = {'Not Started': 'rgb(220, 0, 0)',
          'Incomplete': (1, 0.9, 0.16),
          'Complete': 'rgb(0, 255, 100)'}

fig = ff.create_gantt(df, colors=colors, index_col='Resource', show_colorbar=True,
                      group_tasks=True)
fig.show()
```

#### Color by Numeric Variable

The following example shows how to use the now-deprecated `create_gantt()` [figure factory](/python/figure-factories/) to color tasks by a numeric variable.

```python
import plotly.figure_factory as ff

df = [dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28', Complete=10),
      dict(Task="Job B", Start='2008-12-05', Finish='2009-04-15', Complete=60),
      dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30', Complete=95)]

fig = ff.create_gantt(df, colors='Viridis', index_col='Complete', show_colorbar=True)
fig.show()
```

#### Reference


For more info on `ff.create_gantt()`, see the [full function reference](https://plotly.com/python-api-reference/generated/plotly.figure_factory.create_gantt.html)
