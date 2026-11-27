"""Trace adapters — ``go.Figure`` -> Canvas calls.

An **adapter** translates one Plotly trace (a plain dict from
``fig_dict["data"]``) into a sequence of Plotly-agnostic
:class:`~plotly.io._text.canvas.Canvas` calls. Adapters know **nothing about
braille or glyph encodings** — they speak only the Canvas contract. The
serializers later turn the grid into text.

This package owns:

* the :data:`ADAPTERS` registry keyed by trace ``type`` string,
* :func:`register_adapter` / :func:`get_adapter`,
* :func:`figure_to_canvas`, the top-level ``fig_dict -> drawn Canvas`` driver.

The built-in handlers (``scatter``/``scattergl``, ``bar``, ``histogram``,
``heatmap``/``histogram2d``) live in sibling modules and self-register on import.

The :data:`TraceAdapter` signature, the :class:`AdapterContext` shape, the
registry, and :func:`figure_to_canvas` are the stable interface a new handler
plugs into.
"""

from __future__ import annotations

import base64
import math
import re
import struct
from dataclasses import dataclass, field
from typing import Callable, Dict, List, NamedTuple, Optional, Sequence, Tuple

from _plotly_utils.basevalidators import is_typed_array_spec
from _plotly_utils.utils import plotlyjsShortTypes

from plotly.io._text.canvas import (
    Canvas,
    DEFAULT_HEIGHT,
    DEFAULT_WIDTH,
    Range,
    Tick,
)
from plotly.io._text.rasterizer import MARKER_COLORS, MARKER_GLYPHS


@dataclass
class AdapterContext:
    """Per-trace shared state handed to every adapter by the driver.

    Carries what a handler needs beyond the trace itself: the figure layout, the
    shared data ranges the frame was drawn with, the series' assigned glyph /
    colour, and a sink for degradation notes.
    """

    #: the figure's ``layout`` dict (titles, axis config, ...).
    layout: dict
    #: shared x data range the frame was drawn with.
    x_range: Range
    #: shared y data range the frame was drawn with.
    y_range: Range
    #: 0-based index of this trace among rendered traces.
    series_index: int
    #: the marker glyph assigned to this series.
    glyph: str
    #: colour assigned to this series (v2 modes); None in v1.
    color: Optional[str] = None
    #: degradation notes to print.
    warnings: List[str] = field(default_factory=list)
    #: total number of rendered series — lets bar/histogram offset each series
    #: into its own sub-column so grouped series don't overwrite each other
    #: (scatter ignores it).
    series_count: int = 1
    #: the target output mode, so an adapter can format a mode-correct note
    #: (``text-ascii`` degrades the ``⚠`` prefix to ``!``).
    mode: str = "text-utf"


#: An adapter draws one trace onto the canvas. It must not return anything and
#: must not touch glyph encodings — only Canvas primitives + ``ctx``.
TraceAdapter = Callable[[dict, Canvas, AdapterContext], None]


#: Registry of adapters keyed by trace ``type`` (e.g. ``"scatter"``, ``"bar"``).
#: ``"scattergl"`` maps to the same handler as ``"scatter"``.
ADAPTERS: Dict[str, TraceAdapter] = {}


def register_adapter(trace_type: str, handler: TraceAdapter) -> None:
    """Register ``handler`` for trace ``type`` ``trace_type``."""
    ADAPTERS[trace_type] = handler


def get_adapter(trace_type: str) -> Optional[TraceAdapter]:
    """Return the adapter for ``trace_type`` or ``None`` if unsupported."""
    return ADAPTERS.get(trace_type)


# ---------------------------------------------------------------------------
# Series styling — distinct semantic marker glyph per series.
# ---------------------------------------------------------------------------

