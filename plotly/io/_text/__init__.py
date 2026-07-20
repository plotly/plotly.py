"""Text (Unicode/braille) renderers for ``go.Figure``.

Draws an existing figure as a braille/block-char chart in plain text, as
registered ``plotly.io`` renderer strings (``text-utf`` default, ``text-ascii``;
plus the colour modes ``text-ansi`` and ``text-html``). Pure-Python, **no
external dependency** — the braille + block-char rasterizer is built in here (see
:mod:`~plotly.io._text.rasterizer`).

Architecture ("one grid, many serializers"):

* :mod:`~plotly.io._text.canvas` — Plotly-agnostic drawing surface -> abstract
  cell grid.
* :mod:`~plotly.io._text.serializers` — per-mode grid -> string.
* :mod:`~plotly.io._text.adapters` — ``go.Figure`` -> Canvas calls.
* :mod:`~plotly.io._text.renderers` — ``plotly.io`` registration.

This ``__init__`` is the stable public surface of the subpackage;
:mod:`plotly.io._renderers` imports :func:`register_text_renderers` from here.
"""

from __future__ import annotations

from plotly.io._text.canvas import (
    Canvas,
    Cell,
    CellGrid,
    CellRole,
    Tick,
)
from plotly.io._text.serializers import (
    SERIALIZERS,
    Serializer,
    get_serializer,
    register_serializer,
)
from plotly.io._text.adapters import (
    ADAPTERS,
    AdapterContext,
    TraceAdapter,
    figure_to_canvas,
    get_adapter,
    register_adapter,
)
from plotly.io._text.renderers import TextRenderer, register_text_renderers

__all__ = [
    "Canvas",
    "Cell",
    "CellGrid",
    "CellRole",
    "Tick",
    "Serializer",
    "SERIALIZERS",
    "register_serializer",
    "get_serializer",
    "ADAPTERS",
    "AdapterContext",
    "TraceAdapter",
    "register_adapter",
    "get_adapter",
    "figure_to_canvas",
    "TextRenderer",
    "register_text_renderers",
]
