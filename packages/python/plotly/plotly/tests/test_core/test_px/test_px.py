import plotly.express as px
import numpy as np
import pytest


def test_scatter():
    iris = px.data.iris()
    fig = px.scatter(iris, x="sepal_width", y="sepal_length")
    assert fig.data[0].type == "scatter"
    assert np.all(fig.data[0].x == iris.sepal_width)
    assert np.all(fig.data[0].y == iris.sepal_length)
    # test defaults
    assert fig.data[0].mode == "markers"


def test_custom_data_scatter():
    iris = px.data.iris()
    # No hover, no custom data
    fig = px.scatter(iris, x="sepal_width", y="sepal_length", color="species")
    assert fig.data[0].customdata is None
    # Hover, no custom data
    fig = px.scatter(
        iris,
        x="sepal_width",
        y="sepal_length",
        color="species",
        hover_data=["petal_length", "petal_width"],
    )
    for data in fig.data:
        assert np.all(np.in1d(data.customdata[:, 1], iris.petal_width))
    # Hover and custom data, no repeated arguments
    fig = px.scatter(
        iris,
        x="sepal_width",
        y="sepal_length",
        hover_data=["petal_length", "petal_width"],
        custom_data=["species_id", "species"],
    )
    assert np.all(fig.data[0].customdata[:, 0] == iris.species_id)
    assert fig.data[0].customdata.shape[1] == 4
    # Hover and custom data, with repeated arguments
    fig = px.scatter(
        iris,
        x="sepal_width",
        y="sepal_length",
        hover_data=["petal_length", "petal_width", "species_id"],
        custom_data=["species_id", "species"],
    )
    assert np.all(fig.data[0].customdata[:, 0] == iris.species_id)
    assert fig.data[0].customdata.shape[1] == 4
    assert (
        fig.data[0].hovertemplate
        == "sepal_width=%{x}<br>sepal_length=%{y}<br>petal_length=%{customdata[2]}<br>petal_width=%{customdata[3]}<br>species_id=%{customdata[0]}"
    )


def test_labels():
    tips = px.data.tips()
    fig = px.scatter(
        tips,
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


def test_px_templates():
    import plotly.io as pio
    import plotly.graph_objects as go

    tips = px.data.tips()

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
        tips, x="total_bill", y="tip", marginal_x="histogram", marginal_y="histogram"
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


def test_orthogonal_orderings():
    from itertools import permutations

    df = px.data.tips()

    symbol_sequence = ["circle", "diamond", "square", "cross"]
    color_sequence = ["red", "blue"]

    def assert_orderings(days_order, days_check, times_order, times_check):
        fig = px.scatter(
            df,
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
            for trace in fig.select_traces(row=2 - row):
                assert times_check[row] in trace.hovertemplate

        for trace in fig.data:
            for i, day in enumerate(days_check):
                if day in trace.name:
                    assert trace.marker.symbol == symbol_sequence[i]
            for i, time in enumerate(times_check):
                if time in trace.name:
                    assert trace.marker.color == color_sequence[i]

    assert_orderings(
        ["x", "Sun", "Sat", "y", "Fri", "z"],  # add extra noise, missing Thur
        ["Sun", "Sat", "Fri", "Thur"],  # Thur is at the back
        ["a", "Lunch", "b"],  # add extra noise, missing Dinner
        ["Lunch", "Dinner"],  # Dinner is at the back
    )

    for days in permutations(df["day"].unique()):
        for times in permutations(df["time"].unique()):
            assert_orderings(days, days, times, times)


def test_permissive_defaults():
    msg = "'PxDefaults' object has no attribute 'should_not_work'"
    with pytest.raises(AttributeError, match=msg):
        px.defaults.should_not_work = "test"
