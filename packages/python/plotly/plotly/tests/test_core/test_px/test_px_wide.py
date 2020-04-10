import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from plotly.express._core import build_dataframe
from pandas.util.testing import assert_frame_equal


def test_wide_mode_external():
    # here we test this feature "black box" style by calling actual PX functions and
    # inspecting the figure... this is important but clunky, and is mostly a smoke test
    # allowing us to do more "white box" testing below

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
    # here we prove that the _uglylabels_ can be renamed using the usual labels kwarg
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
    # here we do basic exhaustive testing of the various graph_object permutations
    # via build_dataframe directly, which leads to more compact test code:
    # we pass in args (which includes df) and look at how build_dataframe mutates
    # both args and the df, and assume that since the rest of the downstream PX
    # machinery has not wide-mode-specific code, and the tests above pass, that this is
    # enough to prove things work

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
        assert args_out == dict(
            x="index", y="_value_", color="_column_", orientation="v"
        )

        # now we check with orientation
        args_in = dict(data_frame=df_in.copy(), color=None, orientation="h")
        args_out = extract_and_check_df(build_dataframe(args_in, trace_type))
        assert args_out == dict(
            y="index", x="_value_", color="_column_", orientation="h"
        )

    for trace_type in [go.Violin, go.Box]:
        args_in = dict(data_frame=df_in.copy(), color=None)
        args_out = extract_and_check_df(build_dataframe(args_in, trace_type))
        assert args_out == dict(x="_column_", y="_value_", color=None, orientation="v")

        # now we check with orientation
        args_in = dict(data_frame=df_in.copy(), color=None, orientation="h")
        args_out = extract_and_check_df(build_dataframe(args_in, trace_type))
        assert args_out == dict(y="_column_", x="_value_", color=None, orientation="h")

    for trace_type in [go.Histogram]:
        args_in = dict(data_frame=df_in.copy(), color=None)
        args_out = extract_and_check_df(build_dataframe(args_in, trace_type))
        assert args_out == dict(x="_value_", color="_column_", orientation="v")

        # now we check with orientation
        args_in = dict(data_frame=df_in.copy(), color=None, orientation="h")
        args_out = extract_and_check_df(build_dataframe(args_in, trace_type))
        assert args_out == dict(y="_value_", color="_column_", orientation="h")


