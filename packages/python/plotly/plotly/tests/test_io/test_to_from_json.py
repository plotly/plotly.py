import plotly.graph_objs as go
import plotly.io as pio
import pytest
import plotly
import json
import sys
import os

if sys.version_info.major == 3 and sys.version_info.minor >= 3:
    from unittest.mock import MagicMock
    import tempfile
else:
    from mock import MagicMock
    from backports import tempfile


# fixtures
# --------
@pytest.fixture
def fig1(request):
    return go.Figure(data=[{'type': 'scattergl',
                            'marker': {'color': 'green'}},
                           {'type': 'parcoords',
                            'dimensions': [{'values': [1, 2, 3]},
                                           {'values': [3, 2, 1]}],
                            'line': {'color': 'blue'}}],
                     layout={'title': 'Figure title'})


opts = {'separators': (',', ':'),
        'cls': plotly.utils.PlotlyJSONEncoder,
        'sort_keys': True}
pretty_opts = {'indent': 2,
               'cls': plotly.utils.PlotlyJSONEncoder,
               'sort_keys': True}


# to_json
# -------
def test_to_json(fig1):
    assert pio.to_json(fig1, remove_uids=False) == json.dumps(
        fig1, **opts)


def test_to_json_remove_uids(fig1):
    dict1 = fig1.to_dict()
    for trace in dict1['data']:
        trace.pop('uid', None)

    assert pio.to_json(fig1) == json.dumps(
        dict1, **opts)


def test_to_json_validate(fig1):
    dict1 = fig1.to_dict()
    dict1['layout']['bogus'] = 37

    with pytest.raises(ValueError):
        pio.to_json(dict1)


def test_to_json_validate_false(fig1):
    dict1 = fig1.to_dict()
    dict1['layout']['bogus'] = 37

    assert pio.to_json(dict1, validate=False) == json.dumps(
        dict1, **opts)


def test_to_json_pretty_print(fig1):
    assert pio.to_json(fig1, remove_uids=False, pretty=True) == json.dumps(
        fig1, **pretty_opts)


# from_json
# ---------
def test_from_json(fig1):
    fig1_json = json.dumps(fig1, **opts)
    fig1_loaded = pio.from_json(fig1_json)

    # Check return type
    assert isinstance(fig1_loaded, go.Figure)

    # Check return json
    assert pio.to_json(fig1_loaded) == pio.to_json(fig1.to_dict())


@pytest.mark.parametrize("fig_type_spec,fig_type", [
    ('Figure', go.Figure),
    (go.Figure, go.Figure),
    ('FigureWidget', go.FigureWidget),
    (go.FigureWidget, go.FigureWidget)
])
def test_from_json_output_type(fig1, fig_type_spec, fig_type):
    fig1_json = json.dumps(fig1, **opts)
    fig1_loaded = pio.from_json(fig1_json, output_type=fig_type_spec)

    # Check return type
    assert isinstance(fig1_loaded, fig_type)

    # Check return json
    assert pio.to_json(fig1_loaded) == pio.to_json(fig1.to_dict())


def test_from_json_invalid(fig1):
    dict1 = fig1.to_dict()

    # Set bad property name
    dict1['data'][0]['marker']['bogus'] = 123

    # Set property with bad value
    dict1['data'][0]['marker']['size'] = -1

    # Serialize to json
    bad_json = json.dumps(dict1, **opts)

    with pytest.raises(ValueError):
        pio.from_json(bad_json)


def test_from_json_skip_invalid(fig1):
    dict1 = fig1.to_dict()

    # Set bad property name
    dict1['data'][0]['marker']['bogus'] = 123

    # Set property with bad value
    dict1['data'][0]['marker']['size'] = -1

    # Serialize to json
    bad_json = json.dumps(dict1, **opts)
    fig1_loaded = pio.from_json(bad_json, skip_invalid=True)

    # Check loaded figure
    assert pio.to_json(fig1_loaded) == pio.to_json(fig1.to_dict())


# read_json
# ---------
@pytest.mark.parametrize("fig_type_spec,fig_type", [
    ('Figure', go.Figure),
    (go.Figure, go.Figure),
    ('FigureWidget', go.FigureWidget),
    (go.FigureWidget, go.FigureWidget)
])
def test_read_json_from_filelike(fig1, fig_type_spec, fig_type):
    # Configure file-like mock
    filemock = MagicMock()
    filemock.read.return_value = pio.to_json(fig1)

    # read_json on mock file
    fig1_loaded = pio.read_json(filemock, output_type=fig_type_spec)

    # Check return type
    assert isinstance(fig1_loaded, fig_type)

    # Check loaded figure
    assert pio.to_json(fig1_loaded) == pio.to_json(fig1.to_dict())


@pytest.mark.parametrize("fig_type_spec,fig_type", [
    ('Figure', go.Figure),
    (go.Figure, go.Figure),
    ('FigureWidget', go.FigureWidget),
    (go.FigureWidget, go.FigureWidget)
])
def test_read_json_from_file_string(fig1, fig_type_spec, fig_type):
    with tempfile.TemporaryDirectory() as dir_name:

        # Write json file
        path = os.path.join(dir_name, 'fig1.json')
        with open(path, 'w') as f:
            f.write(pio.to_json(fig1))

        # read json from file as string
        fig1_loaded = pio.read_json(path, output_type=fig_type_spec)

        # Check return type
        assert isinstance(fig1_loaded, fig_type)

        # Check loaded figure
        assert pio.to_json(fig1_loaded) == pio.to_json(fig1.to_dict())


# write_json
# ----------
@pytest.mark.parametrize('pretty', [True, False])
@pytest.mark.parametrize('remove_uids', [True, False])
def test_write_json_filelike(fig1, pretty, remove_uids):
    # Configure file-like mock
    filemock = MagicMock()

    # write_json to mock file
    pio.write_json(fig1, filemock, pretty=pretty, remove_uids=remove_uids)

    # check write contents
    expected = pio.to_json(fig1, pretty=pretty, remove_uids=remove_uids)
    filemock.write.assert_called_once_with(expected)


@pytest.mark.parametrize('pretty', [True, False])
@pytest.mark.parametrize('remove_uids', [True, False])
def test_write_json_from_file_string(fig1, pretty, remove_uids):
    with tempfile.TemporaryDirectory() as dir_name:

        # Write json
        path = os.path.join(dir_name, 'fig1.json')
        pio.write_json(fig1, path, pretty=pretty, remove_uids=remove_uids)

        # Open as text file
        with open(path, 'r') as f:
            result = f.read()

        # Check contents that were written
        expected = pio.to_json(fig1, pretty=pretty, remove_uids=remove_uids)
        assert result == expected
