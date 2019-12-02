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
    description: How to add images as logos to Plotly charts.
    display_as: advanced_opt
    language: python
    layout: base
    name: Logos
    order: 6
    page_type: example_index
    permalink: python/logos/
    thumbnail: thumbnail/your-tutorial-chart.jpg
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


#### Formatting and Positioning Images as Logos

```python
import plotly.plotly as py
import plotly.graph_objs as go

data = [
    go.Bar(
        x=['-35.3', '-15.9', '-15.8', '-15.6', '-11.1',
           '-9.6', '-9.2', '-3.5', '-1.9', '-0.9',
           '1.0', '1.4', '1.7', '2.0', '2.8', '6.2',
           '8.1', '8.5', '8.5', '8.6', '11.4', '12.5',
           '13.3', '13.7', '14.4', '17.5', '17.7',
           '18.9', '25.1', '28.9', '41.4'],
        y=['Designers, musicians, artists, etc.',
           'Secretaries and administrative assistants',
           'Waiters and servers', 'Archivists, curators, and librarians',
           'Sales and related', 'Childcare workers, home car workers, etc.',
           'Food preparation occupations', 'Janitors, maids, etc.',
           'Healthcare technicians, assistants. and aides',
           'Counselors, social and religious workers',
           'Physical, life and social scientists', 'Construction',
           'Factory assembly workers', 'Machinists, repairmen, etc.',
           'Media and communications workers', 'Teachers',
           'Mechanics, repairmen, etc.', 'Financial analysts and advisers',
           'Farming, fishing and forestry workers',
           'Truck drivers, heavy equipment operator, etc.','Accountants and auditors',
           'Human resources, management analysts, etc.', 'Managers',
           'Lawyers and judges', 'Engineers, architects and surveyors',
           'Nurses', 'Legal support workers',
           'Computer programmers and system admin.', 'Police officers and firefighters',
           'Chief executives', 'Doctors, dentists and surgeons'],
        marker=dict(
            color='rgb(253, 240, 54)',
            line=dict(color='rgb(0, 0, 0)',
                      width=2)
        ),
        orientation='h',
    )
]

layout = go.Layout(
    images=[dict(
        source="https://raw.githubusercontent.com/cldougl/plot_images/add_r_img/vox.png",
        xref="paper", yref="paper",
        x=1, y=1.05,
        sizex=0.2, sizey=0.2,
        xanchor="right", yanchor="bottom"
      )],
    autosize=False, height=800, width=700,
    bargap=0.15, bargroupgap=0.1,
    barmode='stack', hovermode='x',
    margin=dict(r=20, l=300,
                  b=75, t=125),
    title='Moving Up, Moving Down<br><i>Percentile change in income between childhood and adulthood</i>',
    xaxis=dict(
        dtick=10, nticks=0,
        gridcolor='rgba(102, 102, 102, 0.4)',
        linecolor='#000', linewidth=1,
        mirror=True,
        showticklabels=True, tick0=0, tickwidth=1,
        title='<i>Change in percentile</i>',
    ),
    yaxis=dict(
        anchor='x',
        gridcolor='rgba(102, 102, 102, 0.4)', gridwidth=1,
        linecolor='#000', linewidth=1,
        mirror=True, showgrid=False,
        showline=True, zeroline=False,
        showticklabels=True, tick0=0,
        type='category',
    )
)
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)
```

```python
import plotly.plotly as py
import plotly.graph_objs as go

fig = py.get_figure('https://plot.ly/~Dreamshot/8152/', raw=True)
fig['layout']['yaxis']['tickangle'] = 0
fig = go.Figure(fig)

fig.layout.images = [dict(
        source="https://raw.githubusercontent.com/cldougl/plot_images/add_r_img/accuweather.jpeg",
        xref="paper", yref="paper",
        x=0.1, y=1.05,
        sizex=0.4, sizey=0.4,
        xanchor="center", yanchor="bottom"
      )]

py.iplot(fig, fileopt='overwrite', filename='Logos/Florida_Rainfall_AccuWeather')
```

```python
import plotly.plotly as py

import plotly.plotly as py
import plotly.graph_objs as go

fig = py.get_figure('https://plot.ly/~Dreamshot/8160/', raw=True)
for j in range(len(fig['data'])):
    del fig['data'][j]['autobinx']
    del fig['data'][j]['autobiny']
fig = go.Figure(fig)

fig.layout.images = [dict(
        source="https://raw.githubusercontent.com/cldougl/plot_images/add_r_img/bleacherreport.png",
        xref="paper", yref="paper",
        x=0.5, y=-0.35,
        sizex=0.3, sizey=0.3,
        xanchor="center", yanchor="top"
      )]

py.iplot(fig, fileopt='overwrite', filename='Logos/Top_Earners_BleacherReport')
```

```python
import plotly.plotly as py

fig = py.get_figure('https://plot.ly/~Dreamshot/8158/')

fig.layout.images = [dict(
        source="https://raw.githubusercontent.com/cldougl/plot_images/add_r_img/theverge.png",
        xref="paper", yref="paper",
        x=0.1, y=1.0,
        sizex=0.2, sizey=0.3,
        xanchor="center", yanchor="bottom"
      )]

fig.layout.legend.orientation = 'h'

py.iplot(fig, fileopt='overwrite', filename='Logos/Apple_Labor_Violations_TheVerge')
```

```python
import plotly.plotly as py

fig = py.get_figure('https://plot.ly/~Dreamshot/8155/')

fig.layout.images = [dict(
        source="https://raw.githubusercontent.com/cldougl/plot_images/add_r_img/politico.png",
        xref="paper", yref="paper",
        x=0.1, y=-0.2,
        sizex=0.4, sizey=0.4,
        xanchor="center", yanchor="bottom"
      )]

py.iplot(fig, fileopt='overwrite', filename='Logos/Foreign_Policy_Politico')
```

#### Reference
See https://plot.ly/python/images/ for more examples of adding images<br>
and https://plot.ly/python/reference/#layout-images for more information and chart attribute options!

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'logos.ipynb', 'python/logos/', 'Add Logos to Charts',
    'How to add images as logos to Plotly charts.',
    title = 'Add Logos to Charts | plotly',
    name = 'Logos',
    has_thumbnail='false', thumbnail='thumbnail/your-tutorial-chart.jpg',
    language='python', page_type='example_index',
    display_as='style_opt', order=6,
    ipynb= '~notebook_demo/92')
```

```python

```
