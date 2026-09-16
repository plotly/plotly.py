import json

import numpy as np
import pandas as pd
import pytest

import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
from _plotly_utils.utils import to_typed_array_spec
from plotly.serializers import _py_to_js

try:
    import orjson  # noqa: F401

    engines = ["json", "orjson"]
except ImportError:
    engines = ["json"]


def json_data(fig, engine):
    return json.loads(pio.to_json(fig, engine=engine))["data"]


@pytest.mark.parametrize("engine", engines)
def test_bar_with_nan_is_sent_as_list(engine):
    fig = go.Figure(go.Bar(x=["a", "b", "c"], y=pd.Series([24.0, np.nan, 11.0])))

    assert json_data(fig, engine)[0]["y"] == [24.0, None, 11.0]


@pytest.mark.parametrize("engine", engines)
def test_scattergl_with_inf_is_sent_as_list(engine):
    df = pd.DataFrame({"x": [0, 1, 2, 3, 4], "y": [0, 1, 4, 9, np.inf]})
    fig = go.Figure(go.Scattergl(x=df["x"], y=df["y"]))

    trace = json_data(fig, engine)[0]
    assert trace["y"] == [0.0, 1.0, 4.0, 9.0, None]
    assert set(trace["x"]) == {"dtype", "bdata"}


@pytest.mark.parametrize("engine", engines)
def test_px_bar_stack_with_missing_value(engine):
    wide_df = px.data.medals_wide()
    wide_df.iloc[0, 2] = None
    fig = px.bar(wide_df, x="nation", y=["gold", "silver", "bronze"])

    traces = {trace["name"]: trace["y"] for trace in json_data(fig, engine)}
    assert traces["silver"] == [None, 15.0, 12.0]
    assert set(traces["gold"]) == {"dtype", "bdata"}
    assert set(traces["bronze"]) == {"dtype", "bdata"}


def test_heatmap_z_with_nan_stays_base64_encoded():
    fig = go.Figure(go.Heatmap(z=np.array([[1.0, np.nan], [2.0, 3.0]])))

    z = json_data(fig, "json")[0]["z"]
    assert set(z) == {"dtype", "bdata", "shape"}
    assert z["shape"] == "2, 2"


@pytest.mark.parametrize("value", [np.nan, np.inf, -np.inf])
@pytest.mark.parametrize("dtype", ["float32", "float64"])
def test_to_typed_array_spec_non_finite(value, dtype):
    v = np.array([1.0, value], dtype=dtype)

    result = to_typed_array_spec(v)
    assert isinstance(result, np.ndarray)
    np.testing.assert_array_equal(result, v)


def test_to_typed_array_spec_finite():
    assert to_typed_array_spec(np.array([1.0, 2.0])) == {
        "dtype": "f8",
        "bdata": "AAAAAAAA8D8AAAAAAAAAQA==",
    }


def test_widget_serializer_non_finite():
    assert _py_to_js(np.array([1.0, np.nan, np.inf]), None) == [1.0, None, None]
    assert _py_to_js(np.array([[1.0, np.nan], [2.0, 3.0]]), None) == [
        [1.0, None],
        [2.0, 3.0],
    ]
    assert _py_to_js({"y": [1.0, float("nan"), -float("inf")]}, None) == {
        "y": [1.0, None, None]
    }


def test_widget_serializer_finite_array_as_buffer():
    v = np.array([1.0, 2.0])

    result = _py_to_js(v, None)
    assert result["dtype"] == "float64"
    assert result["shape"] == (2,)
    assert bytes(result["buffer"]) == v.tobytes()
