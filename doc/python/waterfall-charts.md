---
description: How to make waterfall plots in Python with Plotly.
---
### Simple Waterfall Chart

```python
import plotly.graph_objects as go

fig = go.Figure(go.Waterfall(
    name = "20", orientation = "v",
    measure = ["relative", "relative", "total", "relative", "relative", "total"],
    x = ["Sales", "Consulting", "Net revenue", "Purchases", "Other expenses", "Profit before tax"],
    textposition = "outside",
    text = ["+60", "+80", "", "-40", "-20", "Total"],
    y = [60, 80, 0, -40, -20, 0],
    connector = {"line":{"color":"rgb(63, 63, 63)"}},
))

fig.update_layout(
        title = "Profit and loss statement 2018",
        showlegend = True
)

fig.show()
```

### Multi Category Waterfall Chart
This example uses the [waterfallgroupgap attribute](reference/graph_objects/Layout.md#plotly.graph_objects.Layout.waterfallgroupgap), which sets a gap between bars.

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Waterfall(
    x = [["2016", "2017", "2017", "2017", "2017", "2018", "2018", "2018", "2018"],
        ["initial", "q1", "q2", "q3", "total", "q1", "q2", "q3", "total"]],
    measure = ["absolute", "relative", "relative", "relative", "total", "relative", "relative", "relative", "total"],
    y = [1, 2, 3, -1, None, 1, 2, -4, None],
    base = 1000
))

fig.add_trace(go.Waterfall(
    x = [["2016", "2017", "2017", "2017", "2017", "2018", "2018", "2018", "2018"],
        ["initial", "q1", "q2", "q3", "total", "q1", "q2", "q3", "total"]],
    measure = ["absolute", "relative", "relative", "relative", "total", "relative", "relative", "relative", "total"],
    y = [1.1, 2.2, 3.3, -1.1, None, 1.1, 2.2, -4.4, None],
    base = 1000
))

fig.update_layout(
    waterfallgroupgap = 0.5,
)

fig.show()
```

### Setting Marker Size and Color
This example uses [decreasing](reference/graph_objects/Waterfall.md#plotly.graph_objects.Waterfall.decreasing), [increasing](reference/graph_objects/Waterfall.md#plotly.graph_objects.Waterfall.increasing), and [totals](reference/graph_objects/Waterfall.md#plotly.graph_objects.Waterfall.totals) attributes to customize the bars.

```python
import plotly.graph_objects as go

fig = go.Figure(go.Waterfall(
    x = [["2016", "2017", "2017", "2017", "2017", "2018", "2018", "2018", "2018"],
       ["initial", "q1", "q2", "q3", "total", "q1", "q2", "q3", "total"]],
    measure = ["absolute", "relative", "relative", "relative", "total", "relative", "relative", "relative", "total"],
    y = [10, 20, 30, -10, None, 10, 20, -40, None], base = 300,
    decreasing = {"marker":{"color":"Maroon", "line":{"color":"red", "width":2}}},
    increasing = {"marker":{"color":"Teal"}},
    totals = {"marker":{"color":"deep sky blue", "line":{"color":"blue", "width":3}}}
))

fig.update_layout(title = "Profit and loss statement", waterfallgap = 0.3)

fig.show()
```

### Horizontal Waterfall Chart

```python
import plotly.graph_objects as go

fig = go.Figure(go.Waterfall(
    name = "2018", orientation = "h", measure = ["relative", "relative", "relative", "relative", "total", "relative",
                                              "relative", "relative", "relative", "total", "relative", "relative", "total", "relative", "total"],
    y = ["Sales", "Consulting", "Maintenance", "Other revenue", "Net revenue", "Purchases", "Material expenses",
       "Personnel expenses", "Other expenses", "Operating profit", "Investment income", "Financial income",
       "Profit before tax", "Income tax (15%)", "Profit after tax"],
    x = [375, 128, 78, 27, None, -327, -12, -78, -12, None, 32, 89, None, -45, None],
    connector = {"mode":"between", "line":{"width":4, "color":"rgb(0, 0, 0)", "dash":"solid"}}
))

fig.update_layout(title = "Profit and loss statement 2018")

fig.show()
```

#### Reference
See [https://plotly.com/python/reference/waterfall/](reference/graph_objects/Waterfall.md) for more information and chart attribute options!
