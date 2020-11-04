# Prototype for px.combine
# Combine 2 figures containing subplots
# Run as
# python px_combine.py

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import test_data
import json
from itertools import product, cycle, chain
from functools import reduce


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


def px_simple_combine(fig0, fig1, fig1_secondary_y=False):
    """
    Combines two figures by just using the layout of the first figure and
    appending the data of the second figure.
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
            "Only two figures with the same subplot geometry can be combined."
        )
    # reflow the colors
    colorway = fig0.layout.template.layout.colorway
    specs = None
    if fig1_secondary_y:
        specs = [
            [dict(secondary_y=True) for __ in range(grid_ref_shape[1])]
            for _ in range(grid_ref_shape[0])
        ]
    fig = make_subplots(*fig_grid_ref_shape(fig0), specs=specs)
    for r, c in multi_index(*fig_grid_ref_shape(fig)):
        print("row,col", r + 1, c + 1)
        for (tr, f), color in zip(
            chain(
                *[
                    zip(f.select_traces(row=r + 1, col=c + 1), cycle([f]),)
                    for f in [fig0, fig1]
                ]
            ),
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
    # TODO: How to put annotations on the correct subplot when using secondary y?
    # fig.update_layout(fig0.layout)
    # title will be wrong
    fig.layout.title = None
    # preserve bar mode
    # if both figures have barmode set, the first is taken, otherwise the set one is taken
    # TODO argument to force barmode? or the user can just update it after
    fig.layout.barmode = get_first_set_barmode([fig0, fig1])
    # also include annotations, shapes and layout images from fig1
    for kw in ["annotations", "shapes", "images"]:
        fig.layout[kw] += fig1.layout[kw]
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
    barmode = None
    try:
        barmode = list(
            filter(lambda x: x is not None, [f.layout.barmode for f in figs])
        )[0]
    except IndexError:
        # if no figure sets barmode, then it is not set
        pass
    return barmode


df = test_data.aug_tips()


def simple_combine_example():
    fig0 = px.scatter(df, x="total_bill", y="tip", facet_row="sex", facet_col="smoker")
    fig1 = px.histogram(
        df, x="total_bill", y="tip", facet_row="sex", facet_col="smoker"
    )
    fig1.update_traces(marker_color="red")
    fig = px_simple_combine(fig0, fig1)
    fig.update_layout(title="Simple figure combination")
    return fig


if __name__ == "__main__":
    fig_simple = simple_combine_example()
    fig_simple.show()
