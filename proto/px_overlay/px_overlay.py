# Prototype for px.overlay
# Combine 2 figures containing subplots
# Run as
# python px_overlay.py

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import test_data
import json
from itertools import product, cycle, chain
from functools import reduce
import re


def multi_index(*kwargs):
    return product(*[range(k) for k in kwargs])


def extract_axes(layout):
    ret = dict()
    for k in dir(layout):
        if k[1 : 1 + len("axis")] == "axis":
            ret[k] = layout[k]
    return ret


def fig_grid_ref_shape(fig):
    grid_ref = fig._validate_get_grid_ref()
    return (len(grid_ref), len(grid_ref[0]))


def fig_subplot_axes(fig, r, c):
    grid_ref = fig._validate_get_grid_ref()
    return [fig.layout[k] for k in grid_ref[r - 1][c - 1][0].layout_keys]


def extract_axis_titles(fig):
    """
    Given figure created using make_subplots, with r rows and c columns, return
    r titles from the x axes and y titles from the y axes.
    """
    grid_ref_shape = fig_grid_ref_shape(fig)
    r_titles = [
        fig_subplot_axes(fig, r + 1, 1)[1]["title"] for r in range(grid_ref_shape[0])
    ]
    c_titles = [
        fig_subplot_axes(fig, 1, c + 1)[0]["title"] for c in range(grid_ref_shape[1])
    ]
    return (r_titles, c_titles)


def make_subplots_all_secondary_y(rows, cols):
    """
    Get subplots like make_subplots but all also have secondary y-axes.
    """
    grid_ref_shape = [rows, cols]
    specs = [
        [dict(secondary_y=True) for __ in range(grid_ref_shape[1])]
        for _ in range(grid_ref_shape[0])
    ]
    fig = make_subplots(*grid_ref_shape, specs=specs)
    return fig


def parse_axis_ref(ax):
    """ Find the axis letter, optional number, and domain of axis. """
    # TODO: can this be obtained via codegen?
    pat = re.compile("([xy])(axis)?([0-9]*)( domain)?")
    matches = pat.match(ax)
    if matches is None:
        raise ValueError('Axis "%s" cannot be parsed.' % (ax,))
    return (matches[1], matches[3], matches[4])


def norm_axis_ref(ax):
    """ normalize ax so it is in the format: yaxis, yaxis2, xaxis7 etc. """
    al, an, _ = parse_axis_ref(ax)
    return al + "axis" + an


def axis_pair_to_row_col(fig, axpair):
    """
    returns the row and column of the subplot having the axis pair and whether it is a
    secondary y
    """
    if "paper" in axpair:
        raise ValueError('Cannot find row and column of "paper" axis reference.')
    naxpair = tuple([norm_axis_ref(ax) for ax in axpair])
    nrows, ncols = fig_grid_ref_shape(fig)
    row = None
    col = None
    for r, c in multi_index(nrows, ncols):
        for sp in fig._grid_ref[r][c]:
            if naxpair == sp.layout_keys:
                row = r + 1
                col = c + 1
    if row is None or col is None:
        raise ValueError("Could not find subplot containing axes (%s,%s)." % nax)
    secondary_y = False
    yax = naxpair[1]
    if fig.layout[yax]["side"] == "right":
        secondary_y = True
    return (row, col, secondary_y)


def find_subplot_axes(fig, row, col, secondary_y=False):
    """
    Returns 2-tuple containing (xaxis,yaxis) at specified row, col and secondary y-axis. 
    """
    nrows, ncols = fig_grid_ref_shape(fig)
    try:
        sps = fig._grid_ref[row - 1][col - 1]
    except (IndexError, TypeError):
        # IndexError if fig has _grid_ref but not requested row or column,
        # TypeError if fig has no _grid_ref (it is None)
        raise IndexError(
            "Figure does not have a subplot at the requested row or column."
        )

    def _check_is_secondary_y(sp):
        xax, yax = sp.layout_keys
        # TODO: It may not be totally accurate to assume if an y-axis' "side" is
        # "right" than it is a secondary y axis...
        return fig.layout[yax]["side"] == "right"

    # find the secondary y axis
    err_msg = (
        "Could not find a y-axis " "at the subplot in the requested row or column."
    )
    filter_fun = lambda sp: not _check_is_secondary_y(sp)
    if secondary_y:
        err_msg = (
            "Could not find a secondary y-axis "
            "at the subplot in the requested row or column."
        )
        filter_fun = _check_is_secondary_y
    try:
        sp = list(filter(filter_fun, sps))[0]
    except (IndexError, TypeError):
        # Catch IndexError if the list is empty, catch TypeError if sps isn't
        # iterable (e.g., is None)
        raise IndexError(err_msg)
    return sp.layout_keys


