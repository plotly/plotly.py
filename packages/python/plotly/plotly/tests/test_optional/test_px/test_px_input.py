import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import pytest
from plotly.express._core import build_dataframe
from pandas.testing import assert_frame_equal


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


def test_pandas_series():
    tips = px.data.tips()
    before_tip = tips.total_bill - tips.tip
    fig = px.bar(tips, x="day", y=before_tip)
    assert fig.data[0].hovertemplate == "day=%{x}<br>y=%{y}<extra></extra>"
    fig = px.bar(tips, x="day", y=before_tip, labels={"y": "bill"})
    assert fig.data[0].hovertemplate == "day=%{x}<br>bill=%{y}<extra></extra>"
    # lock down that we can pass df.col to facet_*
    fig = px.bar(tips, x="day", y="tip", facet_row=tips.day, facet_col=tips.day)
    assert fig.data[0].hovertemplate == "day=%{x}<br>tip=%{y}<extra></extra>"


def test_several_dataframes():
    df = pd.DataFrame(dict(x=[0, 1], y=[1, 10], z=[0.1, 0.8]))
    df2 = pd.DataFrame(dict(time=[23, 26], money=[100, 200]))
    fig = px.scatter(df, x="z", y=df2.money, size="x")
    assert (
        fig.data[0].hovertemplate
        == "z=%{x}<br>y=%{y}<br>x=%{marker.size}<extra></extra>"
    )
    fig = px.scatter(df2, x=df.z, y=df2.money, size=df.z)
    assert (
        fig.data[0].hovertemplate
        == "x=%{x}<br>money=%{y}<br>size=%{marker.size}<extra></extra>"
    )
    # Name conflict
    with pytest.raises(NameError) as err_msg:
        fig = px.scatter(df, x="z", y=df2.money, size="y")
    assert "A name conflict was encountered for argument 'y'" in str(err_msg.value)
    with pytest.raises(NameError) as err_msg:
        fig = px.scatter(df, x="z", y=df2.money, size=df.y)
    assert "A name conflict was encountered for argument 'y'" in str(err_msg.value)

    # No conflict when the dataframe is not given, fields are used
    df = pd.DataFrame(dict(x=[0, 1], y=[3, 4]))
    df2 = pd.DataFrame(dict(x=[3, 5], y=[23, 24]))
    fig = px.scatter(x=df.y, y=df2.y)
    assert np.all(fig.data[0].x == np.array([3, 4]))
    assert np.all(fig.data[0].y == np.array([23, 24]))
    assert fig.data[0].hovertemplate == "x=%{x}<br>y=%{y}<extra></extra>"

    df = pd.DataFrame(dict(x=[0, 1], y=[3, 4]))
    df2 = pd.DataFrame(dict(x=[3, 5], y=[23, 24]))
    df3 = pd.DataFrame(dict(y=[0.1, 0.2]))
    fig = px.scatter(x=df.y, y=df2.y, size=df3.y)
    assert np.all(fig.data[0].x == np.array([3, 4]))
    assert np.all(fig.data[0].y == np.array([23, 24]))
    assert (
        fig.data[0].hovertemplate
        == "x=%{x}<br>y=%{y}<br>size=%{marker.size}<extra></extra>"
    )

    df = pd.DataFrame(dict(x=[0, 1], y=[3, 4]))
    df2 = pd.DataFrame(dict(x=[3, 5], y=[23, 24]))
    df3 = pd.DataFrame(dict(y=[0.1, 0.2]))
    fig = px.scatter(x=df.y, y=df2.y, hover_data=[df3.y])
    assert np.all(fig.data[0].x == np.array([3, 4]))
    assert np.all(fig.data[0].y == np.array([23, 24]))
    assert (
        fig.data[0].hovertemplate
        == "x=%{x}<br>y=%{y}<br>hover_data_0=%{customdata[0]}<extra></extra>"
    )


def test_name_heuristics():
    df = pd.DataFrame(dict(x=[0, 1], y=[3, 4], z=[0.1, 0.2]))
    fig = px.scatter(df, x=df.y, y=df.x, size=df.y)
    assert np.all(fig.data[0].x == np.array([3, 4]))
    assert np.all(fig.data[0].y == np.array([0, 1]))
    assert fig.data[0].hovertemplate == "y=%{marker.size}<br>x=%{y}<extra></extra>"


def test_repeated_name():
    iris = px.data.iris()
    fig = px.scatter(
        iris,
        x="sepal_width",
        y="sepal_length",
        hover_data=["petal_length", "petal_width", "species_id"],
        custom_data=["species_id", "species"],
    )
    assert fig.data[0].customdata.shape[1] == 4


def test_arrayattrable_numpy():
    tips = px.data.tips()
    fig = px.scatter(
        tips, x="total_bill", y="tip", hover_data=[np.random.random(tips.shape[0])]
    )
    assert (
        fig.data[0]["hovertemplate"]
        == "total_bill=%{x}<br>tip=%{y}<br>hover_data_0=%{customdata[0]}<extra></extra>"
    )
    tips = px.data.tips()
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


