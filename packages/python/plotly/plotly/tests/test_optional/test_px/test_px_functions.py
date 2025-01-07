import plotly.express as px
import plotly.graph_objects as go
from numpy.testing import assert_array_equal
import narwhals.stable.v1 as nw
import numpy as np
from polars.exceptions import InvalidOperationError
import pytest


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
    values = np.array([4500, 2500, 1053, 500])

    fig = px.pie(names=labels, values=values)
    trace = go.Pie(labels=labels, values=values)
    _compare_figures(trace, fig)

    labels = ["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"]
    parents = ["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve"]
    values = np.array([10, 14, 12, 10, 2, 6, 6, 4, 4])
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
    y = np.array([3, 2, 1])
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
        fig = func(
            names=labels,
            parents=parents,
            values=values,
            color=values,
        )
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


def test_sunburst_treemap_with_path(constructor):
    vendors = ["A", "B", "C", "D", "E", "F", "G", "H"]
    sectors = [
        "Tech",
        "Tech",
        "Finance",
        "Finance",
        "Tech",
        "Tech",
        "Finance",
        "Finance",
    ]
    regions = ["North", "North", "North", "North", "South", "South", "South", "South"]
    values = [1, 3, 2, 4, 2, 2, 1, 4]
    total = ["total"] * 8
    df = constructor(
        dict(
            vendors=vendors,
            sectors=sectors,
            regions=regions,
            values=values,
            total=total,
        )
    )
    path = ["total", "regions", "sectors", "vendors"]
    # No values
    fig = px.sunburst(df, path=path)
    assert fig.data[0].branchvalues == "total"
    # Values passed
    fig = px.sunburst(df, path=path, values="values")
    assert fig.data[0].branchvalues == "total"
    assert fig.data[0].values[-1] == np.sum(values)

    # Error when values cannot be converted to numerical data type
    df = nw.from_native(df)
    native_namespace = nw.get_native_namespace(df)
    df = df.with_columns(
        values=nw.new_series(
            "values",
            ["1 000", "3 000", "2", "4", "2", "2", "1 000", "4 000"],
            dtype=nw.String(),
            native_namespace=native_namespace,
        )
    )
    pd_msg = "Column `values` of `df` could not be converted to a numerical data type."
    pl_msg = "conversion from `str` to `f64` failed in column 'values'"

    with pytest.raises(
        (ValueError, InvalidOperationError), match=f"({pd_msg}|{pl_msg})"
    ):
        fig = px.sunburst(df.to_native(), path=path, values="values")
    #  path is a mixture of column names and array-like
    path = [
        df.get_column("total").to_native(),
        "regions",
        df.get_column("sectors").to_native(),
        "vendors",
    ]
    fig = px.sunburst(df.to_native(), path=path)
    assert fig.data[0].branchvalues == "total"
    # Continuous colorscale
    df = df.with_columns(values=nw.lit(1))
    fig = px.sunburst(df.to_native(), path=path, values="values", color="values")
    assert "coloraxis" in fig.data[0].marker
    assert np.all(np.array(fig.data[0].marker.colors) == 1)
    assert fig.data[0].values[-1] == 8


def test_sunburst_treemap_with_path_and_hover(backend):
    df = px.data.tips(return_type=backend)
    fig = px.sunburst(
        df, path=["sex", "day", "time", "smoker"], color="smoker", hover_data=["smoker"]
    )
    assert "smoker" in fig.data[0].hovertemplate

    df = nw.from_native(px.data.gapminder(year=2007, return_type=backend))
    fig = px.sunburst(
        df.to_native(),
        path=["continent", "country"],
        color="lifeExp",
        hover_data=df.columns,
    )
    assert fig.layout.coloraxis.colorbar.title.text == "lifeExp"

    df = px.data.tips(return_type=backend)
    fig = px.sunburst(df, path=["sex", "day", "time", "smoker"], hover_name="smoker")
    assert "smoker" not in fig.data[0].hovertemplate  # represented as '%{hovertext}'
    assert "%{hovertext}" in fig.data[0].hovertemplate  # represented as '%{hovertext}'

    df = px.data.tips(return_type=backend)
    fig = px.sunburst(df, path=["sex", "day", "time", "smoker"], custom_data=["smoker"])
    assert fig.data[0].customdata[0][0] in ["Yes", "No"]
    assert "smoker" not in fig.data[0].hovertemplate
    assert "%{hovertext}" not in fig.data[0].hovertemplate


