import pytest
from plotly.subplots import make_subplots

def test_add_hline_on_empty_subplots_creates_shape_default():
    fig = make_subplots(rows=1, cols=1)
    fig.add_hline(y=0.25)
    shapes = fig.layout.shapes
    assert len(shapes) == 1, "Expected one shape for the horizontal line"
    shape = shapes[0]
    assert shape.type == 'line'
    assert shape.y0 == 0.25 and shape.y1 == 0.25
    # xref and yref should be set
    assert getattr(shape, 'xref', None) is not None
    assert getattr(shape, 'yref', None) is not None

@pytest.mark.parametrize("row, col", [(None, None), (1, 1)])
def test_add_hline_with_explicit_row_col_on_empty_subplots(row, col):
    fig = make_subplots(rows=1, cols=1)
    # explicit row/col
    fig.add_hline(y=0.5, row=row, col=col)
    shapes = fig.layout.shapes
    assert len(shapes) == 1, f"Expected one shape when row={row}, col={col}"
    shape = shapes[0]
    assert shape.y0 == 0.5 and shape.y1 == 0.5
    assert shape.type == 'line'
    # ensure references default
    assert shape.xref is not None
    assert shape.yref is not None