import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from plotly.express._core import build_dataframe
from pandas.util.testing import assert_frame_equal


def test_wide_mode_external():
    df = pd.DataFrame(dict(a=[1, 2, 3], b=[4, 5, 6], c=[7, 8, 9]), index=[11, 12, 13])
    for px_fn in [px.scatter, px.line, px.area, px.bar]:
        fig = px_fn(df)
        assert len(fig.data) == 3
        assert list(fig.data[0].x) == [11, 12, 13]
        assert list(fig.data[0].y) == [1, 2, 3]
        assert list(fig.data[1].x) == [11, 12, 13]
        assert list(fig.data[1].y) == [4, 5, 6]
        assert fig.layout.xaxis.title.text == "index"
        assert fig.layout.yaxis.title.text == "_value_"
        assert fig.layout.legend.title.text == "_column_"
        if px_fn in [px.area, px.bar]:
            fig = px_fn(df, orientation="h")
            assert len(fig.data) == 3
            assert list(fig.data[0].y) == [11, 12, 13]
            assert list(fig.data[0].x) == [1, 2, 3]
            assert list(fig.data[1].y) == [11, 12, 13]
            assert list(fig.data[1].x) == [4, 5, 6]
            assert fig.layout.yaxis.title.text == "index"
            assert fig.layout.xaxis.title.text == "_value_"
            assert fig.layout.legend.title.text == "_column_"
    for px_fn in [px.violin, px.box, px.strip]:
        fig = px_fn(df)
        assert len(fig.data) == 1
        assert list(fig.data[0].x) == ["a"] * 3 + ["b"] * 3 + ["c"] * 3
        assert list(fig.data[0].y) == list(range(1, 10))
        assert fig.layout.yaxis.title.text == "_value_"
        assert fig.layout.xaxis.title.text == "_column_"
        fig = px_fn(df, orientation="h")
        assert len(fig.data) == 1
        assert list(fig.data[0].y) == ["a"] * 3 + ["b"] * 3 + ["c"] * 3
        assert list(fig.data[0].x) == list(range(1, 10))
        assert fig.layout.xaxis.title.text == "_value_"
        assert fig.layout.yaxis.title.text == "_column_"
    for px_fn in [px.histogram]:
        fig = px_fn(df)
        assert len(fig.data) == 3
        assert list(fig.data[1].x) == [4, 5, 6]
        assert fig.layout.legend.title.text == "_column_"
        assert fig.layout.xaxis.title.text == "_value_"
        fig = px_fn(df, orientation="h")
        assert len(fig.data) == 3
        assert list(fig.data[1].y) == [4, 5, 6]
        assert fig.layout.legend.title.text == "_column_"
        assert fig.layout.yaxis.title.text == "_value_"


def test_wide_mode_labels_external():
    df = pd.DataFrame(dict(a=[1, 2, 3], b=[4, 5, 6], c=[7, 8, 9]), index=[11, 12, 13])
    fig = px.bar(df)
    assert fig.layout.xaxis.title.text == "index"
    assert fig.layout.yaxis.title.text == "_value_"
    assert fig.layout.legend.title.text == "_column_"
    labels = dict(index="my index", _value_="my value", _column_="my column")
    fig = px.bar(df, labels=labels)
    assert fig.layout.xaxis.title.text == "my index"
    assert fig.layout.yaxis.title.text == "my value"
    assert fig.layout.legend.title.text == "my column"
    df.index.name = "my index"
    df.columns.name = "my column"
    fig = px.bar(df)
    assert fig.layout.xaxis.title.text == "my index"
    assert fig.layout.yaxis.title.text == "_value_"
    assert fig.layout.legend.title.text == "my column"


def test_wide_mode_internal():
    df_in = pd.DataFrame(dict(a=[1, 2, 3], b=[4, 5, 6]), index=[11, 12, 13])

    def extract_and_check_df(args_out):
        df_out = args_out.pop("data_frame")
        assert_frame_equal(
            df_out.sort_index(axis=1),
            pd.DataFrame(
                dict(
                    index=[11, 12, 13, 11, 12, 13],
                    _column_=["a", "a", "a", "b", "b", "b"],
                    _value_=[1, 2, 3, 4, 5, 6],
                )
            ).sort_index(axis=1),
        )
        return args_out

    for trace_type in [go.Scatter, go.Bar]:
        args_in = dict(data_frame=df_in.copy(), color=None)
        args_out = extract_and_check_df(build_dataframe(args_in, trace_type))
        assert args_out == dict(x="index", y="_value_", color="_column_")

        # now we check with orientation
        args_in = dict(data_frame=df_in.copy(), color=None, orientation="h")
        args_out = extract_and_check_df(build_dataframe(args_in, trace_type))
        assert args_out == dict(
            y="index", x="_value_", color="_column_", orientation="h"
        )

    for trace_type in [go.Violin, go.Box]:
        args_in = dict(data_frame=df_in.copy(), color=None)
        args_out = extract_and_check_df(build_dataframe(args_in, trace_type))
        assert args_out == dict(x="_column_", y="_value_", color=None)

        # now we check with orientation
        args_in = dict(data_frame=df_in.copy(), color=None, orientation="h")
        args_out = extract_and_check_df(build_dataframe(args_in, trace_type))
        assert args_out == dict(y="_column_", x="_value_", color=None, orientation="h")

    for trace_type in [go.Histogram]:
        args_in = dict(data_frame=df_in.copy(), color=None)
        args_out = extract_and_check_df(build_dataframe(args_in, trace_type))
        assert args_out == dict(x="_value_", color="_column_")

        # now we check with orientation
        args_in = dict(data_frame=df_in.copy(), color=None, orientation="h")
        args_out = extract_and_check_df(build_dataframe(args_in, trace_type))
        assert args_out == dict(y="_value_", color="_column_", orientation="h")
