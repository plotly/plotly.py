import json
import sys
import base64
import threading
import time

import pytest
import requests

import plotly.graph_objs as go
import plotly.io as pio
from plotly.offline import get_plotlyjs

if sys.version_info.major == 3 and sys.version_info.minor >= 3:
    import unittest.mock as mock
    from unittest.mock import MagicMock
else:
    import mock
    from mock import MagicMock


# fixtures
# --------
@pytest.fixture
def fig1(request):
    return go.Figure(data=[{'type': 'scatter',
                            'marker': {'color': 'green'}}],
                     layout={'title': {'text': 'Figure title'}})


# JSON
# ----
def test_json_renderer_mimetype(fig1):
    pio.renderers.default = 'json'
    expected = {'application/json': json.loads(pio.to_json(fig1))}

    pio.renderers.render_on_display = False
    assert fig1._repr_mimebundle_(None, None) is None

    pio.renderers.render_on_display = True
    bundle = fig1._repr_mimebundle_(None, None)
    assert bundle == expected


def test_json_renderer_show(fig1):
    pio.renderers.default = 'json'
    expected_bundle = {'application/json': json.loads(pio.to_json(fig1))}

    with mock.patch('IPython.display.display') as mock_display:
        pio.show(fig1)

    mock_display.assert_called_once_with(expected_bundle, raw=True)


def test_json_renderer_show_override(fig1):
    pio.renderers.default = 'notebook'
    expected_bundle = {'application/json': json.loads(pio.to_json(fig1))}

    with mock.patch('IPython.display.display') as mock_display:
        pio.show(fig1, renderer='json')

    mock_display.assert_called_once_with(expected_bundle, raw=True)


# Plotly mimetype
# ---------------
plotly_mimetype = 'application/vnd.plotly.v1+json'
plotly_mimetype_renderers = [
    'plotly_mimetype', 'jupyterlab', 'vscode', 'nteract']


@pytest.mark.parametrize('renderer', plotly_mimetype_renderers)
def test_plotly_mimetype_renderer_mimetype(fig1, renderer):
    pio.renderers.default = renderer
    expected = {plotly_mimetype: json.loads(
        pio.to_json(fig1, remove_uids=False))}

    expected[plotly_mimetype]['config'] = {
        'plotlyServerURL': 'https://plot.ly'}

    pio.renderers.render_on_display = False
    assert fig1._repr_mimebundle_(None, None) is None

    pio.renderers.render_on_display = True
    bundle = fig1._repr_mimebundle_(None, None)
    assert bundle == expected


@pytest.mark.parametrize('renderer', plotly_mimetype_renderers)
def test_plotly_mimetype_renderer_show(fig1, renderer):
    pio.renderers.default = renderer
    expected = {plotly_mimetype: json.loads(
        pio.to_json(fig1, remove_uids=False))}

    expected[plotly_mimetype]['config'] = {
        'plotlyServerURL': 'https://plot.ly'}

    with mock.patch('IPython.display.display') as mock_display:
        pio.show(fig1)

    mock_display.assert_called_once_with(expected, raw=True)


# Static Image
# ------------
# See plotly/tests/test_orca/test_image_renderers.py

# HTML
# ----
def assert_full_html(html):
    assert html.startswith('<html')


def assert_not_full_html(html):
    assert not html.startswith('<html')


def assert_connected(html):
    assert 'https://cdn.plot.ly/plotly-latest.min' in html


def assert_offline(html):
    assert get_plotlyjs() in html


def assert_requirejs(html):
    assert 'require(["plotly"]' in html


def assert_not_requirejs(html):
    assert 'require(["plotly"]' not in html


def test_colab_renderer_show(fig1):
    pio.renderers.default = 'colab'

    with mock.patch('IPython.display.display') as mock_display:
        pio.show(fig1)

    # Get display call arguments
    mock_call_args = mock_display.call_args
    mock_arg1 = mock_call_args[0][0]

    # Check for html bundle
    assert list(mock_arg1) == ['text/html']

    # Check html contents
    html = mock_arg1['text/html']
    assert_full_html(html)
    assert_connected(html)
    assert_not_requirejs(html)

    # check kwargs
    mock_kwargs = mock_call_args[1]
    assert mock_kwargs == {'raw': True}


