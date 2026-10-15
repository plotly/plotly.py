import pytest
import plotly.io.json as pio
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd
import json
import datetime
import re
import sys
import warnings
from pytz import timezone
from _plotly_utils.optional_imports import get_module

orjson = get_module("orjson")
msgspec = get_module("msgspec")

eastern = timezone("US/Eastern")


# Testing helper
def build_json_opts(pretty=False):
    opts = {"sort_keys": True}
    if pretty:
        opts["indent"] = 2
    else:
        opts["separators"] = (",", ":")
    return opts


def to_json_test(value, pretty=False):
    return json.dumps(value, **build_json_opts(pretty=pretty))


def isoformat_test(dt_value):
    if isinstance(dt_value, np.datetime64):
        return str(dt_value)
    elif isinstance(dt_value, datetime.datetime):
        return dt_value.isoformat()
    else:
        raise ValueError("Unsupported date type: {}".format(type(dt_value)))


def build_test_dict(value):
    return dict(a=value, b=[3, value], c=dict(Z=value))


def build_test_dict_string(value_string, pretty=False):
    if pretty:
        non_pretty_str = build_test_dict_string(value_string, pretty=False)
        return to_json_test(json.loads(non_pretty_str), pretty=True)
    else:
        value_string = str(value_string).replace(" ", "")
        return """{"a":%s,"b":[3,%s],"c":{"Z":%s}}""" % tuple([value_string] * 3)


def check_roundtrip(value, engine, pretty):
    encoded = pio.to_json_plotly(value, engine=engine, pretty=pretty)
    decoded = pio.from_json_plotly(encoded, engine=engine)
    reencoded = pio.to_json_plotly(decoded, engine=engine, pretty=pretty)
    assert encoded == reencoded

    # Check from_plotly_json with bytes on Python 3
    if sys.version_info.major == 3:
        encoded_bytes = encoded.encode("utf8")
        decoded_from_bytes = pio.from_json_plotly(encoded_bytes, engine=engine)
        assert decoded == decoded_from_bytes


# Fixtures
engines = ["json", "auto"]
if orjson is not None:
    engines.append("orjson")
if msgspec is not None:
    engines.append("msgspec")


@pytest.fixture(scope="module", params=engines)
def engine(request):
    return request.param


@pytest.fixture(scope="module", params=[False])
def pretty(request):
    return request.param


@pytest.fixture(scope="module", params=["float64", "int32", "uint32"])
def graph_object(request):
    return request.param


@pytest.fixture(scope="module", params=["float64", "int32", "uint32"])
def numeric_numpy_array(request):
    dtype = request.param
    return np.linspace(-5, 5, 4, dtype=dtype)


@pytest.fixture(scope="module")
def object_numpy_array(request):
    return np.array(["a", 1, [2, 3]], dtype="object")


@pytest.fixture(scope="module")
def numpy_unicode_array(request):
    return np.array(["A", "BB", "CCC"], dtype="U")


@pytest.fixture(
    scope="module",
    params=[
        datetime.datetime(2003, 7, 12, 8, 34, 22),
        datetime.datetime.now(),
        np.datetime64(datetime.datetime.now(datetime.timezone.utc)),
        pd.Timestamp(datetime.datetime.now()),
        eastern.localize(datetime.datetime(2003, 7, 12, 8, 34, 22)),
        eastern.localize(datetime.datetime.now()),
        pd.Timestamp(datetime.datetime.now(), tzinfo=eastern),
    ],
)
def datetime_value(request):
    return request.param


@pytest.fixture(
    params=[
        list,  # plain list of datetime values
        lambda a: pd.DatetimeIndex(a),  # Pandas DatetimeIndex
        lambda a: pd.Series(pd.DatetimeIndex(a)),  # Pandas Datetime Series
        lambda a: pd.DatetimeIndex(a).values,  # Numpy datetime64 array
        lambda a: np.array(a, dtype="object"),  # Numpy object array of datetime
    ]
)
def datetime_array(request, datetime_value):
    return request.param([datetime_value] * 3)


# Encoding tests
def test_graph_object_input(engine, pretty):
    scatter = go.Scatter(x=[1, 2, 3], y=np.array([4, 5, 6]))
    result = pio.to_json_plotly(scatter, engine=engine)
    expected = """{"x":[1,2,3],"y":[4,5,6],"type":"scatter"}"""
    assert result == expected
    check_roundtrip(result, engine=engine, pretty=pretty)


