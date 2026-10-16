"""Figure-factory return type documentation regression checks."""

import inspect

import pytest

import plotly.figure_factory as ff
from plotly.graph_objects import Figure


@pytest.mark.parametrize(
    "factory, kwargs",
    [
        (ff.create_quiver, {"x": [0], "y": [0], "u": [1], "v": [1]}),
        (
            ff.create_streamline,
            {
                "x": [0, 1, 2],
                "y": [0, 1, 2],
                "u": [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
                "v": [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
            },
        ),
    ],
)
def test_factory_return_docs_match_runtime(factory, kwargs):
    assert "Returns\n-------\nplotly.graph_objects.Figure" in inspect.getdoc(factory)
    assert isinstance(factory(**kwargs), Figure)
