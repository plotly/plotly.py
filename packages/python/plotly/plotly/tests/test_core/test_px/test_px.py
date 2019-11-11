import plotly.express as px
import numpy as np


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
