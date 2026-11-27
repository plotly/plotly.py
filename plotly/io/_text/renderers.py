"""``plotly.io`` renderer registration for the ``text-*`` modes.

Wires the text renderers into plotly.py's renderer system so that
``fig.show(renderer="text-utf")`` (and ``"text-ascii"``, ``"text-ansi"``,
``"text-html"``) work like any built-in renderer string. Each mode is one
:class:`ExternalRenderer` that:

1. drives :func:`~plotly.io._text.adapters.figure_to_canvas` to draw the figure,
2. serializes the grid via the mode's serializer,
3. writes the result to stdout as **forced UTF-8** (never inheriting the
   ``sys.stdout`` locale — Windows CI defaults to cp1252 and would mojibake the
   braille; ``text-ascii`` is the escape hatch for locale-hostile sinks).

An ``ExternalRenderer`` (not a mimetype renderer) is the right base: text output
is printed, not embedded in a notebook mime bundle — matching how ``browser`` is
registered.

The class name, constructor signature, and :func:`register_text_renderers` hook
are the stable surface this module exposes to :mod:`plotly.io._renderers`.
"""

from __future__ import annotations

from plotly.io._base_renderers import ExternalRenderer
from plotly.io._text.canvas import DEFAULT_HEIGHT, DEFAULT_WIDTH

# Import the trace handler modules so they self-register into ADAPTERS. New
# handler modules are added to this list as they are implemented.
from plotly.io._text.adapters import bar as _bar  # noqa: F401
from plotly.io._text.adapters import heatmap as _heatmap  # noqa: F401
from plotly.io._text.adapters import histogram as _histogram  # noqa: F401
from plotly.io._text.adapters import scatter as _scatter  # noqa: F401


class TextRenderer(ExternalRenderer):
    """Render a figure as text to stdout for one ``text-*`` mode.

    ``mode`` is the ``plotly.io`` renderer string / serializer key
    (``"text-utf"``, ``"text-ascii"``, ...). ``width``/``height`` are the
    explicit canvas size in character cells (never inferred from a TTY) and can
    be overridden per call via ``pio.show(fig, renderer=..., width=, height=)``.
    """

    def __init__(
        self,
        mode: str = "text-utf",
        width: int = DEFAULT_WIDTH,
        height: int = DEFAULT_HEIGHT,
    ):
        self.mode = mode
        self.width = width
        self.height = height

    def render(self, fig) -> None:
        """Draw ``fig`` and write the text to stdout as forced UTF-8.

        ``fig`` is the figure dict handed in by
        :meth:`plotly.io._renderers.RenderersConfig._perform_external_rendering`
        (a ``go.Figure`` is coerced first, for direct callers). The grid is
        serialized for this renderer's ``mode`` and any degradation notes
        collected during the draw are printed after the plot. An undersized
        canvas (the Canvas raises ``ValueError``) degrades to a one-line note
        instead of crashing out of ``fig.show``.
        """
        from plotly.io._text.adapters import (
            figure_to_canvas,
            _is_too_small_error,
            _too_small_warning,
        )

        fig_dict = fig.to_dict() if hasattr(fig, "to_dict") else fig

        result = figure_to_canvas(
            fig_dict,
            width=self.width,
            height=self.height,
            mode=self.mode,
        )

        parts = []
        if result.canvas is not None:
            try:
                parts.append(result.canvas.render(self.mode))
            except ValueError as exc:
                # Defensive: the driver already degrades frame errors, but guard
                # a late serialize-time size error too. Only a *genuine* undersize
                # signal degrades to the "canvas too small" note — any other
                # ValueError re-raises so it isn't mislabelled on a full canvas.
                if _is_too_small_error(exc):
                    result.warnings.append(_too_small_warning(self.mode, exc))
                else:
                    raise
        parts.extend(result.warnings)

        _write_utf8("\n".join(parts) + "\n" if parts else "\n")


def _write_utf8(text: str) -> None:
    """Write ``text`` to stdout as **forced UTF-8**, never the stdout locale.

    Windows CI defaults ``sys.stdout`` to cp1252, which would mojibake braille /
    block glyphs; we go through the underlying byte buffer with an explicit
    ``utf-8`` encode. Sinks without a byte buffer (e.g. an in-memory
    ``StringIO`` under test) get a plain text write.
    """
    import sys

    stdout = sys.stdout
    buffer = getattr(stdout, "buffer", None)
    if buffer is not None:
        buffer.write(text.encode("utf-8", errors="replace"))
        buffer.flush()
    else:
        stdout.write(text)
        stdout.flush()


def register_text_renderers(renderers) -> None:
    """Register the ``text-*`` renderers into a plotly ``renderers`` config.

    Called once from :mod:`plotly.io._renderers` at import time. Registers the
    monochrome modes ``text-utf`` (default/recommended) and ``text-ascii``, plus
    the colour modes ``text-ansi`` and ``text-html``.
    """
    renderers["text-utf"] = TextRenderer(mode="text-utf")
    renderers["text-ascii"] = TextRenderer(mode="text-ascii")
    # Colour modes. Their renderer strings resolve and are discoverable in
    # ``pio.renderers``; each dispatches to the matching serializer.
    renderers["text-ansi"] = TextRenderer(mode="text-ansi")
    renderers["text-html"] = TextRenderer(mode="text-html")
