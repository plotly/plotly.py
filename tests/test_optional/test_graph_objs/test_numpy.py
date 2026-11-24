import base64
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


def test_np_int64_negative_values_survive_serialization():
    # int64 arrays are sent to plotly.js as a smaller integer type when their
    # values fit; a value below the int8 range must not wrap around
    y = np.array([-1000, 5], dtype="int64")
    spec = go.Figure(go.Scatter(y=y)).to_dict()["data"][0]["y"]

    decoded = np.frombuffer(base64.b64decode(spec["bdata"]), dtype=spec["dtype"])
    assert decoded.tolist() == [-1000, 5]
