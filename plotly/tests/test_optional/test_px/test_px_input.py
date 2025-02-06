import plotly.express as px
import pyarrow as pa
import plotly.graph_objects as go
import narwhals.stable.v1 as nw
import numpy as np
import pandas as pd
import pytest
from packaging import version
import unittest.mock as mock
from plotly.express._core import build_dataframe
from pandas.testing import assert_frame_equal
import sys
import warnings


def test_numpy():
    fig = px.scatter(x=[1, 2, 3], y=[2, 3, 4], color=[1, 3, 9])
    assert np.all(fig.data[0].x == np.array([1, 2, 3]))
    assert np.all(fig.data[0].y == np.array([2, 3, 4]))
    assert np.all(fig.data[0].marker.color == np.array([1, 3, 9]))


def test_numpy_labels():
    fig = px.scatter(
        x=[1, 2, 3], y=[2, 3, 4], labels={"x": "time"}
    )  # other labels will be kw arguments
    assert fig.data[0]["hovertemplate"] == "time=%{x}<br>y=%{y}<extra></extra>"


def test_with_index():
    tips = px.data.tips()
    fig = px.scatter(tips, x=tips.index, y="total_bill")
    assert (
        fig.data[0]["hovertemplate"] == "index=%{x}<br>total_bill=%{y}<extra></extra>"
    )
    fig = px.scatter(tips, x=tips.index, y=tips.total_bill)
    assert (
        fig.data[0]["hovertemplate"] == "index=%{x}<br>total_bill=%{y}<extra></extra>"
    )
    fig = px.scatter(tips, x=tips.index, y=tips.total_bill, labels={"index": "number"})
    assert (
        fig.data[0]["hovertemplate"] == "number=%{x}<br>total_bill=%{y}<extra></extra>"
    )
    # We do not allow "x=index"
    with pytest.raises(ValueError) as err_msg:
        fig = px.scatter(tips, x="index", y="total_bill")
    assert "To use the index, pass it in directly as `df.index`." in str(err_msg.value)
    tips = px.data.tips()
    tips.index.name = "item"
    fig = px.scatter(tips, x=tips.index, y="total_bill")
    assert fig.data[0]["hovertemplate"] == "item=%{x}<br>total_bill=%{y}<extra></extra>"


def test_series(request, backend):
    if backend == "pyarrow":
        # By converting to native, we lose the name for pyarrow chunked_array
        # and the assertions fail
        request.applymarker(pytest.mark.xfail)

    tips = nw.from_native(px.data.tips(return_type=backend))
    before_tip = (tips.get_column("total_bill") - tips.get_column("tip")).to_native()
    day = tips.get_column("day").to_native()
    tips = tips.to_native()

    fig = px.bar(tips, x="day", y=before_tip)
    assert fig.data[0].hovertemplate == "day=%{x}<br>y=%{y}<extra></extra>"
    fig = px.bar(tips, x="day", y=before_tip, labels={"y": "bill"})
    assert fig.data[0].hovertemplate == "day=%{x}<br>bill=%{y}<extra></extra>"
    # lock down that we can pass df.col to facet_*
    fig = px.bar(tips, x="day", y="tip", facet_row=day, facet_col=day)
    assert fig.data[0].hovertemplate == "day=%{x}<br>tip=%{y}<extra></extra>"


