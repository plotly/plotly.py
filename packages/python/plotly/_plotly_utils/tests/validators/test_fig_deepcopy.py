import copy
import plotly.express as px


def test_deepcopy():
    gapminder = px.data.gapminder()
    fig = px.line(gapminder, x="year", y="gdpPercap", color="country")

    fig_copy = copy.deepcopy(fig)

    assert fig_copy is not None
