import base64
from contextlib import redirect_stdout
from io import BytesIO, StringIO
from pathlib import Path
import tempfile
from unittest.mock import patch

from pdfrw import PdfReader
from PIL import Image
import plotly.graph_objects as go
import plotly.io as pio
from plotly.io.kaleido import kaleido_available, kaleido_major
import pytest


fig = {"data": [], "layout": {"title": {"text": "figure title"}}}


def check_image(path_or_buffer, size=(700, 500), format="PNG"):
    if format == "PDF":
        img = PdfReader(path_or_buffer)
        # TODO: There is a conversion factor needed here
        # In Kaleido v0 the conversion factor is 0.75
        factor = 0.75
        expected_size = tuple(int(s * factor) for s in size)
        actual_size = tuple(int(s) for s in img.pages[0].MediaBox[2:])
        assert actual_size == expected_size
    else:
        if isinstance(path_or_buffer, (str, Path)):
            with open(path_or_buffer, "rb") as f:
                img = Image.open(f)
        else:
            img = Image.open(path_or_buffer)
        assert img.size == size
        assert img.format == format


def test_kaleido_engine_to_image_returns_bytes():
    result = pio.to_image(fig, format="svg", engine="kaleido", validate=False)
    assert result.startswith(b"<svg")


def test_kaleido_fulljson():
    empty_fig = dict(data=[], layout={})
    result = pio.full_figure_for_development(empty_fig, warn=False, as_dict=True)
    assert result["layout"]["calendar"] == "gregorian"


def test_kaleido_engine_to_image():
    bytes = pio.to_image(fig, engine="kaleido", validate=False)

    # Check that image dimensions match default dimensions (700x500)
    # and format is default format (png)
    check_image(BytesIO(bytes))


def test_kaleido_engine_write_image(tmp_path):
    path_str = tempfile.mkstemp(suffix=".png", dir=tmp_path)[1]
    path_path = Path(tempfile.mkstemp(suffix=".png", dir=tmp_path)[1])

    for out_path in [path_str, path_path]:
        pio.write_image(fig, out_path, engine="kaleido", validate=False)
        check_image(out_path)


def test_kaleido_engine_to_image_kwargs():
    bytes = pio.to_image(
        fig,
        format="pdf",
        width=700,
        height=600,
        scale=2,
        engine="kaleido",
        validate=False,
    )
    check_image(BytesIO(bytes), size=(700 * 2, 600 * 2), format="PDF")


def test_kaleido_engine_write_image_kwargs(tmp_path):
    path_str = tempfile.mkstemp(suffix=".png", dir=tmp_path)[1]
    path_path = Path(tempfile.mkstemp(suffix=".png", dir=tmp_path)[1])

    for out_path in [path_str, path_path]:
        pio.write_image(
            fig,
            out_path,
            format="jpg",
            width=700,
            height=600,
            scale=2,
            engine="kaleido",
            validate=False,
        )
        check_image(out_path, size=(700 * 2, 600 * 2), format="JPEG")


@pytest.mark.skipif(
    not kaleido_available() or kaleido_major() < 1,
    reason="requires Kaleido v1.0.0 or higher",
)
def test_kaleido_engine_write_images(tmp_path):
    fig1 = {"data": [], "layout": {"title": {"text": "figure 1"}}}
    fig2 = {"data": [], "layout": {"title": {"text": "figure 2"}}}

    path_str = tempfile.mkstemp(suffix=".png", dir=tmp_path)[1]
    path_path = Path(tempfile.mkstemp(suffix=".png", dir=tmp_path)[1])

    pio.write_images(
        [fig1, fig2],
        [path_str, path_path],
        format=["jpg", "png"],
        width=[700, 900],
        height=600,
        scale=2,
        validate=False,
    )
    check_image(path_str, size=(700 * 2, 600 * 2), format="JPEG")
    check_image(str(path_path), size=(900 * 2, 600 * 2), format="PNG")


def test_image_renderer():
    """Verify that the image renderer returns the expected mimebundle."""
    with redirect_stdout(StringIO()) as f:
        pio.show(fig, renderer="png", engine="kaleido", validate=False)
    mimebundle = f.getvalue().strip()
    mimebundle_expected = str(
        {
            "image/png": base64.b64encode(
                pio.to_image(
                    fig,
                    format="png",
                    engine="kaleido",
                    validate=False,
                )
            ).decode("utf8")
        }
    )
    assert mimebundle == mimebundle_expected


def test_bytesio():
    """Verify that writing to a BytesIO object contains the same data as to_image().

    The goal of this test is to ensure that Plotly correctly handles a writable buffer
    which doesn't correspond to a filesystem path.
    """
    bio = BytesIO()
    pio.write_image(fig, bio, format="jpg", engine="kaleido", validate=False)
    bio.seek(0)  # Rewind to the beginning of the buffer, otherwise read() returns b''.
    bio_bytes = bio.read()
    to_image_bytes = pio.to_image(fig, format="jpg", engine="kaleido", validate=False)
    assert bio_bytes == to_image_bytes


def test_defaults():
    """Test that image output defaults can be set using pio.defaults.*"""
    try:
        assert pio.defaults.default_format == "png"
        pio.defaults.default_format = "svg"
        assert pio.defaults.default_format == "svg"
        result = pio.to_image(fig, format="svg", validate=False)
        assert result.startswith(b"<svg")
    finally:
        pio.defaults.default_format = "png"
        assert pio.defaults.default_format == "png"


def test_fig_write_image():
    """Test that fig.write_image() calls the correct underlying Kaleido function."""

    test_fig = go.Figure(fig)
    test_image_bytes = b"mock image data"

    if kaleido_major() > 0:
        patch_funcname = "plotly.io._kaleido.kaleido.calc_fig_sync"
    else:
        patch_funcname = "plotly.io._kaleido.scope.transform"

    with patch(patch_funcname, return_value=test_image_bytes) as mock_calc_fig:
        test_fig.write_image("test_path.png")

        # Verify patched function was called once with fig dict as first argument
        mock_calc_fig.assert_called_once()
        args, _ = mock_calc_fig.call_args
        assert args[0] == test_fig.to_dict()


def test_fig_to_image():
    """Test that fig.to_image() calls the correct underlying Kaleido function."""

    test_fig = go.Figure(fig)
    test_image_bytes = b"mock image data"

    if kaleido_major() > 0:
        patch_funcname = "plotly.io._kaleido.kaleido.calc_fig_sync"
    else:
        patch_funcname = "plotly.io._kaleido.scope.transform"

    with patch(patch_funcname, return_value=test_image_bytes) as mock_calc_fig:
        test_fig.to_image()

        # Verify patched function was called once with fig dict as first argument
        mock_calc_fig.assert_called_once()
        args, _ = mock_calc_fig.call_args
        assert args[0] == test_fig.to_dict()