def test_several_dataframes(request, constructor):
    if "pyarrow_table" in str(constructor):
        # By converting to native, we lose the name for pyarrow chunked_array
        # and the assertions fail
        request.applymarker(pytest.mark.xfail)

    df = nw.from_native(constructor(dict(x=[0, 1], y=[1, 10], z=[0.1, 0.8])))
    df2 = nw.from_native(constructor(dict(time=[23, 26], money=[100, 200])))
    fig = px.scatter(
        df.to_native(), x="z", y=df2.get_column("money").to_native(), size="x"
    )
    assert (
        fig.data[0].hovertemplate
        == "z=%{x}<br>y=%{y}<br>x=%{marker.size}<extra></extra>"
    )
    fig = px.scatter(
        df2.to_native(),
        x=df.get_column("z").to_native(),
        y=df2.get_column("money").to_native(),
        size=df.get_column("z").to_native(),
    )
    assert (
        fig.data[0].hovertemplate
        == "x=%{x}<br>money=%{y}<br>size=%{marker.size}<extra></extra>"
    )
    # Name conflict
    with pytest.raises(NameError) as err_msg:
        fig = px.scatter(
            df.to_native(), x="z", y=df2.get_column("money").to_native(), size="y"
        )
    assert "A name conflict was encountered for argument 'y'" in str(err_msg.value)
    with pytest.raises(NameError) as err_msg:
        fig = px.scatter(
            df.to_native(),
            x="z",
            y=df2.get_column("money").to_native(),
            size=df.get_column("y").to_native(),
        )
    assert "A name conflict was encountered for argument 'y'" in str(err_msg.value)

    # No conflict when the dataframe is not given, fields are used
    df = nw.from_native(constructor(dict(x=[0, 1], y=[3, 4])))
    df2 = nw.from_native(constructor(dict(x=[3, 5], y=[23, 24])))
    fig = px.scatter(
        x=df.get_column("y").to_native(), y=df2.get_column("y").to_native()
    )
    assert np.all(fig.data[0].x == np.array([3, 4]))
    assert np.all(fig.data[0].y == np.array([23, 24]))
    assert fig.data[0].hovertemplate == "x=%{x}<br>y=%{y}<extra></extra>"

    df = nw.from_native(constructor(dict(x=[0, 1], y=[3, 4])))
    df2 = nw.from_native(constructor(dict(x=[3, 5], y=[23, 24])))
    df3 = nw.from_native(constructor(dict(y=[0.1, 0.2])))
    fig = px.scatter(
        x=df.get_column("y").to_native(),
        y=df2.get_column("y").to_native(),
        size=df3.get_column("y").to_native(),
    )
    assert np.all(fig.data[0].x == np.array([3, 4]))
    assert np.all(fig.data[0].y == np.array([23, 24]))
    assert (
        fig.data[0].hovertemplate
        == "x=%{x}<br>y=%{y}<br>size=%{marker.size}<extra></extra>"
    )

    df = nw.from_native(constructor(dict(x=[0, 1], y=[3, 4])))
    df2 = nw.from_native(constructor(dict(x=[3, 5], y=[23, 24])))
    df3 = nw.from_native(constructor(dict(y=[0.1, 0.2])))
    fig = px.scatter(
        x=df.get_column("y").to_native(),
        y=df2.get_column("y").to_native(),
        hover_data=[df3.get_column("y").to_native()],
    )
    assert np.all(fig.data[0].x == np.array([3, 4]))
    assert np.all(fig.data[0].y == np.array([23, 24]))
    assert (
        fig.data[0].hovertemplate
        == "x=%{x}<br>y=%{y}<br>hover_data_0=%{customdata[0]}<extra></extra>"
    )


def test_name_heuristics(request, constructor):
    if "pyarrow_table" in str(constructor):
        # By converting to native, we lose the name for pyarrow chunked_array
        # and the assertions fail
        request.applymarker(pytest.mark.xfail)

    df = nw.from_native(constructor(dict(x=[0, 1], y=[3, 4], z=[0.1, 0.2])))
    fig = px.scatter(
        df.to_native(),
        x=df.get_column("y").to_native(),
        y=df.get_column("x").to_native(),
        size=df.get_column("y").to_native(),
    )
    assert np.all(fig.data[0].x == np.array([3, 4]))
    assert np.all(fig.data[0].y == np.array([0, 1]))
    assert fig.data[0].hovertemplate == "y=%{marker.size}<br>x=%{y}<extra></extra>"


def test_repeated_name(backend):
    iris = px.data.iris(return_type=backend)
    fig = px.scatter(
        iris,
        x="sepal_width",
        y="sepal_length",
        hover_data=["petal_length", "petal_width", "species_id"],
        custom_data=["species_id", "species"],
    )
    assert fig.data[0].customdata.shape[1] == 4


