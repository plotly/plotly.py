---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.14.7
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
    description: How to make a grouped and stacked bar chart in Python with Plotly.
    display_as: scientific
    language: python
    layout: base
    name: Grouped Stacked Bar Charts
    order: 27
    page_type: u-guide
    permalink: python/grouped-stacked-bar/
    thumbnail: thumbnail/grouped-stacked-bar.jpg
---

This page details the use of a [figure factory](/python/figure-factories/). For more examples with bar charts, see [this page](/python/bar-charts/).

#### Simple Grouped Stacked Bar Chart

```python
import plotly.figure_factory as ff
import plotly.express as px

df = px.data.tips().groupby(["day", "sex", "smoker"])[["total_bill", "tip"]].sum().reset_index()

fig = ff.create_grouped_stacked_bar(
    df,
    x="smoker",
    stack_group="day",
    color="sex",
    y="tip",
)
fig.update_layout(legend_title=None)
fig.show()
```

#### Advanced Grouped Stacked Bar Chart

```python
import plotly.figure_factory as ff
import plotly.express as px

df = px.data.tips().groupby(["day", "sex", "smoker"])[["total_bill", "tip"]].sum().reset_index()

fig = ff.create_grouped_stacked_bar(
    df,
    x="smoker",
    stack_group="day",
    color="sex",
    y="tip",
    # Manage the gap between groups
    stack_group_gap=0.2,
    # Manage the gap between bars within groups
    bar_gap=0.05,
    # Manage the category orders
    category_orders={
      "day": ["Thur", "Fri", "Sat", "Sun"],
    },
    # The grouped stacked bar chart respects the template colors
    # Each group will be displayed with nuances of the colorway
    # You can also specify the list of colors with `color_discrete_sequence`
    template="ggplot2",
    # Unified hover label
    hover_unified=True,
)
fig.update_layout(legend_title=None)
fig.show()
```
