---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.13.7
  kernelspec:
    display_name: Python 3 (ipykernel)
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
    version: 3.9.0
  plotly:
    description: How to make violin plots in Python with Plotly.
    display_as: statistical
    language: python
    layout: base
    name: Violin Plots
    order: 10
    page_type: u-guide
    permalink: python/violin/
    redirect_from:
    - /python/violin-plot/
    - /python/violin-plots/
    thumbnail: thumbnail/violin.jpg
---

<!-- #region -->
## Violin Plot with Plotly Express

A [violin plot](https://en.wikipedia.org/wiki/Violin_plot) is a statistical representation of numerical data. It is similar to a [box plot](https://plotly.com/python/box-plots/), with the addition of a rotated [kernel density](https://en.wikipedia.org/wiki/Kernel_density_estimation) plot on each side.

Alternatives to violin plots for visualizing distributions include [histograms](https://plotly.com/python/histograms/), [box plots](https://plotly.com/python/box-plots/), [ECDF plots](https://plotly.com/python/ecdf-plots/) and [strip charts](https://plotly.com/python/strip-charts/).


### Basic Violin Plot with Plotly Express

[Plotly Express](../plotly-express/) is the easy-to-use, high-level interface to Plotly, which [operates on a variety of types of data](../px-arguments/) and produces [easy-to-style figures](../styling-plotly-express/).
<!-- #endregion -->

```python
import plotly.express as px

df = px.data.tips()
fig = px.violin(df, y="total_bill")
fig.show()
```

### Violin plot with box and data points

```python
import plotly.express as px

df = px.data.tips()
fig = px.violin(df, y="total_bill", box=True, # draw box plot inside the violin
                points='all', # can be 'outliers', or False
               )
fig.show()
```

### Multiple Violin Plots

```python
import plotly.express as px

df = px.data.tips()
fig = px.violin(df, y="tip", x="smoker", color="sex", box=True, points="all",
          hover_data=df.columns)
fig.show()
```

```python
import plotly.express as px

df = px.data.tips()
fig = px.violin(df, y="tip", color="sex",
                violinmode='overlay', # draw violins on top of each other
                # default violinmode is 'group' as in example above
                hover_data=df.columns)
fig.show()
```

## Violin Plot with go.Violin

If Plotly Express does not provide a good starting point, you can use [the more generic `go.Violin` class from `plotly.graph_objects`](../graph-objects/). All the options of `go.Violin` are documented in the reference https://plotly.com/python/reference/violin/

#### Basic Violin Plot

```python
import plotly.graph_objects as go

import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/violin_data.csv")

fig = go.Figure(data=go.Violin(y=df['total_bill'], box_visible=True, line_color='black',
                               meanline_visible=True, fillcolor='lightseagreen', opacity=0.6,
                               x0='Total Bill'))

fig.update_layout(yaxis_zeroline=False)
fig.show()
```

#### Multiple Traces

```python
import plotly.graph_objects as go

import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/violin_data.csv")

fig = go.Figure()

days = ['Thur', 'Fri', 'Sat', 'Sun']

for day in days:
    fig.add_trace(go.Violin(x=df['day'][df['day'] == day],
                            y=df['total_bill'][df['day'] == day],
                            name=day,
                            box_visible=True,
                            meanline_visible=True))

fig.show()
```

#### Grouped Violin Plot

```python
import plotly.graph_objects as go

import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/violin_data.csv")

fig = go.Figure()

fig.add_trace(go.Violin(x=df['day'][ df['sex'] == 'Male' ],
                        y=df['total_bill'][ df['sex'] == 'Male' ],
                        legendgroup='M', scalegroup='M', name='M',
                        line_color='blue')
             )
fig.add_trace(go.Violin(x=df['day'][ df['sex'] == 'Female' ],
                        y=df['total_bill'][ df['sex'] == 'Female' ],
                        legendgroup='F', scalegroup='F', name='F',
                        line_color='orange')
             )

fig.update_traces(box_visible=True, meanline_visible=True)
fig.update_layout(violinmode='group')
fig.show()
```

#### Split Violin Plot

```python
import plotly.graph_objects as go

import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/violin_data.csv")

fig = go.Figure()

fig.add_trace(go.Violin(x=df['day'][ df['smoker'] == 'Yes' ],
                        y=df['total_bill'][ df['smoker'] == 'Yes' ],
                        legendgroup='Yes', scalegroup='Yes', name='Yes',
                        side='negative',
                        line_color='blue')
             )
fig.add_trace(go.Violin(x=df['day'][ df['smoker'] == 'No' ],
                        y=df['total_bill'][ df['smoker'] == 'No' ],
                        legendgroup='No', scalegroup='No', name='No',
                        side='positive',
                        line_color='orange')
             )
fig.update_traces(meanline_visible=True)
fig.update_layout(violingap=0, violinmode='overlay')
fig.show()
```

#### Advanced Violin Plot

```python
import plotly.graph_objects as go

import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/violin_data.csv")

pointpos_male = [-0.9,-1.1,-0.6,-0.3]
pointpos_female = [0.45,0.55,1,0.4]
show_legend = [True,False,False,False]

fig = go.Figure()

for i in range(0,len(pd.unique(df['day']))):
    fig.add_trace(go.Violin(x=df['day'][(df['sex'] == 'Male') &
                                        (df['day'] == pd.unique(df['day'])[i])],
                            y=df['total_bill'][(df['sex'] == 'Male')&
                                               (df['day'] == pd.unique(df['day'])[i])],
                            legendgroup='M', scalegroup='M', name='M',
                            side='negative',
                            pointpos=pointpos_male[i], # where to position points
                            line_color='lightseagreen',
                            showlegend=show_legend[i])
             )
    fig.add_trace(go.Violin(x=df['day'][(df['sex'] == 'Female') &
                                        (df['day'] == pd.unique(df['day'])[i])],
                            y=df['total_bill'][(df['sex'] == 'Female')&
                                               (df['day'] == pd.unique(df['day'])[i])],
                            legendgroup='F', scalegroup='F', name='F',
                            side='positive',
                            pointpos=pointpos_female[i],
                            line_color='mediumpurple',
                            showlegend=show_legend[i])
             )

# update characteristics shared by all traces
fig.update_traces(meanline_visible=True,
                  points='all', # show all points
                  jitter=0.05,  # add some jitter on points for better visibility
                  scalemode='count') #scale violin plot area with total count
fig.update_layout(
    title_text="Total bill distribution<br><i>scaled by number of bills per gender",
    violingap=0, violingroupgap=0, violinmode='overlay')
fig.show()
```

#### Ridgeline plot

A ridgeline plot ([previously known as Joy Plot](https://serialmentor.com/blog/2017/9/15/goodbye-joyplots)) shows the distribution of a numerical value for several groups. They can be used for visualizing changes in distributions over time or space.

```python
import plotly.graph_objects as go
from plotly.colors import n_colors
import numpy as np
np.random.seed(1)

# 12 sets of normal distributed random data, with increasing mean and standard deviation
data = (np.linspace(1, 2, 12)[:, np.newaxis] * np.random.randn(12, 200) +
            (np.arange(12) + 2 * np.random.random(12))[:, np.newaxis])

colors = n_colors('rgb(5, 200, 200)', 'rgb(200, 10, 10)', 12, colortype='rgb')

fig = go.Figure()
for data_line, color in zip(data, colors):
    fig.add_trace(go.Violin(x=data_line, line_color=color))

fig.update_traces(orientation='h', side='positive', width=3, points=False)
fig.update_layout(xaxis_showgrid=False, xaxis_zeroline=False)
fig.show()
```

### Violin Plot With Only Points

A [strip chart](../strip-charts/) is like a violin plot with points showing, and no violin:

```python
import plotly.express as px
df = px.data.tips()
fig = px.strip(df, x='day', y='tip')
fig.show()
```

### Choosing The Algorithm For Computing Quartiles

*New in 5.10*

By default, quartiles for violin plots are computed using the `linear` method (for more about linear interpolation, see #10 listed on [http://jse.amstat.org/v14n3/langford.html](http://jse.amstat.org/v14n3/langford.html) and [https://en.wikipedia.org/wiki/Quartile](https://en.wikipedia.org/wiki/Quartile) for more details).

However, you can also choose to use an `exclusive` or an `inclusive` algorithm to compute quartiles.

The _exclusive_ algorithm uses the median to divide the ordered dataset into two halves. If the sample is odd, it does not include the median in either half. Q1 is then the median of the lower half and Q3 is the median of the upper half.

The _inclusive_ algorithm also uses the median to divide the ordered dataset into two halves, but if the sample is odd, it includes the median in both halves. Q1 is then the median of the lower half and Q3 the median of the upper half.

```python
import plotly.express as px

df = px.data.tips()
fig = px.violin(df, y="total_bill")
fig.update_traces(quartilemethod="exclusive") # or "inclusive", or "linear" by default

fig.show()
```

#### Reference

See [function reference for `px.violin()`](https://plotly.com/python-api-reference/generated/plotly.express.violin) or https://plotly.com/python/reference/violin/ for more information and chart attribute options!
