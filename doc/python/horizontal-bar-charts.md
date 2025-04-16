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
        color='rgba(246, 78, 139, 0.6)',
        line=dict(color='rgba(246, 78, 139, 1.0)', width=3)
    )
))
fig.add_trace(go.Bar(
    y=['giraffes', 'orangutans', 'monkeys'],
    x=[12, 18, 29],
    name='LA Zoo',
    orientation='h',
    marker=dict(
        color='rgba(58, 71, 80, 0.6)',
        line=dict(color='rgba(58, 71, 80, 1.0)', width=3)
    )
))

fig.update_layout(barmode='stack')
fig.show()
```

### Color Palette for Bar Chart

```python
import plotly.graph_objects as go

top_labels = ['Strongly<br>agree', 'Agree', 'Neutral', 'Disagree',
              'Strongly<br>disagree']

colors = ['rgba(38, 24, 74, 0.8)', 'rgba(71, 58, 131, 0.8)',
          'rgba(122, 120, 168, 0.8)', 'rgba(164, 163, 204, 0.85)',
          'rgba(190, 192, 213, 1)']

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
                line=dict(color='rgb(248, 248, 249)', width=1)
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
    paper_bgcolor='rgb(248, 248, 255)',
    plot_bgcolor='rgb(248, 248, 255)',
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
                                      color='rgb(67, 67, 67)'),
                            showarrow=False, align='right'))
    # labeling the first percentage of each bar (x_axis)
    annotations.append(dict(xref='x', yref='y',
                            x=xd[0] / 2, y=yd,
                            text=str(xd[0]) + '%',
                            font=dict(family='Arial', size=14,
                                      color='rgb(248, 248, 255)'),
                            showarrow=False))
    # labeling the first Likert scale (on the top)
    if yd == y_data[-1]:
        annotations.append(dict(xref='x', yref='paper',
                                x=xd[0] / 2, y=1.1,
                                text=top_labels[0],
                                font=dict(family='Arial', size=14,
                                          color='rgb(67, 67, 67)'),
                                showarrow=False))
    space = xd[0]
    for i in range(1, len(xd)):
            # labeling the rest of percentages for each bar (x_axis)
            annotations.append(dict(xref='x', yref='y',
                                    x=space + (xd[i]/2), y=yd,
                                    text=str(xd[i]) + '%',
                                    font=dict(family='Arial', size=14,
                                              color='rgb(248, 248, 255)'),
                                    showarrow=False))
            # labeling the Likert scale
            if yd == y_data[-1]:
                annotations.append(dict(xref='x', yref='paper',
                                        x=space + (xd[i]/2), y=1.1,
                                        text=top_labels[i],
                                        font=dict(family='Arial', size=14,
                                                  color='rgb(67, 67, 67)'),
                                        showarrow=False))
            space += xd[i]

fig.update_layout(annotations=annotations)

fig.show()
```
### Diverging Bar (or Butterfly) Chart with Neutral Column

Diverging bar charts offer two imperfect options for responses that are neither positive nor negative:  put them in a separate column, as in this example or omit them as in the example above.  That leaves the unreported neutral value implicit when the categories add to 100%,   Jonathan Schwabish discusses this on page 92-97 of  _Better Data Visualizations_.

```python
import pandas as pd
import plotly.graph_objects as go


df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/refs/heads/master/gss_2002_5_pt_likert.csv')
df.rename(columns={'Unnamed: 0':"Category"}, inplace=True)


#achieve the diverging effect by putting a negative sign on the "disagree" answers 
for v in ["Disagree","Strongly Disagree"]:
    df[v]=df[v]*-1

fig = go.Figure(layout=go.Layout(
    title="Reactions to statements from the 2002 General Social Survey:",
    plot_bgcolor="white",
    barmode='relative',  # Allows bars to diverge from the center
    # Put the legend at the bottom center of the figure
    legend=dict(
        orientation="h",  # a horizontal legend matches the horizontal bars
        yref="container",
        yanchor="bottom",
        y=0.02,
        xanchor="center",
        x=0.5),
    # use an unlabeled Y axis, since we're going to list specific questions on the y-axis.
    yaxis=dict(
        title=""  
    ),
    )
)


