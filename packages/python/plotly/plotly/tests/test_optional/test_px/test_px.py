import plotly.express as px
import plotly.io as pio
import narwhals.stable.v1 as nw
import numpy as np
import pytest
from itertools import permutations


def test_scatter(backend):
    iris = nw.from_native(px.data.iris(return_type=backend))
    fig = px.scatter(iris.to_native(), x="sepal_width", y="sepal_length")
    assert fig.data[0].type == "scatter"
    assert np.all(fig.data[0].x == iris.get_column("sepal_width").to_numpy())
    assert np.all(fig.data[0].y == iris.get_column("sepal_length").to_numpy())
    # test defaults
    assert fig.data[0].mode == "markers"


def test_custom_data_scatter(backend):
    iris = nw.from_native(px.data.iris(return_type=backend))
    # No hover, no custom data
    fig = px.scatter(
        iris.to_native(), x="sepal_width", y="sepal_length", color="species"
    )
    assert fig.data[0].customdata is None
    # Hover, no custom data
    fig = px.scatter(
        iris.to_native(),
        x="sepal_width",
        y="sepal_length",
        color="species",
        hover_data=["petal_length", "petal_width"],
    )
    for data in fig.data:
        assert np.all(
            np.in1d(data.customdata[:, 1], iris.get_column("petal_width").to_numpy())
        )
    # Hover and custom data, no repeated arguments
    fig = px.scatter(
        iris.to_native(),
        x="sepal_width",
        y="sepal_length",
        hover_data=["petal_length", "petal_width"],
        custom_data=["species_id", "species"],
    )
    assert np.all(
        fig.data[0].customdata[:, 0] == iris.get_column("species_id").to_numpy()
    )
    assert fig.data[0].customdata.shape[1] == 4
    # Hover and custom data, with repeated arguments
    fig = px.scatter(
        iris.to_native(),
        x="sepal_width",
        y="sepal_length",
        hover_data=["petal_length", "petal_width", "species_id"],
        custom_data=["species_id", "species"],
    )
    assert np.all(
        fig.data[0].customdata[:, 0] == iris.get_column("species_id").to_numpy()
    )
    assert fig.data[0].customdata.shape[1] == 4
    assert (
        fig.data[0].hovertemplate
        == "sepal_width=%{x}<br>sepal_length=%{y}<br>petal_length=%{customdata[2]}<br>petal_width=%{customdata[3]}<br>species_id=%{customdata[0]}<extra></extra>"
    )


def test_labels(backend):
    tips = nw.from_native(px.data.tips(return_type=backend))
    fig = px.scatter(
        tips.to_native(),
        x="total_bill",
        y="tip",
        facet_row="time",
        facet_col="day",
        color="size",
        symbol="sex",
        labels={c: c.upper() for c in tips.columns},
    )
    assert "SEX" in fig.data[0].hovertemplate
    assert "TOTAL_BILL" in fig.data[0].hovertemplate
    assert "SIZE" in fig.data[0].hovertemplate
    assert "DAY" in fig.data[0].hovertemplate
    assert "TIME" in fig.data[0].hovertemplate
    assert fig.layout.legend.title.text.startswith("SEX")
    assert fig.layout.xaxis.title.text == "TOTAL_BILL"
    assert fig.layout.coloraxis.colorbar.title.text == "SIZE"
    assert fig.layout.annotations[0].text.startswith("DAY")
    assert fig.layout.annotations[4].text.startswith("TIME")


@pytest.mark.parametrize(
    ["extra_kwargs", "expected_mode"],
    [
        ({}, "lines"),
        ({"markers": True}, "lines+markers"),
        ({"text": "continent"}, "lines+markers+text"),
    ],
)
def test_line_mode(backend, extra_kwargs, expected_mode):
    gapminder = px.data.gapminder(return_type=backend)
    fig = px.line(
        gapminder,
        x="year",
        y="pop",
        color="country",
        **extra_kwargs,
    )
    assert fig.data[0].mode == expected_mode