def test_arrayattrable_numpy(backend):
    tips = px.data.tips(return_type=backend)
    fig = px.scatter(
        tips, x="total_bill", y="tip", hover_data=[np.random.random(tips.shape[0])]
    )
    assert (
        fig.data[0]["hovertemplate"]
        == "total_bill=%{x}<br>tip=%{y}<br>hover_data_0=%{customdata[0]}<extra></extra>"
    )
    fig = px.scatter(
        tips,
        x="total_bill",
        y="tip",
        hover_data=[np.random.random(tips.shape[0])],
        labels={"hover_data_0": "suppl"},
    )
    assert (
        fig.data[0]["hovertemplate"]
        == "total_bill=%{x}<br>tip=%{y}<br>suppl=%{customdata[0]}<extra></extra>"
    )


def test_wrong_column_name():
    with pytest.raises(ValueError) as err_msg:
        px.scatter(px.data.tips(), x="bla", y="wrong")
    assert "Value of 'x' is not the name of a column in 'data_frame'" in str(
        err_msg.value
    )


def test_missing_data_frame():
    with pytest.raises(ValueError) as err_msg:
        px.scatter(x="arg1", y="arg2")
    assert "String or int arguments are only possible" in str(err_msg.value)


def test_wrong_dimensions_of_array():
    with pytest.raises(ValueError) as err_msg:
        px.scatter(x=[1, 2, 3], y=[2, 3, 4, 5])
    assert "All arguments should have the same length." in str(err_msg.value)


def test_wrong_dimensions_mixed_case(constructor):
    with pytest.raises(ValueError) as err_msg:
        df = constructor(dict(time=[1, 2, 3], temperature=[20, 30, 25]))
        px.scatter(df, x="time", y="temperature", color=[1, 3, 9, 5])
    assert "All arguments should have the same length." in str(err_msg.value)


def test_wrong_dimensions(backend):
    df = px.data.tips(return_type=backend)
    with pytest.raises(ValueError) as err_msg:
        px.scatter(df, x="tip", y=[1, 2, 3])
    assert "All arguments should have the same length." in str(err_msg.value)
    # the order matters
    with pytest.raises(ValueError) as err_msg:
        px.scatter(df, x=[1, 2, 3], y="tip")
    assert "All arguments should have the same length." in str(err_msg.value)
    with pytest.raises(ValueError):
        px.scatter(px.data.tips(), x=px.data.iris().index, y="tip")
    assert "All arguments should have the same length." in str(err_msg.value)


def test_multiindex_raise_error():
    index = pd.MultiIndex.from_product(
        [[1, 2, 3], ["a", "b"]], names=["first", "second"]
    )
    df = pd.DataFrame(np.random.random((6, 3)), index=index, columns=["A", "B", "C"])
    # This is ok
    px.scatter(df, x="A", y="B")
    with pytest.raises(TypeError) as err_msg:
        px.scatter(df, x=df.index, y="B")
    assert "pandas MultiIndex is not supported by plotly express" in str(err_msg.value)


def test_build_df_from_lists():
    # Just lists
    args = dict(x=[1, 2, 3], y=[2, 3, 4], color=[1, 3, 9])
    output = {key: key for key in args}
    df = pd.DataFrame(args)
    args["data_frame"] = None
    out = build_dataframe(args, go.Scatter)
    df_out = out.pop("data_frame").to_native()

    assert df_out.equals(df)
    assert out == output

    # Arrays
    args = dict(x=np.array([1, 2, 3]), y=np.array([2, 3, 4]), color=[1, 3, 9])
    output = {key: key for key in args}
    df = pd.DataFrame(args)
    args["data_frame"] = None
    out = build_dataframe(args, go.Scatter)
    df_out = out.pop("data_frame").to_native()
    assert df_out.equals(df)
    assert out == output


def test_build_df_with_index():
    tips = px.data.tips()
    args = dict(data_frame=tips, x=tips.index, y="total_bill")
    out = build_dataframe(args, go.Scatter)
    assert_frame_equal(
        tips.reset_index()[out["data_frame"].columns], out["data_frame"].to_pandas()
    )