def test_numeric_numpy_encoding(numeric_numpy_array, engine, pretty):
    value = build_test_dict(numeric_numpy_array)
    result = pio.to_json_plotly(value, engine=engine, pretty=pretty)

    array_str = to_json_test(numeric_numpy_array.tolist())
    expected = build_test_dict_string(array_str, pretty=pretty)
    assert result == expected
    check_roundtrip(result, engine=engine, pretty=pretty)


def test_numpy_unicode_encoding(numpy_unicode_array, engine, pretty):
    value = build_test_dict(numpy_unicode_array)
    result = pio.to_json_plotly(value, engine=engine, pretty=pretty)

    array_str = to_json_test(numpy_unicode_array.tolist())
    expected = build_test_dict_string(array_str)
    assert result == expected
    check_roundtrip(result, engine=engine, pretty=pretty)


def test_object_numpy_encoding(object_numpy_array, engine, pretty):
    value = build_test_dict(object_numpy_array)
    result = pio.to_json_plotly(value, engine=engine, pretty=pretty)

    array_str = to_json_test(object_numpy_array.tolist())
    expected = build_test_dict_string(array_str)
    assert result == expected
    check_roundtrip(result, engine=engine, pretty=pretty)


def test_datetime(datetime_value, engine, pretty):
    value = build_test_dict(datetime_value)
    result = pio.to_json_plotly(value, engine=engine, pretty=pretty)
    expected = build_test_dict_string('"{}"'.format(isoformat_test(datetime_value)))
    assert result == expected
    check_roundtrip(result, engine=engine, pretty=pretty)


def test_datetime_arrays(datetime_array, engine, pretty):
    value = build_test_dict(datetime_array)
    result = pio.to_json_plotly(value, engine=engine)

    def to_str(v):
        try:
            v = v.isoformat(sep="T")
        except (TypeError, AttributeError):
            pass

        return str(v)

    if isinstance(datetime_array, list):
        dt_values = [to_str(d) for d in datetime_array]
    elif isinstance(datetime_array, pd.Series):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", FutureWarning)
            # Series.dt.to_pydatetime will return Index[object]
            # https://github.com/pandas-dev/pandas/pull/52459
            dt_values = [
                to_str(d) for d in np.array(datetime_array.dt.to_pydatetime()).tolist()
            ]
    elif isinstance(datetime_array, pd.DatetimeIndex):
        dt_values = [to_str(d) for d in datetime_array.to_pydatetime().tolist()]
    else:  # numpy datetime64 array
        dt_values = [to_str(d) for d in datetime_array]

    array_str = to_json_test(dt_values)
    expected = build_test_dict_string(array_str)
    if orjson:
        # orjson always serializes datetime64 to ns, but json will return either
        # full seconds or microseconds, if the rest is zeros.
        # we don't care about any trailing zeros
        trailing_zeros = re.compile(r'[.]?0+"')
        result = trailing_zeros.sub('"', result)
        expected = trailing_zeros.sub('"', expected)

    assert result == expected
    check_roundtrip(result, engine=engine, pretty=pretty)


def test_object_array(engine, pretty):
    fig = px.scatter(px.data.tips(), x="total_bill", y="tip", custom_data=["sex"])
    result = fig.to_plotly_json()
    check_roundtrip(result, engine=engine, pretty=pretty)


def test_nonstring_key(engine, pretty):
    value = build_test_dict({0: 1})
    result = pio.to_json_plotly(value, engine=engine)
    check_roundtrip(result, engine=engine, pretty=pretty)


def test_mixed_string_nonstring_key(engine, pretty):
    value = build_test_dict({0: 1, "a": 2})
    result = pio.to_json_plotly(value, engine=engine)
    check_roundtrip(result, engine=engine, pretty=pretty)


def test_sanitize_json(engine):
    layout = {"title": {"text": "</script>\u2028\u2029"}}
    fig = go.Figure(layout=layout)
    fig_json = pio.to_json_plotly(fig, engine=engine)
    layout_2 = json.loads(fig_json)["layout"]
    if "template" in layout_2:
        del layout_2["template"]

    assert layout == layout_2

    replacements = {
        "<": "\\u003c",
        ">": "\\u003e",
        "/": "\\u002f",
        "\u2028": "\\u2028",
        "\u2029": "\\u2029",
    }

    for bad, good in replacements.items():
        assert bad not in fig_json
        assert good in fig_json


