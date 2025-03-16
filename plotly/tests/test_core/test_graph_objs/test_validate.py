import plotly.graph_objs as go
import json
import pytest
import plotly.io as pio


def build_invalid_fig():
    return dict(
        data=[{"type": "bar", "y": "not_a_list", "bogus": 23}],
        layout_title_text="valid title",
        layout_colorway="not a dict",
    )


expected_invalid_dict = dict(
    data=[{"type": "bar", "y": "not_a_list", "bogus": 23}],
    layout={"title": {"text": "valid title"}, "colorway": "not a dict"},
)


def test_validate_false():
    template = pio.templates.default
    try:
        pio.templates.default = None

        # Build figure with variety of invalid properties (both name and value),
        # make sure underscore notation is still applied properly

        fig = go.Figure(_validate=False, **build_invalid_fig())
        assert json.loads(fig.to_json()) == expected_invalid_dict

        with pytest.raises(ValueError):
            go.Figure(_validate=True, **build_invalid_fig())

    finally:
        pio.templates.default = template
