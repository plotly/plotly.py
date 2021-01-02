import pytest
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from itertools import combinations, product
from functools import reduce


def all_combos(it):
    return list(
        reduce(
            lambda a, b: a + b,
            [list(combinations(it, r)) for r in range(1, len(it))],
            [],
        )
    )


def translate_layout_keys(t):
    xr, yr = t
    xr = xr.replace("axis", "")
    yr = yr.replace("axis", "")
    return (xr, yr)


def get_non_empty_subplots(fig, selector):
    gr = fig._validate_get_grid_ref()
    nrows = len(gr)
    ncols = len(gr[0])
    sp_addresses = product(range(nrows), range(ncols))
    # assign a number similar to plotly's xref/yref (e.g, xref=x2) to each
    # subplot address (xref=x -> 1, but xref=x3 -> 3)
    # sp_ax_numbers=range(1,len(sp_addresses)+1)
    # Get those subplot numbers which contain something
    ret = list(
        filter(
            lambda sp: fig._subplot_not_empty(
                *translate_layout_keys(sp.layout_keys), selector=selector
            ),
            [gr[r][c][0] for r, c in sp_addresses],
        )
    )
    return ret


def test_choose_correct_non_empty_subplots():
    # This checks to see that the correct subplots are selected for all
    # combinations of selectors
    fig = make_subplots(2, 2)
    fig.add_trace(go.Scatter(x=[1, 2], y=[3, 4]), row=1, col=1)
    fig.add_shape(dict(type="rect", x0=1, x1=2, y0=3, y1=4), row=1, col=2)
    fig.add_annotation(dict(text="A", x=1, y=2), row=2, col=1)
    fig.add_layout_image(
        dict(source="test", x=1, y=2, sizex=0.5, sizey=0.5), row=2, col=2
    )
    all_subplots = get_non_empty_subplots(fig, "all")
    selectors = all_combos(["traces", "shapes", "annotations", "images"])
    subplot_combos = all_combos(all_subplots)
    assert len(selectors) == len(subplot_combos)
    for s, spc in zip(selectors, subplot_combos):
        sps = tuple(get_non_empty_subplots(fig, s))
        assert sps == spc
