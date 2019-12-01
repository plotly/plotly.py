import plotly.express as px
import numpy as np
import pandas as pd
import pytest
from plotly.express._core import build_dataframe
from pandas.util.testing import assert_frame_equal

attrables = (
    ["x", "y", "z", "a", "b", "c", "r", "theta", "size", "dimensions"]
    + ["custom_data", "hover_name", "hover_data", "text"]
    + ["error_x", "error_x_minus"]
    + ["error_y", "error_y_minus", "error_z", "error_z_minus"]
    + ["lat", "lon", "locations", "animation_group"]
)
array_attrables = ["dimensions", "custom_data", "hover_data"]
group_attrables = ["animation_frame", "facet_row", "facet_col", "line_group"]

all_attrables = attrables + group_attrables + ["color"]


def test_numpy():
    fig = px.scatter(x=[1, 2, 3], y=[2, 3, 4], color=[1, 3, 9])
    assert np.all(fig.data[0].x == np.array([1, 2, 3]))
    assert np.all(fig.data[0].y == np.array([2, 3, 4]))
    assert np.all(fig.data[0].marker.color == np.array([1, 3, 9]))


def test_numpy_labels():
    fig = px.scatter(
        x=[1, 2, 3], y=[2, 3, 4], labels={"x": "time"}
    )  # other labels will be kw arguments
    assert fig.data[0]["hovertemplate"] == "time=%{x}<br>y=%{y}"


def test_with_index():
    tips = px.data.tips()
    fig = px.scatter(tips, x=tips.index, y="total_bill")
    assert fig.data[0]["hovertemplate"] == "index=%{x}<br>total_bill=%{y}"
    fig = px.scatter(tips, x=tips.index, y=tips.total_bill)
    assert fig.data[0]["hovertemplate"] == "index=%{x}<br>total_bill=%{y}"
    fig = px.scatter(tips, x=tips.index, y=tips.total_bill, labels={"index": "number"})
    assert fig.data[0]["hovertemplate"] == "number=%{x}<br>total_bill=%{y}"
    # We do not allow "x=index"
    with pytest.raises(ValueError) as err_msg:
        fig = px.scatter(tips, x="index", y="total_bill")
        assert "To use the index, pass it in directly as `df.index`." in str(
            err_msg.value
        )
    tips = px.data.tips()
    tips.index.name = "item"
    fig = px.scatter(tips, x=tips.index, y="total_bill")
    assert fig.data[0]["hovertemplate"] == "item=%{x}<br>total_bill=%{y}"


def test_pandas_series():
    tips = px.data.tips()
    before_tip = tips.total_bill - tips.tip
    fig = px.bar(tips, x="day", y=before_tip)
    assert fig.data[0].hovertemplate == "day=%{x}<br>y=%{y}"
    fig = px.bar(tips, x="day", y=before_tip, labels={"y": "bill"})
    assert fig.data[0].hovertemplate == "day=%{x}<br>bill=%{y}"
    # lock down that we can pass df.col to facet_*
    fig = px.bar(tips, x="day", y="tip", facet_row=tips.day, facet_col=tips.day)
    assert fig.data[0].hovertemplate == "day=%{x}<br>tip=%{y}"