#: Semantic marker glyphs cycled across series. Sourced from the canonical
#: :data:`plotly.io._text.rasterizer.MARKER_GLYPHS` (which pairs each unicode
#: glyph with a distinct 7-bit ascii fallback) so ``text-utf`` and ``text-ascii``
#: markers stay index-aligned. These are *intent* glyphs handed to
#: :meth:`Canvas.markers` via :attr:`AdapterContext.glyph`.
GLYPH_PALETTE: Tuple[str, ...] = tuple(MARKER_GLYPHS)

#: Per-series colour palette cycled across series (colour modes). Sourced from
#: the canonical :data:`plotly.io._text.rasterizer.MARKER_COLORS`, which is
#: index-aligned with :data:`GLYPH_PALETTE` so a series' glyph and colour share a
#: slot. Handed to the colour-aware Canvas calls via :attr:`AdapterContext.color`.
COLOR_PALETTE: Tuple[str, ...] = tuple(MARKER_COLORS)

#: Human-facing template for an unsupported trace type.
UNSUPPORTED_MSG = "{ttype} traces aren't supported by the text renderer"


def _warn_prefix(mode: str) -> str:
    """``⚠`` for unicode modes, ascii ``!`` for ``text-ascii`` (encodable)."""
    return "! " if mode == "text-ascii" else "⚠ "


def _assign_glyph(series_index: int) -> str:
    """Return the marker glyph for the ``series_index``-th rendered series."""
    return GLYPH_PALETTE[series_index % len(GLYPH_PALETTE)]


# ---------------------------------------------------------------------------
# Colour normalization — every colour that reaches a Cell must be a
# ``#rrggbb`` hex, because the v2 colour serializers parse ``#hex`` only. Plotly
# colours arrive in many idiomatic forms (``#hex`` / ``#rgb``, ``rgb()`` /
# ``rgba()``, and CSS names like ``"red"`` / ``"steelblue"``); this bridge maps
# all of them to hex and returns ``None`` for anything unresolvable so the caller
# can fall back to the palette rather than crash the serializer. Same discipline
# the heatmap colorscale path already uses (which now imports :func:`_color_to_hex`
# from here so there is a single implementation for the whole adapter package).
# ---------------------------------------------------------------------------

