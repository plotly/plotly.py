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
    version: 3.6.7
  plotly:
    description: How to make Gantt Charts in Python with Plotly. Gantt Charts use
      horizontal bars to represent the start and end times of tasks.
    display_as: basic
    language: python
    layout: base
    name: Gantt Charts
    order: 10
    page_type: u-guide
    permalink: python/gantt/
    thumbnail: thumbnail/gantt.jpg
---

A [Gantt chart](https://en.wikipedia.org/wiki/Gantt_chart) is a type of bar chart that illustrates a project schedule. The chart lists the tasks to be performed on the vertical axis, and time intervals on the horizontal axis. The width of the horizontal bars in the graph shows the duration of each activity.

See also the [bar charts examples](https://plot.ly/python/bar-charts/).


#### Simple Gantt Chart

```python
import plotly.figure_factory as ff

df = [dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28'),
      dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15'),
      dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30')]

fig = ff.create_gantt(df)
fig.show()
```

#### Index by Numeric Variable

```python
import plotly.figure_factory as ff

df = [dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28', Complete=10),
      dict(Task="Job B", Start='2008-12-05', Finish='2009-04-15', Complete=60),
      dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30', Complete=95)]

fig = ff.create_gantt(df, colors='Viridis', index_col='Complete', show_colorbar=True)
fig.show()
```

#### Index by String Variable

```python
import plotly.figure_factory as ff

df = [dict(Task="Job A", Start='2009-01-01', Finish='2009-02-01', Resource='Apple'),
      dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15', Resource='Grape'),
      dict(Task="Job C", Start='2009-04-20', Finish='2009-09-30', Resource='Banana')]

colors = ['#7a0504', (0.2, 0.7, 0.3), 'rgb(210, 60, 180)']

fig = ff.create_gantt(df, colors=colors, index_col='Resource', reverse_colors=True,
                      show_colorbar=True)
fig.show()
```

#### Use a Dictionary for Colors

```python
import plotly.figure_factory as ff

df = [dict(Task="Job A", Start='2016-01-01', Finish='2016-01-02', Resource='Apple'),
      dict(Task="Job B", Start='2016-01-02', Finish='2016-01-04', Resource='Grape'),
      dict(Task="Job C", Start='2016-01-02', Finish='2016-01-03', Resource='Banana')]

colors = dict(Apple='rgb(220, 0, 0)', Grape='rgb(170, 14, 200)', Banana=(1, 0.9, 0.16))

fig = ff.create_gantt(df, colors=colors, index_col='Resource', show_colorbar=True)
fig.show()
```

#### Use a Pandas Dataframe

```python
import plotly.figure_factory as ff

import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gantt_example.csv')

fig = ff.create_gantt(df, colors=['#333F44', '#93e4c1'], index_col='Complete',
                      show_colorbar=True, bar_width=0.2, showgrid_x=True, showgrid_y=True)
fig.show()
```

#### Using Hours and Minutes in Times

```python
import plotly.figure_factory as ff

df = [
    dict(Task='Morning Sleep', Start='2016-01-01', Finish='2016-01-01 6:00:00', Resource='Sleep'),
    dict(Task='Breakfast', Start='2016-01-01 7:00:00', Finish='2016-01-01 7:30:00', Resource='Food'),
    dict(Task='Work', Start='2016-01-01 9:00:00', Finish='2016-01-01 11:25:00', Resource='Brain'),
    dict(Task='Break', Start='2016-01-01 11:30:00', Finish='2016-01-01 12:00:00', Resource='Rest'),
    dict(Task='Lunch', Start='2016-01-01 12:00:00', Finish='2016-01-01 13:00:00', Resource='Food'),
    dict(Task='Work', Start='2016-01-01 13:00:00', Finish='2016-01-01 17:00:00', Resource='Brain'),
    dict(Task='Exercise', Start='2016-01-01 17:30:00', Finish='2016-01-01 18:30:00', Resource='Cardio'),
    dict(Task='Post Workout Rest', Start='2016-01-01 18:30:00', Finish='2016-01-01 19:00:00', Resource='Rest'),
    dict(Task='Dinner', Start='2016-01-01 19:00:00', Finish='2016-01-01 20:00:00', Resource='Food'),
    dict(Task='Evening Sleep', Start='2016-01-01 21:00:00', Finish='2016-01-01 23:59:00', Resource='Sleep')
]

colors = dict(Cardio = 'rgb(46, 137, 205)',
              Food = 'rgb(114, 44, 121)',
              Sleep = 'rgb(198, 47, 105)',
              Brain = 'rgb(58, 149, 136)',
              Rest = 'rgb(107, 127, 135)')

fig = ff.create_gantt(df, colors=colors, index_col='Resource', title='Daily Schedule',
                      show_colorbar=True, bar_width=0.8, showgrid_x=True, showgrid_y=True)
fig.show()
```

#### Group Tasks Together

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

#### Reference


```python
help(ff.create_gantt)
```

```python

```
