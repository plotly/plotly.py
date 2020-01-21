import plotly.express as px
import plotly.graph_objects as go
from numpy.testing import assert_array_equal
import numpy as np


def _compare_figures(go_trace, px_fig):
    """Compare a figure created with a go trace and a figure created with
    a px function call. Check that all values inside the go Figure are the
    same in the px figure (which sets more parameters).
    """
    go_fig = go.Figure(go_trace)
    go_fig = go_fig.to_plotly_json()
    px_fig = px_fig.to_plotly_json()
    del go_fig["layout"]["template"]
    del px_fig["layout"]["template"]
    for key in go_fig["data"][0]:
        assert_array_equal(go_fig["data"][0][key], px_fig["data"][0][key])
    for key in go_fig["layout"]:
        assert go_fig["layout"][key] == px_fig["layout"][key]


def test_pie_like_px():
    # Pie
    labels = ["Oxygen", "Hydrogen", "Carbon_Dioxide", "Nitrogen"]
    values = [4500, 2500, 1053, 500]

    fig = px.pie(names=labels, values=values)
    trace = go.Pie(labels=labels, values=values)
    _compare_figures(trace, fig)

    labels = ["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"]
    parents = ["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve"]
    values = [10, 14, 12, 10, 2, 6, 6, 4, 4]
    # Sunburst
    fig = px.sunburst(names=labels, parents=parents, values=values)
    trace = go.Sunburst(labels=labels, parents=parents, values=values)
    _compare_figures(trace, fig)
    # Treemap
    fig = px.treemap(names=labels, parents=parents, values=values)
    trace = go.Treemap(labels=labels, parents=parents, values=values)
    _compare_figures(trace, fig)

    # Funnel
    x = ["A", "B", "C"]
    y = [3, 2, 1]
    fig = px.funnel(y=y, x=x)
    trace = go.Funnel(y=y, x=x)
    _compare_figures(trace, fig)
    # Funnelarea
    fig = px.funnel_area(values=y, names=x)
    trace = go.Funnelarea(values=y, labels=x)
    _compare_figures(trace, fig)


def test_sunburst_treemap_colorscales():
    labels = ["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"]
    parents = ["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve"]
    values = [10, 14, 12, 10, 2, 6, 6, 4, 4]
    for func, colorway in zip(
        [px.sunburst, px.treemap], ["sunburstcolorway", "treemapcolorway"]
    ):
        # Continuous colorscale
        fig = func(
            names=labels,
            parents=parents,
            values=values,
            color=values,
            color_continuous_scale="Viridis",
            range_color=(5, 15),
        )
        assert fig.layout.coloraxis.cmin, fig.layout.coloraxis.cmax == (5, 15)
        # Discrete colorscale, color arg passed
        color_seq = px.colors.sequential.Reds
        fig = func(
            names=labels,
            parents=parents,
            values=values,
            color=labels,
            color_discrete_sequence=color_seq,
        )
        assert np.all([col in color_seq for col in fig.data[0].marker.colors])
        # Numerical color arg passed, fall back to continuous
        fig = func(names=labels, parents=parents, values=values, color=values,)
        assert [
            el[0] == px.colors.sequential.Viridis
            for i, el in enumerate(fig.layout.coloraxis.colorscale)
        ]
        # Numerical color arg passed, continuous colorscale
        # even if color_discrete_sequence if passed
        fig = func(
            names=labels,
            parents=parents,
            values=values,
            color=values,
            color_discrete_sequence=color_seq,
        )
        assert [
            el[0] == px.colors.sequential.Viridis
            for i, el in enumerate(fig.layout.coloraxis.colorscale)
        ]

        # Discrete colorscale, no color arg passed
        color_seq = px.colors.sequential.Reds
        fig = func(
            names=labels,
            parents=parents,
            values=values,
            color_discrete_sequence=color_seq,
        )
        assert list(fig.layout[colorway]) == color_seq


def test_pie_funnelarea_colorscale():
    labels = ["A", "B", "C", "D"]
    values = [3, 2, 1, 4]
    for func, colorway in zip(
        [px.sunburst, px.treemap], ["sunburstcolorway", "treemapcolorway"]
    ):
        # Discrete colorscale, no color arg passed
        color_seq = px.colors.sequential.Reds
        fig = func(names=labels, values=values, color_discrete_sequence=color_seq,)
        assert list(fig.layout[colorway]) == color_seq
        # Discrete colorscale, color arg passed
        color_seq = px.colors.sequential.Reds
        fig = func(
            names=labels,
            values=values,
            color=labels,
            color_discrete_sequence=color_seq,
        )
        assert np.all([col in color_seq for col in fig.data[0].marker.colors])


def test_funnel():
    fig = px.funnel(
        x=[5, 4, 3, 3, 2, 1],
        y=["A", "B", "C", "A", "B", "C"],
        color=["0", "0", "0", "1", "1", "1"],
    )
    assert len(fig.data) == 2


def test_parcats_dimensions_max():
    df = px.data.tips()

    # default behaviour
    fig = px.parallel_categories(df)
    assert [d.label for d in fig.data[0].dimensions] == [
        "sex",
        "smoker",
        "day",
        "time",
        "size",
    ]

    # explicit subset of default
    fig = px.parallel_categories(df, dimensions=["sex", "smoker", "day"])
    assert [d.label for d in fig.data[0].dimensions] == ["sex", "smoker", "day"]

    # shrinking max
    fig = px.parallel_categories(df, dimensions_max_cardinality=4)
    assert [d.label for d in fig.data[0].dimensions] == [
        "sex",
        "smoker",
        "day",
        "time",
    ]

    # explicit superset of default, violating the max
    fig = px.parallel_categories(
        df, dimensions=["sex", "smoker", "day", "size"], dimensions_max_cardinality=4
    )
    assert [d.label for d in fig.data[0].dimensions] == ["sex", "smoker", "day", "size"]