# this color palette conveys meaning:  blues for agreement, reds and oranges for disagreement, gray for Neither Agree nor Disagree
color_by_category={
    "Strongly Agree":'darkblue',
    "Agree":'lightblue',
    "Disagree":'orange',
    "Strongly Disagree":'red',
    "Neither Agree nor Disagree":'gray',
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
    "Neither Agree nor Disagree":5
}

# Add bars
for col in ["Disagree","Strongly Disagree","Agree","Strongly Agree","Neither Agree nor Disagree"]:
    fig.add_trace(go.Bar(
        y=df["Category"],
        x=df[col],
        name=col,
        orientation='h',
        marker=dict(color=color_by_category[col]),
        legendrank=legend_rank_by_category[col],
        xaxis=f"x{1+(col=='Neither Agree nor Disagree')}", # in this context, putting "Neither Agree nor Disagree" on a secondary x-axis on a different domain 
                       # yields results equivalent to subplots with far less code
    )
)

# make calculations to split the plot into two columns with a shared x axis scale
# by setting the domain and range of the x axes appropriately

# Find the maximum width of the bars to the left and right sides of the origin; remember that the width of 
# the plot is the sum of the longest negative bar and the longest positive bar even if they are on separate rows
max_left = min(df[["Disagree","Strongly Disagree"]].sum(axis=1))
max_right = max(df[["Agree","Strongly Agree"]].sum(axis=1))

# we are working in percent, but coded the negative reactions as negative numbers; so we need to take the absolute value
max_width_signed = abs(max_left)+max_right
max_width_neither = max(df["Neither Agree nor Disagree"])

fig.update_xaxes(
        zeroline=True, #the zero line distinguishes between positive and negative segments
        zerolinecolor="black",
        #starting here, we set domain and range to create a shared x-axis scale
        # multiply by .98 to add space between the two columns
        range=[max_left, max_right],  
        domain=[0, 0.98*(max_width_signed/(max_width_signed+max_width_neither))]  
)
    
fig.update_layout(
    xaxis2=dict(
        range=[0, max_width_neither],  
        domain=[(1-.98*(1-max_width_signed/(max_width_signed+max_width_neither))), 1.0],
    )
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

fig.append_trace(go.Bar(
    x=y_saving,
    y=x,
    marker=dict(
        color='rgba(50, 171, 96, 0.6)',
        line=dict(
            color='rgba(50, 171, 96, 1.0)',
            width=1),
    ),
    name='Household savings, percentage of household disposable income',
    orientation='h',
), 1, 1)

fig.append_trace(go.Scatter(
    x=y_net_worth, y=x,
    mode='lines+markers',
    line_color='rgb(128, 0, 128)',
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
        linecolor='rgba(102, 102, 102, 0.8)',
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
    paper_bgcolor='rgb(248, 248, 255)',
    plot_bgcolor='rgb(248, 248, 255)',
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
                                      color='rgb(128, 0, 128)'),
                            showarrow=False))
    # labeling the bar net worth
    annotations.append(dict(xref='x1', yref='y1',
                            y=xd, x=yd + 3,
                            text=str(yd) + '%',
                            font=dict(family='Arial', size=12,
                                      color='rgb(50, 171, 96)'),
                            showarrow=False))
# Source
annotations.append(dict(xref='paper', yref='paper',
                        x=-0.2, y=-0.109,
                        text='OECD "' +
                             '(2015), Household savings (indicator), ' +
                             'Household net worth (indicator). doi: ' +
                             '10.1787/cfc6f499-en (Accessed on 05 June 2015)',
                        font=dict(family='Arial', size=10, color='rgb(150,150,150)'),
                        showarrow=False))

fig.update_layout(annotations=annotations)

fig.show()
```

### Reference

See more examples of bar charts and styling options [here](https://plotly.com/python/bar-charts/).<br> See https://plotly.com/python/reference/bar/ for more information and chart attribute options!
