import plotly.express as px
import plotly.graph_objects as go
from numpy.testing import assert_array_equal


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


def test_pie_like_colors():
    labels = ["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"]
    parents = ["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve"]
    values = [10, 14, 12, 10, 2, 6, 6, 4, 4]
    # Sunburst
    fig = px.sunburst(
        names=labels,
        parents=parents,
        values=values,
        color=values,
        color_continuous_scale="Viridis",
        range_color=(5, 15),
    )
    assert fig.layout.coloraxis.cmin, fig.layout.coloraxis.cmax == (5, 15)
    assert fig.layout.coloraxis.colorscale[0] == (0.0, "#440154")
    # Treemap
    fig = px.treemap(
        names=labels,
        parents=parents,
        values=values,
        color=values,
        color_continuous_scale="Viridis",
        range_color=(5, 15),
    )
    assert fig.layout.coloraxis.cmin, fig.layout.coloraxis.cmax == (5, 15)
    assert fig.layout.coloraxis.colorscale[0] == (0.0, "#440154")