def map_axis_pair(
    old_fig,
    new_fig,
    axpair,
    new_row=None,
    new_col=None,
    new_secondary_y=None,
    make_axis_ref=True,
):
    """
    Find the axes on the new figure that will give the same subplot and
    possibly secondary y axis as on the old figure. This can only
    work if the axis pair is ("paper","paper") or the axis pair corresponds to a
    subplot on the old figure the new figure has corresponding rows,
    columns and secondary y-axes.
    if make_axis_ref is True, axis is removed from the resulting strings, e.g., xaxis2 -> x2
    """
    if None in axpair:
        raise ValueError("Cannot map axis whose value is None.")
    if axpair == ("paper", "paper"):
        return axpair
    row, col, secondary_y = axis_pair_to_row_col(old_fig, axpair)
    row = new_row if new_row is not None else row
    col = new_col if new_col is not None else col
    secondary_y = new_secondary_y if new_secondary_y is not None else secondary_y
    newaxpair = find_subplot_axes(new_fig, row, col, secondary_y)
    axpair_extras = [" domain" if ax.endswith("domain") else "" for ax in axpair]
    newaxpair = tuple(ax + extra for ax, extra in zip(newaxpair, axpair_extras))
    if make_axis_ref:
        newaxpair = tuple(ax.replace("axis", "") for ax in newaxpair)
    return newaxpair


def map_annotation_like_obj_axis(oldfig, newfig, an, force_secondary_y=False):
    """
    Take an annotation-like object with xref and yref referring to axes in oldfig
    and map them to axes in newfig. This makes it possible to map an annotation
    to the same subplot row, column or secondary y in a new plot even if they do
    not have matching subplots.
    If force_secondary_y is True, attempt is made to map the annotation to a
    secondary y axis in the new figure.
    Returns the new annotation. Note that it has not been added to newfig, the
    caller must then do this if it wants it added to newfig.
    """
    oldaxpair = tuple([an[ref] for ref in ["xref", "yref"]])
    newaxpair = map_axis_pair(
        oldfig, newfig, oldaxpair, new_secondary_y=force_secondary_y
    )
    newan = an.__class__(an)
    newan["xref"], newan["yref"] = newaxpair
    return newan


