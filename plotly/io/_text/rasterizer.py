"""Braille + block-char rasterization primitives (built in — no dependencies).

We deliberately do **not** depend on ``plotli`` / ``drawille`` / ``plotille`` or
any external terminal library: those duplicate the figure/plot layer we already
have in ``go.Figure`` and assume an interactive TTY, whereas these text renderers
are CI-first (no TTY) and must stay portable, dependency-free plain-text output.

This module owns the low-level glyph tables and the (x, y) -> sub-cell packing
that :class:`~plotly.io._text.canvas.Canvas` builds on. The braille bit layout
below is a fixed constant defined by the Unicode braille standard, not a stub.
"""

from __future__ import annotations

import re
from typing import Dict, Optional, Tuple

#: Unicode braille patterns occupy U+2800..U+28FF; a cell's 8 dots are a 2x4
#: grid whose set bits are OR-ed onto this base to pick the codepoint.
BRAILLE_BASE = 0x2800

#: Braille dot bit for each (sub-column, sub-row) within a 2x4 cell, using the
#: standard Unicode braille numbering. ``BRAILLE_BITS[col][row]``:
#:
#:      col 0   col 1
#:   r0  0x01    0x08
#:   r1  0x02    0x10
#:   r2  0x04    0x20
#:   r3  0x40    0x80
BRAILLE_BITS: Tuple[Tuple[int, int, int, int], Tuple[int, int, int, int]] = (
    (0x01, 0x02, 0x04, 0x40),
    (0x08, 0x10, 0x20, 0x80),
)

#: Vertical block ramp for bars / partial fills, index = eighths filled (0..8).
#: 0 -> space, 8 -> full block. Used by the ``text-utf`` serializer.
BLOCK_RAMP_V = (" ", "▁", "▂", "▃", "▄", "▅", "▆", "▇", "█")

#: Horizontal block ramp (left-growing), index = eighths filled (0..8).
BLOCK_RAMP_H = (" ", "▏", "▎", "▍", "▌", "▋", "▊", "▉", "█")

#: ASCII fallback ramp for braille-dot density (popcount 0..8), for ``text-ascii``.
ASCII_DENSITY = (" ", ".", ".", ":", ":", "+", "+", "#", "#")

#: ASCII fallback ramp for bar fill fraction, index = round(fill * 4), 0..4.
ASCII_BAR_RAMP = (" ", ".", ":", "+", "#")

# ---------------------------------------------------------------------------
# Box-drawing glyphs for the axis frame (text-utf). The Canvas stamps these as
# ``CellRole.FRAME`` chars; the ascii serializer degrades them via
# :data:`FRAME_ASCII`. Keeping the vocabulary here (not in the Canvas) means the
# frame's glyph set and its ascii fallback stay defined side by side.
# ---------------------------------------------------------------------------

BOX_V = "│"  #: │  vertical axis line
BOX_H = "─"  #: ─  horizontal axis line
BOX_CORNER_BL = "└"  #: └  bottom-left corner (origin)
BOX_TICK_Y = "┤"  #: ┤  y-axis tick mark (on the vertical line)
BOX_TICK_X = "┬"  #: ┬  x-axis tick mark (on the horizontal line)

#: Degrade box-drawing / tick glyphs to the 7-bit ``text-ascii`` palette.
FRAME_ASCII = {
    BOX_V: "|",
    BOX_H: "-",
    BOX_CORNER_BL: "+",
    BOX_TICK_Y: "+",
    BOX_TICK_X: "+",
}

# ---------------------------------------------------------------------------
# Per-series marker glyphs. This is the *canonical* palette for the whole
# renderer: the trace adapters import :data:`MARKER_GLYPHS` and
# assign one glyph per series (cycling); the ascii serializer degrades each to
# its distinct 7-bit counterpart via :data:`MARKER_GLYPHS_ASCII` (index-aligned)
# so multi-series ``text-ascii`` plots stay legible instead of collapsing to a
# single ``*``. Keep the two tuples the same length and order.
# ---------------------------------------------------------------------------

#: Unicode per-series marker glyphs, in assignment order. Canonical home — do
#: not redefine elsewhere; the trace adapters import this.
MARKER_GLYPHS = ("●", "■", "▲", "◆", "▼", "★", "✚", "◇")

#: 7-bit ASCII counterparts, index-aligned with :data:`MARKER_GLYPHS`.
MARKER_GLYPHS_ASCII = ("o", "#", "^", "x", "v", "*", "+", "@")

#: Map each Unicode marker glyph to its distinct ascii counterpart. Typed as a
#: plain ``str`` -> ``str`` map so serializers can look up an arbitrary
#: ``Cell.char`` (a ``str``) without a literal-key mismatch.
MARKER_ASCII: Dict[str, str] = dict(zip(MARKER_GLYPHS, MARKER_GLYPHS_ASCII))