def test_sunburst_treemap_with_path_color(constructor):
    vendors = ["A", "B", "C", "D", "E", "F", "G", "H"]
    sectors = [
        "Tech",
        "Tech",
        "Finance",
        "Finance",
        "Tech",
        "Tech",
        "Finance",
        "Finance",
    ]
    regions = ["North", "North", "North", "North", "South", "South", "South", "South"]
    values = [1, 3, 2, 4, 2, 2, 1, 4]
    calls = [8, 2, 1, 3, 2, 2, 4, 1]
    total = ["total"] * 8
    hover = [el.lower() for el in vendors]

    data = dict(
        vendors=vendors,
        sectors=sectors,
        regions=regions,
        values=values,
        total=total,
        calls=calls,
    )
    df = nw.from_native(constructor(data))
    path = ["total", "regions", "sectors", "vendors"]
    fig = px.sunburst(df.to_native(), path=path, values="values", color="calls")
    colors = fig.data[0].marker.colors
    assert np.all(np.array(np.sort(colors[:8])) == np.array(sorted(calls)))
    fig = px.sunburst(df.to_native(), path=path, color="calls")
    colors = fig.data[0].marker.colors
    assert np.all(np.sort(colors[:8]) == np.array(sorted(calls)))

    # Hover info
    df = df.with_columns(
        hover=nw.new_series(
            name="hover",
            values=hover,
            dtype=nw.String(),
            native_namespace=nw.get_native_namespace(df),
        )
    )
    fig = px.sunburst(df.to_native(), path=path, color="calls", hover_data=["hover"])
    custom = fig.data[0].customdata
    assert np.all(np.sort(custom[:8, 0]) == sorted(hover))
    assert np.all(np.sort(custom[8:, 0]) == "(?)")
    assert np.all(np.sort(custom[:8, 1]) == sorted(calls))

    # Discrete color
    fig = px.sunburst(df.to_native(), path=path, color="vendors")
    assert len(np.unique(fig.data[0].marker.colors)) == 9

    # Discrete color and color_discrete_map
    cmap = {"Tech": "yellow", "Finance": "magenta", "(?)": "black"}
    fig = px.sunburst(
        df.to_native(), path=path, color="sectors", color_discrete_map=cmap
    )
    assert np.all(np.in1d(fig.data[0].marker.colors, list(cmap.values())))

    # Numerical column in path
    df = (
        nw.from_native(df)
        .with_columns(
            regions=nw.when(nw.col("regions") == "North")
            .then(1)
            .otherwise(2)
            .cast(nw.Int64())
        )
        .to_native()
    )
    path = ["total", "regions", "sectors", "vendors"]
    fig = px.sunburst(df, path=path, values="values", color="calls")
    colors = fig.data[0].marker.colors
    assert np.all(np.sort(colors[:8]) == sorted(calls))


def test_sunburst_treemap_column_parent(constructor):
    vendors = ["A", "B", "C", "D", "E", "F", "G", "H"]
    sectors = [
        "Tech",
        "Tech",
        "Finance",
        "Finance",
        "Tech",
        "Tech",
        "Finance",
        "Finance",
    ]
    regions = ["North", "North", "North", "North", "South", "South", "South", "South"]
    values = [1, 3, 2, 4, 2, 2, 1, 4]
    df = constructor(
        dict(
            id=vendors,
            sectors=sectors,
            parent=regions,
            values=values,
        )
    )
    path = ["parent", "sectors", "id"]
    # One column of the path is a reserved name - this is ok and should not raise
    px.sunburst(df, path=path, values="values")


def test_sunburst_treemap_with_path_non_rectangular(constructor):
    vendors = ["A", "B", "C", "D", None, "E", "F", "G", "H", None]
    sectors = [
        "Tech",
        "Tech",
        "Finance",
        "Finance",
        None,
        "Tech",
        "Tech",
        "Finance",
        "Finance",
        "Finance",
    ]
    regions = [
        "North",
        "North",
        "North",
        "North",
        "North",
        "South",
        "South",
        "South",
        "South",
        "South",
    ]
    values = [1, 3, 2, 4, 1, 2, 2, 1, 4, 1]
    total = ["total"] * 10
    df = constructor(
        dict(
            vendors=vendors,
            sectors=sectors,
            regions=regions,
            values=values,
            total=total,
        )
    )
    path = ["total", "regions", "sectors", "vendors"]
    msg = "Non-leaves rows are not permitted in the dataframe"
    with pytest.raises(ValueError, match=msg):
        fig = px.sunburst(df, path=path, values="values")

    df = (
        nw.from_native(df)
        .with_columns(
            sectors=(
                nw.when(~nw.col("vendors").is_null())
                .then(nw.col("sectors"))
                .otherwise(nw.lit("Other"))
            )
        )
        .to_native()
    )
    fig = px.sunburst(df, path=path, values="values")
    assert fig.data[0].values[-1] == np.sum(values)


def test_pie_funnelarea_colorscale():
    labels = ["A", "B", "C", "D"]
    values = [3, 2, 1, 4]
    for func, colorway in zip(
        [px.sunburst, px.treemap], ["sunburstcolorway", "treemapcolorway"]
    ):
        # Discrete colorscale, no color arg passed
        color_seq = px.colors.sequential.Reds
        fig = func(
            names=labels,
            values=values,
            color_discrete_sequence=color_seq,
        )
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


def test_parcats_dimensions_max(backend):
    df = px.data.tips(return_type=backend)

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


