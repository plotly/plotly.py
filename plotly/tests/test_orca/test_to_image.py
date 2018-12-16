import plotly.io as pio
import plotly.graph_objs as go
import os
import shutil
import pytest
import sys
import pandas as pd

if sys.version_info.major == 3 and sys.version_info.minor >= 3:
    from unittest.mock import MagicMock
else:
    from mock import MagicMock

# Constants
# ---------
images_root = 'plotly/tests/test_orca/images/'

if sys.platform.startswith('linux'):
    images_dir = images_root + 'linux/'
elif sys.platform == 'darwin':
    images_dir = images_root + 'darwin/'
else:
    raise ValueError(
        'No reference images available for platform: {platform}'
        .format(platform=sys.platform))


failed_dir = images_dir + 'failed/'
tmp_dir = images_dir + 'tmp/'
# These formats are deterministic. PDF and svg don't seem to be
image_formats = ['eps']
topo_df = pd.read_csv('plotly/tests/test_orca/resources/2011_us_ag_exports.csv')

# Fixtures
# --------
@pytest.fixture()
def setup():
    # Reset orca state
    pio.orca.config.restore_defaults(reset_server=False)

    # Clear out temp images dir
    shutil.rmtree(tmp_dir, ignore_errors=True)
    os.mkdir(tmp_dir)

    # Make failed directory
    if not os.path.exists(failed_dir):
        os.mkdir(failed_dir)


# Run setup before every test function in this file
pytestmark = pytest.mark.usefixtures("setup")


@pytest.fixture(params=image_formats)
def format(request):
    return request.param


@pytest.fixture()
def fig1():
    return go.Figure(data=[
        go.Bar(y=[2, 1, 4],
               marker=go.bar.Marker(color='purple',
                                    opacity=0.7)),
        go.Scattergl(y=[3, 4, 2])
    ], layout={
        'font': {'family': 'Arial', 'size': 12},
        'xaxis': {'showticklabels': False},
        'yaxis': {'showticklabels': False},
        'showlegend': False
    })


@pytest.fixture()
def topofig():
    for col in topo_df.columns:
        topo_df[col] = topo_df[col].astype(str)

    scl = [[0.0, 'rgb(242,240,247)'], [0.2, 'rgb(218,218,235)'],
           [0.4, 'rgb(188,189,220)'], \
           [0.6, 'rgb(158,154,200)'], [0.8, 'rgb(117,107,177)'],
           [1.0, 'rgb(84,39,143)']]

    topo_df['text'] = topo_df['state'] + '<br>' + \
                      'Beef ' + topo_df['beef'] + ' Dairy ' + \
                      topo_df['dairy'] + '<br>' + \
                      'Fruits ' + topo_df['total fruits'] + \
                      ' Veggies ' + topo_df[
                          'total veggies'] + '<br>' + \
                      'Wheat ' + topo_df['wheat'] + \
                      ' Corn ' + topo_df['corn']

    data = [dict(
        type='choropleth',
        colorscale=scl,
        autocolorscale=False,
        locations=topo_df['code'],
        z=topo_df['total exports'].astype(float),
        locationmode='USA-states',
        text=topo_df['text'],
        marker=dict(
            line=dict(
                color='rgb(255,255,255)',
                width=2
            )),
        showscale=False,
    )]

    layout = dict(
        geo=dict(
            scope='usa',
            projection=dict(type='albers usa'),
            showlakes=True,
            lakecolor='rgb(255, 255, 255)'),
        font={'family': 'Arial', 'size': 12},
    )

    return dict(data=data, layout=layout)


@pytest.fixture()
def latexfig():
    trace1 = go.Scatter(
        x=[1, 2, 3, 4],
        y=[1, 4, 9, 16],
    )
    trace2 = go.Scatter(
        x=[1, 2, 3, 4],
        y=[0.5, 2, 4.5, 8],
    )
    data = [trace1, trace2]
    layout = go.Layout(
        xaxis=dict(
            title='$\\sqrt{(n_\\text{c}(t|{T_\\text{early}}))}$',
            showticklabels=False,
        ),
        yaxis=dict(
            title='$d, r \\text{ (solar radius)}$',
            showticklabels=False,
        ),
        showlegend=False,
        font={'family': 'Arial', 'size': 12}
    )
    fig = go.Figure(data=data, layout=layout)
    return fig


