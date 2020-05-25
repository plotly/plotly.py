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
        (lambda df: df.plot.scatter("A", "B"), lambda df: px.scatter(df, "A", "B"),),
        (lambda df: df.plot.line(), px.line),
        (lambda df: df.plot.area(), px.area),
        (lambda df: df.plot.bar(), px.bar),
        (lambda df: df.plot.barh(), lambda df: px.bar(df, orientation="h")),
        (lambda df: df.plot.box(), px.box),
        (lambda df: df.plot.hist(), px.histogram),
        (lambda df: df.boxplot(), px.box),
        (lambda df: df.hist(), px.histogram),
        (lambda df: df["A"].hist(), lambda df: px.histogram(df["A"])),
    ],
)
def test_pandas_equiv(pandas_fn, px_fn):
    pd.options.plotting.backend = "plotly"
    df = pd.DataFrame(np.random.randn(100, 4), columns=list("ABCD")).cumsum()
    assert pandas_fn(df) == px_fn(df)