#: Standard CSS3 / SVG named-colour hex table (CSS Color Module Level 4). Keys
#: are exactly the names plotly validates in
#: :attr:`_plotly_utils.basevalidators.ColorValidator.named_colors`; we assert
#: full coverage on import (below) so a plotly-accepted name always resolves.
_CSS_NAMED_COLORS: Dict[str, str] = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aqua": "#00ffff",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "bisque": "#ffe4c4",
    "black": "#000000",
    "blanchedalmond": "#ffebcd",
    "blue": "#0000ff",
    "blueviolet": "#8a2be2",
    "brown": "#a52a2a",
    "burlywood": "#deb887",
    "cadetblue": "#5f9ea0",
    "chartreuse": "#7fff00",
    "chocolate": "#d2691e",
    "coral": "#ff7f50",
    "cornflowerblue": "#6495ed",
    "cornsilk": "#fff8dc",
    "crimson": "#dc143c",
    "cyan": "#00ffff",
    "darkblue": "#00008b",
    "darkcyan": "#008b8b",
    "darkgoldenrod": "#b8860b",
    "darkgray": "#a9a9a9",
    "darkgrey": "#a9a9a9",
    "darkgreen": "#006400",
    "darkkhaki": "#bdb76b",
    "darkmagenta": "#8b008b",
    "darkolivegreen": "#556b2f",
    "darkorange": "#ff8c00",
    "darkorchid": "#9932cc",
    "darkred": "#8b0000",
    "darksalmon": "#e9967a",
    "darkseagreen": "#8fbc8f",
    "darkslateblue": "#483d8b",
    "darkslategray": "#2f4f4f",
    "darkslategrey": "#2f4f4f",
    "darkturquoise": "#00ced1",
    "darkviolet": "#9400d3",
    "deeppink": "#ff1493",
    "deepskyblue": "#00bfff",
    "dimgray": "#696969",
    "dimgrey": "#696969",
    "dodgerblue": "#1e90ff",
    "firebrick": "#b22222",
    "floralwhite": "#fffaf0",
    "forestgreen": "#228b22",
    "fuchsia": "#ff00ff",
    "gainsboro": "#dcdcdc",
    "ghostwhite": "#f8f8ff",
    "gold": "#ffd700",
    "goldenrod": "#daa520",
    "gray": "#808080",
    "grey": "#808080",
    "green": "#008000",
    "greenyellow": "#adff2f",
    "honeydew": "#f0fff0",
    "hotpink": "#ff69b4",
    "indianred": "#cd5c5c",
    "indigo": "#4b0082",
    "ivory": "#fffff0",
    "khaki": "#f0e68c",
    "lavender": "#e6e6fa",
    "lavenderblush": "#fff0f5",
    "lawngreen": "#7cfc00",
    "lemonchiffon": "#fffacd",
    "lightblue": "#add8e6",
    "lightcoral": "#f08080",
    "lightcyan": "#e0ffff",
    "lightgoldenrodyellow": "#fafad2",
    "lightgray": "#d3d3d3",
    "lightgrey": "#d3d3d3",
    "lightgreen": "#90ee90",
    "lightpink": "#ffb6c1",
    "lightsalmon": "#ffa07a",
    "lightseagreen": "#20b2aa",
    "lightskyblue": "#87cefa",
    "lightslategray": "#778899",
    "lightslategrey": "#778899",
    "lightsteelblue": "#b0c4de",
    "lightyellow": "#ffffe0",
    "lime": "#00ff00",
    "limegreen": "#32cd32",
    "linen": "#faf0e6",
    "magenta": "#ff00ff",
    "maroon": "#800000",
    "mediumaquamarine": "#66cdaa",
    "mediumblue": "#0000cd",
    "mediumorchid": "#ba55d3",
    "mediumpurple": "#9370db",
    "mediumseagreen": "#3cb371",
    "mediumslateblue": "#7b68ee",
    "mediumspringgreen": "#00fa9a",
    "mediumturquoise": "#48d1cc",
    "mediumvioletred": "#c71585",
    "midnightblue": "#191970",
    "mintcream": "#f5fffa",
    "mistyrose": "#ffe4e1",
    "moccasin": "#ffe4b5",
    "navajowhite": "#ffdead",
    "navy": "#000080",
    "oldlace": "#fdf5e6",
    "olive": "#808000",
    "olivedrab": "#6b8e23",
    "orange": "#ffa500",
    "orangered": "#ff4500",
    "orchid": "#da70d6",
    "palegoldenrod": "#eee8aa",
    "palegreen": "#98fb98",
    "paleturquoise": "#afeeee",
    "palevioletred": "#db7093",
    "papayawhip": "#ffefd5",
    "peachpuff": "#ffdab9",
    "peru": "#cd853f",
    "pink": "#ffc0cb",
    "plum": "#dda0dd",
    "powderblue": "#b0e0e6",
    "purple": "#800080",
    "red": "#ff0000",
    "rosybrown": "#bc8f8f",
    "royalblue": "#4169e1",
    "rebeccapurple": "#663399",
    "saddlebrown": "#8b4513",
    "salmon": "#fa8072",
    "sandybrown": "#f4a460",
    "seagreen": "#2e8b57",
    "seashell": "#fff5ee",
    "sienna": "#a0522d",
    "silver": "#c0c0c0",
    "skyblue": "#87ceeb",
    "slateblue": "#6a5acd",
    "slategray": "#708090",
    "slategrey": "#708090",
    "snow": "#fffafa",
    "springgreen": "#00ff7f",
    "steelblue": "#4682b4",
    "tan": "#d2b48c",
    "teal": "#008080",
    "thistle": "#d8bfd8",
    "tomato": "#ff6347",
    "turquoise": "#40e0d0",
    "violet": "#ee82ee",
    "wheat": "#f5deb3",
    "white": "#ffffff",
    "whitesmoke": "#f5f5f5",
    "yellow": "#ffff00",
    "yellowgreen": "#9acd32",
}


