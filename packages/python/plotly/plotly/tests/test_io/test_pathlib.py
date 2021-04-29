"""Test compatibility with pathlib.Path.

See also relevant tests in
   packages/python/plotly/plotly/tests/test_optional/test_kaleido/test_kaleido.py
"""

from unittest import mock
import plotly.io as pio
from io import StringIO
from pathlib import Path
import re
from unittest.mock import Mock

fig = {"layout": {"title": {"text": "figure title"}}}


def test_write_html():
    """Verify that various methods for producing HTML have equivalent results.

    The results will not be identical because the div id is pseudorandom. Thus
    we compare the results after replacing the div id.

    We test the results of
    - pio.to_html
    - pio.write_html with a StringIO buffer
    - pio.write_html with a mock pathlib Path
    - pio.write_html with a mock file descriptor
    """
    # Test pio.to_html
    html = pio.to_html(fig)

    # Test pio.write_html with a StringIO buffer
    sio = StringIO()
    pio.write_html(fig, sio)
    sio.seek(0)  # Rewind to the beginning of the buffer, otherwise read() returns ''.
    sio_html = sio.read()
    assert replace_div_id(html) == replace_div_id(sio_html)

    # Test pio.write_html with a mock pathlib Path
    mock_pathlib_path = Mock(spec=Path)
    pio.write_html(fig, mock_pathlib_path)
    mock_pathlib_path.write_text.assert_called_once()
    (pl_html,) = mock_pathlib_path.write_text.call_args[0]
    assert replace_div_id(html) == replace_div_id(pl_html)

    # Test pio.write_html with a mock file descriptor
    mock_file_descriptor = Mock()
    del mock_file_descriptor.write_bytes
    pio.write_html(fig, mock_file_descriptor)
    mock_file_descriptor.write.assert_called_once()
    (fd_html,) = mock_file_descriptor.write.call_args[0]
    assert replace_div_id(html) == replace_div_id(fd_html)


def replace_div_id(s):
    uuid = re.search(r'<div id="([^"]*)"', s).groups()[0]
    return s.replace(uuid, "XXXX")
