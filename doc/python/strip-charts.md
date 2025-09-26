---
description: Strip charts are like 1-dimensional jittered scatter plots.
---
### Strip Charts with Plotly Express

[Plotly Express](plotly-express.md) is the easy-to-use, high-level interface to Plotly, which [operates on a variety of types of data](px-arguments.md) and produces [easy-to-style figures](styling-plotly-express.md).

The `px.strip()` function will make strip charts using underlying `box` traces with the box hidden.

See also [box plots](box-plots.md) and [violin plots](violin.md).

```python
import plotly.express as px

df = px.data.tips()
fig = px.strip(df, x="total_bill", y="day")
fig.show()
```

Strip charts support [faceting](facet-plots.md) and [discrete color](discrete-color.md):

```python
import plotly.express as px

df = px.data.tips()
fig = px.strip(df, x="total_bill", y="time", color="sex", facet_col="day")
fig.show()
```

#### Reference

See [function reference for `px.strip()`](https://plotly.com/python-api-reference/generated/plotly.express.strip) for more information and chart attribute options!
