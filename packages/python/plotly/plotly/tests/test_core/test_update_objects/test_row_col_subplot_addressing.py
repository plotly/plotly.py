import plotly.graph_objs as go
from plotly.subplots import make_subplots
from plotly.basedatatypes import _indexing_combinations
import pytest
from itertools import product

NROWS = 4
NCOLS = 5


@pytest.fixture
def subplot_fig_fixture():
    fig = make_subplots(NROWS, NCOLS)
    return fig


@pytest.fixture
def non_subplot_fig_fixture():
    fig = go.Figure(go.Scatter(x=[1, 2, 3], y=[4, 3, 2]))
    return fig


def test_invalid_validate_get_grid_ref(non_subplot_fig_fixture):
    with pytest.raises(Exception):
        _ = non_subplot_fig_fixture._validate_get_grid_ref()


def test_get_subplot_coordinates(subplot_fig_fixture):
    assert set(subplot_fig_fixture._get_subplot_coordinates()) == set(
        [(r, c) for r in range(1, NROWS + 1) for c in range(1, NCOLS + 1)]
    )


def test_indexing_combinations_edge_cases():
    # Although in theory _indexing_combinations works for any number of
    # dimensions, we're just interested in 2D for subplots so that's what we
    # test here.
    assert _indexing_combinations([], []) == []
    with pytest.raises(ValueError):
        _ = _indexing_combinations([[1, 2], [3, 4, 5]], [[1, 2]])


# 18 combinations of input possible:
# ('all', 'all', 'product=True'),
# ('all', 'all', 'product=False'),
# ('all', '<list>', 'product=True'),
# ('all', '<list>', 'product=False'),
# ('all', '<not-list>', 'product=True'),
# ('all', '<not-list>', 'product=False'),
# ('<list>', 'all', 'product=True'),
# ('<list>', 'all', 'product=False'),
# ('<list>', '<list>', 'product=True'),
# ('<list>', '<list>', 'product=False'),
# ('<list>', '<not-list>', 'product=True'),
# ('<list>', '<not-list>', 'product=False'),
# ('<not-list>', 'all', 'product=True'),
# ('<not-list>', 'all', 'product=False'),
# ('<not-list>', '<list>', 'product=True'),
# ('<not-list>', '<list>', 'product=False'),
# ('<not-list>', '<not-list>', 'product=True'),
# ('<not-list>', '<not-list>', 'product=False')
# For <not-list> we choose int because that's what the subplot indexing routines
# will work with.
all_rows = [1, 2, 3, 4]
all_cols = [1, 2, 3, 4, 5]


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            dict(dims=["all", "all"], alls=[all_rows, all_cols], product=False),
            set(zip(all_rows, all_cols)),
        ),
        (
            dict(dims=["all", "all"], alls=[all_rows, all_cols], product=True),
            set([(r, c) for r in all_rows for c in all_cols]),
        ),
        (
            dict(dims=["all", [2, 4, 5]], alls=[all_rows, all_cols], product=False),
            set(zip(all_rows, [2, 4, 5])),
        ),
        (
            dict(dims=["all", [2, 4, 5]], alls=[all_rows, all_cols], product=True),
            set([(r, c) for r in all_rows for c in [2, 4, 5]]),
        ),
        (
            dict(dims=["all", 3], alls=[all_rows, all_cols], product=False),
            set([(all_rows[0], 3)]),
        ),
        (
            dict(dims=["all", 3], alls=[all_rows, all_cols], product=True),
            set([(r, c) for r in all_rows for c in [3]]),
        ),
        (
            dict(dims=[[1, 3], "all"], alls=[all_rows, all_cols], product=False),
            set(zip([1, 3], all_cols)),
        ),
        (
            dict(dims=[[1, 3], "all"], alls=[all_rows, all_cols], product=True),
            set([(r, c) for r in [1, 3] for c in all_cols]),
        ),
        (
            dict(dims=[[1, 3], [2, 4, 5]], alls=[all_rows, all_cols], product=False),
            set(zip([1, 3], [2, 4, 5])),
        ),
        (
            dict(dims=[[1, 3], [2, 4, 5]], alls=[all_rows, all_cols], product=True),
            set([(r, c) for r in [1, 3] for c in [2, 4, 5]]),
        ),
        (
            dict(dims=[[1, 3], 3], alls=[all_rows, all_cols], product=False),
            set([(1, 3)]),
        ),
        (
            dict(dims=[[1, 3], 3], alls=[all_rows, all_cols], product=True),
            set([(r, c) for r in [1, 3] for c in [3]]),
        ),
        (
            dict(dims=[2, "all"], alls=[all_rows, all_cols], product=False),
            set([(2, all_cols[0])]),
        ),
        (
            dict(dims=[2, "all"], alls=[all_rows, all_cols], product=True),
            set([(r, c) for r in [2] for c in all_cols]),
        ),
        (
            dict(dims=[2, [2, 4, 5]], alls=[all_rows, all_cols], product=False),
            set([(2, 2)]),
        ),
        (
            dict(dims=[2, [2, 4, 5]], alls=[all_rows, all_cols], product=True),
            set([(r, c) for r in [2] for c in [2, 4, 5]]),
        ),
        (dict(dims=[2, 3], alls=[all_rows, all_cols], product=False), set([(2, 3)])),
        (dict(dims=[2, 3], alls=[all_rows, all_cols], product=True), set([(2, 3)])),
    ],
)
def test_indexing_combinations(test_input, expected):
    assert set(_indexing_combinations(**test_input)) == expected


def _sort_row_col_lists(rows, cols):
    # makes sure that row and column lists are compared in the same order
    # sorted on rows
    si = sorted(range(len(rows)), key=lambda i: rows[i])
    rows = [rows[i] for i in si]
    cols = [cols[i] for i in si]
    return (rows, cols)


# _indexing_combinations tests most cases of the following function
# we just need to test that setting rows or cols to 'all' makes product True,
# and if not, we can still set product to True.
@pytest.mark.parametrize(
    "test_input,expected",
    [
        (("all", [2, 4, 5], False), zip(*product(range(1, NROWS + 1), [2, 4, 5])),),
        (([1, 3], "all", False), zip(*product([1, 3], range(1, NCOLS + 1))),),
        (([1, 3], "all", True), zip(*product([1, 3], range(1, NCOLS + 1))),),
        (([1, 3], [2, 4, 5], False), [(1, 3), (2, 4)]),
        (([1, 3], [2, 4, 5], True), zip(*product([1, 3], [2, 4, 5])),),
    ],
)
def test_select_subplot_coordinates(subplot_fig_fixture, test_input, expected):
    rows, cols, product = test_input
    er, ec = _sort_row_col_lists(*expected)
    t = subplot_fig_fixture._select_subplot_coordinates(rows, cols, product=product)
    r, c = zip(*t)
    r, c = _sort_row_col_lists(r, c)
    assert (r == er) and (c == ec)
