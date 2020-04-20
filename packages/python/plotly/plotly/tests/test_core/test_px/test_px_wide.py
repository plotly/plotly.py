import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from plotly.express._core import build_dataframe, _is_col_list
from pandas.testing import assert_frame_equal
import pytest


def test_is_col_list():
    df_input = pd.DataFrame(dict(a=[1, 2], b=[1, 2]))
    assert _is_col_list(df_input, ["a"])
    assert _is_col_list(df_input, ["a", "b"])
    assert _is_col_list(df_input, [[3, 4]])
    assert _is_col_list(df_input, [[3, 4], [3, 4]])
    assert not _is_col_list(df_input, pytest)
    assert not _is_col_list(df_input, False)
    assert not _is_col_list(df_input, ["a", 1])
    assert not _is_col_list(df_input, "a")
    assert not _is_col_list(df_input, 1)
    assert not _is_col_list(df_input, ["a", "b", "c"])
    assert not _is_col_list(df_input, [1, 2])
    df_input = pd.DataFrame([[1, 2], [1, 2]])
    assert _is_col_list(df_input, [0])
    assert _is_col_list(df_input, [0, 1])
    assert _is_col_list(df_input, [[3, 4]])
    assert _is_col_list(df_input, [[3, 4], [3, 4]])
    assert not _is_col_list(df_input, pytest)
    assert not _is_col_list(df_input, False)
    assert not _is_col_list(df_input, ["a", 1])
    assert not _is_col_list(df_input, "a")
    assert not _is_col_list(df_input, 1)
    assert not _is_col_list(df_input, [0, 1, 2])
    assert not _is_col_list(df_input, ["a", "b"])
    df_input = None
    assert _is_col_list(df_input, [[3, 4]])
    assert _is_col_list(df_input, [[3, 4], [3, 4]])
    assert not _is_col_list(df_input, [0])
    assert not _is_col_list(df_input, [0, 1])
    assert not _is_col_list(df_input, pytest)
    assert not _is_col_list(df_input, False)
    assert not _is_col_list(df_input, ["a", 1])
    assert not _is_col_list(df_input, "a")
    assert not _is_col_list(df_input, 1)
    assert not _is_col_list(df_input, [0, 1, 2])
    assert not _is_col_list(df_input, ["a", "b"])