@pytest.mark.parametrize("histfunc,y", [(None, None), ("count", "tip")])
def test_histfunc_hoverlabels_univariate(backend, histfunc, y):
    def check_label(label, fig):
        assert fig.layout.yaxis.title.text == label
        assert label + "=" in fig.data[0].hovertemplate

    df = px.data.tips(return_type=backend)

    # base case, just "count" (note count(tip) is same as count())
    fig = px.histogram(df, x="total_bill", y=y, histfunc=histfunc)
    check_label("count", fig)

    # without y, label is just histnorm
    for histnorm in ["probability", "percent", "density", "probability density"]:
        fig = px.histogram(
            df, x="total_bill", y=y, histfunc=histfunc, histnorm=histnorm
        )
        check_label(histnorm, fig)

    for histnorm in ["probability", "percent", "density", "probability density"]:
        for barnorm in ["percent", "fraction"]:
            fig = px.histogram(
                df,
                x="total_bill",
                y=y,
                histfunc=histfunc,
                histnorm=histnorm,
                barnorm=barnorm,
            )
            check_label("%s (normalized as %s)" % (histnorm, barnorm), fig)


def test_histfunc_hoverlabels_bivariate(backend):
    def check_label(label, fig):
        assert fig.layout.yaxis.title.text == label
        assert label + "=" in fig.data[0].hovertemplate

    df = px.data.tips(return_type=backend)

    # with y, should be same as forcing histfunc to sum
    fig = px.histogram(df, x="total_bill", y="tip")
    check_label("sum of tip", fig)

    # change probability to fraction when histfunc is sum
    fig = px.histogram(df, x="total_bill", y="tip", histnorm="probability")
    check_label("fraction of sum of tip", fig)

    # percent is percent
    fig = px.histogram(df, x="total_bill", y="tip", histnorm="percent")
    check_label("percent of sum of tip", fig)

    # the other two are "weighted by"
    for histnorm in ["density", "probability density"]:
        fig = px.histogram(df, x="total_bill", y="tip", histnorm=histnorm)
        check_label("%s weighted by tip" % histnorm, fig)

    # check a few "normalized by"
    for histnorm in ["density", "probability density"]:
        for barnorm in ["fraction", "percent"]:
            fig = px.histogram(
                df, x="total_bill", y="tip", histnorm=histnorm, barnorm=barnorm
            )
            check_label(
                "%s weighted by tip (normalized as %s)" % (histnorm, barnorm), fig
            )

    # these next two are weird but OK...
    fig = px.histogram(
        df,
        x="total_bill",
        y="tip",
        histfunc="min",
        histnorm="probability",
        barnorm="percent",
    )
    check_label("fraction of sum of min of tip (normalized as percent)", fig)

    fig = px.histogram(
        df,
        x="total_bill",
        y="tip",
        histfunc="avg",
        histnorm="percent",
        barnorm="fraction",
    )
    check_label("percent of sum of avg of tip (normalized as fraction)", fig)

    # this next one is basically "never do this" but needs a defined behaviour
    fig = px.histogram(df, x="total_bill", y="tip", histfunc="max", histnorm="density")
    check_label("density of max of tip", fig)


def test_timeline(constructor):

    df = constructor(
        {
            "Task": ["Job A", "Job B", "Job C"],
            "Start": ["2009-01-01", "2009-03-05", "2009-02-20"],
            "Finish": ["2009-02-28", "2009-04-15", "2009-05-30"],
        }
    )
    fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", color="Task")
    assert len(fig.data) == 3
    assert fig.layout.xaxis.type == "date"
    assert fig.layout.xaxis.title.text is None
    fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", facet_row="Task")
    assert len(fig.data) == 3
    assert fig.data[1].xaxis == "x2"
    assert fig.layout.xaxis.type == "date"

    msg = "Both x_start and x_end are required"
    with pytest.raises(ValueError, match=msg):
        px.timeline(df, x_start="Start", y="Task", color="Task")

    msg = "Both x_start and x_end must refer to data convertible to datetimes."
    with pytest.raises(TypeError, match=msg):
        px.timeline(df, x_start="Start", x_end=["a", "b", "c"], y="Task", color="Task")


@pytest.mark.parametrize(
    "datetime_columns",
    [
        ["Start"],
        ["Start", "Finish"],
        ["Finish"],
    ],
)
def test_timeline_cols_already_temporal(constructor, datetime_columns):
    # https://github.com/plotly/plotly.py/issues/4913
    data = {
        "Task": ["Job A", "Job B", "Job C"],
        "Start": ["2009-01-01", "2009-03-05", "2009-02-20"],
        "Finish": ["2009-02-28", "2009-04-15", "2009-05-30"],
    }
    df = (
        nw.from_native(constructor(data))
        .with_columns(nw.col(datetime_columns).str.to_datetime(format="%Y-%m-%d"))
        .to_native()
    )
    fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", color="Task")
    assert len(fig.data) == 3
    assert fig.layout.xaxis.type == "date"
    assert fig.layout.xaxis.title.text is None