def _hex_or_none(s: str) -> Optional[str]:
    """Normalize ``#rgb``/``#rrggbb`` to lowercase ``#rrggbb``, else ``None``."""
    h = s[1:] if s.startswith("#") else s
    if len(h) == 3:
        h = "".join(ch * 2 for ch in h)
    if len(h) == 6 and all(ch in "0123456789abcdef" for ch in h):
        return "#" + h
    return None


def _color_to_hex(c) -> Optional[str]:
    """Convert one plotly colour spec to ``#rrggbb``, or ``None`` if unresolvable.

    Handles every idiomatic plotly colour string: ``#hex`` / ``#rgb`` (normalized),
    ``rgb(...)`` / ``rgba(...)`` (parsed; alpha dropped — the text grid has no
    compositing), and CSS named colours via :data:`_CSS_NAMED_COLORS`. Returns
    ``None`` for a non-string, an empty string, or anything unrecognized so the
    caller can fall back to the palette instead of feeding a raw string to the
    ``#hex``-only colour serializers. This is the single colour bridge for the
    whole adapter package (the heatmap colorscale path imports it too).
    """
    if not isinstance(c, str):
        return None
    s = c.strip().lower()
    if not s:
        return None
    if s.startswith("#"):
        return _hex_or_none(s)
    if s.startswith("rgb"):
        nums = re.findall(r"[-+]?\d*\.?\d+", s)
        if len(nums) >= 3:
            r, g, b = (max(0, min(255, int(round(float(nums[i]))))) for i in range(3))
            return "#%02x%02x%02x" % (r, g, b)
        return None
    return _CSS_NAMED_COLORS.get(s)


def _single_trace_color(trace: dict) -> Optional[str]:
    """Return the trace's own single colour as ``#rrggbb``, or ``None``.

    Reads ``marker.color`` then ``line.color`` and accepts only a *single* colour
    string (e.g. ``"#636efa"`` / ``"red"`` / ``"rgb(1,2,3)"``), which is
    **normalized to hex** via :func:`_color_to_hex` before it can reach a
    :class:`~plotly.io._text.canvas.Cell` — the v2 colour serializers parse hex
    only, so a raw CSS name / ``rgb()`` string would otherwise crash them. A
    per-point colour **array** (numeric or list) is not a series colour, and an
    unresolvable colour string also yields ``None``, so the caller falls back to
    the categorical palette. This is the per-series colour source for the colour
    modes.
    """
    for key in ("marker", "line"):
        spec = trace.get(key)
        if isinstance(spec, dict):
            c = spec.get("color")
            if isinstance(c, str):
                return _color_to_hex(c)
    return None


def _assign_color(trace: dict, series_index: int) -> str:
    """Resolve the ``series_index``-th series' colour hex (v2 colour modes).

    The trace's own single :func:`_single_trace_color` wins; otherwise a colour
    is assigned from :data:`COLOR_PALETTE` (Plotly's default qualitative colorway)
    by ``series_index``, index-aligned with the assigned glyph. Always returns a
    hex/colour string so the colour-aware Canvas calls have a value; the
    monochrome v1 modes simply ignore :attr:`Cell.fg`.
    """
    return (
        _single_trace_color(trace) or COLOR_PALETTE[series_index % len(COLOR_PALETTE)]
    )


def _unsupported_warning(ttype: str, mode: str) -> str:
    """Format the one-line degradation note for an unsupported ``ttype``.

    The prefix degrades to ASCII for ``text-ascii`` so the note itself stays
    encodable on locale-hostile sinks (the whole point of that mode).
    """
    return _warn_prefix(mode) + UNSUPPORTED_MSG.format(ttype=ttype)