def test_wrong_dimensions_mixed_case():
    with pytest.raises(ValueError) as err_msg:
        df = pd.DataFrame(dict(time=[1, 2, 3], temperature=[20, 30, 25]))
        px.scatter(df, x="time", y="temperature", color=[1, 3, 9, 5])
    assert "All arguments should have the same length." in str(err_msg.value)


def test_wrong_dimensions():
    with pytest.raises(ValueError) as err_msg:
        px.scatter(px.data.tips(), x="tip", y=[1, 2, 3])
    assert "All arguments should have the same length." in str(err_msg.value)
    # the order matters
    with pytest.raises(ValueError) as err_msg:
        px.scatter(px.data.tips(), x=[1, 2, 3], y="tip")
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
    assert_frame_equal(df.sort_index(axis=1), out["data_frame"].sort_index(axis=1))
    out.pop("data_frame")
    assert out == output

    # Arrays
    args = dict(x=np.array([1, 2, 3]), y=np.array([2, 3, 4]), color=[1, 3, 9])
    output = {key: key for key in args}
    df = pd.DataFrame(args)
    args["data_frame"] = None
    out = build_dataframe(args, go.Scatter)
    assert_frame_equal(df.sort_index(axis=1), out["data_frame"].sort_index(axis=1))
    out.pop("data_frame")
    assert out == output


def test_build_df_with_index():
    tips = px.data.tips()
    args = dict(data_frame=tips, x=tips.index, y="total_bill")
    out = build_dataframe(args, go.Scatter)
    assert_frame_equal(tips.reset_index()[out["data_frame"].columns], out["data_frame"])


def test_timezones():
    df = pd.DataFrame({"date": ["2015-04-04 19:31:30+1:00"], "value": [3]})
    df["date"] = pd.to_datetime(df["date"])
    args = dict(data_frame=df, x="date", y="value")
    out = build_dataframe(args, go.Scatter)
    assert str(out["data_frame"]["date"][0]) == str(df["date"][0])


def test_non_matching_index():
    df = pd.DataFrame(dict(y=[1, 2, 3]), index=["a", "b", "c"])

    expected = pd.DataFrame(dict(index=["a", "b", "c"], y=[1, 2, 3]))

    args = dict(data_frame=df, x=df.index, y="y")
    out = build_dataframe(args, go.Scatter)
    assert_frame_equal(expected, out["data_frame"])

    expected = pd.DataFrame(dict(x=["a", "b", "c"], y=[1, 2, 3]))

    args = dict(data_frame=None, x=df.index, y=df.y)
    out = build_dataframe(args, go.Scatter)
    assert_frame_equal(expected, out["data_frame"])

    args = dict(data_frame=None, x=["a", "b", "c"], y=df.y)
    out = build_dataframe(args, go.Scatter)
    assert_frame_equal(expected, out["data_frame"])


def test_splom_case():
    iris = px.data.iris()
    fig = px.scatter_matrix(iris)
    assert len(fig.data[0].dimensions) == len(iris.columns)
    dic = {"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]}
    fig = px.scatter_matrix(dic)
    assert np.all(fig.data[0].dimensions[0].values == np.array(dic["a"]))
    ar = np.arange(9).reshape((3, 3))
    fig = px.scatter_matrix(ar)
    assert np.all(fig.data[0].dimensions[0].values == ar[:, 0])


def test_int_col_names():
    # DataFrame with int column names
    lengths = pd.DataFrame(np.random.random(100))
    fig = px.histogram(lengths, x=0)
    assert np.all(np.array(lengths).flatten() == fig.data[0].x)
    # Numpy array
    ar = np.arange(100).reshape((10, 10))
    fig = px.scatter(ar, x=2, y=8)
    assert np.all(fig.data[0].x == ar[:, 2])


def test_data_frame_from_dict():
    fig = px.scatter({"time": [0, 1], "money": [1, 2]}, x="time", y="money")
    assert fig.data[0].hovertemplate == "time=%{x}<br>money=%{y}<extra></extra>"
    assert np.all(fig.data[0].x == [0, 1])


def test_arguments_not_modified():
    iris = px.data.iris()
    petal_length = iris.petal_length
    hover_data = [iris.sepal_length]
    px.scatter(iris, x=petal_length, y="petal_width", hover_data=hover_data)
    assert iris.petal_length.equals(petal_length)
    assert iris.sepal_length.equals(hover_data[0])


def test_pass_df_columns():
    tips = px.data.tips()
    fig = px.histogram(
        tips,
        x="total_bill",
        y="tip",
        color="sex",
        marginal="rug",
        hover_data=tips.columns,
    )
    # the "- 2" is because we re-use x and y in the hovertemplate where possible
    assert fig.data[1].hovertemplate.count("customdata") == len(tips.columns) - 2
    tips_copy = px.data.tips()
    assert tips_copy.columns.equals(tips.columns)


def test_size_column():
    df = px.data.tips()
    fig = px.scatter(df, x=df["size"], y=df.tip)
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
def test_auto_boxlike_overlay(fn, mode, x, y, color, result):
    df = pd.DataFrame(
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
