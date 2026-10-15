import json

import pytest

import plotly.graph_objects as go


# Plotly.js no longer accepts strings for title attributes, so plain string
# titles in updatemenu button and slider step args must be sent as title.text
# (https://github.com/plotly/plotly.py/issues/5032)
TITLE_ARGS = [
    ({"title": "T"}, {"title.text": "T"}),
    ({"xaxis.title": "T"}, {"xaxis.title.text": "T"}),
    ({"yaxis2.title": "T"}, {"yaxis2.title.text": "T"}),
    ({"scene.xaxis.title": "T"}, {"scene.xaxis.title.text": "T"}),
    ({"coloraxis.colorbar.title": "T"}, {"coloraxis.colorbar.title.text": "T"}),
    ({"xaxis": {"title": "T"}}, {"xaxis": {"title": {"text": "T"}}}),
    ({"title.text": "T"}, {"title.text": "T"}),
    ({"xaxis.title.text": "T"}, {"xaxis.title.text": "T"}),
    ({"xaxis": {"title": {"text": "T"}}}, {"xaxis": {"title": {"text": "T"}}}),
]


def serialized_layout(fig):
    return json.loads(fig.to_json())["layout"]


@pytest.mark.parametrize("arg,expected", TITLE_ARGS)
def test_updatemenu_button_args_title(arg, expected):
    fig = go.Figure(
        layout=dict(
            updatemenus=[
                dict(
                    buttons=[
                        dict(method="relayout", args=[arg], args2=[arg]),
                        dict(method="update", args=[{"visible": [True]}, arg]),
                    ]
                )
            ]
        )
    )
    buttons = serialized_layout(fig)["updatemenus"][0]["buttons"]
    assert buttons[0]["args"] == [expected]
    assert buttons[0]["args2"] == [expected]
    assert buttons[1]["args"] == [{"visible": [True]}, expected]


@pytest.mark.parametrize("arg,expected", TITLE_ARGS)
def test_slider_step_args_title(arg, expected):
    fig = go.Figure()
    fig.update_layout(
        sliders=[
            dict(
                steps=[
                    dict(method="relayout", args=[arg]),
                    dict(method="update", args=[{"visible": [True]}, arg]),
                ]
            )
        ]
    )
    steps = serialized_layout(fig)["sliders"][0]["steps"]
    assert steps[0]["args"] == [expected]
    assert steps[1]["args"] == [{"visible": [True]}, expected]


def test_button_args_title_property_assignment():
    button = go.layout.updatemenu.Button(method="relayout")
    button.args = [{"xaxis.title": "T"}]
    assert button.to_plotly_json()["args"] == [{"xaxis.title.text": "T"}]


def test_restyle_args_trace_title():
    fig = go.Figure(
        layout=dict(
            updatemenus=[
                dict(
                    buttons=[
                        dict(
                            method="restyle",
                            args=[{"marker.colorbar.title": "T", "name": "N"}],
                        )
                    ]
                )
            ]
        )
    )
    button = serialized_layout(fig)["updatemenus"][0]["buttons"][0]
    assert button["args"] == [{"marker.colorbar.title.text": "T", "name": "N"}]
