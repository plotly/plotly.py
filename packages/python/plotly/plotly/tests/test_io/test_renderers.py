import json
import sys
import base64
import threading
import time

import pytest
import requests
import numpy as np
import webbrowser

import plotly.graph_objs as go
import plotly.io as pio
from plotly.offline import get_plotlyjs
from plotly.io._utils import plotly_cdn_url

if sys.version_info >= (3, 3):
    import unittest.mock as mock
    from unittest.mock import MagicMock
else:
    import mock
    from mock import MagicMock


# fixtures
# --------
@pytest.fixture
def fig1(request):
    return go.Figure(
        data=[
            {
                "type": "scatter",
                "y": np.array([2, 1, 3, 2, 4, 2]),
                "marker": {"color": "green"},
            }
        ],
        layout={"title": {"text": "Figure title"}},
    )


# JSON
# ----
def test_json_renderer_mimetype(fig1):
    pio.renderers.default = "json"
    expected = {"application/json": json.loads(pio.to_json(fig1, remove_uids=False))}

    pio.renderers.render_on_display = False

    with mock.patch("IPython.display.display") as mock_display:
        fig1._ipython_display_()

    mock_display.assert_not_called()

    pio.renderers.render_on_display = True
    with mock.patch("IPython.display.display") as mock_display:
        fig1._ipython_display_()

    mock_display.assert_called_once_with(expected, raw=True)


def test_json_renderer_show(fig1):
    pio.renderers.default = "json"
    expected_bundle = {
        "application/json": json.loads(pio.to_json(fig1, remove_uids=False))
    }

    with mock.patch("IPython.display.display") as mock_display:
        pio.show(fig1)

    mock_display.assert_called_once_with(expected_bundle, raw=True)


def test_json_renderer_show_override(fig1):
    pio.renderers.default = "notebook"
    expected_bundle = {
        "application/json": json.loads(pio.to_json(fig1, remove_uids=False))
    }

    with mock.patch("IPython.display.display") as mock_display:
        pio.show(fig1, renderer="json")

    mock_display.assert_called_once_with(expected_bundle, raw=True)


# Plotly mimetype
# ---------------
plotly_mimetype = "application/vnd.plotly.v1+json"
plotly_mimetype_renderers = ["plotly_mimetype", "jupyterlab", "vscode", "nteract"]


@pytest.mark.parametrize("renderer", plotly_mimetype_renderers)
def test_plotly_mimetype_renderer_mimetype(fig1, renderer):
    pio.renderers.default = renderer
    expected = {plotly_mimetype: json.loads(pio.to_json(fig1, remove_uids=False))}

    expected[plotly_mimetype]["config"] = {"plotlyServerURL": "https://plot.ly"}

    pio.renderers.render_on_display = False

    with mock.patch("IPython.display.display") as mock_display:
        fig1._ipython_display_()

    mock_display.assert_not_called()

    pio.renderers.render_on_display = True
    with mock.patch("IPython.display.display") as mock_display:
        fig1._ipython_display_()

    mock_display.assert_called_once_with(expected, raw=True)


@pytest.mark.parametrize("renderer", plotly_mimetype_renderers)
def test_plotly_mimetype_renderer_show(fig1, renderer):
    pio.renderers.default = renderer
    expected = {plotly_mimetype: json.loads(pio.to_json(fig1, remove_uids=False))}

    expected[plotly_mimetype]["config"] = {"plotlyServerURL": "https://plot.ly"}

    with mock.patch("IPython.display.display") as mock_display:
        pio.show(fig1)

    mock_display.assert_called_once_with(expected, raw=True)


# Static Image
# ------------
# See plotly/tests/test_orca/test_image_renderers.py

# HTML
# ----
def assert_full_html(html):
    assert html.startswith("<html")


def assert_not_full_html(html):
    assert not html.startswith("<html")


def assert_html_renderer_connected(html):
    assert plotly_cdn_url().rstrip(".js") in html


def assert_offline(html):
    assert get_plotlyjs() in html


def assert_requirejs(html):
    assert 'require(["plotly"]' in html


def assert_not_requirejs(html):
    assert 'require(["plotly"]' not in html


def test_colab_renderer_show(fig1):
    pio.renderers.default = "colab"

    with mock.patch("IPython.display.display") as mock_display:
        pio.show(fig1)

    # Get display call arguments
    mock_call_args = mock_display.call_args
    mock_arg1 = mock_call_args[0][0]

    # Check for html bundle
    assert list(mock_arg1) == ["text/html"]

    # Check html contents
    html = mock_arg1["text/html"]
    assert_full_html(html)
    assert_html_renderer_connected(html)
    assert_not_requirejs(html)

    # check kwargs
    mock_kwargs = mock_call_args[1]
    assert mock_kwargs == {"raw": True}


@pytest.mark.parametrize(
    "name,connected",
    [("notebook", False), ("notebook_connected", True), ("kaggle", True)],
)
def test_notebook_connected_show(fig1, name, connected):
    # Set renderer
    pio.renderers.default = name

    # Show
    with mock.patch("IPython.display.display_html") as mock_display_html:
        with mock.patch("IPython.display.display") as mock_display:
            pio.show(fig1)

    # ### Check initialization ###
    # Get display call arguments
    mock_call_args_html = mock_display_html.call_args
    mock_arg1_html = mock_call_args_html[0][0]

    # Check init display contents
    bundle_display_html = mock_arg1_html
    if connected:
        assert_html_renderer_connected(bundle_display_html)
    else:
        assert_offline(bundle_display_html)

    # ### Check display call ###
    # Get display call arguments
    mock_call_args = mock_display.call_args
    mock_arg1 = mock_call_args[0][0]

    # Check for html bundle
    assert list(mock_arg1) == ["text/html"]

    # Check html display contents
    bundle_html = mock_arg1["text/html"]
    assert_not_full_html(bundle_html)
    assert_requirejs(bundle_html)

    # check kwargs
    mock_kwargs = mock_call_args[1]
    assert mock_kwargs == {"raw": True}