def _is_too_small_error(exc: Exception) -> bool:
    """True only for the genuine undersized-canvas / frame ``ValueError``.

    :meth:`Canvas.__init__` and :meth:`Canvas.frame` are the only
    places that raise a *size* ``ValueError`` — their messages say ``"too small"``
    (frame) or ``"must be at least"`` (constructor). Matching on that lets the
    renderer's defensive serialize-time ``except`` degrade a real undersize signal
    to a note while re-raising any *other* ``ValueError`` accurately, instead of
    mislabelling it "canvas too small" on a full-size canvas.
    """
    msg = str(exc)
    return "too small" in msg or "must be at least" in msg


def _too_small_warning(mode: str, exc: Exception) -> str:
    """One-line graceful note for an undersized canvas (the Canvas raises
    ``ValueError`` from :meth:`Canvas.__init__` / :meth:`Canvas.frame`).

    Surfaces the minimum size from the Canvas message when present, using an
    ascii ``x`` separator so the note is safe in every mode.
    """
    m = re.search(r"at least (\d+)\s*[x×]\s*(\d+)", str(exc))
    if m:
        core = f"canvas too small to render (need at least {m.group(1)}x{m.group(2)} cells)"
    else:
        core = "canvas too small to render (increase width/height)"
    return _warn_prefix(mode) + core


def _grouped_density_warning(mode: str) -> str:
    """Honesty note when grouped bars can't be separated into sub-columns."""
    return _warn_prefix(mode) + (
        "grouped bars exceed the canvas width — some series merge (widen the canvas)"
    )


# ---------------------------------------------------------------------------
# Typed-array decoding — plotly.py base64-encodes numpy arrays on
# ``to_dict`` into ``{"dtype": "f8", "bdata": "..."}`` typed-array specs; the
# adapters must decode them back to numbers or the coercion path iterates the
# dict *keys* and renders garbage. numpy is used when present (fast path) with a
# stdlib ``struct`` fallback so the renderer stays numpy-optional.
# ---------------------------------------------------------------------------

#: plotly.js short dtype -> numpy dtype name (inverse of plotly's own table).
_SHORT_TO_NP: Dict[str, str] = {
    short: name for name, short in plotlyjsShortTypes.items()
}

#: plotly.js short dtype -> stdlib ``struct`` format char (fixed little-endian
#: sizes when prefixed with ``<``), for the numpy-absent fallback.
_SHORT_TO_STRUCT: Dict[str, str] = {
    "i1": "b",
    "u1": "B",
    "i2": "h",
    "u2": "H",
    "i4": "i",
    "u4": "I",
    "f4": "f",
    "f8": "d",
}

#: Test hook: force the numpy-optional pure-Python paths even when numpy is
#: importable (so both branches are covered without uninstalling numpy).
_FORCE_NO_NUMPY = False


def _numpy():
    """Return the ``numpy`` module, or ``None`` (honouring :data:`_FORCE_NO_NUMPY`)."""
    if _FORCE_NO_NUMPY:
        return None
    try:
        import numpy as np

        return np
    except ImportError:
        return None


def _decode_typed_array(spec: dict) -> List[float]:
    """Decode a plotly.js typed-array spec ``{"dtype", "bdata"}`` to a list.

    Uses ``numpy.frombuffer`` when numpy is available, else a stdlib
    ``base64`` + ``struct`` unpack (little-endian, matching plotly.js).
    """
    dtype = spec.get("dtype")
    bdata = spec.get("bdata", "")
    raw = base64.b64decode(bdata) if isinstance(bdata, str) else bytes(bdata)

    np = _numpy()
    if np is not None and dtype in _SHORT_TO_NP:
        return np.frombuffer(raw, dtype=_SHORT_TO_NP[dtype]).tolist()

    if not isinstance(dtype, str):
        return []
    code = _SHORT_TO_STRUCT.get(dtype)
    if code is None:
        return []
    size = struct.calcsize("<" + code)
    n = len(raw) // size
    if n == 0:
        return []
    return list(struct.unpack("<%d%s" % (n, code), raw[: n * size]))