def test_several_dataframes():
    df = pd.DataFrame(dict(x=[0, 1], y=[1, 10], z=[0.1, 0.8]))
    df2 = pd.DataFrame(dict(time=[23, 26], money=[100, 200]))
    fig = px.scatter(df, x="z", y=df2.money, size="x")
    assert fig.data[0].hovertemplate == "z=%{x}<br>y=%{y}<br>x=%{marker.size}"
    fig = px.scatter(df2, x=df.z, y=df2.money, size=df.z)
    assert fig.data[0].hovertemplate == "x=%{x}<br>money=%{y}<br>size=%{marker.size}"
    # Name conflict
    with pytest.raises(NameError) as err_msg:
        fig = px.scatter(df, x="z", y=df2.money, size="y")
        assert "A name conflict was encountered for argument y" in str(err_msg.value)
    with pytest.raises(NameError) as err_msg:
        fig = px.scatter(df, x="z", y=df2.money, size=df.y)
        assert "A name conflict was encountered for argument y" in str(err_msg.value)

    # No conflict when the dataframe is not given, fields are used
    df = pd.DataFrame(dict(x=[0, 1], y=[3, 4]))
    df2 = pd.DataFrame(dict(x=[3, 5], y=[23, 24]))
    fig = px.scatter(x=df.y, y=df2.y)
    assert np.all(fig.data[0].x == np.array([3, 4]))
    assert np.all(fig.data[0].y == np.array([23, 24]))
    assert fig.data[0].hovertemplate == "x=%{x}<br>y=%{y}"

    df = pd.DataFrame(dict(x=[0, 1], y=[3, 4]))
    df2 = pd.DataFrame(dict(x=[3, 5], y=[23, 24]))
    df3 = pd.DataFrame(dict(y=[0.1, 0.2]))
    fig = px.scatter(x=df.y, y=df2.y, size=df3.y)
    assert np.all(fig.data[0].x == np.array([3, 4]))
    assert np.all(fig.data[0].y == np.array([23, 24]))
    assert fig.data[0].hovertemplate == "x=%{x}<br>y=%{y}<br>size=%{marker.size}"

    df = pd.DataFrame(dict(x=[0, 1], y=[3, 4]))
    df2 = pd.DataFrame(dict(x=[3, 5], y=[23, 24]))
    df3 = pd.DataFrame(dict(y=[0.1, 0.2]))
    fig = px.scatter(x=df.y, y=df2.y, hover_data=[df3.y])
    assert np.all(fig.data[0].x == np.array([3, 4]))
    assert np.all(fig.data[0].y == np.array([23, 24]))
    assert (
        fig.data[0].hovertemplate == "x=%{x}<br>y=%{y}<br>hover_data_0=%{customdata[0]}"
    )


def test_name_heuristics():
    df = pd.DataFrame(dict(x=[0, 1], y=[3, 4], z=[0.1, 0.2]))
    fig = px.scatter(df, x=df.y, y=df.x, size=df.y)
    assert np.all(fig.data[0].x == np.array([3, 4]))
    assert np.all(fig.data[0].y == np.array([0, 1]))
    assert fig.data[0].hovertemplate == "y=%{marker.size}<br>x=%{y}"


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
        == "total_bill=%{x}<br>tip=%{y}<br>hover_data_0=%{customdata[0]}"
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
        == "total_bill=%{x}<br>tip=%{y}<br>suppl=%{customdata[0]}"
    )


def test_wrong_column_name():
    with pytest.raises(ValueError) as err_msg:
        fig = px.scatter(px.data.tips(), x="bla", y="wrong")
        assert "Value of 'x' is not the name of a column in 'data_frame'" in str(
            err_msg.value
        )


def test_missing_data_frame():
    with pytest.raises(ValueError) as err_msg:
        fig = px.scatter(x="arg1", y="arg2")
        assert "String or int arguments are only possible" in str(err_msg.value)


def test_wrong_dimensions_of_array():
    with pytest.raises(ValueError) as err_msg:
        fig = px.scatter(x=[1, 2, 3], y=[2, 3, 4, 5])
        assert "All arguments should have the same length." in str(err_msg.value)


def test_wrong_dimensions_mixed_case():
    with pytest.raises(ValueError) as err_msg:
        df = pd.DataFrame(dict(time=[1, 2, 3], temperature=[20, 30, 25]))
        fig = px.scatter(df, x="time", y="temperature", color=[1, 3, 9, 5])
        assert "All arguments should have the same length." in str(err_msg.value)


