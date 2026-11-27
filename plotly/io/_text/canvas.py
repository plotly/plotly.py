"""Text Canvas — a stateful text drawing surface.

This module is the *rasterizer* half of the text renderers. It knows **nothing
about Plotly**: it exposes a tiny drawing surface whose primitives accumulate
into an abstract **cell grid**, where each cell is a glyph slot plus optional
colour attributes with *no output encoding baked in*.

The grid is turned into a string by a per-mode :class:`~plotly.io._text.serializers.Serializer`
(``text-utf`` / ``text-ascii`` / ``text-ansi`` / ``text-html``) — that grid ->
string step is the seam the "one grid, many serializers" design rests on.

The Canvas signatures are the stable interface the adapters and serializers build
on: the trace adapters (in :mod:`~plotly.io._text.adapters`) drive these methods,
and the serializers consume the resulting grid.

Design invariants:

* **Never queries a TTY.** Size is always explicit (``width`` x ``height`` in
  character cells, default 80x24). Output is byte-identical in a CI log, a file,
  or a pipe.
* **Data coordinates in, cells out.** Drawing primitives take *data-space*
  points; the Canvas maps them to cell / sub-cell positions using ranges
  established by :meth:`set_ranges` (called directly or via :meth:`frame`).
* **No encoding in the grid.** A cell records *intent* (a braille sub-dot mask, a
  bar fill fraction, a marker/frame/label character, an optional colour), never a
  finished ``text-utf`` vs ``text-ascii`` glyph. The serializer bakes encoding.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from enum import IntEnum
from typing import Any, Iterable, List, Optional, Sequence, Tuple, cast

from plotly.io._text.rasterizer import (
    NEUTRAL_COLOR,
    NEUTRAL_RGB,
    color_to_rgb,
    norm_hex,
)

# ---------------------------------------------------------------------------
# Coordinate / geometry types
# ---------------------------------------------------------------------------

#: A single point in *data* coordinates.
Point = Tuple[float, float]
#: An ordered sequence of data-space points (e.g. a line or a marker set).
Points = Sequence[Point]
#: An inclusive ``(min, max)`` range in data coordinates.
Range = Tuple[float, float]

#: Number of braille sub-columns per character cell (braille is a 2x4 dot grid).
SUBCELL_COLS = 2
#: Number of braille sub-rows per character cell.
SUBCELL_ROWS = 4

#: Default canvas size in character cells. Never inferred from a terminal.
DEFAULT_WIDTH = 80
DEFAULT_HEIGHT = 24


class CellRole(IntEnum):
    """What a cell *means*, so a serializer can encode / degrade it per mode.

    The role tells the serializer which of the payload fields on :class:`Cell`
    to read and which glyph set to draw from.
    """

    EMPTY = 0  #: nothing drawn here — renders as blank in every mode.
    DOTS = 1  #: braille sub-dot field (lines, scatter, dot-markers): read ``dots``.
    MARKER = 2  #: a whole-cell marker glyph chosen by the adapter: read ``char``.
    BAR = 3  #: a bar segment: read ``fill`` (0..1 fraction of the cell).
    FRAME = 4  #: an axis / frame element (box-drawing): read ``char``.
    LABEL = 5  #: literal text (titles, tick labels, notes): read ``char``.
    HEATMAP = 6  #: a heatmap/histogram2d cell: read ``fill`` (0..1 density) and
    #: ``bg`` (the colorscale-sampled hex); the serializer maps ``fill`` to the
    #: shade ramp (``rasterizer.SHADE_RAMP`` / ``SHADE_ASCII``).


@dataclass
class Cell:
    """One character slot in the grid — abstract intent, not a finished glyph.

    Exactly which fields are meaningful is determined by :attr:`role`:

    ============  ============================================================
    role          meaningful payload
    ============  ============================================================
    ``EMPTY``     (none)
    ``DOTS``      :attr:`dots` — 8-bit 2x4 braille sub-dot bitmask (0..255)
    ``MARKER``    :attr:`char` — the semantic marker glyph
    ``BAR``       :attr:`fill` — fractional fill of the cell, 0.0..1.0
    ``FRAME``     :attr:`char` — the box-drawing / axis character
    ``LABEL``     :attr:`char` — the literal text character
    ``HEATMAP``   :attr:`fill` — normalized density 0..1; :attr:`bg` — hex
    ============  ============================================================

    :attr:`fg` / :attr:`bg` are colour hints consumed only by the v2 colour
    serializers (``text-ansi`` / ``text-html``); ``None`` means monochrome, which
    is what the v1 serializers always emit.
    """

    #: what this cell means; selects which payload field below is read.
    role: CellRole = CellRole.EMPTY
    #: DOTS: 2x4 braille sub-dot bitmask, see ``rasterizer.BRAILLE_BITS``.
    dots: int = 0
    #: BAR: fractional fill of the cell, 0.0..1.0.
    fill: float = 0.0
    #: MARKER / FRAME / LABEL: the semantic character (pre-encoding).
    char: str = ""
    #: colour hint for v2 serializers; None = monochrome.
    fg: Optional[str] = None
    #: background colour hint for v2 serializers.
    bg: Optional[str] = None


@dataclass
class CellGrid:
    """A ``height`` x ``width`` matrix of :class:`Cell` — the grid hand-off.

    This is the *entire* interface between the Canvas (which fills the grid) and
    the serializers (which read it). ``rows[y][x]`` is the cell at column ``x``
    (0 = left) and row ``y`` (0 = top).
    """

    width: int
    height: int
    rows: List[List[Cell]] = field(default_factory=list)

    @classmethod
    def blank(cls, width: int, height: int) -> "CellGrid":
        """Return a fresh grid of the given size, every cell ``EMPTY``."""
        return cls(
            width=width,
            height=height,
            rows=[[Cell() for _ in range(width)] for _ in range(height)],
        )

    def cell(self, x: int, y: int) -> Cell:
        """Return the cell at column ``x``, row ``y`` (top-left origin)."""
        return self.rows[y][x]


@dataclass
class Tick:
    """A single axis tick: a data-space position and its rendered label."""

    value: float
    label: str


class Canvas:
    """A stateful text drawing surface backed by an abstract :class:`CellGrid`.

    Usage (from a trace adapter)::

        canvas = Canvas(width=80, height=24)
        canvas.frame(x_range=(0, 10), y_range=(-1, 1), title="sin(x)")
        canvas.line([(x, math.sin(x)) for x in ...])
        text = canvas.render("text-utf")

    The Canvas is deliberately Plotly-agnostic: adapters translate a figure into
    these calls. All primitives take **data coordinates**; call :meth:`frame`
    (or :meth:`set_ranges`) first to fix the data->cell mapping.
    """

    def __init__(self, width: int = DEFAULT_WIDTH, height: int = DEFAULT_HEIGHT):
        """Create a blank canvas ``width`` x ``height`` character cells.

        Size is **explicit and mandatory-with-default**; the Canvas never reads
        ``$COLUMNS`` or probes a TTY. Sub-cell (braille) resolution is
        ``width*2`` x ``height*4`` dots.
        """
        if width < 1 or height < 1:
            raise ValueError("Canvas size must be at least 1x1 cells")
        self._width = int(width)
        self._height = int(height)
        self._grid = CellGrid.blank(self._width, self._height)
        # Data ranges (set by set_ranges / frame). None until fixed.
        self._x_range: Optional[Range] = None
        self._y_range: Optional[Range] = None
        # Plot region in character cells (inclusive). Defaults to the whole
        # grid; frame() shrinks it to reserve margins for axes and labels.
        self._px0 = 0
        self._py0 = 0
        self._px1 = self._width - 1
        self._py1 = self._height - 1

    # -- geometry -----------------------------------------------------------

    @property
    def width(self) -> int:
        """Canvas width in character cells."""
        return self._width

    @property
    def height(self) -> int:
        """Canvas height in character cells."""
        return self._height

    @property
    def grid(self) -> CellGrid:
        """The accumulated :class:`CellGrid` (the hand-off to serializers)."""
        return self._grid

    def set_ranges(self, x_range: Range, y_range: Range) -> None:
        """Fix the data->cell coordinate transform.

        Must be called (directly, or via :meth:`frame`) before any data-space
        primitive. ``x_range``/``y_range`` are inclusive ``(min, max)`` data
        bounds mapped onto the plot region. Establishes both the character-cell
        and the finer braille sub-cell mapping.
        """
        self._x_range = (float(x_range[0]), float(x_range[1]))
        self._y_range = (float(y_range[0]), float(y_range[1]))

    # -- internal coordinate helpers ----------------------------------------

    def _require_ranges(self) -> Tuple[Range, Range]:
        """Return the fixed ``(x_range, y_range)``, raising if not yet set.

        Returning the (now non-``None``) ranges lets callers bind them to locals
        so the coordinate maths type-checks without repeating the None guard.
        """
        if self._x_range is None or self._y_range is None:
            raise RuntimeError(
                "set_ranges() (or frame()) must be called before drawing"
            )
        return self._x_range, self._y_range

    @staticmethod
    def _frac(value: float, lo: float, hi: float) -> float:
        """Fractional position of ``value`` within ``[lo, hi]``, clamped 0..1."""
        span = hi - lo
        if span == 0:
            return 0.5
        f = (value - lo) / span
        if f < 0.0:
            return 0.0
        if f > 1.0:
            return 1.0
        return f

    def _sub_dims(self) -> Tuple[int, int]:
        """Sub-dot (width, height) of the plot region."""
        sw = (self._px1 - self._px0 + 1) * SUBCELL_COLS
        sh = (self._py1 - self._py0 + 1) * SUBCELL_ROWS
        return sw, sh

    def _data_to_subdot(self, x: float, y: float) -> Tuple[int, int]:
        """Map a data-space point to global braille sub-dot ``(scol, srow)``."""
        x_range, y_range = self._require_ranges()
        sw, sh = self._sub_dims()
        fx = self._frac(x, x_range[0], x_range[1])
        fy = self._frac(y, y_range[0], y_range[1])
        scol = self._px0 * SUBCELL_COLS + round(fx * (sw - 1))
        # y grows up, sub-rows grow down -> invert.
        srow = self._py0 * SUBCELL_ROWS + round((1.0 - fy) * (sh - 1))
        return scol, srow

    def _set_dot(self, scol: int, srow: int, color: Optional[str] = None) -> None:
        """Light one braille sub-dot, without disturbing frame/label cells.

        When ``color`` is given, the cell's :attr:`Cell.fg` is set to that hex
        (consumed only by the v2 colour serializers); ``None`` leaves it
        monochrome, so v1 callers are unaffected.
        """
        from plotly.io._text.rasterizer import BRAILLE_BITS

        cx = scol // SUBCELL_COLS
        cy = srow // SUBCELL_ROWS
        if not (0 <= cx < self._width and 0 <= cy < self._height):
            return
        cell = self._grid.rows[cy][cx]
        if cell.role not in (CellRole.EMPTY, CellRole.DOTS):
            return  # protect axis frame / labels already drawn there
        cell.role = CellRole.DOTS
        cell.dots |= BRAILLE_BITS[scol % SUBCELL_COLS][srow % SUBCELL_ROWS]
        if color is not None:
            cell.fg = color

    def _place_text(
        self, x: int, y: int, text: str, role: CellRole = CellRole.LABEL
    ) -> None:
        """Write ``text`` left-to-right starting at cell ``(x, y)`` (clamped)."""
        if not (0 <= y < self._height):
            return
        for i, ch in enumerate(text):
            cx = x + i
            if 0 <= cx < self._width:
                cell = self._grid.rows[y][cx]
                cell.role = role
                cell.char = ch

    # -- drawing primitives (data coordinates) ------------------------------

    def line(self, points: Points, *, color: Optional[str] = None) -> None:
        """Draw a polyline through ``points`` (data coords) into the grid.

        Consecutive points are connected with straight segments rasterized at
        braille sub-cell resolution (``CellRole.DOTS``); the serializer picks the
        encoding (Unicode braille for ``text-utf``, the density ramp for
        ``text-ascii``).

        ``color`` (a hex string, v2) tags every drawn cell's :attr:`Cell.fg` so
        the colour serializers (``text-ansi`` / ``text-html``) can tint the line;
        omitting it (the v1 default) leaves the cells monochrome.
        """
        self._require_ranges()
        pts = list(points)
        if not pts:
            return
        if len(pts) == 1:
            scol, srow = self._data_to_subdot(pts[0][0], pts[0][1])
            self._set_dot(scol, srow, color)
            return
        prev = self._data_to_subdot(pts[0][0], pts[0][1])
        for x, y in pts[1:]:
            cur = self._data_to_subdot(x, y)
            self._draw_subdot_segment(prev, cur, color)
            prev = cur

    def _draw_subdot_segment(
        self, a: Tuple[int, int], b: Tuple[int, int], color: Optional[str] = None
    ) -> None:
        """Bresenham line between two global sub-dot coordinates."""
        x0, y0 = a
        x1, y1 = b
        dx = abs(x1 - x0)
        dy = -abs(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        err = dx + dy
        while True:
            self._set_dot(x0, y0, color)
            if x0 == x1 and y0 == y1:
                break
            e2 = 2 * err
            if e2 >= dy:
                err += dy
                x0 += sx
            if e2 <= dx:
                err += dx
                y0 += sy

    def markers(
        self, points: Points, glyph: str, *, color: Optional[str] = None
    ) -> None:
        """Stamp a whole-cell marker ``glyph`` at each point (data coords).

        Produces ``CellRole.MARKER`` cells. ``glyph`` is the *semantic* marker
        character chosen by the adapter (e.g. one per series); a serializer may
        substitute a mode-appropriate equivalent (e.g. ``*`` in ``text-ascii``).

        ``color`` (a hex string, v2) tags each marker cell's :attr:`Cell.fg`;
        omitting it (the v1 default) leaves the markers monochrome.
        """
        self._require_ranges()
        for x, y in points:
            scol, srow = self._data_to_subdot(x, y)
            cx = scol // SUBCELL_COLS
            cy = srow // SUBCELL_ROWS
            if 0 <= cx < self._width and 0 <= cy < self._height:
                cell = self._grid.rows[cy][cx]
                cell.role = CellRole.MARKER
                cell.char = glyph
                if color is not None:
                    cell.fg = color

    def bar(
        self,
        positions: Sequence[float],
        values: Sequence[float],
        *,
        orientation: str = "v",
        base: float = 0.0,
        color: Optional[str] = None,
    ) -> None:
        """Draw bars as fractionally-filled cells (``CellRole.BAR``).

        ``positions`` are the category centres and ``values`` the bar lengths, in
        data coordinates (one entry each, paired). ``orientation`` is ``"v"``
        (vertical, grows in +y) or ``"h"`` (horizontal, grows in +x) — the
        adapter passes the figure's own orientation; the Canvas never silently
        reorients. ``base`` is the value each bar grows from. Fill fractions let
        a bar end mid-cell; the serializer maps fraction -> block ramp
        (``full block .. thin``) for ``text-utf`` or ``#`` for ``text-ascii``.

        ``color`` (a hex string, v2) tags every filled bar cell's
        :attr:`Cell.fg`; omitting it (the v1 default) leaves the bars monochrome.
        """
        self._require_ranges()
        if orientation not in ("v", "h"):
            raise ValueError("orientation must be 'v' or 'h'")
        for pos, val in zip(positions, values):
            if orientation == "v":
                self._bar_vertical(pos, val, base, color)
            else:
                self._bar_horizontal(pos, val, base, color)

    def _bar_vertical(
        self, pos: float, val: float, base: float, color: Optional[str] = None
    ) -> None:
        # Which cell column does this bar live in?
        x_range, _ = self._require_ranges()
        sw, _ = self._sub_dims()
        fx = self._frac(pos, x_range[0], x_range[1])
        cx = (self._px0 * SUBCELL_COLS + round(fx * (sw - 1))) // SUBCELL_COLS
        # Continuous cell-row edges of the bar span (top = smaller row coord).
        top = self._row_coord(max(base, val))
        bottom = self._row_coord(min(base, val))
        for cy in range(self._py0, self._py1 + 1):
            overlap = min(bottom, cy + 1) - max(top, cy)
            if overlap > 1e-9:
                self._set_bar(cx, cy, overlap, "v", color)

    def _bar_horizontal(
        self, pos: float, val: float, base: float, color: Optional[str] = None
    ) -> None:
        _, y_range = self._require_ranges()
        _, sh = self._sub_dims()
        fy = self._frac(pos, y_range[0], y_range[1])
        cy = (self._py0 * SUBCELL_ROWS + round((1.0 - fy) * (sh - 1))) // SUBCELL_ROWS
        left = self._col_coord(min(base, val))
        right = self._col_coord(max(base, val))
        for cx in range(self._px0, self._px1 + 1):
            overlap = min(right, cx + 1) - max(left, cx)
            if overlap > 1e-9:
                self._set_bar(cx, cy, overlap, "h", color)

    def _row_coord(self, y: float) -> float:
        """Continuous cell-row edge coordinate of data ``y`` (top=py0)."""
        _, y_range = self._require_ranges()
        fy = self._frac(y, y_range[0], y_range[1])
        ph = self._py1 - self._py0 + 1
        return self._py0 + (1.0 - fy) * ph

    def _col_coord(self, x: float) -> float:
        """Continuous cell-column edge coordinate of data ``x`` (left=px0)."""
        x_range, _ = self._require_ranges()
        fx = self._frac(x, x_range[0], x_range[1])
        pw = self._px1 - self._px0 + 1
        return self._px0 + fx * pw

    def _set_bar(
        self, cx: int, cy: int, fill: float, orient: str, color: Optional[str] = None
    ) -> None:
        if not (0 <= cx < self._width and 0 <= cy < self._height):
            return
        cell = self._grid.rows[cy][cx]
        if cell.role not in (CellRole.EMPTY, CellRole.BAR):
            return
        new_fill = 1.0 if fill > 1.0 else fill
        # Honesty floor: when two bars collide in one cell (grouped series, or
        # more categories/bins than plot-width columns), keep the *tallest*
        # fill so a larger value can never be silently clobbered by a later,
        # smaller one. The bar adapters separate grouped bars by column offset
        # where width allows; this max-merge is the fallback when they still overlap.
        cell.fill = max(cell.fill, new_fill) if cell.role == CellRole.BAR else new_fill
        cell.role = CellRole.BAR
        # BAR cells carry their orientation in ``char`` so the serializer knows
        # which block ramp (vertical vs horizontal) to draw the partial cell.
        cell.char = orient
        if color is not None:
            cell.fg = color

    def heatmap(
        self,
        z: Sequence[Sequence[float]],
        *,
        colorscale: Optional[object] = None,
    ) -> None:
        """Fill the plot region with a heatmap of the 2D grid ``z``.

        ``z`` is a 2D sequence of numeric rows (``z[row][col]``, row 0 at the
        top). Each character cell in the current plot region is mapped to a
        ``z`` sample, given ``CellRole.HEATMAP``, and gets:

        * :attr:`Cell.fill` = the value normalized to ``0..1`` across ``z``
          (min->0, max->1); a serializer maps that to the shade ramp
          (:data:`~plotly.io._text.rasterizer.SHADE_RAMP` for unicode modes,
          :data:`~plotly.io._text.rasterizer.SHADE_ASCII` for ``text-ascii``);
        * :attr:`Cell.bg` = the hex colour sampled from ``colorscale`` at that
          normalized value (consumed by the colour serializers).

        ``colorscale`` is a Plotly colorscale — a list of ``[stop, "#hex"]``
        pairs (stops in ``0..1``) or a named scale string; ``None`` defaults to
        Viridis (:data:`DEFAULT_COLORSCALE`). Unlike the other primitives this
        one draws in *cell space* (it needs no :meth:`set_ranges`): ``z`` is
        resampled to the plot-region cell grid directly.

        The heatmap / histogram2d adapters depend on this signature. The internal
        ``z``->cell resampling is an implementation detail that may be refined
        (e.g. averaging instead of nearest) without changing this API.
        """
        rows = [list(r) for r in (z or []) if r is not None]
        rows = [r for r in rows if len(r) > 0]
        if not rows:
            return
        scale = _resolve_colorscale(colorscale)

        # Only *finite* numbers set the normalization range and paint a cell:
        # NaN / +-inf (and bools) are skipped so they never poison zmin/zmax or
        # flow into Cell.fill (which would crash round() in the shade serializer).
        flat = [float(v) for r in rows for v in r if _is_finite_number(v)]
        if not flat:
            return
        zmin, zmax = min(flat), max(flat)
        span = zmax - zmin

        nrows = len(rows)
        region_h = self._py1 - self._py0 + 1
        region_w = self._px1 - self._px0 + 1
        for ry in range(region_h):
            zr = min(nrows - 1, int(ry * nrows / region_h))
            row = rows[zr]
            ncols = len(row)
            cy = self._py0 + ry
            for rx in range(region_w):
                zc = min(ncols - 1, int(rx * ncols / region_w))
                val = row[zc]
                if not _is_finite_number(val):
                    continue  # non-finite sample -> leave the cell EMPTY (blank)
                t = 0.5 if span == 0 else (float(val) - zmin) / span
                cx = self._px0 + rx
                if not (0 <= cx < self._width and 0 <= cy < self._height):
                    continue
                cell = self._grid.rows[cy][cx]
                cell.role = CellRole.HEATMAP
                cell.fill = t
                cell.bg = _sample_colorscale(t, scale)

    def frame(
        self,
        x_range: Range,
        y_range: Range,
        *,
        x_ticks: Optional[Sequence[Tick]] = None,
        y_ticks: Optional[Sequence[Tick]] = None,
        title: Optional[str] = None,
        x_title: Optional[str] = None,
        y_title: Optional[str] = None,
    ) -> None:
        """Draw the axis frame and fix the data ranges in one call.

        Reserves the margin cells for axes/labels, draws the box, tick marks and
        tick labels (``CellRole.FRAME`` / ``CellRole.LABEL``), places the
        ``title`` / axis titles, and calls :meth:`set_ranges` so subsequent
        primitives map into the plot region. Ticks are supplied by the trace
        adapters so the Canvas stays Plotly-agnostic; if omitted the Canvas
        derives simple min/max ticks from the ranges.
        """
        from plotly.io._text.rasterizer import (
            BOX_CORNER_BL,
            BOX_H,
            BOX_TICK_X,
            BOX_TICK_Y,
            BOX_V,
        )

        # Derive default min/max ticks when the adapter supplies none.
        if x_ticks is None:
            x_ticks = [
                Tick(x_range[0], _fmt_num(x_range[0])),
                Tick(x_range[1], _fmt_num(x_range[1])),
            ]
        if y_ticks is None:
            y_ticks = [
                Tick(y_range[0], _fmt_num(y_range[0])),
                Tick(y_range[1], _fmt_num(y_range[1])),
            ]

        # --- compute margins -------------------------------------------------
        top_margin = 1 if title else 0
        bottom_margin = 1 + 1 + (1 if x_title else 0)  # border, x labels, x title
        ylabel_w = max((len(t.label) for t in y_ticks), default=0)
        ytitle_col = 1 if y_title else 0
        left_margin = ytitle_col + ylabel_w + 1  # y title, y labels, border
        right_margin = 1  # room for the right-most x tick label to spill

        # --- fix the plot region + ranges -----------------------------------
        self._px0 = left_margin
        self._py0 = top_margin
        self._px1 = self._width - 1 - right_margin
        self._py1 = self._height - 1 - bottom_margin
        if self._px1 < self._px0 or self._py1 < self._py0:
            # Need at least a 1x1 plot area inside the reserved margins.
            req_w = left_margin + right_margin + 1
            req_h = top_margin + bottom_margin + 1
            usable_w = self._px1 - self._px0 + 1
            usable_h = self._py1 - self._py0 + 1
            raise ValueError(
                f"Canvas too small for the requested frame: canvas is "
                f"{self._width}x{self._height} cells but the frame needs at "
                f"least {req_w}x{req_h} (margins consume "
                f"{left_margin + right_margin} cols x "
                f"{top_margin + bottom_margin} rows for axis/labels/title, "
                f"leaving a {usable_w}x{usable_h} plot area). "
                f"Increase width/height or drop titles/tick labels."
            )
        self.set_ranges(x_range, y_range)

        border_col = self._px0 - 1
        border_row = self._py1 + 1

        # --- box: left vertical + bottom horizontal + origin corner ---------
        for cy in range(self._py0, self._py1 + 1):
            self._set_frame(border_col, cy, BOX_V)
        for cx in range(border_col, self._px1 + 1):
            self._set_frame(cx, border_row, BOX_H)
        self._set_frame(border_col, border_row, BOX_CORNER_BL)

        # --- y ticks: mark + right-aligned label ----------------------------
        for t in y_ticks:
            cy = self._value_to_cell_row(t.value)
            if self._py0 <= cy <= self._py1:
                self._set_frame(border_col, cy, BOX_TICK_Y)
                start = border_col - len(t.label)
                self._place_text(max(ytitle_col, start), cy, t.label)

        # --- x ticks: mark + centered label ---------------------------------
        for t in x_ticks:
            cx = self._value_to_cell_col(t.value)
            if self._px0 <= cx <= self._px1:
                self._set_frame(cx, border_row, BOX_TICK_X)
                start = cx - len(t.label) // 2
                start = max(0, min(start, self._width - len(t.label)))
                self._place_text(start, border_row + 1, t.label)

        # --- titles ----------------------------------------------------------
        if title:
            start = max(0, (self._width - len(title)) // 2)
            self._place_text(start, 0, title)
        if x_title:
            xt_row = border_row + 2
            span0, span1 = self._px0, self._px1
            start = span0 + max(0, (span1 - span0 + 1 - len(x_title)) // 2)
            self._place_text(start, xt_row, x_title)
        if y_title:
            ph = self._py1 - self._py0 + 1
            start_row = self._py0 + max(0, (ph - len(y_title)) // 2)
            for i, ch in enumerate(y_title):
                cy = start_row + i
                if self._py0 <= cy <= self._py1:
                    cell = self._grid.rows[cy][0]
                    cell.role = CellRole.LABEL
                    cell.char = ch

    def _set_frame(self, cx: int, cy: int, char: str) -> None:
        if 0 <= cx < self._width and 0 <= cy < self._height:
            cell = self._grid.rows[cy][cx]
            cell.role = CellRole.FRAME
            cell.char = char

    def _value_to_cell_row(self, y: float) -> int:
        _, y_range = self._require_ranges()
        _, sh = self._sub_dims()
        fy = self._frac(y, y_range[0], y_range[1])
        srow = self._py0 * SUBCELL_ROWS + round((1.0 - fy) * (sh - 1))
        return srow // SUBCELL_ROWS

    def _value_to_cell_col(self, x: float) -> int:
        x_range, _ = self._require_ranges()
        sw, _ = self._sub_dims()
        fx = self._frac(x, x_range[0], x_range[1])
        scol = self._px0 * SUBCELL_COLS + round(fx * (sw - 1))
        return scol // SUBCELL_COLS

    # -- output -------------------------------------------------------------

    def render(self, mode: str = "text-utf") -> str:
        """Serialize the accumulated grid to a string for ``mode``.

        Looks up ``mode`` (a ``text-*`` renderer string) in the serializer
        registry (:data:`plotly.io._text.serializers.SERIALIZERS`) and returns
        ``serializer.serialize(self.grid)``. This is the only place the abstract
        grid becomes a concrete encoding.
        """
        from plotly.io._text.serializers import get_serializer

        return get_serializer(mode).serialize(self._grid)


def _fmt_num(value: float) -> str:
    """Format a tick value compactly and deterministically (``%g``-style)."""
    if value == int(value):
        return str(int(value))
    return f"{value:g}"


# ---------------------------------------------------------------------------
# Colorscale sampling (v2, for heatmap). A colorscale is a list of
# ``[stop, "#hex"]`` pairs with stops ascending over ``0..1``. Named scales are
# resolved to such a list. The default is Viridis, coarse-sampled — enough to
# tint a heatmap; this could later defer to plotly's full colorscale resolver
# without changing :meth:`Canvas.heatmap`'s signature.
# ---------------------------------------------------------------------------

#: A perceptual default colorscale (Viridis), coarse-sampled as ``[stop, hex]``.
DEFAULT_COLORSCALE = [
    [0.0, "#440154"],
    [0.25, "#3b528b"],
    [0.5, "#21918c"],
    [0.75, "#5ec962"],
    [1.0, "#fde725"],
]

#: Minimal named-scale table. This can be extended (or deferred to plotly's
#: colorscale machinery); unknown names fall back to
#: :data:`DEFAULT_COLORSCALE`.
_NAMED_COLORSCALES = {
    "viridis": DEFAULT_COLORSCALE,
    "greys": [[0.0, "#000000"], [1.0, "#ffffff"]],
    "gray": [[0.0, "#000000"], [1.0, "#ffffff"]],
}


def _resolve_colorscale(colorscale: Optional[object]) -> List[list]:
    """Normalize a colorscale argument to a ``[[stop, hex], ...]`` list.

    Accepts ``None`` (-> :data:`DEFAULT_COLORSCALE`), a named-scale string, or a
    list of ``[stop, "#hex"]`` pairs (passed through). Resolving the full plotly
    named-scale catalog is left as a future extension.
    """
    if colorscale is None:
        return DEFAULT_COLORSCALE
    if isinstance(colorscale, str):
        return _NAMED_COLORSCALES.get(colorscale.lower(), DEFAULT_COLORSCALE)
    try:
        pairs = [
            [float(stop), str(hexc)] for stop, hexc in cast("Iterable[Any]", colorscale)
        ]
    except (TypeError, ValueError):
        return DEFAULT_COLORSCALE
    return pairs or DEFAULT_COLORSCALE


def _is_finite_number(v: object) -> bool:
    """True for a real, finite numeric value (excludes bool, NaN, +-inf)."""
    return (
        isinstance(v, (int, float))
        and not isinstance(v, bool)
        and math.isfinite(float(v))
    )


def _sample_colorscale(t: float, scale: List[list]) -> str:
    """Return the hex colour for normalized position ``t`` (``0..1``) on ``scale``.

    Linearly interpolates in RGB between the two bounding stops. Deterministic and
    dependency-free (no numpy / plotly colour utilities). Colour strings are
    parsed tolerantly (``#hex`` *and* ``rgb()/rgba()``); an unparseable stop
    colour degrades to :data:`~plotly.io._text.rasterizer.NEUTRAL_COLOR` rather
    than raising, so the Canvas surface never crashes a direct caller.
    """
    if t <= scale[0][0]:
        return norm_hex(scale[0][1]) or NEUTRAL_COLOR
    if t >= scale[-1][0]:
        return norm_hex(scale[-1][1]) or NEUTRAL_COLOR
    for (s0, c0), (s1, c1) in zip(scale, scale[1:]):
        if s0 <= t <= s1:
            frac = 0.0 if s1 == s0 else (t - s0) / (s1 - s0)
            r0, g0, b0 = color_to_rgb(c0) or NEUTRAL_RGB
            r1, g1, b1 = color_to_rgb(c1) or NEUTRAL_RGB
            r = round(r0 + (r1 - r0) * frac)
            g = round(g0 + (g1 - g0) * frac)
            b = round(b0 + (b1 - b0) * frac)
            return f"#{r:02x}{g:02x}{b:02x}"
    return norm_hex(scale[-1][1]) or NEUTRAL_COLOR