@pytest.mark.parametrize('name,connected', [
    ('notebook', False),
    ('notebook_connected', True),
    ('kaggle', True)])
def test_notebook_connected_show(fig1, name, connected):
    # Set renderer
    with mock.patch('IPython.display.display_html') as mock_display_html:
        pio.renderers.default = name

    # Get display call arguments
    mock_call_args = mock_display_html.call_args
    mock_arg1 = mock_call_args[0][0]

    # Check init display contents
    html = mock_arg1
    if connected:
        assert_connected(html)
    else:
        assert_offline(html)

    # Show
    with mock.patch('IPython.display.display') as mock_display:
        pio.show(fig1)

    # Get display call arguments
    mock_call_args = mock_display.call_args
    mock_arg1 = mock_call_args[0][0]

    # Check for html bundle
    assert list(mock_arg1) == ['text/html']

    # Check html display contents
    html = mock_arg1['text/html']
    assert_not_full_html(html)
    assert_requirejs(html)

    # check kwargs
    mock_kwargs = mock_call_args[1]
    assert mock_kwargs == {'raw': True}


# Browser
# -------
@pytest.mark.parametrize('renderer', ['browser', 'chrome', 'firefox'])
def test_browser_renderer_show(fig1, renderer):
    pio.renderers.default = renderer
    renderer_obj = pio.renderers[renderer]

    # Setup mocks
    mock_get = MagicMock(name='test get')
    mock_browser = MagicMock(name='test browser')
    mock_get.return_value = mock_browser

    request_responses = []

    def perform_request(url):
        request_responses.append(requests.get(url))

    def open_url(url, new=0, autoraise=True):
        print('open url')
        # Perform request in thread so that we don't block
        request_thread = threading.Thread(target=lambda: perform_request(url))
        request_thread.daemon = True
        request_thread.start()

    mock_browser.open.side_effect = open_url

    with mock.patch('webbrowser.get', mock_get):
        pio.show(fig1)

    # check get args
    mock_get.assert_called_once_with(renderer_obj.using)

    # check open args
    mock_call_args = mock_browser.open.call_args
    mock_arg1 = mock_call_args[0][0]
    mock_arg1.startswith('http://127.0.0.1:')

    mock_kwargs = mock_call_args[1]
    assert mock_kwargs == dict(
        new=renderer_obj.new,
        autoraise=renderer_obj.autoraise)

    # Give request content a little time to show up
    tries = 0
    while tries < 5 and not request_responses:
        time.sleep(0.5)

    # Check request content
    assert len(request_responses) == 1
    response = request_responses[0]
    assert response.status_code == 200
    html = response.content.decode('utf8')
    assert_full_html(html)
    assert_offline(html)
    assert_not_requirejs(html)


# Combination
# -----------
def test_mimetype_combination(fig1):
    pio.renderers.default = 'pdf+jupyterlab'

    # Configure renderer so that we can use the same parameters
    # to build expected image below
    pio.renderers['pdf'].width = 400
    pio.renderers['pdf'].height = 500
    pio.renderers['pdf'].scale = 1

    # pdf
    image_bytes = pio.to_image(
        fig1, format='pdf', width=400, height=500, scale=1)

    image_str = base64.b64encode(image_bytes).decode('utf8')

    # plotly mimetype
    plotly_mimetype_dict = json.loads(
        pio.to_json(fig1, remove_uids=False))

    plotly_mimetype_dict['config'] = {
        'plotlyServerURL': 'https://plot.ly'}

    # Build expected bundle
    expected = {
        'application/pdf': image_str,
        plotly_mimetype: plotly_mimetype_dict,
    }

    pio.renderers.render_on_display = False
    assert fig1._repr_mimebundle_(None, None) is None

    pio.renderers.render_on_display = True
    bundle = fig1._repr_mimebundle_(None, None)
    assert bundle == expected


# Validation
# ----------
@pytest.mark.parametrize(
    'renderer', ['bogus', 'png+bogus', 'bogus+png'])
def test_reject_invalid_renderer(renderer):
    with pytest.raises(ValueError) as e:
        pio.renderers.default = renderer

    e.match('Invalid named renderer')


@pytest.mark.parametrize(
    'renderer', ['png', 'png+jpg', 'jpg+png+pdf+notebook+json'])
def test_accept_valid_renderer(renderer):
    pio.renderers.default = renderer
