"""
Pandas plotting backend functions, see:
https://github.com/pandas-dev/pandas/blob/master/pandas/plotting/__init__.py

To activate, set pandas.options.plotting.backend="plotly.express.pandas_backend"
"""
from ._chart_types import scatter, line, area, bar, box, histogram


def plot(data, kind, **kwargs):
    if kind == "scatter":
        del kwargs["s"]
        del kwargs["c"]
        return scatter(data, **kwargs)
    if kind == "line":
        return line(data, **kwargs)
    if kind == "area":
        return area(data, **kwargs)
    if kind == "bar":
        return bar(data, **kwargs)
    if kind == "barh":
        return bar(data, orientation="h", **kwargs)
    if kind == "box":
        del kwargs["by"]
        return box(data, **kwargs)
    if kind in "hist":
        del kwargs["by"]
        if kwargs.get("bins"):
            kwargs["nbins"] = kwargs["bins"]
        del kwargs["bins"]
        return histogram(data, **kwargs)
    raise NotImplementedError(
        "The plotly.express backend doesn't yet support kind='%s'" % kind
    )


def boxplot_frame(data, **kwargs):
    del kwargs["by"]
    del kwargs["column"]
    del kwargs["ax"]
    del kwargs["fontsize"]
    del kwargs["rot"]
    del kwargs["grid"]
    del kwargs["figsize"]
    del kwargs["layout"]
    del kwargs["return_type"]
    return box(data, **kwargs)


def hist_frame(data, **kwargs):
    del kwargs["column"]
    del kwargs["by"]
    del kwargs["grid"]
    del kwargs["xlabelsize"]
    del kwargs["xrot"]
    del kwargs["ylabelsize"]
    del kwargs["yrot"]
    del kwargs["ax"]
    del kwargs["sharex"]
    del kwargs["sharey"]
    del kwargs["figsize"]
    del kwargs["layout"]
    if kwargs.get("bins"):
        kwargs["nbins"] = kwargs["bins"]
    del kwargs["bins"]
    return histogram(data, **kwargs)


def hist_series(data, **kwargs):
    del kwargs["by"]
    del kwargs["grid"]
    del kwargs["xlabelsize"]
    del kwargs["xrot"]
    del kwargs["ylabelsize"]
    del kwargs["yrot"]
    del kwargs["ax"]
    del kwargs["figsize"]
    if kwargs.get("bins"):
        kwargs["nbins"] = kwargs["bins"]
    del kwargs["bins"]
    return histogram(data, **kwargs)
