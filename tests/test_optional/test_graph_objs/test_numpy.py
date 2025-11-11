from datetime import datetime

import numpy as np

import plotly.graph_objs as go


def test_np_ns_datetime():
    x = [np.datetime64("2025-09-26").astype("datetime64[ns]")]
    y = [1.23]
    scatter = go.Scatter(x=x, y=y, mode="markers")

    # x value should be converted to native datetime
    assert isinstance(scatter.x[0], datetime)
    # x value should match original numpy value at microsecond precision
    assert x[0].astype("datetime64[us]").item() == scatter.x[0]
