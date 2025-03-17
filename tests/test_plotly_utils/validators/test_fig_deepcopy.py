import copy
import pytest
import plotly.express as px

"""
This test is in the validators folder since copy.deepcopy ends up calling
BaseFigure(*args) which hits `validate_coerce`.

When inputs are dataframes and arrays, then the copied figure is called with
base64 encoded arrays.
"""


@pytest.mark.parametrize("return_type", ["pandas", "polars", "pyarrow"])
@pytest.mark.filterwarnings(
    r"ignore:\*scattermapbox\* is deprecated! Use \*scattermap\* instead"
)
def test_deepcopy_dataframe(return_type):
    gapminder = px.data.gapminder(return_type=return_type)
    fig = px.line(gapminder, x="year", y="gdpPercap", color="country")
    fig_copied = copy.deepcopy(fig)

    assert fig_copied.to_dict() == fig.to_dict()


@pytest.mark.filterwarnings(
    r"ignore:\*scattermapbox\* is deprecated! Use \*scattermap\* instead"
)
def test_deepcopy_array():
    gapminder = px.data.gapminder()
    x = gapminder["year"].to_numpy()
    y = gapminder["gdpPercap"].to_numpy()
    color = gapminder["country"].to_numpy()

    fig = px.line(x=x, y=y, color=color)
    fig_copied = copy.deepcopy(fig)

    assert fig_copied.to_dict() == fig.to_dict()