#: Per-series colour palette for the v2 colour modes (``text-ansi`` /
#: ``text-html``). Plotly's default qualitative colorway (``plotly`` template),
#: as hex, **index-aligned with** :data:`MARKER_GLYPHS` so a series' glyph and
#: its colour come from the same slot. The trace adapters assign one per series
#: (cycling) when the figure doesn't set an explicit single trace colour; the colour rides
#: :attr:`~plotly.io._text.canvas.Cell.fg`. Keep length == ``len(MARKER_GLYPHS)``.
MARKER_COLORS = (
    "#636efa",
    "#EF553B",
    "#00cc96",
    "#ab63fa",
    "#FFA15A",
    "#19d3f3",
    "#FF6692",
    "#B6E880",
)

# ---------------------------------------------------------------------------
# Heatmap density ramp. A HEATMAP cell carries a normalized value
# in ``Cell.fill`` (0..1) and an optional ``Cell.bg`` hex sampled from the
# trace's colorscale; the serializer maps the fill to a shade glyph — the block
# ramp below for ``text-utf`` / ``text-ansi`` / ``text-html``, or the 7-bit
# fallback for ``text-ascii``. Kept beside the other ramps so the density
# vocabulary and its ascii degrade live side by side (like the bar ramps).
# ---------------------------------------------------------------------------

#: Block-shade density ramp for heatmaps, index 0..4 (space -> full block).
SHADE_RAMP = (" ", "░", "▒", "▓", "█")

#: 7-bit ASCII fallback for :data:`SHADE_RAMP`, index-aligned (0..4).
SHADE_ASCII = (" ", ".", ":", "+", "#")


# ---------------------------------------------------------------------------
# Colour parsing — the single, tolerant home for turning a colour string into an
# ``(r, g, b)`` triple (canonical, imported by both canvas.py and serializers.py
# so the two never drift). Lives here beside the colour tables (MARKER_COLORS,
# the heatmap ramps). Deliberately *tolerant*: the low-level Canvas / serializers
# are the reusable, Plotly-agnostic surface, so an unparseable colour degrades to
# "no colour" (``None``) or a neutral fallback rather than crashing.
# The plotly-colour -> hex bridge (named CSS colours, colorscale name catalog)
# is the trace adapters' job; this only needs ``#hex`` and ``rgb()/rgba()``.
# ---------------------------------------------------------------------------

#: Neutral mid-grey used when a colour is required but unparseable.
NEUTRAL_COLOR = "#808080"
NEUTRAL_RGB: Tuple[int, int, int] = (128, 128, 128)

#: ``rgb(...)`` / ``rgba(...)`` head — captures the first three numeric channels.
_RGB_RE = re.compile(
    r"^rgba?\(\s*([\d.]+)\s*,\s*([\d.]+)\s*,\s*([\d.]+)", re.IGNORECASE
)


def color_to_rgb(color: object) -> Optional[Tuple[int, int, int]]:
    """Parse a colour to an ``(r, g, b)`` int triple, or ``None`` if unparseable.

    Accepts ``#rgb`` / ``#rrggbb`` (any case) and ``rgb(...)`` / ``rgba(...)``
    strings (integer or float channels, clamped to 0..255; any alpha is ignored).
    Anything else — a named CSS colour, a malformed string, a non-string — returns
    ``None`` so the caller can degrade cleanly instead of raising.
    """
    if not isinstance(color, str):
        return None
    s = color.strip()
    if not s:
        return None
    if s.startswith("#"):
        h = s[1:]
        if len(h) == 3:
            h = "".join(ch * 2 for ch in h)
        if len(h) != 6:
            return None
        try:
            return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
        except ValueError:
            return None
    m = _RGB_RE.match(s)
    if m:
        try:
            vals = [max(0, min(255, round(float(g)))) for g in m.groups()]
        except ValueError:
            return None
        return vals[0], vals[1], vals[2]
    return None


def norm_hex(color: object) -> Optional[str]:
    """Normalize a colour to lowercase ``#rrggbb``, or ``None`` if unparseable.

    De-dup (HTML classes) and byte-stable output need one canonical spelling per
    colour (trace palettes mix case, e.g. ``#EF553B``; colorscale samples are
    already lowercase; adapters may hand through ``rgb(...)``).
    """
    rgb = color_to_rgb(color)
    if rgb is None:
        return None
    return "#%02x%02x%02x" % rgb


def braille_char(dots: int) -> str:
    """Return the Unicode braille glyph for an 8-bit sub-dot bitmask.

    ``dots`` is the OR of :data:`BRAILLE_BITS` entries for the set sub-dots.
    """
    return chr(BRAILLE_BASE + (dots & 0xFF))


def dot_bit(sub_col: int, sub_row: int) -> int:
    """Return the braille bit for a sub-dot at ``(sub_col, sub_row)`` in a cell."""
    return BRAILLE_BITS[sub_col][sub_row]


def popcount(dots: int) -> int:
    """Return the number of set sub-dots in an 8-bit braille bitmask (0..8)."""
    return bin(dots & 0xFF).count("1")
