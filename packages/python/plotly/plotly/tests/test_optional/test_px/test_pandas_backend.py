import plotly.express as px
import numpy as np
import pandas as pd
import pytest


@pytest.mark.skipif(
    not hasattr(pd.options.plotting, "backend"),
    reason="Currently installed pandas doesn't support plotting backends.",
)
@pytest.mark.parametrize(
    "pandas_fn,px_fn",
    [
        (lambda df: df.plot(), px.line),
        (
            lambda df: df.plot.scatter("A", "B"),
            lambda df: px.scatter(df, "A", "B"),
        ),
        (
            lambda df: df.plot.scatter("A", "B", c="C"),
            lambda df: px.scatter(df, "A", "B", color="C"),
        ),
        (lambda df: df.plot.line(), px.line),
        (lambda df: df.plot.area(), px.area),
        (lambda df: df.plot.bar(), px.bar),
        (lambda df: df.plot.barh(), lambda df: px.bar(df, orientation="h")),
        (lambda df: df.plot.box(), px.box),
        (lambda df: df.plot.hist(), px.histogram),
        (lambda df: df.boxplot(), px.box),
        (lambda df: df.hist(), px.histogram),
        (lambda df: df["A"].hist(), lambda df: px.histogram(df["A"])),
        (lambda df: df.plot(kind="line"), px.line),
        (lambda df: df.plot(kind="area"), px.area),
        (lambda df: df.plot(kind="bar"), px.bar),
        (lambda df: df.plot(kind="box"), px.box),
        (lambda df: df.plot(kind="hist"), px.histogram),
        (lambda df: df.plot(kind="histogram"), px.histogram),
        (lambda df: df.plot(kind="violin"), px.violin),
        (lambda df: df.plot(kind="strip"), px.strip),
        (lambda df: df.plot(kind="funnel"), px.funnel),
        (lambda df: df.plot(kind="density_contour"), px.density_contour),
        (lambda df: df.plot(kind="density_heatmap"), px.density_heatmap),
        (lambda df: df.plot(kind="imshow"), px.imshow),
    ],
)
def test_pandas_equiv(pandas_fn, px_fn):
    pd.options.plotting.backend = "plotly"
    df = pd.DataFrame(np.random.randn(100, 4), columns=list("ABCD")).cumsum()
    assert pandas_fn(df) == px_fn(df)


@pytest.mark.skipif(
    not hasattr(pd.options.plotting, "backend"),
    reason="Currently installed pandas doesn't support plotting backends.",
)
def test_pandas_example():
    pd.options.plotting.backend = "plotly"
    ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))
    df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=list("ABCD"))
    fig = df.iloc[5].plot.bar()
    assert len(fig.data) == 1


@pytest.mark.skipif(
    not hasattr(pd.options.plotting, "backend"),
    reason="Currently installed pandas doesn't support plotting backends.",
)
def test_pandas_invalid_c_kwarg():
    pd.options.plotting.backend = "plotly"
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9], "d": [1, 1, 2]})
    with pytest.raises(
        ValueError,
        match="plotly.express.scatter does not support both 'color' and 'c' kwargs",
    ):
        df.plot.scatter(x="a", y="b", c="c", color="d")
    with pytest.raises(
        ValueError,
        match="plotly.express.scatter only supports the 'c' kwarg as a column name",
    ):
        df.plot.scatter(x="a", y="b", c="blue")
    with pytest.raises(
        ValueError,
        match="plotly.express.scatter does not support both 'size' and 's' kwargs",
    ):
        df.plot.scatter(x="a", y="b", s="d", size="d")
    with pytest.raises(
        ValueError,
        match="plotly.express.scatter only supports the 's' kwarg as a column name",
    ):
        df.plot.scatter(x="a", y="b", s=2)