def test_build_df_using_interchange_protocol_mock():
    class InterchangeDataFrame:
        def __init__(self, df):
            self._df = df

        def __dataframe__(self):
            return self

        def column_names(self):
            return list(self._df._data.keys())

        def select_columns_by_name(self, columns):
            return InterchangeDataFrame(
                CustomDataFrame(
                    {
                        key: value
                        for key, value in self._df._data.items()
                        if key in columns
                    }
                )
            )

    class CustomDataFrame:
        def __init__(self, data):
            self._data = data

        def __dataframe__(self, allow_copy: bool = True):
            return InterchangeDataFrame(self)

    input_dataframe = CustomDataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})

    input_dataframe_pa = pa.table({"a": [1, 2, 3], "b": [4, 5, 6]})

    args = dict(data_frame=input_dataframe, x="a", y="b")
    with mock.patch(
        "narwhals._interchange.dataframe.InterchangeFrame.to_arrow",
        return_value=input_dataframe_pa,
    ) as mock_from_dataframe:
        out = build_dataframe(args, go.Scatter)

        mock_from_dataframe.assert_called_once()

        assert_frame_equal(
            input_dataframe_pa.select(out["data_frame"].columns).to_pandas(),
            out["data_frame"].to_pandas(),
        )


@pytest.mark.skipif(
    version.parse(pd.__version__) < version.parse("2.0.2")
    or sys.version_info >= (3, 12),
    reason="plotly doesn't use a dataframe interchange protocol for pandas < 2.0.2",
)
@pytest.mark.parametrize("test_lib", ["vaex", "polars"])
def test_build_df_from_vaex_and_polars(test_lib):
    if test_lib == "vaex":
        import vaex as lib
    else:
        import polars as lib

    # take out the 'species' columns since the vaex implementation does not cover strings yet
    iris_pandas = px.data.iris()[["petal_width", "sepal_length"]]
    iris_vaex = lib.from_pandas(iris_pandas)
    args = dict(data_frame=iris_vaex, x="petal_width", y="sepal_length")
    out = build_dataframe(args, go.Scatter)
    assert_frame_equal(
        iris_pandas.reset_index()[out["data_frame"].columns],
        out["data_frame"].to_pandas(),
    )


@pytest.mark.skipif(
    version.parse(pd.__version__) < version.parse("2.0.2")
    or sys.version_info >= (3, 12),
    reason="plotly doesn't use a dataframe interchange protocol for pandas < 2.0.2",
)
@pytest.mark.parametrize("test_lib", ["vaex", "polars"])
@pytest.mark.parametrize(
    "hover_data", [["sepal_width"], {"sepal_length": False, "sepal_width": ":.2f"}]
)
def test_build_df_with_hover_data_from_vaex_and_polars(test_lib, hover_data):
    if test_lib == "vaex":
        import vaex as lib
    else:
        import polars as lib

    # take out the 'species' columns since the vaex implementation does not cover strings yet
    iris_pandas = px.data.iris()[["petal_width", "sepal_length", "sepal_width"]]
    iris_vaex = lib.from_pandas(iris_pandas)
    args = dict(
        data_frame=iris_vaex,
        x="petal_width",
        y="sepal_length",
        hover_data=hover_data,
    )
    out = build_dataframe(args, go.Scatter)
    assert_frame_equal(
        iris_pandas.reset_index()[out["data_frame"].columns],
        out["data_frame"].to_pandas(),
    )


def test_timezones(constructor):
    df = nw.from_native(
        constructor({"date": ["2015-04-04 19:31:30+01:00"], "value": [3]})
    ).with_columns(nw.col("date").str.to_datetime(format="%Y-%m-%d %H:%M:%S%z"))
    args = dict(data_frame=df.to_native(), x="date", y="value")
    out = build_dataframe(args, go.Scatter)

    assert str(out["data_frame"].item(row=0, column="date")) == str(
        nw.from_native(df).item(row=0, column="date")
    )


def test_non_matching_index():
    df = pd.DataFrame(dict(y=[1, 2, 3]), index=["a", "b", "c"])

    expected = pd.DataFrame(dict(index=["a", "b", "c"], y=[1, 2, 3]))

    args = dict(data_frame=df, x=df.index, y="y")
    out = build_dataframe(args, go.Scatter)
    assert_frame_equal(expected, out["data_frame"].to_pandas())

    expected = pd.DataFrame(dict(x=["a", "b", "c"], y=[1, 2, 3]))

    args = dict(data_frame=None, x=df.index, y=df.y)
    out = build_dataframe(args, go.Scatter)
    assert_frame_equal(expected, out["data_frame"].to_pandas())

    args = dict(data_frame=None, x=["a", "b", "c"], y=df.y)
    out = build_dataframe(args, go.Scatter)
    assert_frame_equal(expected, out["data_frame"].to_pandas())