def test_wide_mode_internal_special_cases():
    # given all of the above tests, and given that the melt() code is not sensitive
    # to the trace type, we can do all sorts of special-case testing just by focusing
    # on build_dataframe(args, go.Scatter) for various values of args, and looking at
    # how args and df get mutated

    def assert_df_and_args(df_in, args_in, args_expect, df_expect):
        args_in["data_frame"] = df_in
        args_out = build_dataframe(args_in, go.Scatter)
        df_out = args_out.pop("data_frame")
        # print(df_out.info())
        # print(df_expect.info())
        assert_frame_equal(
            df_out.sort_index(axis=1), df_expect.sort_index(axis=1),
        )
        assert args_out == args_expect

    # input is single bare array: column comes out as string "0"
    assert_df_and_args(
        df_in=[1, 2, 3],
        args_in=dict(x=None, y=None, color=None),
        args_expect=dict(x="index", y="_value_", color="_column_", orientation="v"),
        df_expect=pd.DataFrame(
            dict(index=[0, 1, 2], _value_=[1, 2, 3], _column_=["0", "0", "0"])
        ),
    )

    # input is single bare Series: column comes out as string "0"
    assert_df_and_args(
        df_in=pd.Series([1, 2, 3]),
        args_in=dict(x=None, y=None, color=None),
        args_expect=dict(x="index", y="_value_", color="_column_", orientation="v"),
        df_expect=pd.DataFrame(
            dict(index=[0, 1, 2], _value_=[1, 2, 3], _column_=["0", "0", "0"])
        ),
    )

    # input is a Series from a DF: we pick up the name and index values automatically
    df = pd.DataFrame(dict(my_col=[1, 2, 3]), index=["a", "b", "c"])
    assert_df_and_args(
        df_in=df["my_col"],
        args_in=dict(x=None, y=None, color=None),
        args_expect=dict(x="index", y="_value_", color="_column_", orientation="v"),
        df_expect=pd.DataFrame(
            dict(
                index=["a", "b", "c"],
                _value_=[1, 2, 3],
                _column_=["my_col", "my_col", "my_col"],
            )
        ),
    )

    # input is an index from a DF: treated like a Series basically
    df = pd.DataFrame(dict(my_col=[1, 2, 3]), index=["a", "b", "c"])
    df.index.name = "my_index"
    assert_df_and_args(
        df_in=df.index,
        args_in=dict(x=None, y=None, color=None),
        args_expect=dict(x="index", y="_value_", color="_column_", orientation="v"),
        df_expect=pd.DataFrame(
            dict(
                index=[0, 1, 2],
                _value_=["a", "b", "c"],
                _column_=["my_index", "my_index", "my_index"],
            )
        ),
    )

    # input is a data frame with named row and col indices: we grab those
    df = pd.DataFrame(dict(my_col=[1, 2, 3]), index=["a", "b", "c"])
    df.index.name = "my_index"
    df.columns.name = "my_col_name"
    assert_df_and_args(
        df_in=df,
        args_in=dict(x=None, y=None, color=None),
        args_expect=dict(
            x="my_index", y="_value_", color="my_col_name", orientation="v"
        ),
        df_expect=pd.DataFrame(
            dict(
                my_index=["a", "b", "c"],
                _value_=[1, 2, 3],
                my_col_name=["my_col", "my_col", "my_col"],
            )
        ),
    )

    # input is array of arrays: treated as rows, columns come out as string "0", "1"
    assert_df_and_args(
        df_in=[[1, 2], [4, 5]],
        args_in=dict(x=None, y=None, color=None),
        args_expect=dict(x="index", y="_value_", color="_column_", orientation="v"),
        df_expect=pd.DataFrame(
            dict(
                index=[0, 1, 0, 1], _value_=[1, 4, 2, 5], _column_=["0", "0", "1", "1"],
            )
        ),
    )

    # partial-melting by assigning symbol: we pick up that column and don't melt it
    assert_df_and_args(
        df_in=pd.DataFrame(dict(a=[1, 2], b=[3, 4], symbol_col=["q", "r"])),
        args_in=dict(x=None, y=None, color=None, symbol="symbol_col"),
        args_expect=dict(
            x="index",
            y="_value_",
            color="_column_",
            symbol="symbol_col",
            orientation="v",
        ),
        df_expect=pd.DataFrame(
            dict(
                index=[0, 1, 0, 1],
                _value_=[1, 2, 3, 4],
                _column_=["a", "a", "b", "b"],
                symbol_col=["q", "r", "q", "r"],
            )
        ),
    )

    # partial-melting by assigning the same column twice: we pick it up once
    assert_df_and_args(
        df_in=pd.DataFrame(dict(a=[1, 2], b=[3, 4], symbol_col=["q", "r"])),
        args_in=dict(
            x=None, y=None, color=None, symbol="symbol_col", custom_data=["symbol_col"],
        ),
        args_expect=dict(
            x="index",
            y="_value_",
            color="_column_",
            symbol="symbol_col",
            custom_data=["symbol_col"],
            orientation="v",
        ),
        df_expect=pd.DataFrame(
            dict(
                index=[0, 1, 0, 1],
                _value_=[1, 2, 3, 4],
                _column_=["a", "a", "b", "b"],
                symbol_col=["q", "r", "q", "r"],
            )
        ),
    )

    # partial-melting by assigning more than one column: we pick them both up
    assert_df_and_args(
        df_in=pd.DataFrame(
            dict(a=[1, 2], b=[3, 4], symbol_col=["q", "r"], data_col=["i", "j"])
        ),
        args_in=dict(
            x=None, y=None, color=None, symbol="symbol_col", custom_data=["data_col"],
        ),
        args_expect=dict(
            x="index",
            y="_value_",
            color="_column_",
            symbol="symbol_col",
            custom_data=["data_col"],
            orientation="v",
        ),
        df_expect=pd.DataFrame(
            dict(
                index=[0, 1, 0, 1],
                _value_=[1, 2, 3, 4],
                _column_=["a", "a", "b", "b"],
                symbol_col=["q", "r", "q", "r"],
                data_col=["i", "j", "i", "j"],
            )
        ),
    )

    # partial-melting by assigning symbol to a bare array: we pick it up with the attr name
    assert_df_and_args(
        df_in=pd.DataFrame(dict(a=[1, 2], b=[3, 4])),
        args_in=dict(x=None, y=None, color=None, symbol=["q", "r"]),
        args_expect=dict(
            x="index", y="_value_", color="_column_", symbol="symbol", orientation="v"
        ),
        df_expect=pd.DataFrame(
            dict(
                index=[0, 1, 0, 1],
                _value_=[1, 2, 3, 4],
                _column_=["a", "a", "b", "b"],
                symbol=["q", "r", "q", "r"],
            )
        ),
    )

    # assigning color to _column_ explicitly: just works
    assert_df_and_args(
        df_in=pd.DataFrame(dict(a=[1, 2], b=[3, 4])),
        args_in=dict(x=None, y=None, color="_column_"),
        args_expect=dict(x="index", y="_value_", color="_column_", orientation="v"),
        df_expect=pd.DataFrame(
            dict(
                index=[0, 1, 0, 1], _value_=[1, 2, 3, 4], _column_=["a", "a", "b", "b"]
            )
        ),
    )

    # assigning color to a different column: _column_ drops out of args
    assert_df_and_args(
        df_in=pd.DataFrame(dict(a=[1, 2], b=[3, 4], color_col=["q", "r"])),
        args_in=dict(x=None, y=None, color="color_col"),
        args_expect=dict(x="index", y="_value_", color="color_col", orientation="v"),
        df_expect=pd.DataFrame(
            dict(
                index=[0, 1, 0, 1],
                _value_=[1, 2, 3, 4],
                _column_=["a", "a", "b", "b"],
                color_col=["q", "r", "q", "r"],
            )
        ),
    )

    # assigning _column_ to something else: just works
    assert_df_and_args(
        df_in=pd.DataFrame(dict(a=[1, 2], b=[3, 4])),
        args_in=dict(x=None, y=None, color=None, symbol="_column_"),
        args_expect=dict(
            x="index", y="_value_", color="_column_", symbol="_column_", orientation="v"
        ),
        df_expect=pd.DataFrame(
            dict(
                index=[0, 1, 0, 1], _value_=[1, 2, 3, 4], _column_=["a", "a", "b", "b"],
            )
        ),
    )

    # swapping symbol and color: just works
    assert_df_and_args(
        df_in=pd.DataFrame(dict(a=[1, 2], b=[3, 4], color_col=["q", "r"])),
        args_in=dict(x=None, y=None, color="color_col", symbol="_column_"),
        args_expect=dict(
            x="index",
            y="_value_",
            color="color_col",
            symbol="_column_",
            orientation="v",
        ),
        df_expect=pd.DataFrame(
            dict(
                index=[0, 1, 0, 1],
                _value_=[1, 2, 3, 4],
                _column_=["a", "a", "b", "b"],
                color_col=["q", "r", "q", "r"],
            )
        ),
    )

    # a DF with a named column index: have to use that instead of _column_
    df = pd.DataFrame(dict(a=[1, 2], b=[3, 4]))
    df.columns.name = "my_col_name"
    assert_df_and_args(
        df_in=df,
        args_in=dict(x=None, y=None, color=None, facet_row="my_col_name"),
        args_expect=dict(
            x="index",
            y="_value_",
            color="my_col_name",
            facet_row="my_col_name",
            orientation="v",
        ),
        df_expect=pd.DataFrame(
            dict(
                index=[0, 1, 0, 1],
                _value_=[1, 2, 3, 4],
                my_col_name=["a", "a", "b", "b"],
            )
        ),
    )

    # passing the DF index into some other attr: works
    df = pd.DataFrame(dict(a=[1, 2], b=[3, 4]))
    df.columns.name = "my_col_name"
    df.index.name = "my_index_name"
    assert_df_and_args(
        df_in=df,
        args_in=dict(x=None, y=None, color=None, hover_name=df.index),
        args_expect=dict(
            x="my_index_name",
            y="_value_",
            color="my_col_name",
            hover_name="my_index_name",
            orientation="v",
        ),
        df_expect=pd.DataFrame(
            dict(
                my_index_name=[0, 1, 0, 1],
                _value_=[1, 2, 3, 4],
                my_col_name=["a", "a", "b", "b"],
            )
        ),
    )

    # assigning _value_ to something: works
    df = pd.DataFrame(dict(a=[1, 2], b=[3, 4]))
    df.columns.name = "my_col_name"
    df.index.name = "my_index_name"
    assert_df_and_args(
        df_in=df,
        args_in=dict(x=None, y=None, color=None, hover_name="_value_"),
        args_expect=dict(
            x="my_index_name",
            y="_value_",
            color="my_col_name",
            hover_name="_value_",
            orientation="v",
        ),
        df_expect=pd.DataFrame(
            dict(
                my_index_name=[0, 1, 0, 1],
                _value_=[1, 2, 3, 4],
                my_col_name=["a", "a", "b", "b"],
            )
        ),
    )

    # assigning a px.Constant: works
    df = pd.DataFrame(dict(a=[1, 2], b=[3, 4]))
    df.columns.name = "my_col_name"
    df.index.name = "my_index_name"
    assert_df_and_args(
        df_in=df,
        args_in=dict(x=None, y=None, color=None, symbol=px.Constant(1)),
        args_expect=dict(
            x="my_index_name",
            y="_value_",
            color="my_col_name",
            symbol="symbol",
            orientation="v",
        ),
        df_expect=pd.DataFrame(
            dict(
                my_index_name=[0, 1, 0, 1],
                _value_=[1, 2, 3, 4],
                my_col_name=["a", "a", "b", "b"],
                symbol=[1, 1, 1, 1],
            )
        ),
    )
