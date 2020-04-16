import plotly.graph_objs as go
import json
import pytest
import plotly.io as pio


def build_invalid_fig():
    return go.Figure(
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
    should_validate = go.validate._should_validate
    try:
        pio.templates.default = None

        # Build figure with variety of invalid properties (both name and value),
        # make sure underscore notation is still applied properly
        with go.validate(False):
            fig = build_invalid_fig()
            assert json.loads(fig.to_json()) == expected_invalid_dict

        with go.validate(True):
            with pytest.raises(ValueError):
                build_invalid_fig()

        # Use validate as callable
        go.validate(False)
        fig = build_invalid_fig()
        assert json.loads(fig.to_json()) == expected_invalid_dict

        go.validate(True)
        with pytest.raises(ValueError):
            build_invalid_fig()

    finally:
        pio.templates.default = template
        go.validate(should_validate)
