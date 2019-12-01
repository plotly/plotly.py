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
    description: How to make 3D Filled Line Plots in Python
    display_as: 3d_charts
    language: python
    layout: base
    name: 3D Filled Line Plots
    order: 5
    permalink: python/3d-filled-line-plots/
    thumbnail: thumbnail/3d-filled-line-plot.jpg
---

<!-- #region {"deletable": true, "editable": true} -->
#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!
<!-- #endregion -->

<!-- #region {"deletable": true, "editable": true} -->
#### Basic Filled Line Plot
<!-- #endregion -->

```python deletable=true editable=true
import plotly.plotly as py
import pandas as pd

# The datasets' url. Thanks Jennifer Bryan!
url_csv = 'http://www.stat.ubc.ca/~jenny/notOcto/STAT545A/examples/gapminder/data/gapminderDataFiveYear.txt'

df = pd.read_csv(url_csv, sep='\t')
df.head()

countries = ['China', 'India', 'United States', 'Bangladesh', 'South Africa']
fill_colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854']
gf = df.groupby('country')

data = []

for country, fill_color in zip(countries[::-1], fill_colors):
    group = gf.get_group(country)
    years = group['year'].tolist()
    length = len(years)
    country_coords = [country] * length
    pop = group['pop'].tolist()
    zeros = [0] * length

    data.append(dict(
        type='scatter3d',
        mode='lines',
        x=years + years[::-1] + [years[0]],  # year loop: in incr. order then in decr. order then years[0]
        y=country_coords * 2 + [country_coords[0]],
        z=pop + zeros + [pop[0]],
        name='',
        surfaceaxis=1, # add a surface axis ('1' refers to axes[1] i.e. the y-axis)
        surfacecolor=fill_color,
        line=dict(
            color='black',
            width=4
        ),
    ))

layout = dict(
    title='Population from 1957 to 2007 [Gapminder]',
    showlegend=False,
    scene=dict(
        xaxis=dict(title=''),
        yaxis=dict(title=''),
        zaxis=dict(title=''),
        camera=dict(
            eye=dict(x=-1.7, y=-1.7, z=0.5)
        )
    )
)

fig = dict(data=data, layout=layout)

# IPython notebook
# py.iplot(fig, filename='filled-3d-lines')

py.iplot(fig, filename='filled-3d-lines')
```

<!-- #region {"deletable": true, "editable": true} -->
#### Reference
<!-- #endregion -->

<!-- #region {"deletable": true, "editable": true} -->
See https://plot.ly/python/reference/ for more information!
<!-- #endregion -->

```python deletable=true editable=true
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade

import publisher
publisher.publish(
    '3d-filled-line.ipynb', 'python/3d-filled-line-plots/', '3D Filled Line Plots in Python | plotly',
    'How to make 3D Filled Line Plots in Python',
    title = '3D Filled Line Plots in Python | plotly',
    name = '3D Filled Line Plots',
    has_thumbnail='true', thumbnail='thumbnail/3d-filled-line-plot.jpg',
    language='python',
    display_as='3d_charts', order=5,
    ipynb= '~notebook_demo/65')
```

```python deletable=true editable=true

```