# Utilities
# ---------
def assert_image_bytes(img_bytes, file_name, _raise=True):
    expected_img_path = images_dir + file_name

    try:
        with open(expected_img_path, 'rb') as f:
            expected = f.read()

        assert expected == img_bytes

    except (OSError, AssertionError) as e:
        failed_path = failed_dir + file_name
        print('Saving failed image to "{failed_path}"'
              .format(failed_path=failed_path))

        if not os.path.exists(failed_dir):
            os.mkdir(failed_dir)

        with open(failed_path, 'wb') as f:
            f.write(img_bytes)

        if _raise:
            raise e


# Tests
# -----
def test_simple_to_image(fig1, format):
    img_bytes = pio.to_image(fig1, format=format, width=700, height=500)
    assert_image_bytes(img_bytes, 'fig1.' + format)


def test_to_image_default(fig1, format):
    pio.orca.config.default_format = format
    img_bytes = pio.to_image(fig1, width=700, height=500)
    assert_image_bytes(img_bytes, 'fig1.' + format)


def test_write_image_string(fig1, format):

    # Build file paths
    file_name = 'fig1.' + format
    file_path = tmp_dir + file_name

    pio.write_image(fig1, tmp_dir + file_name,
                    format=format, width=700, height=500)

    with open(file_path, 'rb') as f:
        written_bytes = f.read()

    with open(images_dir + file_name, 'rb') as f:
        expected_bytes = f.read()

    assert written_bytes == expected_bytes


def test_write_image_writeable(fig1, format):

    file_name = 'fig1.' + format
    with open(images_dir + file_name, 'rb') as f:
        expected_bytes = f.read()

    mock_file = MagicMock()
    pio.write_image(fig1, mock_file, format=format,
                    width=700, height=500)

    mock_file.write.assert_called_once_with(expected_bytes)


def test_write_image_string_format_inference(fig1, format):
    # Build file paths
    file_name = 'fig1.' + format
    file_path = tmp_dir + file_name

    # Use file extension to infer image type.
    pio.write_image(fig1, tmp_dir + file_name,
                    width=700, height=500)

    with open(file_path, 'rb') as f:
        written_bytes = f.read()

    with open(images_dir + file_name, 'rb') as f:
        expected_bytes = f.read()

    assert written_bytes == expected_bytes


def test_write_image_string_no_extension_failure(fig1):
    # No extension
    file_path = tmp_dir + 'fig1'

    # Use file extension to infer image type.
    with pytest.raises(ValueError) as err:
        pio.write_image(fig1, file_path + 'fig1')

    assert 'add a file extension or specify the type' in str(err.value)


def test_write_image_string_bad_extension_failure(fig1):
    # Bad extension
    file_path = tmp_dir + 'fig1.bogus'

    # Use file extension to infer image type.
    with pytest.raises(ValueError) as err:
        pio.write_image(fig1, file_path + 'fig1')

    assert 'must be specified as one of the following' in str(err.value)


def test_write_image_string_bad_extension_override(fig1):
    # Bad extension
    file_name = 'fig1.bogus'
    tmp_path = tmp_dir + file_name

    pio.write_image(fig1, tmp_path, format='eps', width=700, height=500)

    with open(tmp_path, 'rb') as f:
        written_bytes = f.read()

    with open(images_dir + 'fig1.eps', 'rb') as f:
        expected_bytes = f.read()

    assert written_bytes == expected_bytes


# Topojson
# --------
def test_topojson_fig_to_image(topofig, format):
    img_bytes = pio.to_image(topofig, format=format, width=700, height=500)
    assert_image_bytes(img_bytes, 'topofig.' + format)


# Latex / MathJax
# ---------------
def test_latex_fig_to_image(latexfig, format):
    img_bytes = pio.to_image(latexfig, format=format, width=700, height=500)
    assert_image_bytes(img_bytes, 'latexfig.' + format)