def test_px_templates(backend):
    try:
        import plotly.graph_objects as go

        tips = px.data.tips(return_type=backend)

        # use the normal defaults
        fig = px.scatter()
        assert fig.layout.template == pio.templates[pio.templates.default]

        # respect changes to defaults
        pio.templates.default = "seaborn"
        fig = px.scatter()
        assert fig.layout.template == pio.templates["seaborn"]

        # special px-level defaults over pio defaults
        pio.templates.default = "seaborn"
        px.defaults.template = "ggplot2"
        fig = px.scatter()
        assert fig.layout.template == pio.templates["ggplot2"]

        # accept names in args over pio and px defaults
        fig = px.scatter(template="seaborn")
        assert fig.layout.template == pio.templates["seaborn"]

        # accept objects in args
        fig = px.scatter(template={})
        assert fig.layout.template == go.layout.Template(data_scatter=[{}])

        # read colorway from the template
        fig = px.scatter(
            tips,
            x="total_bill",
            y="tip",
            color="sex",
            template=dict(layout_colorway=["red", "blue"]),
        )
        assert fig.data[0].marker.color == "red"
        assert fig.data[1].marker.color == "blue"

        # default colorway fallback
        fig = px.scatter(tips, x="total_bill", y="tip", color="sex", template=dict())
        assert fig.data[0].marker.color == px.colors.qualitative.D3[0]
        assert fig.data[1].marker.color == px.colors.qualitative.D3[1]

        # pio default template colorway fallback
        pio.templates.default = "seaborn"
        px.defaults.template = None
        fig = px.scatter(tips, x="total_bill", y="tip", color="sex")
        assert fig.data[0].marker.color == pio.templates["seaborn"].layout.colorway[0]
        assert fig.data[1].marker.color == pio.templates["seaborn"].layout.colorway[1]

        # pio default template colorway fallback
        pio.templates.default = "seaborn"
        px.defaults.template = "ggplot2"
        fig = px.scatter(tips, x="total_bill", y="tip", color="sex")
        assert fig.data[0].marker.color == pio.templates["ggplot2"].layout.colorway[0]
        assert fig.data[1].marker.color == pio.templates["ggplot2"].layout.colorway[1]

        # don't overwrite top margin when set in template
        fig = px.scatter(title="yo")
        assert fig.layout.margin.t is None

        fig = px.scatter()
        assert fig.layout.margin.t == 60

        fig = px.scatter(template=dict(layout_margin_t=2))
        assert fig.layout.margin.t is None

        # don't force histogram gridlines when set in template
        pio.templates.default = "none"
        px.defaults.template = None
        fig = px.scatter(
            tips,
            x="total_bill",
            y="tip",
            marginal_x="histogram",
            marginal_y="histogram",
        )
        assert fig.layout.xaxis2.showgrid
        assert fig.layout.xaxis3.showgrid
        assert fig.layout.yaxis2.showgrid
        assert fig.layout.yaxis3.showgrid

        fig = px.scatter(
            tips,
            x="total_bill",
            y="tip",
            marginal_x="histogram",
            marginal_y="histogram",
            template=dict(layout_yaxis_showgrid=False),
        )
        assert fig.layout.xaxis2.showgrid
        assert fig.layout.xaxis3.showgrid
        assert fig.layout.yaxis2.showgrid is None
        assert fig.layout.yaxis3.showgrid is None

        fig = px.scatter(
            tips,
            x="total_bill",
            y="tip",
            marginal_x="histogram",
            marginal_y="histogram",
            template=dict(layout_xaxis_showgrid=False),
        )
        assert fig.layout.xaxis2.showgrid is None
        assert fig.layout.xaxis3.showgrid is None
        assert fig.layout.yaxis2.showgrid
        assert fig.layout.yaxis3.showgrid
    finally:
        # reset defaults to prevent all other tests from failing if this one does
        px.defaults.reset()
        pio.templates.default = "plotly"


def test_px_defaults():
    px.defaults.labels = dict(x="hey x")
    px.defaults.category_orders = dict(color=["b", "a"])
    px.defaults.color_discrete_map = dict(b="red")
    fig = px.scatter(x=[1, 2], y=[1, 2], color=["a", "b"])
    try:
        assert fig.data[0].name == "b"
        assert fig.data[0].marker.color == "red"
        assert fig.layout.xaxis.title.text == "hey x"
    finally:
        # reset defaults to prevent all other tests from failing if this one does
        px.defaults.reset()
        pio.templates.default = "plotly"


