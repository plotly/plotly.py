import plotly.io as pio
import plotly.graph_objs as go
import os
import shutil
import pytest
import sys

if sys.version_info.major == 3 and sys.version_info.minor >= 3:
    from unittest.mock import MagicMock
else:
    from mock import MagicMock

# Constants
# ---------
images_dir = 'plotly/tests/test_orca/images/'
failed_dir = images_dir + 'failed/'
tmp_dir = images_dir + 'tmp/'
# These formats are deterministic. PDF and svg don't seem to be
image_formats = ['png', 'jpg', 'jpeg', 'webp', 'eps']


# Fixtures
# --------
@pytest.fixture()
def setup():
    # Reset orca state
    pio.orca.config.restore_defaults()

    # Clear out temp images dir
    shutil.rmtree(tmp_dir, ignore_errors=True)
    os.mkdir(tmp_dir)


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
    ])


# Utilities
# ---------
def assert_image_bytes(img_bytes, file_name, _raise=True):
    expected_img_path = images_dir + file_name

    try:
        with open(expected_img_path, 'rb') as f:
            expected = f.read()

        assert expected == img_bytes

    except (FileNotFoundError, AssertionError) as e:
        with open(failed_dir + file_name, 'wb') as f:
            f.write(img_bytes)

        if _raise:
            raise e


# Tests
# -----
def test_simple_to_image(fig1, format):
    img_bytes = pio.to_image(fig1, format=format)
    assert_image_bytes(img_bytes, 'fig1.' + format)


def test_to_image_default(fig1, format):
    pio.orca.config.default_format = format
    img_bytes = pio.to_image(fig1)
    assert_image_bytes(img_bytes, 'fig1.' + format)


def test_write_image_string(fig1, format):

    # Build file paths
    file_name = 'fig1.' + format
    file_path = tmp_dir + file_name

    pio.write_image(fig1, tmp_dir + file_name, format=format)

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
    pio.write_image(fig1, mock_file, format=format)

    mock_file.write.assert_called_once_with(expected_bytes)


def test_write_image_string_format_inference(fig1, format):
    # Build file paths
    file_name = 'fig1.' + format
    file_path = tmp_dir + file_name

    # Use file extension to infer image type.
    pio.write_image(fig1, tmp_dir + file_name)

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

    pio.write_image(fig1, tmp_path, format='jpg')

    with open(tmp_path, 'rb') as f:
        written_bytes = f.read()

    with open(images_dir + 'fig1.jpg', 'rb') as f:
        expected_bytes = f.read()

    assert written_bytes == expected_bytes