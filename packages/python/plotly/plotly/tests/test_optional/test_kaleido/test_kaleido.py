import plotly.io as pio
import plotly.io.kaleido
from contextlib import contextmanager
from io import BytesIO
from pathlib import Path
from unittest.mock import Mock

fig = {"layout": {"title": {"text": "figure title"}}}


def make_writeable_mocks():
    """Produce some mocks which we will use for testing the `write_image()` function.

    These mocks should be passed as the `file=` argument to `write_image()`.

    The tests should verify that the method specified in the `active_write_function`
    attribute is called once, and that scope.transform is called with the `format=`
    argument specified by the `.expected_format` attribute.

    In total we provide two mocks: one for a writable file descriptor, and other for a
    pathlib.Path object.
    """

    # Part 1: A mock for a file descriptor
    # ------------------------------------
    mock_file_descriptor = Mock()

    # A file descriptor has no write_bytes method, unlike a pathlib Path.
    del mock_file_descriptor.write_bytes

    # The expected write method for a file descriptor is .write
    mock_file_descriptor.active_write_function = mock_file_descriptor.write

    # Since there is no filename, there should be no format detected.
    mock_file_descriptor.expected_format = None

    # Part 2: A mock for a pathlib path
    # ---------------------------------
    mock_pathlib_path = Mock(spec=Path)

    # A pathlib Path object has no write method, unlike a file descriptor.
    del mock_pathlib_path.write

    # The expected write method for a pathlib Path is .write_bytes
    mock_pathlib_path.active_write_function = mock_pathlib_path.write_bytes

    # Mock a path with PNG suffix
    mock_pathlib_path.suffix = ".png"
    mock_pathlib_path.expected_format = "png"

    return mock_file_descriptor, mock_pathlib_path


@contextmanager
def mocked_scope():
    # Code to acquire resource, e.g.:
    scope_mock = Mock()
    original_scope = pio._kaleido.scope
    pio._kaleido.scope = scope_mock
    try:
        yield scope_mock
    finally:
        pio._kaleido.scope = original_scope


def test_kaleido_engine_to_image_returns_bytes():
    result = pio.to_image(fig, format="svg", engine="kaleido", validate=False)
    assert result.startswith(b"<svg")


def test_kaleido_fulljson():
    empty_fig = dict(data=[], layout={})
    result = pio.full_figure_for_development(empty_fig, warn=False, as_dict=True)
    assert result["layout"]["calendar"] == "gregorian"


def test_kaleido_engine_to_image():
    with mocked_scope() as scope:
        pio.to_image(fig, engine="kaleido", validate=False)

    scope.transform.assert_called_with(
        fig, format=None, width=None, height=None, scale=None
    )


def test_kaleido_engine_write_image():
    for writeable_mock in make_writeable_mocks():
        with mocked_scope() as scope:
            pio.write_image(fig, writeable_mock, engine="kaleido", validate=False)

        scope.transform.assert_called_with(
            fig,
            format=writeable_mock.expected_format,
            width=None,
            height=None,
            scale=None,
        )

        assert writeable_mock.active_write_function.call_count == 1


def test_kaleido_engine_to_image_kwargs():
    with mocked_scope() as scope:
        pio.to_image(
            fig,
            format="pdf",
            width=700,
            height=600,
            scale=2,
            engine="kaleido",
            validate=False,
        )

    scope.transform.assert_called_with(
        fig, format="pdf", width=700, height=600, scale=2
    )


def test_kaleido_engine_write_image_kwargs():
    for writeable_mock in make_writeable_mocks():
        with mocked_scope() as scope:
            pio.write_image(
                fig,
                writeable_mock,
                format="jpg",
                width=700,
                height=600,
                scale=2,
                engine="kaleido",
                validate=False,
            )

        scope.transform.assert_called_with(
            fig, format="jpg", width=700, height=600, scale=2
        )

        assert writeable_mock.active_write_function.call_count == 1


def test_image_renderer():
    with mocked_scope() as scope:
        pio.show(fig, renderer="svg", engine="kaleido", validate=False)

    renderer = pio.renderers["svg"]
    scope.transform.assert_called_with(
        fig, format="svg", width=None, height=None, scale=renderer.scale,
    )


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
