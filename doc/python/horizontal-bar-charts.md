---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.16.4
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
    version: 3.11.10
  plotly:
    description: How to make horizontal bar charts in Python with Plotly.
    display_as: basic
    language: python
    layout: base
    name: Horizontal Bar Charts
    order: 8
    page_type: u-guide
    permalink: python/horizontal-bar-charts/
    thumbnail: thumbnail/horizontal-bar.jpg
---

See more examples of bar charts (including vertical bar charts) and styling options [here](https://plotly.com/python/bar-charts/).

### Horizontal Bar Chart with Plotly Express

[Plotly Express](/python/plotly-express/) is the easy-to-use, high-level interface to Plotly, which [operates on a variety of types of data](/python/px-arguments/) and produces [easy-to-style figures](/python/styling-plotly-express/). For a horizontal bar char, use the `px.bar` function with `orientation='h'`.

#### Basic Horizontal Bar Chart with Plotly Express

```python
import plotly.express as px
df = px.data.tips()
fig = px.bar(df, x="total_bill", y="day", orientation='h')
fig.show()
```

#### Configure horizontal bar chart

In this example a column is used to color the bars, and we add the information from other columns to the hover data.

```python
import plotly.express as px
df = px.data.tips()
fig = px.bar(df, x="total_bill", y="sex", color='day', orientation='h',
             hover_data=["tip", "size"],
             height=400,
             title='Restaurant bills')
fig.show()
```

### Horizontal Bar Chart with go.Bar

You can also use [the more generic `go.Bar` class from `plotly.graph_objects`](/python/graph-objects/). All the options of `go.Bar` are documented in the reference https://plotly.com/python/reference/bar/

#### Basic Horizontal Bar Chart

```python
import plotly.graph_objects as go

fig = go.Figure(go.Bar(
            x=[20, 14, 23],
            y=['giraffes', 'orangutans', 'monkeys'],
            orientation='h'))

fig.show()
```

### Colored Horizontal Bar Chart

```python
import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Bar(
    y=['giraffes', 'orangutans', 'monkeys'],
    x=[20, 14, 23],
    name='SF Zoo',
    orientation='h',
    marker=dict(
        color='hotpink',
        line=dict(color='deeppink', width=3)
    )
))
fig.add_trace(go.Bar(
    y=['giraffes', 'orangutans', 'monkeys'],
    x=[12, 18, 29],
    name='LA Zoo',
    orientation='h',
    marker=dict(
        color='dimgray',
        line=dict(color='black', width=3)
    )
))

fig.update_layout(barmode='stack')
fig.show()
```
### Small multiple horizontal bar charts show each component's size more clearly than a stacked bar

Bar charts with multiple components pose a fundamental trade off between presenting the total clearly and presenting the component values clearly. This small multiples approach shows the component magnitudes clearly at the cost of slightly obscuring the totals. A stacked bar does the opposite. Small multiple bar charts often work better in a horizontal orientation; and are easy to create with the px.bar orientation and facet_col parameters.
```python
import pandas as pd
import plotly.express as px

data = {
    "Quarter": ["Q1", "Q2", "Q3", "Q4"] * 3,
    "Region": ["North", "North", "North", "North", "South", "South", "South", "South", "West", "West", "West", "West"],
    "Outcome": [150, 200, 250, 300, 120, 180, 240, 310, 100, 150, 220, 280]
}
df = pd.DataFrame(data)


fig = px.bar(
    df, 
    x="Outcome", 
    y="Region",
    orientation="h",  
    facet_col="Quarter", 
    title="Number of Patients Served by Region and Quarter", 
    labels={"Outcome": "Patients Served", "Region": "Region"} 
)

## the section below is optional clean up to make this presentation ready

fig.update_layout(
    height=400,  #the Plotly default makes the bars awkwardly large; setting a height improves the display
    showlegend=False,  # the legend does not add anything
)

# remove the default "facet_variable =" text from the title of each facet graph
fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))  

# Remove duplicate axis labels
fig.for_each_yaxis(lambda axis: axis.update(title=None))
fig.for_each_xaxis(lambda axis: axis.update(title=None))
# add the one valuable axis label back in
fig.update_xaxes(title="Count", row=1, col=1)

fig.show()
```

### Color Palette for Bar Chart

This bar chart uses a sequential palette to show gradations of responses.  Additional color options for sequential palettes are available at [The Urban Institute](https://urbaninstitute.github.io/graphics-styleguide/#color) and [Colorbrewer](https://colorbrewer2.org/#type=sequential)

```python
import plotly.graph_objects as go

top_labels = ['Strongly<br>agree', 'Agree', 'Neutral', 'Disagree',
              'Strongly<br>disagree']

colors = ['DarkBlue', 'MediumBlue', 'DarkSlateBlue', 'mediumpurple', 'thistle']
x_data = [[21, 30, 21, 16, 12],
          [24, 31, 19, 15, 11],
          [27, 26, 23, 11, 13],
          [29, 24, 15, 18, 14]]

y_data = ['The course was effectively<br>organized',
          'The course developed my<br>abilities and skills ' +
          'for<br>the subject', 'The course developed ' +
          'my<br>ability to think critically about<br>the subject',
          'I would recommend this<br>course to a friend']

fig = go.Figure()

for i in range(0, len(x_data[0])):
    for xd, yd in zip(x_data, y_data):
        fig.add_trace(go.Bar(
            x=[xd[i]], y=[yd],
            orientation='h',
            marker=dict(
                color=colors[i],
                line=dict(color='ghostwhite', width=1)
            )
        ))

fig.update_layout(
    xaxis=dict(
        showgrid=False,
        showline=False,
        showticklabels=False,
        zeroline=False,
        domain=[0.15, 1]
    ),
    yaxis=dict(
        showgrid=False,
        showline=False,
        showticklabels=False,
        zeroline=False,
    ),
    barmode='stack',
    paper_bgcolor='lavenderblush',
    plot_bgcolor='lavenderblush',
    margin=dict(l=120, r=10, t=140, b=80),
    showlegend=False,
)

annotations = []

for yd, xd in zip(y_data, x_data):
    # labeling the y-axis
    annotations.append(dict(xref='paper', yref='y',
                            x=0.14, y=yd,
                            xanchor='right',
                            text=str(yd),
                            font=dict(family='Arial', size=14,
                                      color='dimgray'),
                            showarrow=False, align='right'))
    # labeling the first percentage of each bar (x_axis)
    annotations.append(dict(xref='x', yref='y',
                            x=xd[0] / 2, y=yd,
                            text=str(xd[0]) + '%',
                            font=dict(family='Arial', size=14,
                                      color='white'),
                            showarrow=False))
    # labeling the first Likert scale (on the top)
    if yd == y_data[-1]:
        annotations.append(dict(xref='x', yref='paper',
                                x=xd[0] / 2, y=1.1,
                                text=top_labels[0],
                                font=dict(family='Arial', size=14,
                                          color='dimgray'),
                                showarrow=False))
    space = xd[0]
    for i in range(1, len(xd)):
            # labeling the rest of percentages for each bar (x_axis)
            annotations.append(dict(xref='x', yref='y',
                                    x=space + (xd[i]/2), y=yd,
                                    text=str(xd[i]) + '%',
                                    font=dict(family='Arial', size=14,
                                              color='ghostwhite'),
                                    showarrow=False))
            # labeling the Likert scale
            if yd == y_data[-1]:
                annotations.append(dict(xref='x', yref='paper',
                                        x=space + (xd[i]/2), y=1.1,
                                        text=top_labels[i],
                                        font=dict(family='Arial', size=14,
                                                  color='dimgray'),
                                        showarrow=False))
            space += xd[i]

fig.update_layout(annotations=annotations)

fig.show()
```

### Diverging Bar (or Butterfly) Chart

Diverging bar charts show counts of positive outcomes or sentiments to the right of zero and counts of negative outcomes to the left of zero, allowing the reader to easily spot areas of excellence and concern.  This example allows the reader of the graph to infer the number of people offering a neutral response because the neutral category, which is left implicit, would make the responses add to 100%.

```python
import plotly.graph_objects as go
import pandas as pd


df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/refs/heads/master/gss_2002_5_pt_likert.csv')

df.rename(columns={'Unnamed: 0':"Category"}, inplace=True)

#achieve the diverging effect by putting a negative sign on the "disagree" answers 
for v in ["Disagree","Strongly Disagree"]:
    df[v]=df[v]*-1

fig = go.Figure()
# this color palette conveys meaning:  blues for positive, red and orange for negative
color_by_category={
    "Strongly Agree":'darkblue',
    "Agree":'lightblue',
    "Disagree":'orange',
    "Strongly Disagree":'red',
}


# We want the legend to be ordered in the same order that the categories appear, left to right --
# which is different from the order in which we have to add the traces to the figure.
# since we need to create the "somewhat" traces before the "strongly" traces to display
# the segments in the desired order
legend_rank_by_category={
    "Strongly Disagree":1,
    "Disagree":2,
    "Agree":3,
    "Strongly Agree":4,
}
# Add bars for each category
for col in ["Disagree","Strongly Disagree","Agree","Strongly Agree"]:
    fig.add_trace(go.Bar(
        y=df["Category"], 
        x=df[col], 
        name=col, 
        orientation='h',
        marker=dict(color=color_by_category[col]),
        legendrank=legend_rank_by_category[col]
    ))

fig.update_layout(
   title="Reactions to statements from the 2002 General Social Survey:",
    yaxis_title = "",
    barmode='relative',  # Allows bars to diverge from the center
    plot_bgcolor="white",
)

fig.update_xaxes(
        title="Percent of Responses",
        zeroline=True,  # Ensure there's a zero line for divergence
        zerolinecolor="black",
        # use array tick mode to show that the counts to the left of zero are still positive.
        # this is hard coded; generalize this if you plan to create a function that takes unknown or widely varying data
        tickmode = 'array',     
        tickvals = [-50, 0, 50, 100],
        ticktext = [50, 0, 50, 100]
)

fig.show()

```

### Bar Chart with Line Plot

```python
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import numpy as np

y_saving = [1.3586, 2.2623000000000002, 4.9821999999999997, 6.5096999999999996,
            7.4812000000000003, 7.5133000000000001, 15.2148, 17.520499999999998
            ]
y_net_worth = [93453.919999999998, 81666.570000000007, 69889.619999999995,
               78381.529999999999, 141395.29999999999, 92969.020000000004,
               66090.179999999993, 122379.3]
x = ['Japan', 'United Kingdom', 'Canada', 'Netherlands',
     'United States', 'Belgium', 'Sweden', 'Switzerland']


# Creating two subplots
fig = make_subplots(rows=1, cols=2, specs=[[{}, {}]], shared_xaxes=True,
                    shared_yaxes=False, vertical_spacing=0.001)

fig.add_trace(go.Bar(
    x=y_saving,
    y=x,
    marker=dict(
        color='mediumseagreen',
        line=dict(
            color='seagreen',
            width=1),
    ),
    name='Household savings, percentage of household disposable income',
    orientation='h',
), 1, 1)

fig.add_trace(go.Scatter(
    x=y_net_worth, y=x,
    mode='lines+markers',
    line_color='purple',
    name='Household net worth, Million USD/capita',
), 1, 2)

fig.update_layout(
    title=dict(text='Household savings & net worth for eight OECD countries'),
    yaxis=dict(
        showgrid=False,
        showline=False,
        showticklabels=True,
        domain=[0, 0.85],
    ),
    yaxis2=dict(
        showgrid=False,
        showline=True,
        showticklabels=False,
        linecolor='gray',
        linewidth=2,
        domain=[0, 0.85],
    ),
    xaxis=dict(
        zeroline=False,
        showline=False,
        showticklabels=True,
        showgrid=True,
        domain=[0, 0.42],
    ),
    xaxis2=dict(
        zeroline=False,
        showline=False,
        showticklabels=True,
        showgrid=True,
        domain=[0.47, 1],
        side='top',
        dtick=25000,
    ),
    legend=dict(x=0.029, y=1.038, font_size=10),
    margin=dict(l=100, r=20, t=70, b=70),
    paper_bgcolor='lavenderblush',
    plot_bgcolor='lavenderblush',
)

annotations = []

y_s = np.round(y_saving, decimals=2)
y_nw = np.rint(y_net_worth)

# Adding labels
for ydn, yd, xd in zip(y_nw, y_s, x):
    # labeling the scatter savings
    annotations.append(dict(xref='x2', yref='y2',
                            y=xd, x=ydn - 20000,
                            text='{:,}'.format(ydn) + 'M',
                            font=dict(family='Arial', size=12,
                                      color='purple'),
                            showarrow=False))
    # labeling the bar net worth
    annotations.append(dict(xref='x1', yref='y1',
                            y=xd, x=yd + 3,
                            text=str(yd) + '%',
                            font=dict(family='Arial', size=16,
                                      color='mediumseagreen'),
                            showarrow=False))
# Source
annotations.append(dict(xref='paper', yref='paper',
                        x=-0.2, y=-0.109,
                        text='OECD "' +
                             '(2015), Household savings (indicator), ' +
                             'Household net worth (indicator). doi: ' +
                             '10.1787/cfc6f499-en (Accessed on 05 June 2015)',
                        font=dict(family='Arial', size=10, color='gray'),
                        showarrow=False))

fig.update_layout(annotations=annotations)

fig.show()
```

### Reference

See more examples of bar charts and styling options [here](https://plotly.com/python/bar-charts/).<br> See https://plotly.com/python/reference/bar/ for more information and chart attribute options!