def test_wrong_dimensions():
    with pytest.raises(ValueError) as err_msg:
        fig = px.scatter(px.data.tips(), x="tip", y=[1, 2, 3])
        assert "All arguments should have the same length." in str(err_msg.value)
    # the order matters
    with pytest.raises(ValueError) as err_msg:
        fig = px.scatter(px.data.tips(), x=[1, 2, 3], y="tip")
        assert "All arguments should have the same length." in str(err_msg.value)
    with pytest.raises(ValueError):
        fig = px.scatter(px.data.tips(), x=px.data.iris().index, y="tip")
        # assert "All arguments should have the same length." in str(err_msg.value)


def test_multiindex_raise_error():
    index = pd.MultiIndex.from_product(
        [[1, 2, 3], ["a", "b"]], names=["first", "second"]
    )
    df = pd.DataFrame(np.random.random((6, 3)), index=index, columns=["A", "B", "C"])
    # This is ok
    fig = px.scatter(df, x="A", y="B")
    with pytest.raises(TypeError) as err_msg:
        fig = px.scatter(df, x=df.index, y="B")
        assert "pandas MultiIndex is not supported by plotly express" in str(
            err_msg.value
        )


def test_build_df_from_lists():
    # Just lists
    args = dict(x=[1, 2, 3], y=[2, 3, 4], color=[1, 3, 9])
    output = {key: key for key in args}
    df = pd.DataFrame(args)
    args["data_frame"] = None
    out = build_dataframe(args, all_attrables, array_attrables)
    assert_frame_equal(df.sort_index(axis=1), out["data_frame"].sort_index(axis=1))
    out.pop("data_frame")
    assert out == output

    # Arrays
    args = dict(x=np.array([1, 2, 3]), y=np.array([2, 3, 4]), color=[1, 3, 9])
    output = {key: key for key in args}
    df = pd.DataFrame(args)
    args["data_frame"] = None
    out = build_dataframe(args, all_attrables, array_attrables)
    assert_frame_equal(df.sort_index(axis=1), out["data_frame"].sort_index(axis=1))
    out.pop("data_frame")
    assert out == output


def test_build_df_with_index():
    tips = px.data.tips()
    args = dict(data_frame=tips, x=tips.index, y="total_bill")
    out = build_dataframe(args, all_attrables, array_attrables)
    assert_frame_equal(tips.reset_index()[out["data_frame"].columns], out["data_frame"])


def test_non_matching_index():
    df = pd.DataFrame(dict(y=[1, 2, 3]), index=["a", "b", "c"])

    expected = pd.DataFrame(dict(x=["a", "b", "c"], y=[1, 2, 3]))

    args = dict(data_frame=df, x=df.index, y="y")
    out = build_dataframe(args, all_attrables, array_attrables)
    assert_frame_equal(expected, out["data_frame"])

    args = dict(data_frame=None, x=df.index, y=df.y)
    out = build_dataframe(args, all_attrables, array_attrables)
    assert_frame_equal(expected, out["data_frame"])

    args = dict(data_frame=None, x=["a", "b", "c"], y=df.y)
    out = build_dataframe(args, all_attrables, array_attrables)
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
    assert fig.data[0].hovertemplate == "time=%{x}<br>money=%{y}"
    assert np.all(fig.data[0].x == [0, 1])


def test_arguments_not_modified():
    iris = px.data.iris()
    petal_length = iris.petal_length
    hover_data = [iris.sepal_length]
    fig = px.scatter(iris, x=petal_length, y="petal_width", hover_data=hover_data)
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
    assert fig.data[1].hovertemplate.count("customdata") == len(tips.columns)
    tips_copy = px.data.tips()
    assert tips_copy.columns.equals(tips.columns)


def test_size_column():
    df = px.data.tips()
    fig = px.scatter(df, x=df["size"], y=df.tip)
    assert fig.data[0].hovertemplate == "size=%{x}<br>tip=%{y}"
