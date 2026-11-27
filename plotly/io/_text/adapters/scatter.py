"""``scatter`` / ``scattergl`` adapter.

The canonical case: lines -> braille via :meth:`Canvas.line`, markers -> distinct
glyphs via :meth:`Canvas.markers`, honouring the trace ``mode``
(``lines`` / ``markers`` / ``lines+markers``). ``scattergl`` shares this path
(same data model). Knows nothing about braille encoding — only Canvas calls.
"""

from __future__ import annotations

from typing import List, Optional, Tuple

from plotly.io._text.adapters import (
    AdapterContext,
    _as_sequence,
    _coerce_numeric,
    register_adapter,
)
from plotly.io._text.canvas import Canvas


def scatter_xy(trace: dict) -> Tuple[List[float], List[float], Optional[str]]:
    """Extract paired numeric ``(xs, ys)`` and the draw ``mode`` from a trace.

    A missing ``x`` (or ``y``) is filled with positional indices, categorical
    values map to their index, and the two arrays are truncated to a common
    length. ``x``/``y`` are normalized via :func:`_as_sequence` first so a
    base64 typed-array (numpy data through ``fig.to_dict()``) is decoded rather
    than counted by its dict keys. Used both to draw and (by the driver) to
    compute data extents, so the two never disagree.
    """
    x = _as_sequence(trace.get("x"))
    y = _as_sequence(trace.get("y"))
    mode = trace.get("mode")

    if x is None and y is None:
        return [], [], mode
    if x is None:
        assert y is not None  # guaranteed by the both-None early return above
        x = list(range(len(y)))
    if y is None:
        assert x is not None  # x was non-None or was filled in just above
        y = list(range(len(x)))

    xs = _coerce_numeric(x)
    ys = _coerce_numeric(y)
    n = min(len(xs), len(ys))
    return xs[:n], ys[:n], mode


def scatter_adapter(trace: dict, canvas: Canvas, ctx: AdapterContext) -> None:
    """Draw one ``scatter``/``scattergl`` trace onto ``canvas``.

    Reads ``trace["x"]``/``trace["y"]`` and ``trace["mode"]``; calls
    :meth:`Canvas.line` for line segments and/or :meth:`Canvas.markers`
    (with ``ctx.glyph``) for markers.
    """
    xs, ys, mode = scatter_xy(trace)
    if not xs:
        return

    points = list(zip(xs, ys))

    # Plotly's true default mode depends on point count / other traces; "lines"
    # is the sensible text-renderer default. Honour explicit lines / markers.
    mode = mode or "lines"
    draw_line = "lines" in mode
    draw_markers = "markers" in mode
    if not draw_line and not draw_markers:
        # e.g. mode="text" or "none" — fall back to a line so the series shows.
        draw_line = True

    if draw_line:
        canvas.line(points, color=ctx.color)
    if draw_markers:
        canvas.markers(points, ctx.glyph, color=ctx.color)


register_adapter("scatter", scatter_adapter)
register_adapter("scattergl", scatter_adapter)