@pytest.mark.parametrize(
    "px_fn",
    [px.scatter, px.line, px.area, px.bar, px.violin, px.box, px.strip]
    + [px.histogram, px.funnel, px.density_contour, px.density_heatmap],
)
@pytest.mark.parametrize("orientation", [None, "v", "h"])
@pytest.mark.parametrize("style", ["implicit", "explicit"])
def test_wide_mode_external(px_fn, orientation, style):
    # here we test this feature "black box" style by calling actual PX functions and
    # inspecting the figure... this is important but clunky, and is mostly a smoke test
    # allowing us to do more "white box" testing below

    if px_fn != px.funnel:
        x, y = ("y", "x") if orientation == "h" else ("x", "y")
    else:
        x, y = ("y", "x") if orientation != "v" else ("x", "y")
    xaxis, yaxis = x + "axis", y + "axis"

    df = pd.DataFrame(dict(a=[1, 2, 3], b=[4, 5, 6], c=[7, 8, 9]), index=[11, 12, 13])
    if style == "implicit":
        fig = px_fn(df, orientation=orientation)

    if px_fn in [px.scatter, px.line, px.area, px.bar, px.funnel, px.density_contour]:
        if style == "explicit":
            fig = px_fn(**{"data_frame": df, y: list(df.columns), x: df.index})
        assert len(fig.data) == 3
        assert list(fig.data[0][x]) == [11, 12, 13]
        assert list(fig.data[0][y]) == [1, 2, 3]
        assert list(fig.data[1][x]) == [11, 12, 13]
        assert list(fig.data[1][y]) == [4, 5, 6]
        assert fig.layout[xaxis].title.text == "index"
        assert fig.layout[yaxis].title.text == "_value_"
        assert fig.layout.legend.title.text == "_column_"
    if px_fn in [px.density_heatmap]:
        if style == "explicit":
            fig = px_fn(**{"data_frame": df, y: list(df.columns), x: df.index})
        assert len(fig.data) == 1
        assert list(fig.data[0][x]) == [11, 12, 13, 11, 12, 13, 11, 12, 13]
        assert list(fig.data[0][y]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
        assert fig.layout[xaxis].title.text == "index"
        assert fig.layout[yaxis].title.text == "_value_"
    if px_fn in [px.violin, px.box, px.strip]:
        if style == "explicit":
            fig = px_fn(**{"data_frame": df, y: list(df.columns)})
        assert len(fig.data) == 1
        assert list(fig.data[0][x]) == ["a"] * 3 + ["b"] * 3 + ["c"] * 3
        assert list(fig.data[0][y]) == list(range(1, 10))
        assert fig.layout[yaxis].title.text == "_value_"
        assert fig.layout[xaxis].title.text == "_column_"
    if px_fn in [px.histogram]:
        if style == "explicit":
            fig = px_fn(**{"data_frame": df, x: list(df.columns)})
        assert len(fig.data) == 3
        assert list(fig.data[1][x]) == [4, 5, 6]
        assert fig.layout.legend.title.text == "_column_"
        assert fig.layout[xaxis].title.text == "_value_"


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


# here we do basic exhaustive testing of the various graph_object permutations
# via build_dataframe directly, which leads to more compact test code:
# we pass in args (which includes df) and look at how build_dataframe mutates
# both args and the df, and assume that since the rest of the downstream PX
# machinery has no wide-mode-specific code, and the tests above pass, that this is
# enough to prove things work
@pytest.mark.parametrize(
    "trace_type,x,y,color",
    [
        (go.Scatter, "index", "_value_", "_column_"),
        (go.Histogram2dContour, "index", "_value_", "_column_"),
        (go.Histogram2d, "index", "_value_", None),
        (go.Bar, "index", "_value_", "_column_"),
        (go.Funnel, "index", "_value_", "_column_"),
        (go.Box, "_column_", "_value_", None),
        (go.Violin, "_column_", "_value_", None),
        (go.Histogram, "_value_", None, "_column_"),
    ],
)
@pytest.mark.parametrize("orientation", [None, "v", "h"])
def test_wide_mode_internal(trace_type, x, y, color, orientation):
    df_in = pd.DataFrame(dict(a=[1, 2, 3], b=[4, 5, 6]), index=[11, 12, 13])
    args_in = dict(data_frame=df_in, color=None, orientation=orientation)
    args_out = build_dataframe(args_in, trace_type)
    df_out = args_out.pop("data_frame")
    expected = dict(
        _column_=["a", "a", "a", "b", "b", "b"], _value_=[1, 2, 3, 4, 5, 6],
    )
    if x == "index":
        expected["index"] = [11, 12, 13, 11, 12, 13]
    assert_frame_equal(
        df_out.sort_index(axis=1), pd.DataFrame(expected).sort_index(axis=1),
    )
    if trace_type in [go.Histogram2dContour, go.Histogram2d]:
        if orientation is None or orientation == "v":
            assert args_out == dict(x=x, y=y, color=color)
        else:
            assert args_out == dict(x=y, y=x, color=color)
    else:
        if (orientation is None and trace_type != go.Funnel) or orientation == "v":
            assert args_out == dict(x=x, y=y, color=color, orientation="v")
        else:
            assert args_out == dict(x=y, y=x, color=color, orientation="h")


cases = []
for transpose in [True, False]:
    for tt in [go.Scatter, go.Bar, go.Funnel, go.Histogram2dContour, go.Histogram2d]:
        color = None if tt == go.Histogram2d else "_column_"
        df_in = dict(a=[1, 2], b=[3, 4])
        args = dict(x=None, y=["a", "b"], color=None, orientation=None)
        df_exp = dict(
            _column_=["a", "a", "b", "b"], _value_=[1, 2, 3, 4], index=[0, 1, 0, 1],
        )
        cases.append((tt, df_in, args, "index", "_value_", color, df_exp, transpose))

        df_in = dict(a=[1, 2], b=[3, 4], c=[5, 6])
        args = dict(x="c", y=["a", "b"], color=None, orientation=None)
        df_exp = dict(
            _column_=["a", "a", "b", "b"], _value_=[1, 2, 3, 4], c=[5, 6, 5, 6],
        )
        cases.append((tt, df_in, args, "c", "_value_", color, df_exp, transpose))

        args = dict(x=None, y=[[1, 2], [3, 4]], color=None, orientation=None)
        df_exp = dict(
            _column_=["_column__0", "_column__0", "_column__1", "_column__1"],
            _value_=[1, 2, 3, 4],
            index=[0, 1, 0, 1],
        )
        cases.append((tt, None, args, "index", "_value_", color, df_exp, transpose))

    for tt in [go.Bar]:  # bar categorical exception
        df_in = dict(a=["q", "r"], b=["s", "t"])
        args = dict(x=None, y=["a", "b"], color=None, orientation=None)
        df_exp = dict(
            _column_=["a", "a", "b", "b"],
            _value_=["q", "r", "s", "t"],
            index=[0, 1, 0, 1],
            _count_=[1, 1, 1, 1],
        )
        cases.append(
            (tt, df_in, args, "_value_", "_count_", "_column_", df_exp, transpose)
        )

    for tt in [go.Violin, go.Box]:
        df_in = dict(a=[1, 2], b=[3, 4])
        args = dict(x=None, y=["a", "b"], color=None, orientation=None)
        df_exp = dict(_column_=["a", "a", "b", "b"], _value_=[1, 2, 3, 4],)
        cases.append((tt, df_in, args, "_column_", "_value_", None, df_exp, transpose))

        df_in = dict(a=[1, 2], b=[3, 4], c=[5, 6])
        args = dict(x="c", y=["a", "b"], color=None, orientation=None)
        df_exp = dict(
            _column_=["a", "a", "b", "b"], _value_=[1, 2, 3, 4], c=[5, 6, 5, 6],
        )
        cases.append((tt, df_in, args, "c", "_value_", None, df_exp, transpose))

        args = dict(x=None, y=[[1, 2], [3, 4]], color=None, orientation=None)
        df_exp = dict(
            _column_=["_column__0", "_column__0", "_column__1", "_column__1"],
            _value_=[1, 2, 3, 4],
        )
        cases.append((tt, None, args, "_column_", "_value_", None, df_exp, transpose))

    for tt in [go.Histogram]:
        df_in = dict(a=[1, 2], b=[3, 4])
        args = dict(x=None, y=["a", "b"], color=None, orientation=None)
        df_exp = dict(_column_=["a", "a", "b", "b"], _value_=[1, 2, 3, 4],)
        cases.append((tt, df_in, args, None, "_value_", "_column_", df_exp, transpose))

        df_in = dict(a=[1, 2], b=[3, 4], c=[5, 6])
        args = dict(x="c", y=["a", "b"], color=None, orientation=None)
        df_exp = dict(
            _column_=["a", "a", "b", "b"], _value_=[1, 2, 3, 4], c=[5, 6, 5, 6],
        )
        cases.append((tt, df_in, args, "c", "_value_", "_column_", df_exp, transpose))

        args = dict(x=None, y=[[1, 2], [3, 4]], color=None, orientation=None)
        df_exp = dict(
            _column_=["_column__0", "_column__0", "_column__1", "_column__1"],
            _value_=[1, 2, 3, 4],
        )
        cases.append((tt, None, args, None, "_value_", "_column_", df_exp, transpose))


@pytest.mark.parametrize("tt,df_in,args_in,x,y,color,df_out_exp,transpose", cases)
def test_wide_x_or_y(tt, df_in, args_in, x, y, color, df_out_exp, transpose):
    if transpose:
        args_in["y"], args_in["x"] = args_in["x"], args_in["y"]
    args_in["data_frame"] = df_in
    args_out = build_dataframe(args_in, tt)
    df_out = args_out.pop("data_frame").sort_index(axis=1)
    assert_frame_equal(df_out, pd.DataFrame(df_out_exp).sort_index(axis=1))
    if transpose:
        args_exp = dict(x=y, y=x, color=color)
    else:
        args_exp = dict(x=x, y=y, color=color)
    if tt not in [go.Histogram2dContour, go.Histogram2d]:
        orientation_exp = args_in["orientation"]
        if (args_in["x"] is None) != (args_in["y"] is None) and tt != go.Histogram:
            orientation_exp = "h" if transpose else "v"
        args_exp["orientation"] = orientation_exp
    assert args_out == args_exp


@pytest.mark.parametrize("orientation", [None, "v", "h"])
def test_wide_mode_internal_bar_exception(orientation):
    df_in = pd.DataFrame(dict(a=["q", "r", "s"], b=["t", "u", "v"]), index=[11, 12, 13])
    args_in = dict(data_frame=df_in, color=None, orientation=orientation)
    args_out = build_dataframe(args_in, go.Bar)
    df_out = args_out.pop("data_frame")
    assert_frame_equal(
        df_out.sort_index(axis=1),
        pd.DataFrame(
            dict(
                index=[11, 12, 13, 11, 12, 13],
                _column_=["a", "a", "a", "b", "b", "b"],
                _value_=["q", "r", "s", "t", "u", "v"],
                _count_=[1, 1, 1, 1, 1, 1],
            )
        ).sort_index(axis=1),
    )
    if orientation is None or orientation == "v":
        assert args_out == dict(
            x="_value_", y="_count_", color="_column_", orientation="v"
        )
    else:
        assert args_out == dict(
            x="_count_", y="_value_", color="_column_", orientation="h"
        )


# given all of the above tests, and given that the melt() code is not sensitive
# to the trace type, we can do all sorts of special-case testing just by focusing
# on build_dataframe(args, go.Scatter) for various values of args, and looking at
# how args and df get mutated
special_cases = []


def append_special_case(df_in, args_in, args_expect, df_expect):
    special_cases.append((df_in, args_in, args_expect, df_expect))


# input is single bare array: column comes out as string "0"
append_special_case(
    df_in=[1, 2, 3],
    args_in=dict(x=None, y=None, color=None),
    args_expect=dict(x="index", y="_value_", color="_column_", orientation="v"),
    df_expect=pd.DataFrame(
        dict(index=[0, 1, 2], _value_=[1, 2, 3], _column_=["0", "0", "0"])
    ),
)

# input is single bare Series: column comes out as string "0"
append_special_case(
    df_in=pd.Series([1, 2, 3]),
    args_in=dict(x=None, y=None, color=None),
    args_expect=dict(x="index", y="_value_", color="_column_", orientation="v"),
    df_expect=pd.DataFrame(
        dict(index=[0, 1, 2], _value_=[1, 2, 3], _column_=["0", "0", "0"])
    ),
)

# input is a Series from a DF: we pick up the name and index values automatically
df = pd.DataFrame(dict(my_col=[1, 2, 3]), index=["a", "b", "c"])
append_special_case(
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
append_special_case(
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
append_special_case(
    df_in=df,
    args_in=dict(x=None, y=None, color=None),
    args_expect=dict(x="my_index", y="_value_", color="my_col_name", orientation="v"),
    df_expect=pd.DataFrame(
        dict(
            my_index=["a", "b", "c"],
            _value_=[1, 2, 3],
            my_col_name=["my_col", "my_col", "my_col"],
        )
    ),
)

# input is array of arrays: treated as rows, columns come out as string "0", "1"
append_special_case(
    df_in=[[1, 2], [4, 5]],
    args_in=dict(x=None, y=None, color=None),
    args_expect=dict(x="index", y="_value_", color="_column_", orientation="v"),
    df_expect=pd.DataFrame(
        dict(index=[0, 1, 0, 1], _value_=[1, 4, 2, 5], _column_=["0", "0", "1", "1"],)
    ),
)

# partial-melting by assigning symbol: we pick up that column and don't melt it
append_special_case(
    df_in=pd.DataFrame(dict(a=[1, 2], b=[3, 4], symbol_col=["q", "r"])),
    args_in=dict(x=None, y=None, color=None, symbol="symbol_col"),
    args_expect=dict(
        x="index", y="_value_", color="_column_", symbol="symbol_col", orientation="v",
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
append_special_case(
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
append_special_case(
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
append_special_case(
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
append_special_case(
    df_in=pd.DataFrame(dict(a=[1, 2], b=[3, 4])),
    args_in=dict(x=None, y=None, color="_column_"),
    args_expect=dict(x="index", y="_value_", color="_column_", orientation="v"),
    df_expect=pd.DataFrame(
        dict(index=[0, 1, 0, 1], _value_=[1, 2, 3, 4], _column_=["a", "a", "b", "b"])
    ),
)

# assigning color to a different column: _column_ drops out of args
append_special_case(
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
append_special_case(
    df_in=pd.DataFrame(dict(a=[1, 2], b=[3, 4])),
    args_in=dict(x=None, y=None, color=None, symbol="_column_"),
    args_expect=dict(
        x="index", y="_value_", color="_column_", symbol="_column_", orientation="v"
    ),
    df_expect=pd.DataFrame(
        dict(index=[0, 1, 0, 1], _value_=[1, 2, 3, 4], _column_=["a", "a", "b", "b"],)
    ),
)

# swapping symbol and color: just works
append_special_case(
    df_in=pd.DataFrame(dict(a=[1, 2], b=[3, 4], color_col=["q", "r"])),
    args_in=dict(x=None, y=None, color="color_col", symbol="_column_"),
    args_expect=dict(
        x="index", y="_value_", color="color_col", symbol="_column_", orientation="v",
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
append_special_case(
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
            index=[0, 1, 0, 1], _value_=[1, 2, 3, 4], my_col_name=["a", "a", "b", "b"],
        )
    ),
)

# passing the DF index into some other attr: works
df = pd.DataFrame(dict(a=[1, 2], b=[3, 4]))
df.columns.name = "my_col_name"
df.index.name = "my_index_name"
append_special_case(
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
append_special_case(
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
append_special_case(
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


@pytest.mark.parametrize("df_in, args_in, args_expect, df_expect", special_cases)
def test_wide_mode_internal_special_cases(df_in, args_in, args_expect, df_expect):
    args_in["data_frame"] = df_in
    args_out = build_dataframe(args_in, go.Scatter)
    df_out = args_out.pop("data_frame")
    assert_frame_equal(
        df_out.sort_index(axis=1), df_expect.sort_index(axis=1),
    )
    assert args_out == args_expect
