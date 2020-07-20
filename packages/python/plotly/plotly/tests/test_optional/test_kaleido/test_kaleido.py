import plotly.io as pio
import plotly.io.kaleido
import sys
from contextlib import contextmanager

if sys.version_info >= (3, 3):
    from unittest.mock import Mock
else:
    from mock import Mock

fig = {"layout": {"title": {"text": "figure title"}}}


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


def test_kaleido_engine_to_image():
    with mocked_scope() as scope:
        pio.to_image(fig, engine="kaleido", validate=False)

    scope.transform.assert_called_with(
        fig, format=None, width=None, height=None, scale=None
    )


def test_kaleido_engine_write_image():
    writeable_mock = Mock()
    with mocked_scope() as scope:
        pio.write_image(fig, writeable_mock, engine="kaleido", validate=False)

    scope.transform.assert_called_with(
        fig, format=None, width=None, height=None, scale=None
    )

    assert writeable_mock.write.call_count == 1


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
    writeable_mock = Mock()
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

    assert writeable_mock.write.call_count == 1


def test_image_renderer():
    with mocked_scope() as scope:
        pio.show(fig, renderer="svg", engine="kaleido", validate=False)

    renderer = pio.renderers["svg"]
    scope.transform.assert_called_with(
        fig,
        format="svg",
        width=renderer.width,
        height=renderer.height,
        scale=renderer.scale,
    )