@pytest.mark.parametrize("na_value", [np.nan, pd.NaT, pd.NA])
def test_na_values(engine, na_value):
    result = pio.to_json_plotly(na_value, engine=engine)
    assert result == "null"


def _figure_with_frames():
    x = [datetime.datetime(2024, 1, 1) + datetime.timedelta(hours=i) for i in range(4)]
    return go.Figure(
        data=[go.Scatter(x=x, y=np.arange(4.0)), go.Bar(y=[1, 2, 3])],
        layout={"title": {"text": "t"}},
        frames=[go.Frame(data=[go.Scatter(y=np.array([4, 5, 6]))], name="f")],
    )


def test_figure_is_not_deep_copied(engine, monkeypatch):
    fig = _figure_with_frames()
    trace = go.Scatter(y=np.array([1.5, 2.5]))
    payload = {"fig": fig, "trace": trace, "when": pd.Timestamp("2024-01-01")}
    expected = pio.to_json_plotly(
        {
            "fig": fig.to_dict(),
            "trace": trace.to_plotly_json(),
            "when": "2024-01-01T00:00:00",
        },
        engine=engine,
    )
    before = fig.to_dict()

    def no_deepcopy(value, memo=None):
        raise AssertionError("serializing a figure should not deep copy it")

    monkeypatch.setattr("plotly.basedatatypes.deepcopy", no_deepcopy)
    result = pio.to_json_plotly(payload, engine=engine)
    monkeypatch.undo()

    assert json.loads(result) == json.loads(expected)
    assert isinstance(fig.data[0].y, np.ndarray)
    assert isinstance(fig.frames[0].data[0].y, np.ndarray)
    assert fig.to_dict() == before


def test_subclass_overrides_are_kept(engine):
    class MyFigure(go.Figure):
        def to_dict(self):
            res = super().to_dict()
            res["layout"]["title"] = {"text": "from to_dict"}
            return res

    class MyScatter(go.Scatter):
        def to_plotly_json(self):
            return dict(super().to_plotly_json(), name="from to_plotly_json")

    result = json.loads(
        pio.to_json_plotly(
            {"fig": MyFigure(go.Bar(y=[1])), "trace": MyScatter(y=[1])}, engine=engine
        )
    )
    assert result["fig"]["layout"]["title"] == {"text": "from to_dict"}
    assert result["trace"]["name"] == "from to_plotly_json"


def test_datetime_series_with_nat(engine):
    value = {"v": pd.Series([pd.Timestamp("2024-01-01"), pd.NaT])}
    result = pio.to_json_plotly(value, engine=engine)
    assert json.loads(result) == {"v": ["2024-01-01T00:00:00", None]}


@pytest.mark.parametrize("value", [object(), 1j, {(1, 2): 1}, [{(1,): 2}]])
def test_unserializable_raises_type_error(engine, value):
    with pytest.raises(TypeError):
        pio.to_json_plotly({"v": value}, engine=engine)


@pytest.mark.skipif(msgspec is None, reason="requires msgspec")
def test_auto_engine_uses_msgspec_without_orjson(monkeypatch):
    def without_orjson(name, **kwargs):
        return None if name == "orjson" else get_module(name, **kwargs)

    monkeypatch.setattr("plotly.io._json.get_module", without_orjson)
    utc = datetime.datetime(2024, 1, 1, tzinfo=datetime.timezone.utc)
    # msgspec writes UTC as Z, the json engine as +00:00
    assert (
        pio.to_json_plotly({"t": utc}, engine="auto") == '{"t":"2024-01-01T00:00:00Z"}'
    )
    assert pio.from_json_plotly('{"a":[1]}', engine="auto") == {"a": [1]}


@pytest.mark.skipif(msgspec is None, reason="requires msgspec")
def test_msgspec_default_engine():
    original = pio.config.default_engine
    try:
        pio.config.default_engine = "msgspec"
        assert pio.to_json_plotly(go.Figure(go.Bar(y=[1]))) == pio.to_json_plotly(
            go.Figure(go.Bar(y=[1])), engine="json"
        )
    finally:
        pio.config.default_engine = original