def test_splom_case(backend):
    iris = px.data.iris(return_type=backend)
    fig = px.scatter_matrix(iris)
    assert len(fig.data[0].dimensions) == len(iris.columns)
    dic = {"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]}
    fig = px.scatter_matrix(dic)
    assert np.all(fig.data[0].dimensions[0].values == np.array(dic["a"]))
    ar = np.arange(9).reshape((3, 3))
    fig = px.scatter_matrix(ar)
    assert np.all(fig.data[0].dimensions[0].values == ar[:, 0])


def test_scatter_matrix_indexed_pandas():
    # https://github.com/plotly/plotly.py/issues/4917
    # https://github.com/plotly/plotly.py/issues/4788
    df = pd.DataFrame(
        {
            "x": [1, 2, 3, 4],
            "y": [10, 20, 10, 20],
            "z": [-1, -2, -3, -4],
            "color": [1, 2, 3, 4],
        }
    )
    df.index = pd.DatetimeIndex(
        [
            "1/1/2020 10:00:00+00:00",
            "2/1/2020 11:00:00+00:00",
            "3/1/2020 10:00:00+00:00",
            "4/1/2020 11:00:00+00:00",
        ]
    )
    fig = px.scatter_matrix(df, color="color")
    assert np.all(fig.data[0].marker["color"] == np.array([1, 2, 3, 4]))


def test_int_col_names(constructor):
    # DataFrame with int column names
    lengths = constructor({"0": np.random.random(100)})
    fig = px.histogram(lengths, x="0")
    assert np.all(nw.from_native(lengths).to_numpy().flatten() == fig.data[0].x)
    # Numpy array
    ar = np.arange(100).reshape((10, 10))
    fig = px.scatter(ar, x=2, y=8)
    assert np.all(fig.data[0].x == ar[:, 2])


def test_data_frame_from_dict():
    fig = px.scatter({"time": [0, 1], "money": [1, 2]}, x="time", y="money")
    assert fig.data[0].hovertemplate == "time=%{x}<br>money=%{y}<extra></extra>"
    assert np.all(fig.data[0].x == [0, 1])


def test_arguments_not_modified(backend):
    iris = nw.from_native(px.data.iris(return_type=backend))
    petal_length = iris.get_column("petal_length").to_native()
    hover_data = [iris.get_column("sepal_length").to_native()]
    px.scatter(iris.to_native(), x=petal_length, y="petal_width", hover_data=hover_data)
    assert petal_length.equals(petal_length)
    assert iris.get_column("sepal_length").to_native().equals(hover_data[0])


def test_pass_df_columns(backend):
    tips = nw.from_native(px.data.tips(return_type=backend))
    fig = px.histogram(
        tips.to_native(),
        x="total_bill",
        y="tip",
        color="sex",
        marginal="rug",
        hover_data=tips.columns,
    )
    # the "- 2" is because we re-use x and y in the hovertemplate where possible
    assert fig.data[1].hovertemplate.count("customdata") == len(tips.columns) - 2
    tips_copy = nw.from_native(px.data.tips(return_type=backend))
    assert tips_copy.columns == tips.columns


def test_size_column(request, backend):
    if backend == "pyarrow":
        # By converting to native, we lose the name for pyarrow chunked_array
        # and the assertions fail
        request.applymarker(pytest.mark.xfail)
    tips = nw.from_native(px.data.tips(return_type=backend))
    fig = px.scatter(
        tips.to_native(),
        x=tips.get_column("size").to_native(),
        y=tips.get_column("tip").to_native(),
    )
    assert fig.data[0].hovertemplate == "size=%{x}<br>tip=%{y}<extra></extra>"


def test_identity_map():
    fig = px.scatter(
        x=[1, 2],
        y=[1, 2],
        symbol=["a", "b"],
        color=["red", "blue"],
        color_discrete_map=px.IdentityMap(),
    )
    assert fig.data[0].marker.color == "red"
    assert fig.data[1].marker.color == "blue"
    assert "color=" not in fig.data[0].hovertemplate
    assert "symbol=" in fig.data[0].hovertemplate
    assert fig.layout.legend.title.text == "symbol"

    fig = px.scatter(
        x=[1, 2],
        y=[1, 2],
        symbol=["a", "b"],
        color=["red", "blue"],
        color_discrete_map="identity",
    )
    assert fig.data[0].marker.color == "red"
    assert fig.data[1].marker.color == "blue"
    assert "color=" not in fig.data[0].hovertemplate
    assert "symbol=" in fig.data[0].hovertemplate
    assert fig.layout.legend.title.text == "symbol"


def test_constants():
    fig = px.scatter(x=px.Constant(1), y=[1, 2])
    assert fig.data[0].x[0] == 1
    assert fig.data[0].x[1] == 1
    assert "x=" in fig.data[0].hovertemplate

    fig = px.scatter(x=px.Constant(1, label="time"), y=[1, 2])
    assert fig.data[0].x[0] == 1
    assert fig.data[0].x[1] == 1
    assert "x=" not in fig.data[0].hovertemplate
    assert "time=" in fig.data[0].hovertemplate

    fig = px.scatter(
        x=[1, 2],
        y=[1, 2],
        symbol=["a", "b"],
        color=px.Constant("red", label="the_identity_label"),
        hover_data=[px.Constant("data", label="the_data")],
        color_discrete_map=px.IdentityMap(),
    )
    assert fig.data[0].marker.color == "red"
    assert fig.data[0].customdata[0][0] == "data"
    assert fig.data[1].marker.color == "red"
    assert "color=" not in fig.data[0].hovertemplate
    assert "the_identity_label=" not in fig.data[0].hovertemplate
    assert "symbol=" in fig.data[0].hovertemplate
    assert "the_data=" in fig.data[0].hovertemplate
    assert fig.layout.legend.title.text == "symbol"


def test_ranges():
    fig = px.scatter(x=px.Range(), y=[1, 2], hover_data=[px.Range()])
    assert fig.data[0].x[0] == 0
    assert fig.data[0].x[1] == 1
    assert fig.data[0].customdata[0][0] == 0
    assert fig.data[0].customdata[1][0] == 1
    assert "x=" in fig.data[0].hovertemplate

    fig = px.scatter(x=px.Range(label="time"), y=[1, 2])
    assert fig.data[0].x[0] == 0
    assert fig.data[0].x[1] == 1
    assert "x=" not in fig.data[0].hovertemplate
    assert "time=" in fig.data[0].hovertemplate


@pytest.mark.parametrize(
    "fn",
    [px.scatter, px.line, px.area, px.violin, px.box, px.strip]
    + [px.bar, px.funnel, px.histogram],
)
@pytest.mark.parametrize(
    "x,y,result",
    [
        ("numerical", "categorical", "h"),
        ("categorical", "numerical", "v"),
        ("categorical", "categorical", "v"),
        ("numerical", "numerical", "v"),
        ("numerical", "none", "h"),
        ("categorical", "none", "h"),
        ("none", "categorical", "v"),
        ("none", "numerical", "v"),
    ],
)
def test_auto_orient_x_and_y(fn, x, y, result):
    series = dict(categorical=["a", "a", "b", "b"], numerical=[1, 2, 3, 4], none=None)

    if "none" not in [x, y]:
        assert fn(x=series[x], y=series[y]).data[0].orientation == result
    else:
        if fn == px.histogram or (fn == px.bar and "categorical" in [x, y]):
            assert fn(x=series[x], y=series[y]).data[0].orientation != result
        else:
            assert fn(x=series[x], y=series[y]).data[0].orientation == result


def test_histogram_auto_orient():
    numerical = [1, 2, 3, 4]
    assert px.histogram(x=numerical, nbins=5).data[0].nbinsx == 5
    assert px.histogram(y=numerical, nbins=5).data[0].nbinsy == 5
    assert px.histogram(x=numerical, y=numerical, nbins=5).data[0].nbinsx == 5


def test_auto_histfunc():
    a = [1, 2]
    assert px.histogram(x=a).data[0].histfunc is None
    assert px.histogram(y=a).data[0].histfunc is None
    assert px.histogram(x=a, y=a).data[0].histfunc == "sum"
    assert px.histogram(x=a, y=a, histfunc="avg").data[0].histfunc == "avg"

    assert px.density_heatmap(x=a, y=a).data[0].histfunc is None
    assert px.density_heatmap(x=a, y=a, z=a).data[0].histfunc == "sum"
    assert px.density_heatmap(x=a, y=a, z=a, histfunc="avg").data[0].histfunc == "avg"


@pytest.mark.parametrize(
    "fn,mode", [(px.violin, "violinmode"), (px.box, "boxmode"), (px.strip, "boxmode")]
)
@pytest.mark.parametrize(
    "x,y,color,result",
    [
        ("categorical1", "numerical", None, "group"),
        ("categorical1", "numerical", "categorical2", "group"),
        ("categorical1", "numerical", "categorical1", "overlay"),
        ("numerical", "categorical1", None, "group"),
        ("numerical", "categorical1", "categorical2", "group"),
        ("numerical", "categorical1", "categorical1", "overlay"),
    ],
)
def test_auto_boxlike_overlay(constructor, fn, mode, x, y, color, result):
    df = constructor(
        dict(
            categorical1=["a", "a", "b", "b"],
            categorical2=["a", "a", "b", "b"],
            numerical=[1, 2, 3, 4],
        )
    )
    assert fn(df, x=x, y=y, color=color).layout[mode] == result


@pytest.mark.parametrize("fn", [px.scatter, px.line, px.area, px.bar])
def test_x_or_y(fn):
    categorical = ["a", "a", "b", "b"]
    numerical = [1, 2, 3, 4]
    constant = [1, 1, 1, 1]
    range_4 = [0, 1, 2, 3]
    index = [11, 12, 13, 14]
    numerical_df = pd.DataFrame(dict(col=numerical), index=index)
    categorical_df = pd.DataFrame(dict(col=categorical), index=index)

    fig = fn(x=numerical)
    assert list(fig.data[0].x) == numerical
    assert list(fig.data[0].y) == range_4
    assert fig.data[0].orientation == "h"
    fig = fn(y=numerical)
    assert list(fig.data[0].x) == range_4
    assert list(fig.data[0].y) == numerical
    assert fig.data[0].orientation == "v"
    fig = fn(numerical_df, x="col")
    assert list(fig.data[0].x) == numerical
    assert list(fig.data[0].y) == index
    assert fig.data[0].orientation == "h"
    fig = fn(numerical_df, y="col")
    assert list(fig.data[0].x) == index
    assert list(fig.data[0].y) == numerical
    assert fig.data[0].orientation == "v"

    if fn != px.bar:
        fig = fn(x=categorical)
        assert list(fig.data[0].x) == categorical
        assert list(fig.data[0].y) == range_4
        assert fig.data[0].orientation == "h"
        fig = fn(y=categorical)
        assert list(fig.data[0].x) == range_4
        assert list(fig.data[0].y) == categorical
        assert fig.data[0].orientation == "v"
        fig = fn(categorical_df, x="col")
        assert list(fig.data[0].x) == categorical
        assert list(fig.data[0].y) == index
        assert fig.data[0].orientation == "h"
        fig = fn(categorical_df, y="col")
        assert list(fig.data[0].x) == index
        assert list(fig.data[0].y) == categorical
        assert fig.data[0].orientation == "v"

    else:
        fig = fn(x=categorical)
        assert list(fig.data[0].x) == categorical
        assert list(fig.data[0].y) == constant
        assert fig.data[0].orientation == "v"
        fig = fn(y=categorical)
        assert list(fig.data[0].x) == constant
        assert list(fig.data[0].y) == categorical
        assert fig.data[0].orientation == "h"
        fig = fn(categorical_df, x="col")
        assert list(fig.data[0].x) == categorical
        assert list(fig.data[0].y) == constant
        assert fig.data[0].orientation == "v"
        fig = fn(categorical_df, y="col")
        assert list(fig.data[0].x) == constant
        assert list(fig.data[0].y) == categorical
        assert fig.data[0].orientation == "h"


def test_no_futurewarning():
    with warnings.catch_warnings(record=True) as warn_list:
        _ = px.scatter(
            x=[15, 20, 29],
            y=[10, 20, 30],
            color=["Category 1", "Category 2", "Category 1"],
        )
    future_warnings = [
        warn for warn in warn_list if issubclass(warn.category, FutureWarning)
    ]
    assert len(future_warnings) == 0, "FutureWarning(s) raised!"