# Browser
# -------
@pytest.mark.parametrize("renderer", ["browser", "chrome", "chromium", "firefox"])
def test_browser_renderer_show(fig1, renderer):
    pio.renderers.default = renderer
    renderer_obj = pio.renderers[renderer]
    using = renderer_obj.using
    if not isinstance(renderer_obj.using, tuple):
        using = (using,)

    # Setup mocks
    mock_get = MagicMock(name="test get")
    mock_browser = MagicMock(name="test browser")
    mock_get.return_value = mock_browser

    request_responses = []

    def perform_request(url):
        request_responses.append(requests.get(url))

    def open_url(url, new=0, autoraise=True):
        print("open url")
        # Perform request in thread so that we don't block
        request_thread = threading.Thread(target=lambda: perform_request(url))
        request_thread.daemon = True
        request_thread.start()

    mock_browser.open.side_effect = open_url

    with mock.patch("webbrowser.get", mock_get):
        pio.show(fig1)

    # check get args
    mock_get.assert_any_call(using[0])

    # check open args
    mock_call_args = mock_browser.open.call_args
    mock_arg1 = mock_call_args[0][0]
    mock_arg1.startswith("http://127.0.0.1:")

    mock_kwargs = mock_call_args[1]
    assert mock_kwargs == dict(new=renderer_obj.new, autoraise=renderer_obj.autoraise)

    # Give request content a little time to show up
    tries = 0
    while tries < 5 and not request_responses:
        time.sleep(0.5)

    # Check request content
    assert len(request_responses) == 1
    response = request_responses[0]
    assert response.status_code == 200
    html = response.content.decode("utf8")
    assert_full_html(html)
    assert_offline(html)
    assert_not_requirejs(html)


# Validation
# ----------
@pytest.mark.parametrize("renderer", ["bogus", "json+bogus", "bogus+chrome"])
def test_reject_invalid_renderer(renderer):
    with pytest.raises(ValueError) as e:
        pio.renderers.default = renderer

    e.match("Invalid named renderer")


@pytest.mark.parametrize(
    "renderer", ["json", "json+firefox", "chrome+colab+notebook+vscode"]
)
def test_accept_valid_renderer(renderer):
    pio.renderers.default = renderer


@pytest.mark.parametrize(
    "renderer",
    plotly_mimetype_renderers
    + ["notebook", "notebook_connected", "browser", "notebook+plotly_mimetype"],
)
def test_repr_html(renderer):
    pio.renderers.default = renderer
    fig = go.Figure()
    fig.update_layout(template=None)
    str_html = fig._repr_html_()
    bundle = fig._repr_mimebundle_()
    # id number of figure
    id_html = str_html.split('document.getElementById("')[1].split('")')[0]
    id_pattern = "cd462b94-79ce-42a2-887f-2650a761a144"
    template = (
        '<div>                        <script type="text/javascript">'
        "window.PlotlyConfig = {MathJaxConfig: 'local'};</script>\n        "
        '<script src="' + plotly_cdn_url() + '"></script>                '
        '<div id="cd462b94-79ce-42a2-887f-2650a761a144" class="plotly-graph-div" '
        'style="height:100%; width:100%;"></div>            <script type="text/javascript">'
        "                                    window.PLOTLYENV=window.PLOTLYENV || {};"
        '                                    if (document.getElementById("cd462b94-79ce-42a2-887f-2650a761a144"))'
        ' {                    Plotly.newPlot(                        "cd462b94-79ce-42a2-887f-2650a761a144",'
        '                        [],                        {"template":{}},'
        '                        {"responsive": true}                    )                };'
        "                            </script>        </div>"
    )
    if "text/html" in bundle:
        str_bundle = bundle["text/html"]
        id_bundle = str_bundle.split('document.getElementById("')[1].split('")')[0]
        assert str_html.replace(id_html, "") == str_bundle.replace(id_bundle, "")
    else:
        assert str_html.replace(id_html, "") == template.replace(id_pattern, "")


all_renderers_without_orca = [
    "plotly_mimetype",
    "jupyterlab",
    "nteract",
    "vscode",
    "notebook",
    "notebook_connected",
    "kaggle",
    "azure",
    "colab",
    "cocalc",
    "databricks",
    "json",
    "browser",
    "firefox",
    "chrome",
    "chromium",
    "iframe",
    "iframe_connected",
    "sphinx_gallery",
]


@pytest.mark.parametrize("renderer_str", all_renderers_without_orca)
def test_repr_mimebundle(renderer_str):
    pio.renderers.default = renderer_str
    fig = go.Figure()
    fig.update_layout(template=None)
    bundle = fig._repr_mimebundle_()
    renderer = pio.renderers[renderer_str]
    from plotly.io._renderers import MimetypeRenderer

    if isinstance(renderer, MimetypeRenderer):
        ref_bundle = renderer.to_mimebundle(fig.to_dict())
        for key in bundle:
            if "getElementById" in bundle[key]:
                id1 = bundle[key].split('document.getElementById("')[1].split('")')[0]
                id2 = (
                    ref_bundle[key].split('document.getElementById("')[1].split('")')[0]
                )
                assert bundle[key].replace(id1, "") == ref_bundle[key].replace(id2, "")
    else:
        assert bundle == {}


def test_repr_mimebundle_mixed_renderer(fig1):
    pio.renderers.default = "notebook+plotly_mimetype"
    assert set(fig1._repr_mimebundle_().keys()) == set(
        {"application/vnd.plotly.v1+json", "text/html"}
    )