def _as_sequence(v):
    """Normalize any array-like to a plain sequence (or ``None``).

    Handles typed-array specs (decoded), lists/tuples (passed through), other
    iterables like numpy arrays / pandas Series (materialized), and rejects a
    non-array dict (returns ``None``) so it is never iterated by key.
    """
    if v is None:
        return None
    if is_typed_array_spec(v):
        return _decode_typed_array(v)
    if isinstance(v, (list, tuple)):
        return v
    if isinstance(v, dict):
        return None
    try:
        return list(v)
    except TypeError:
        return [v]


# ---------------------------------------------------------------------------
# Numeric coercion helpers — shared with the sibling handler modules.
# ---------------------------------------------------------------------------


def _is_finite_number(v) -> bool:
    """True for a real, finite int/float (bools and NaN/inf excluded)."""
    return isinstance(v, (int, float)) and not isinstance(v, bool) and math.isfinite(v)


def _as_float(v) -> Optional[float]:
    """Best-effort convert ``v`` to a finite float, else ``None``.

    Booleans are rejected (they are not data), as are NaN/inf and unparseable
    strings — categorical/None values return ``None`` so callers can decide how
    to place them (typically by positional index).
    """
    if isinstance(v, bool) or v is None:
        return None
    if isinstance(v, (int, float)):
        return float(v) if math.isfinite(v) else None
    try:
        f = float(v)
    except (TypeError, ValueError):
        return None
    return f if math.isfinite(f) else None


def _coerce_numeric(seq) -> List[float]:
    """Map a data array to floats, substituting the positional index for any
    non-numeric (categorical / missing) entry.

    The input is first normalized via :func:`_as_sequence`, so a base64
    typed-array spec (from ``fig.to_dict()`` on numpy data) is decoded rather
    than iterated by key. This is a v1 simplification: categorical axes render
    against integer positions rather than true category ticks.
    """
    seq = _as_sequence(seq)
    if not seq:
        return []
    out: List[float] = []
    for i, v in enumerate(seq):
        f = _as_float(v)
        out.append(f if f is not None else float(i))
    return out


# ---------------------------------------------------------------------------
# Range / frame helpers.
# ---------------------------------------------------------------------------


def _range_of(vals: Sequence, fallback: Range) -> Range:
    """Return a ``(min, max)`` range over the finite numbers in ``vals``.

    Falls back to ``fallback`` when there is no numeric data, and pads a
    degenerate (min == max) range so the frame has non-zero extent.
    """
    nums = [float(v) for v in vals if _is_finite_number(v)]
    if not nums:
        return fallback
    lo, hi = min(nums), max(nums)
    if lo == hi:
        pad = abs(lo) * 0.05 or 0.5
        return (lo - pad, hi + pad)
    return (lo, hi)


def _bar_extent(
    positions: Sequence[float],
    values: Sequence[float],
    orientation: str,
    base: float,
) -> Tuple[List[float], List[float]]:
    """(xs, ys) data extent contributed by a bar/histogram-style trace.

    The value axis includes ``base`` so bars are always framed from their
    baseline; orientation decides which axis carries positions vs values.
    """
    vals = [float(v) for v in values] + [float(base)]
    pos = [float(p) for p in positions]
    if orientation == "h":
        return (vals, pos)
    return (pos, vals)


