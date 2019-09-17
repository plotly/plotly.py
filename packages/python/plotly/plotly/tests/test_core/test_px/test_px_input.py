import plotly.express as px
import numpy as np
import pandas as pd
import pytest
import plotly.graph_objects as go
import plotly
from plotly.express._core import build_or_augment_dataframe
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


def test_numpy_labels():
    fig = px.scatter(
        x=[1, 2, 3], y=[2, 3, 4], labels={"x": "time"}
    )  # other labels will be kw arguments
    assert fig.data[0]["hovertemplate"] == "time=%{x}<br>y=%{y}"


def test_with_index():
    tips = px.data.tips()
    fig = px.scatter(tips, x=tips.index, y="total_bill")
    fig = px.scatter(tips, x=tips.index, y=tips.total_bill)
    fig = px.scatter(tips, x=tips.index, y=tips.total_bill)
    assert fig.data[0]["hovertemplate"] == "index=%{x}<br>total_bill=%{y}"
    # If we tinker with the column then the name is the one of the kw argument
    fig = px.scatter(tips, x=tips.index, y=10 * tips.total_bill)
    assert fig.data[0]["hovertemplate"] == "index=%{x}<br>y=%{y}"
    fig = px.scatter(tips, x=tips.index, y=tips.total_bill, labels={"index": "number"})
    assert fig.data[0]["hovertemplate"] == "number=%{x}<br>total_bill=%{y}"
    # We do not allow "x=index"
    with pytest.raises(ValueError) as err_msg:
        fig = px.scatter(tips, x="index", y="total_bill")
        assert (
            "ValueError: Value of 'x' is not the name of a column in 'data_frame'"
            in str(err_msg.value)
        )


def test_mixed_case():
    df = pd.DataFrame(dict(time=[1, 2, 3], temperature=[20, 30, 25]))
    fig = px.scatter(df, x="time", y="temperature", color=[1, 3, 9])


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
    with pytest.raises(ValueError):
        fig = px.scatter(px.data.tips(), x="bla", y="wrong")


def test_missing_data_frame():
    with pytest.raises(ValueError) as err_msg:
        fig = px.scatter(x="arg1", y="arg2")
        assert "String arguments are only possible when a DataFrame" in str(
            err_msg.value
        )


def test_wrong_dimensions_of_array():
    with pytest.raises(ValueError) as err_msg:
        fig = px.scatter(x=[1, 2, 3], y=[2, 3, 4, 5])
        assert "Length of values does not match length of index" in str(err_msg.value)


def test_wrong_dimensions_mixed_cqse():
    with pytest.raises(ValueError) as err_msg:
        df = pd.DataFrame(dict(time=[1, 2, 3], temperature=[20, 30, 25]))
        fig = px.scatter(df, x="time", y="temperature", color=[1, 3, 9, 5])
        assert "Length of values does not match length of index" in str(err_msg.value)


def test_build_df_from_lists():
    # Just lists
    args = dict(x=[1, 2, 3], y=[2, 3, 4], color=[1, 3, 9])
    output = {key: key for key in args}
    df = pd.DataFrame(args)
    args["data_frame"] = None
    out = build_or_augment_dataframe(args, all_attrables, array_attrables)
    assert_frame_equal(df.sort_index(axis=1), out["data_frame"].sort_index(axis=1))
    out.pop("data_frame")
    assert out == output

    # Arrays
    args = dict(x=np.array([1, 2, 3]), y=np.array([2, 3, 4]), color=[1, 3, 9])
    output = {key: key for key in args}
    df = pd.DataFrame(args)
    args["data_frame"] = None
    out = build_or_augment_dataframe(args, all_attrables, array_attrables)
    assert_frame_equal(df.sort_index(axis=1), out["data_frame"].sort_index(axis=1))
    out.pop("data_frame")
    assert out == output


def test_build_df_with_index():
    tips = px.data.tips()
    args = dict(data_frame=tips, x=tips.index, y="total_bill")
    changed_output = dict(x="index")
    out = build_or_augment_dataframe(args, all_attrables, array_attrables)
    assert_frame_equal(tips.reset_index()[out["data_frame"].columns], out["data_frame"])
    out.pop("data_frame")
    assert out == args


def test_splom_case():
    iris = px.data.iris()
    fig = px.scatter_matrix(iris)
    assert len(fig.data[0].dimensions) == len(iris.columns)
