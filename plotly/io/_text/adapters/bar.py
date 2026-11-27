"""``bar`` adapter.

Bars -> fractionally filled cells via :meth:`Canvas.bar`. **Honours the figure's
``orientation``** (``"v"``/``"h"``) — never silently reorients the user's chart.
Knows nothing about block-char glyphs.
"""

from __future__ import annotations

from typing import List, Tuple

from plotly.io._text.adapters import (
    AdapterContext,
    _as_float,
    _coerce_numeric,
    _group_offset,
    _grouped_density_warning,
    register_adapter,
)
from plotly.io._text.canvas import Canvas


def bar_positions_values(trace: dict) -> Tuple[List[float], List[float], str, float]:
    """Return ``(positions, values, orientation, base)`` for a bar trace.

    Honours the figure's own ``orientation`` (never silently reorients): for the
    default ``"v"`` the categories live on ``x`` and the lengths on ``y``; for
    ``"h"`` the categories live on ``y`` and the lengths on ``x``. Categorical
    positions map to integer indices; only a scalar ``base`` is supported in v1
    (a per-bar ``base`` array falls back to ``0``).
    """
    orientation = trace.get("orientation") or "v"
    base = _as_float(trace.get("base"))
    base = base if base is not None else 0.0

    x = trace.get("x")
    y = trace.get("y")

    if orientation == "h":
        values = _coerce_numeric(x) if x is not None else []
        positions = (
            _coerce_numeric(y)
            if y is not None
            else list(map(float, range(len(values))))
        )
    else:
        values = _coerce_numeric(y) if y is not None else []
        positions = (
            _coerce_numeric(x)
            if x is not None
            else list(map(float, range(len(values))))
        )

    n = min(len(positions), len(values))
    return positions[:n], values[:n], orientation, base


def bar_adapter(trace: dict, canvas: Canvas, ctx: AdapterContext) -> None:
    """Draw one ``bar`` trace onto ``canvas``.

    Derives category positions and values from ``trace["x"]``/``trace["y"]``
    per ``trace.get("orientation", "v")`` and calls :meth:`Canvas.bar` with the
    same orientation. When several series share a category axis, each is offset
    into its own sub-column (via :func:`_group_offset`) so a later series never
    silently overwrites an earlier one; if the canvas is too narrow to separate
    them a one-line density note is appended (honesty floor).
    """
    positions, values, orientation, base = bar_positions_values(trace)
    if not positions:
        return
    positions, collided = _group_offset(positions, ctx, orientation, canvas)
    if collided:
        note = _grouped_density_warning(ctx.mode)
        if note not in ctx.warnings:
            ctx.warnings.append(note)
    canvas.bar(positions, values, orientation=orientation, base=base, color=ctx.color)


register_adapter("bar", bar_adapter)