def _trace_extent(trace: dict, ttype: str):
    """Return ``(xs, ys)`` this trace contributes to the shared ranges.

    Reuses each handler's own data extraction (imported lazily to avoid an
    import cycle) so the range and the drawing never disagree. ``None`` means
    the trace contributes nothing.
    """
    if ttype in ("scatter", "scattergl"):
        from plotly.io._text.adapters.scatter import scatter_xy

        xs, ys, _mode = scatter_xy(trace)
        return (xs, ys)
    if ttype == "bar":
        from plotly.io._text.adapters.bar import bar_positions_values

        positions, values, orientation, base = bar_positions_values(trace)
        return _bar_extent(positions, values, orientation, base)
    if ttype == "histogram":
        from plotly.io._text.adapters.histogram import histogram_bins

        _centers, counts, edges, orientation = histogram_bins(trace)
        # Use the bin *edges* for the position axis so the frame spans the data.
        return _bar_extent(edges, counts, orientation, 0.0)
    if ttype == "heatmap":
        from plotly.io._text.adapters.heatmap import heatmap_extent

        return heatmap_extent(trace)
    if ttype == "histogram2d":
        from plotly.io._text.adapters.heatmap import histogram2d_extent

        return histogram2d_extent(trace)
    return None


def _fmt_tick(v: float) -> str:
    """Compact label for a tick value (integers without a trailing ``.0``)."""
    try:
        if v == int(v):
            return str(int(v))
    except (OverflowError, ValueError):
        pass
    return f"{v:.3g}"


def _derive_ticks(rng: Range, n: int = 3) -> List[Tick]:
    """Evenly spaced ticks across ``rng`` (Plotly-agnostic numeric ticks)."""
    lo, hi = rng
    if n < 2 or hi <= lo:
        return [Tick(lo, _fmt_tick(lo))]
    step = (hi - lo) / (n - 1)
    return [Tick(lo + i * step, _fmt_tick(lo + i * step)) for i in range(n)]


def _layout_title(layout: dict) -> Optional[str]:
    """Extract the figure title text from ``layout`` (dict or bare string)."""
    t = layout.get("title")
    if isinstance(t, dict):
        return t.get("text")
    if isinstance(t, str):
        return t
    return None


def _axis_title(layout: dict, axis: str) -> Optional[str]:
    """Extract an axis title text (``xaxis`` / ``yaxis``) from ``layout``."""
    ax = layout.get(axis)
    if not isinstance(ax, dict):
        return None
    t = ax.get("title")
    if isinstance(t, dict):
        return t.get("text")
    if isinstance(t, str):
        return t
    return None


def _group_offset(
    positions: Sequence[float],
    ctx: "AdapterContext",
    orientation: str,
    canvas: Canvas,
) -> Tuple[List[float], bool]:
    """Shift a bar/histogram series into its own sub-column within each category.

    Uses :attr:`AdapterContext.series_index` / :attr:`~AdapterContext.series_count`
    to split the ~80%-wide category slot into one lane per series (matching
    Plotly's grouped-bar layout) so concurrent series never draw into the same
    cells. Returns ``(shifted_positions, collided)`` where ``collided`` is True
    when a lane is narrower than one character cell (so bars would still merge).
    """
    positions = [float(p) for p in positions]
    count = max(1, getattr(ctx, "series_count", 1))
    if count <= 1 or not positions:
        return positions, False

    if orientation == "h":
        lo, hi = ctx.y_range
        span_cells = getattr(canvas, "height", DEFAULT_HEIGHT)
    else:
        lo, hi = ctx.x_range
        span_cells = getattr(canvas, "width", DEFAULT_WIDTH)

    uniq = sorted(set(positions))
    if len(uniq) > 1:
        spacing = min(b - a for a, b in zip(uniq, uniq[1:]))
    else:
        spacing = (hi - lo) if hi > lo else 1.0

    lane = (spacing * 0.8) / count
    offset = (ctx.series_index - (count - 1) / 2.0) * lane
    shifted = [p + offset for p in positions]

    data_per_cell = (hi - lo) / max(1, span_cells) if hi > lo else float("inf")
    collided = lane < data_per_cell
    return shifted, collided


