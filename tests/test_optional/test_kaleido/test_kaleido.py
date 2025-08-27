import base64
from contextlib import redirect_stdout
from io import BytesIO, StringIO
from pathlib import Path
import tempfile
from unittest.mock import patch
import xml.etree.ElementTree as ET

from pdfrw import PdfReader
from PIL import Image
import plotly.graph_objects as go
import plotly.io as pio
from plotly.io.kaleido import kaleido_available, kaleido_major
import pytest


fig = {"data": [], "layout": {"title": {"text": "figure title"}}}


def create_figure(width=None, height=None):
    """Create a simple figure with optional layout dimensions."""
    layout = {}
    if width:
        layout["width"] = width
    if height:
        layout["height"] = height

    return go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[1, 2, 3])], layout=layout)


def parse_svg_dimensions(svg_bytes):
    """Parse width and height from SVG bytes."""
    svg_str = svg_bytes.decode("utf-8")
    root = ET.fromstring(svg_str)
    width = root.get("width")
    height = root.get("height")
    return int(width) if width else None, int(height) if height else None


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
    test_fig = go.Figure(fig)
    test_image_bytes = b"mock image data"

    # Check initial defaults
    assert pio.defaults.default_format == "png"
    assert pio.defaults.default_width == 700
    assert pio.defaults.default_height == 500
    assert pio.defaults.default_scale == 1
    assert pio.defaults.mathjax is None
    assert pio.defaults.topojson is None
    assert pio.defaults.plotlyjs is None

    try:
        # Set new defaults
        pio.defaults.default_format = "svg"
        pio.defaults.default_width = 701
        pio.defaults.default_height = 501
        pio.defaults.default_scale = 2
        pio.defaults.mathjax = (
            "https://cdn.jsdelivr.net/npm/mathjax@3.1.2/es5/tex-svg.js"
        )
        pio.defaults.topojson = "path/to/topojson/files/"
        pio.defaults.plotlyjs = "https://cdn.plot.ly/plotly-3.0.0.js"

        # Check that new defaults are saved
        assert pio.defaults.default_format == "svg"
        assert pio.defaults.default_width == 701
        assert pio.defaults.default_height == 501
        assert pio.defaults.default_scale == 2
        assert (
            pio.defaults.mathjax
            == "https://cdn.jsdelivr.net/npm/mathjax@3.1.2/es5/tex-svg.js"
        )
        assert pio.defaults.topojson == "path/to/topojson/files/"
        assert pio.defaults.plotlyjs == "https://cdn.plot.ly/plotly-3.0.0.js"

        if kaleido_major() > 0:
            # Check that all the defaults values are passed through to the function call to calc_fig_sync
            with patch(
                "plotly.io._kaleido.kaleido.calc_fig_sync",
                return_value=test_image_bytes,
            ) as mock_calc_fig:
                result = pio.to_image(test_fig, validate=False)

                # Verify calc_fig_sync was called with correct args
                # taken from pio.defaults
                mock_calc_fig.assert_called_once()
                args, kwargs = mock_calc_fig.call_args
                assert args[0] == test_fig.to_dict()
                assert kwargs["opts"]["format"] == "svg"
                assert kwargs["opts"]["width"] == 701
                assert kwargs["opts"]["height"] == 501
                assert kwargs["opts"]["scale"] == 2
                assert kwargs["topojson"] == "path/to/topojson/files/"
                # mathjax and plotlyjs are passed through in kopts
                assert (
                    kwargs["kopts"]["mathjax"]
                    == "https://cdn.jsdelivr.net/npm/mathjax@3.1.2/es5/tex-svg.js"
                )
                assert (
                    kwargs["kopts"]["plotlyjs"] == "https://cdn.plot.ly/plotly-3.0.0.js"
                )

        else:
            # Check that all the default values have been set in pio._kaleido.scope
            assert pio._kaleido.scope.default_format == "svg"
            assert pio._kaleido.scope.default_width == 701
            assert pio._kaleido.scope.default_height == 501
            assert pio._kaleido.scope.default_scale == 2
            assert (
                pio._kaleido.scope.mathjax
                == "https://cdn.jsdelivr.net/npm/mathjax@3.1.2/es5/tex-svg.js"
            )
            assert pio._kaleido.scope.topojson == "path/to/topojson/files/"
            assert pio._kaleido.scope.plotlyjs == "https://cdn.plot.ly/plotly-3.0.0.js"

        # Set topojson default back to None
        # (otherwise image generation will fail)
        pio.defaults.topojson = None
        # Generate image for real and make sure it's an SVG
        result = test_fig.to_image(format="svg", validate=False)
        assert result.startswith(b"<svg")

    finally:
        # Reset defaults to original values and check that they are restored
        pio.defaults.default_format = "png"
        pio.defaults.default_width = 700
        pio.defaults.default_height = 500
        pio.defaults.default_scale = 1
        pio.defaults.mathjax = None
        pio.defaults.topojson = None
        pio.defaults.plotlyjs = None
        assert pio.defaults.default_format == "png"
        assert pio.defaults.default_width == 700
        assert pio.defaults.default_height == 500
        assert pio.defaults.default_scale == 1
        assert pio.defaults.mathjax is None
        assert pio.defaults.topojson is None
        assert pio.defaults.plotlyjs is None


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


def test_get_chrome():
    """Test that plotly.io.get_chrome() can be called."""

    if not kaleido_available() or kaleido_major() < 1:
        # Test that ValueError is raised when Kaleido requirements aren't met
        with pytest.raises(
            ValueError, match="This command requires Kaleido v1.0.0 or greater"
        ):
            pio.get_chrome()
    else:
        # Test normal operation when Kaleido v1+ is available
        with patch(
            "plotly.io._kaleido.kaleido.get_chrome_sync",
            return_value="/mock/path/to/chrome",
        ) as mock_get_chrome:
            pio.get_chrome()

            # Verify that kaleido.get_chrome_sync was called
            mock_get_chrome.assert_called_once()


def test_width_height_priority():
    """Test width/height priority: arguments > layout.width/height > defaults."""

    # Test case 1: Arguments override layout
    fig = create_figure(width=800, height=600)
    svg_bytes = pio.to_image(fig, format="svg", width=1000, height=900)
    width, height = parse_svg_dimensions(svg_bytes)
    assert width == 1000 and height == 900, (
        "Arguments should override layout dimensions"
    )

    # Test case 2: Layout dimensions used when no arguments
    fig = create_figure(width=800, height=600)
    svg_bytes = pio.to_image(fig, format="svg")
    width, height = parse_svg_dimensions(svg_bytes)
    assert width == 800 and height == 600, (
        "Layout dimensions should be used when no arguments provided"
    )

    # Test case 3: Partial override (only width argument)
    fig = create_figure(width=800, height=600)
    svg_bytes = pio.to_image(fig, format="svg", width=1200)
    width, height = parse_svg_dimensions(svg_bytes)
    assert width == 1200 and height == 600, (
        "Width argument should override layout, height should use layout"
    )

    # Test case 4: Defaults used when no layout or arguments
    fig = create_figure()
    svg_bytes = pio.to_image(fig, format="svg")
    width, height = parse_svg_dimensions(svg_bytes)
    assert width == pio.defaults.default_width, (
        "Default width should be used when no layout or argument"
    )
    assert height == pio.defaults.default_height, (
        "Default height should be used when no layout or argument"
    )