def px_simple_overlay(fig0, fig1, fig1_secondary_y=False):
    """
    Combines two figures by putting all the traces from fig0 and fig1 on a new
    figure (fig). Then the annotation-like objects are copied to fig (i.e., the
    titles are not copied).
    The colors are reassigned so each trace has a unique color until all the
    colors in the colorway are exhausted and then loops through the colorway to
    assign additional colors (this is referred to as "reflowing" below).
    In order to differentiate the traces in the legend, if fig0 or fig1 have
    titles, they are prepended to the trace name.
    If fig1_secondary_y is True, then the yaxes from fig1 are placed on
    secondary y axes in the new figure.
    """
    if fig1_secondary_y and (
        ("px" not in fig0._aux.keys()) or ("px" not in fig0._aux.keys())
    ):
        raise ValueError(
            "To place fig1's traces on secondary y-axes, both figures must have "
            "been made with Plotly Express."
        )
    grid_ref_shape = fig_grid_ref_shape(fig0)
    if grid_ref_shape != fig_grid_ref_shape(fig1):
        raise ValueError(
            "Only two figures with the same subplot geometry can be overlayed."
        )
    # get colors for reflowing
    colorway = fig0.layout.template.layout.colorway
    specs = None
    if fig1_secondary_y:
        specs = [
            [dict(secondary_y=True) for __ in range(grid_ref_shape[1])]
            for _ in range(grid_ref_shape[0])
        ]
    # TODO: This needs to detect the start_cell of the input figures rather than
    # assuming 'bottom-left', which is just the px default start_cell
    fig = make_subplots(
        *fig_grid_ref_shape(fig0), specs=specs, start_cell="bottom-left"
    )
    for r, c in multi_index(*fig_grid_ref_shape(fig)):
        print("row,col", r + 1, c + 1)
        for (tr, f), color in zip(
            chain(
                *[
                    zip(f.select_traces(row=r + 1, col=c + 1), cycle([f]),)
                    for f in [fig0, fig1]
                ]
            ),
            # reflow the colors
            cycle(colorway),
        ):
            title = f.layout.title.text
            set_main_trace_color(tr, color)
            # use figure title to differentiate the legend items
            tr["name"] = "%s %s" % (title, tr["name"])
            # TODO: argument to group legend items?
            tr["legendgroup"] = None
            fig.add_trace(
                tr, row=r + 1, col=c + 1, secondary_y=(fig1_secondary_y and (f == fig1))
            )
    # TODO: How to preserve axis sizes when adding secondary y?

    # Map the axes of the annotation-like objects to the new figure. Map the
    # fig1 objects to the secondary-y if requested.
    selectors = product(
        [fig0, fig1],
        [
            go.Figure.select_annotations,
            go.Figure.select_shapes,
            go.Figure.select_layout_images,
        ],
    )
    adders = product(
        [(fig, False), (fig, fig1_secondary_y)],
        [go.Figure.add_annotation, go.Figure.add_shape, go.Figure.add_layout_image],
    )
    for (oldfig, selector), ((newfig, secy), adder) in zip(selectors, adders):
        for ann in selector(oldfig):
            # TODO this function needs to eventually take into consideration the
            # start_cell arguments of the figures involved in the mapping.
            newann = map_annotation_like_obj_axis(
                oldfig, newfig, ann, force_secondary_y=secy
            )
            adder(newfig, newann)

    # fig.update_layout(fig0.layout)
    # title will be wrong
    fig.layout.title = None
    # preserve bar mode
    # if both figures have barmode set, the first is taken from the figure that
    # has bars (so just the one from fig0 if both have bars), otherwise the set
    # one is taken.
    # TODO argument to force barmode? or the user can just update it after
    fig.layout.barmode = get_first_set_barmode([fig0, fig1])
    return fig


def select_all_traces(figs):
    traces = list(
        reduce(
            lambda a, b: a + b,
            map(lambda t: list(go.Figure.select_traces(t)), figs),
            [],
        )
    )
    return traces


def check_trace_type_xy(tr):
    return ("xaxis" in tr) and ("yaxis" in tr)


def check_figs_trace_types_xy(figs):
    traces = select_all_traces(figs)
    xy_traces = list(map(check_trace_type_xy, traces))
    return xy_traces


def set_main_trace_color(tr, color):
    # Set the main color of a trace
    if type(tr) == type(go.Scatter()):
        if tr["mode"] == "lines":
            tr["line_color"] = color
        else:
            tr["marker_color"] = color
    elif type(tr) == type(go.Bar()):
        tr["marker_color"] = color


def get_first_set_barmode(figs):
    """ Get first bar mode from the figure that has it set and has bar traces. """

    def _bar_mode_filter(f):
        return (
            any([type(tr) == type(go.Bar()) for tr in f.data])
            and f.layout.barmode is not None
        )

    barmode = None
    try:
        barmode = [f.layout.barmode for f in filter(_bar_mode_filter, figs)][0]
    except IndexError:
        # if no figure sets barmode, then it is not set
        pass
    return barmode


def simple_overlay_example():
    df = test_data.aug_tips()
    fig0 = px.scatter(df, x="total_bill", y="tip", facet_row="sex", facet_col="smoker")
    fig1 = px.histogram(
        df, x="total_bill", y="tip", facet_row="sex", facet_col="smoker"
    )
    fig1.update_traces(marker_color="red")
    fig = px_simple_overlay(fig0, fig1)
    fig.update_layout(title="Simple figure combination")
    return fig


if __name__ == "__main__":
    fig_simple = simple_overlay_example()
    fig_simple.show()