class DrawResult(NamedTuple):
    """The result of :func:`figure_to_canvas`: the drawn canvas (``None`` when
    the figure could not be drawn, e.g. an undersized canvas) plus the ordered
    degradation notes to print after the plot.

    Replaces an earlier ``canvas._adapter_warnings`` dynamic-attribute stash:
    passing the notes back explicitly keeps this a clean internal contract
    between :func:`figure_to_canvas` and
    :class:`plotly.io._text.renderers.TextRenderer`, not a Canvas API change.
    """

    canvas: Optional[Canvas]
    warnings: List[str]


def figure_to_canvas(
    fig_dict: dict,
    *,
    width: int = DEFAULT_WIDTH,
    height: int = DEFAULT_HEIGHT,
    mode: str = "text-utf",
) -> DrawResult:
    """Draw a figure dict onto a fresh :class:`Canvas` and return a
    :class:`DrawResult` (the canvas + degradation notes).

    Responsibilities:

    1. compute the shared x/y data ranges across all *supported* traces,
    2. create the Canvas and draw the frame (title, axes, ticks); if the canvas
       is too small the Canvas raises ``ValueError`` — caught here and degraded to
       a one-line note with ``canvas=None`` (no crash out of ``fig.show``),
    3. assign a distinct glyph / colour per series and the shared series count so
       grouped bars/histograms fan out into sub-columns,
    4. dispatch each trace to its :data:`ADAPTERS` handler; for an unsupported
       trace, append a one-line note and skip it (graceful degradation),
    5. return the :class:`DrawResult` (the caller serializes ``result.canvas``).

    ``mode`` is passed through (via :attr:`AdapterContext.mode`) so handlers can
    format mode-correct notes; the grid->string step happens in
    :meth:`Canvas.render`.
    """
    data = list(fig_dict.get("data") or [])
    layout = dict(fig_dict.get("layout") or {})
    warnings: List[str] = []

    # 1. Partition traces into supported / unsupported, preserving order.
    supported: List[Tuple[dict, str]] = []
    for trace in data:
        ttype = trace.get("type") or "scatter"
        if get_adapter(ttype) is not None:
            supported.append((trace, ttype))
        else:
            warnings.append(_unsupported_warning(ttype, mode))

    # 2. Shared ranges across the supported traces.
    xs_all: List[float] = []
    ys_all: List[float] = []
    for trace, ttype in supported:
        extent = _trace_extent(trace, ttype)
        if extent is not None:
            txs, tys = extent
            xs_all.extend(txs)
            ys_all.extend(tys)

    x_range = _range_of(xs_all, (0.0, 1.0))
    y_range = _range_of(ys_all, (0.0, 1.0))

    # 3. Frame (fixes the data->cell transform). Degrade an undersized canvas.
    try:
        canvas = Canvas(width=width, height=height)
        canvas.frame(
            x_range,
            y_range,
            x_ticks=_derive_ticks(x_range),
            y_ticks=_derive_ticks(y_range),
            title=_layout_title(layout),
            x_title=_axis_title(layout, "xaxis"),
            y_title=_axis_title(layout, "yaxis"),
        )
    except ValueError as exc:
        warnings.append(_too_small_warning(mode, exc))
        return DrawResult(canvas=None, warnings=warnings)

    # 4. Dispatch each supported trace with a shared warning sink + series count.
    series_count = len(supported)
    for series_index, (trace, ttype) in enumerate(supported):
        ctx = AdapterContext(
            layout=layout,
            x_range=x_range,
            y_range=y_range,
            series_index=series_index,
            glyph=_assign_glyph(series_index),
            color=_assign_color(trace, series_index),
            warnings=warnings,
            series_count=series_count,
            mode=mode,
        )
        handler = get_adapter(ttype)
        if handler is None:
            continue  # unreachable: only supported (registered) ttypes reach here
        handler(trace, canvas, ctx)

    return DrawResult(canvas=canvas, warnings=warnings)