def assert_orderings(backend, days_order, days_check, times_order, times_check):
    symbol_sequence = ["circle", "diamond", "square", "cross", "circle", "diamond"]
    color_sequence = ["red", "blue", "red", "blue", "red", "blue", "red", "blue"]

    tips = nw.from_native(px.data.tips(return_type=backend))

    fig = px.scatter(
        tips.to_native(),
        x="total_bill",
        y="tip",
        facet_row="time",
        facet_col="day",
        color="time",
        symbol="day",
        symbol_sequence=symbol_sequence,
        color_discrete_sequence=color_sequence,
        category_orders=dict(day=days_order, time=times_order),
    )

    for col in range(len(days_check)):
        for trace in fig.select_traces(col=col + 1):
            assert days_check[col] in trace.hovertemplate

    for row in range(len(times_check)):
        for trace in fig.select_traces(row=len(times_check) - row):
            assert times_check[row] in trace.hovertemplate

    for trace in fig.data:
        for i, day in enumerate(days_check):
            if day in trace.name:
                assert trace.marker.symbol == symbol_sequence[i]
        for i, time in enumerate(times_check):
            if time in trace.name:
                assert trace.marker.color == color_sequence[i]


@pytest.mark.parametrize("days", permutations(["Sun", "Sat", "Fri", "x"]))
@pytest.mark.parametrize("times", permutations(["Lunch", "x"]))
def test_orthogonal_and_missing_orderings(backend, days, times):
    assert_orderings(
        backend, days, list(days) + ["Thur"], times, list(times) + ["Dinner"]
    )


@pytest.mark.parametrize("days", permutations(["Sun", "Sat", "Fri", "Thur"]))
@pytest.mark.parametrize("times", permutations(["Lunch", "Dinner"]))
def test_orthogonal_orderings(backend, days, times):
    assert_orderings(backend, days, days, times, times)


def test_category_order_with_category_as_x(backend):
    # https://github.com/plotly/plotly.py/issues/4875
    tips = nw.from_native(px.data.tips(return_type=backend))
    fig = px.bar(
        tips.to_native(),
        x="day",
        y="total_bill",
        color="smoker",
        barmode="group",
        facet_col="sex",
        category_orders={
            "day": ["Thur", "Fri", "Sat", "Sun"],
            "smoker": ["Yes", "No"],
            "sex": ["Male", "Female"],
        },
    )
    assert fig["layout"]["xaxis"]["categoryarray"] == ("Thur", "Fri", "Sat", "Sun")
    for trace in fig["data"]:
        assert set(trace["x"]) == {"Thur", "Fri", "Sat", "Sun"}


def test_permissive_defaults():
    msg = "'PxDefaults' object has no attribute 'should_not_work'"
    with pytest.raises(AttributeError, match=msg):
        px.defaults.should_not_work = "test"


def test_marginal_ranges(backend):
    df = px.data.tips(return_type=backend)
    fig = px.scatter(
        df,
        x="total_bill",
        y="tip",
        marginal_x="histogram",
        marginal_y="histogram",
        range_x=[5, 10],
        range_y=[5, 10],
    )
    assert fig.layout.xaxis2.range is None
    assert fig.layout.yaxis3.range is None


def test_render_mode(backend):
    df = nw.from_native(px.data.gapminder(return_type=backend))
    df2007 = df.filter(nw.col("year") == 2007)

    fig = px.scatter(df2007.to_native(), x="gdpPercap", y="lifeExp", trendline="ols")
    assert fig.data[0].type == "scatter"
    assert fig.data[1].type == "scatter"
    fig = px.scatter(
        df2007.to_native(),
        x="gdpPercap",
        y="lifeExp",
        trendline="ols",
        render_mode="webgl",
    )
    assert fig.data[0].type == "scattergl"
    assert fig.data[1].type == "scattergl"
    fig = px.scatter(df.to_native(), x="gdpPercap", y="lifeExp", trendline="ols")
    assert fig.data[0].type == "scattergl"
    assert fig.data[1].type == "scattergl"
    fig = px.scatter(
        df.to_native(), x="gdpPercap", y="lifeExp", trendline="ols", render_mode="svg"
    )
    assert fig.data[0].type == "scatter"
    assert fig.data[1].type == "scatter"
    fig = px.density_contour(
        df.to_native(), x="gdpPercap", y="lifeExp", trendline="ols"
    )
    assert fig.data[0].type == "histogram2dcontour"
    assert fig.data[1].type == "scatter"


def test_empty_df_int64(backend):
    # Load px data, then filter it such that the dataframe is empty
    df = px.data.tips(return_type=backend)
    df = nw.from_native(px.data.tips(return_type=backend))
    df_empty = df.filter(nw.col("day") == "banana").to_native()

    fig = px.scatter(
        df_empty,
        x="total_bill",
        y="size",  # size is an int64 column
    )
    # to_dict() should not raise an exception
    fig.to_dict()
