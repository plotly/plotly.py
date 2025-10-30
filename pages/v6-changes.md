---
description: Guide to changes in version 6 of Plotly.py and how to migrate from version
  5
---
This page outlines the changes in Plotly.py version 6 and cases where you may need to update your charts or tools that you use for working with Plotly.py.

<!-- #region -->
## Jupyter Notebook Support

Versions of Jupyter Notebook earlier than version 7 are no longer supported. To upgrade to the latest Jupyter Notebook:

```
pip install notebook --upgrade
```

## Change to anywidget for go.FigureWidget

[go.FigureWidget](figurewidget.md) now uses [anywidget](https://anywidget.dev/). Install `anywidget` with:

```python
pip install anywidget
```

## Processing NumPy and NumPy-Convertible Arrays

Plotly.py now takes advantage of recent changes in how Plotly.js handles typed arrays for improved performance. See the [performance page](performance.md) for more details.

!!! note

    If you are using Plotly.py 6 or later with Dash Design Kit, you may need to upgrade your Dash Design Kit version. See the [Dash Design Kit Compatibility section on the performance page](performance.md#dash-design-kit-compatibility) for more details.


## Dataframe Support

Plotly Express now uses [Narwhals](https://narwhals-dev.github.io/narwhals/) to natively support pandas, Polars, and PyArrow. With this change, the [performance](performance.md) of using Polars or PyArrow with Plotly Express is significantly improved.

## Mapbox Deprecation

Mapbox-based traces are deprecated and will be removed in a future version of Plotly.py. Use [Maplibre-based](mapbox-to-maplibre.md) traces instead.

## Removed Attributes

The following attributes have been removed in Plotly.py 6.

### `titlefont`,`titleposition`, `titleside`, and `titleoffset`

The layout attributes `titlefont`,`titleposition`, `titleside`, and `titleoffset` have been removed. Replace them with `title.font`, `title.position`, `title.side`, and `title.offset`.

The following example shows how to use `layout.title.font`:

```python
import plotly.graph_objects as go

fig = go.Figure(
    data=[
      go.Bar(
        x=["A", "B", "C", "D"],
        y=[10, 15, 13, 17]
        )
    ],
    layout=dict(
      title=dict(
        text="Chart Title",
        font=dict(
          size=40
          )
        )
      ),
    # Previously the title font could be set like this:
    # titlefont=dict(size=40)
)

fig.show()
```

## Removed Traces

The following traces have been removed.

### `heatmapgl`

The `heatmapgl` trace has been removed. Use [`heatmap`](heatmaps.md) instead.


### `pointcloud`

The `pointcloud` trace has been removed. Use [`scattergl`](/reference/graph_objects/Scattergl.md).

<!-- #endregion -->

<!-- #region -->
## Other Removed Features

### Transforms

Transforms, which were deprecated in Plotly.py v5, have been removed. You can achieve similar functionality by preprocessing the data with a dataframe library.

For example, a transform to filter the data:

```python
  dict(
    type = 'filter',
    target = df['year'],
    orientation = '=',
    value = 2007
  ),
```

Could be rewritten using Pandas:

```python
df_2007 = df[df['year'] == 2007]
```
<!-- #endregion -->
