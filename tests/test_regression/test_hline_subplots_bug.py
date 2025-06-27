import pytest
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def _apply_line(fig, orientation):
    if orientation == "h":
        fig.add_hline(y=0.5)
    elif orientation == "v":
        fig.add_vline(x=0.3)
    else:
        raise ValueError("orientation must be 'h' or 'v'")


@pytest.mark.parametrize("orientation,kwargs", [
    ("h", dict(line_coord_key="y0", coord=0.5, span_keys=("x0", "x1"), span_vals=(0, 1))),
    ("v", dict(line_coord_key="x0", coord=0.3, span_keys=("y0", "y1"), span_vals=(0, 1))),
])
@pytest.mark.parametrize("constructor", [
    pytest.param(lambda: go.Figure(), id="plain-figure"),
    pytest.param(lambda: make_subplots(rows=1, cols=1), id="make_subplots"),
])

def test_add_line_presence(orientation, kwargs, constructor):
    """Both add_hline and add_vline must create a shape, even on empty subplots."""
    fig = constructor()

    assert len(fig.data) == 0
    assert len(fig.layout.shapes) == 0

    _apply_line(fig, orientation)

    # exactly one shape expected regardless of constructor and orientation
    assert len(fig.layout.shapes) == 1, (
        f"add_{orientation}line must create a shape on an empty figure; "
        "currently fails for make_subplots."
    )

    shape = fig.layout.shapes[0]
    # validate coordinate of line
    assert pytest.approx(shape[kwargs["line_coord_key"]]) == kwargs["coord"]
    # validate full-span of the other axis
    span_key0, span_key1 = kwargs["span_keys"]
    expected0, expected1 = kwargs["span_vals"]
    assert shape[span_key0] == expected0
    assert shape[span_key1] == expected1