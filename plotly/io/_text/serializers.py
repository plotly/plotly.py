"""Grid -> string serializers, one per output mode.

A **serializer** is the second half of the "one grid, many serializers"
architecture: a total function from a finished
:class:`~plotly.io._text.canvas.CellGrid` to a string, for exactly one ``text-*``
mode. It is the seam the design rests on — the serializers own grid -> text, and
the renderers select one by renderer string.

The four modes (monochrome ``text-utf``, ``text-ascii``; colour ``text-ansi``,
``text-html``) differ only in **glyph set x colorizer** over the *same* grid, so
adding a mode is adding a serializer here, never re-rasterizing.

The :class:`Serializer` interface and the :data:`SERIALIZERS` registry shape are
the stable extension points: each serializer implements ``serialize`` and
registers itself.
"""

from __future__ import annotations

import math
from typing import Dict

from plotly.io._text.canvas import Cell, CellGrid, CellRole
from plotly.io._text.rasterizer import (
    ASCII_BAR_RAMP,
    ASCII_DENSITY,
    BLOCK_RAMP_H,
    BLOCK_RAMP_V,
    FRAME_ASCII,
    MARKER_ASCII,
    SHADE_ASCII,
    SHADE_RAMP,
    braille_char,
    color_to_rgb,
    norm_hex,
    popcount,
)


class Serializer:
    """Turn a finished :class:`CellGrid` into a string for one output mode.

    Subclasses set :attr:`name` (the ``plotly.io`` renderer string, e.g.
    ``"text-utf"``) and implement :meth:`serialize`. A serializer must be
    deterministic and must not query a TTY: the same grid always yields the same
    bytes. The v1 serializers emit monochrome plain text and force UTF-8 where
    they use non-ASCII glyphs.
    """

    #: The ``plotly.io`` renderer string this serializer answers to.
    name: str = ""

    #: Whether output contains non-ASCII (UTF-8) glyphs. ``text-utf`` sets True
    #: so the renderer knows to force a UTF-8 write; ``text-ascii`` sets False.
    unicode: bool = True

    def serialize(self, grid: CellGrid) -> str:
        """Return the string encoding of ``grid`` for this mode.

        Reads each :class:`~plotly.io._text.canvas.Cell` by its
        :class:`~plotly.io._text.canvas.CellRole` and emits the mode-appropriate
        glyph (braille codepoint, block ramp char, ascii fallback, ...), joining
        rows with ``"\\n"``.
        """
        raise NotImplementedError


#: Registry of serializers keyed by ``text-*`` renderer string (one entry per
#: implemented mode); read by
#: :meth:`plotly.io._text.canvas.Canvas.render` and by the renderer classes.
SERIALIZERS: Dict[str, Serializer] = {}


def register_serializer(serializer: Serializer) -> None:
    """Register ``serializer`` under its :attr:`~Serializer.name`."""
    SERIALIZERS[serializer.name] = serializer


def get_serializer(mode: str) -> Serializer:
    """Return the serializer for ``mode`` or raise ``KeyError`` if unknown."""
    return SERIALIZERS[mode]


# ---------------------------------------------------------------------------
# v1 serializers — monochrome plain text. text-utf is the default (Unicode
# braille + block); text-ascii is the guaranteed-portable 7-bit floor.
# ---------------------------------------------------------------------------


def _bar_index(fill: float, steps: int) -> int:
    """Quantise a 0..1 fill fraction to ``0..steps`` (never 0 for fill > 0)."""
    idx = round(fill * steps)
    if idx <= 0 and fill > 0.0:
        idx = 1
    if idx > steps:
        idx = steps
    return idx


def _shade_index(fill: float, steps: int) -> int:
    """Quantise a 0..1 heatmap density to ``1..steps`` on a shade ramp.

    A ``HEATMAP`` cell is always a *sample* (every region cell carries data), so
    the floor is index 1 (the lightest shade) rather than 0 (blank): even the
    minimum-density cell stays visible, which is what makes a heatmap legible in
    the monochrome modes. The maximum maps to ``steps`` (full block).

    Defensive: a non-finite ``fill`` (NaN / inf that slipped past the Canvas)
    degrades to index 0 (blank) instead of crashing ``round(nan)``.
    """
    if not math.isfinite(fill):
        return 0
    idx = round(fill * steps)
    if idx < 1:
        idx = 1
    if idx > steps:
        idx = steps
    return idx


def _utf_glyph(cell: Cell) -> str:
    """Return the Unicode glyph for ``cell`` (shared by utf / ansi / html).

    The three Unicode modes draw the *same* glyph grid and differ only in the
    colorizer, so the braille / block / shade / frame / marker mapping lives here
    once. Colour attributes (:attr:`Cell.fg` / :attr:`Cell.bg`) are not consulted.
    """
    role = cell.role
    if role == CellRole.EMPTY:
        return " "
    if role == CellRole.DOTS:
        return braille_char(cell.dots)
    if role == CellRole.BAR:
        ramp = BLOCK_RAMP_H if cell.char == "h" else BLOCK_RAMP_V
        return ramp[_bar_index(cell.fill, 8)]
    if role == CellRole.HEATMAP:
        return SHADE_RAMP[_shade_index(cell.fill, len(SHADE_RAMP) - 1)]
    return cell.char or " "  # MARKER / FRAME / LABEL


def _ascii_glyph(cell: Cell) -> str:
    """Return the 7-bit ASCII glyph for ``cell`` (the ``text-ascii`` mapping)."""
    role = cell.role
    if role == CellRole.EMPTY:
        return " "
    if role == CellRole.DOTS:
        return ASCII_DENSITY[popcount(cell.dots)]
    if role == CellRole.BAR:
        return ASCII_BAR_RAMP[_bar_index(cell.fill, 4)]
    if role == CellRole.HEATMAP:
        return SHADE_ASCII[_shade_index(cell.fill, len(SHADE_ASCII) - 1)]
    if role == CellRole.FRAME:
        return FRAME_ASCII.get(cell.char, "+")
    if role == CellRole.MARKER:
        ch = cell.char
        ascii_ch = MARKER_ASCII.get(ch)
        if ascii_ch is not None:
            return ascii_ch
        if ch and ch.isascii():
            return ch
        return "*"
    # LABEL
    ch = cell.char
    return ch if ch and ch.isascii() else "?"


class TextUtfSerializer(Serializer):
    """Default mode: Unicode braille + block glyphs, monochrome plain text.

    Handles every :class:`CellRole`, including ``HEATMAP`` (the block-shade ramp
    :data:`~plotly.io._text.rasterizer.SHADE_RAMP` keyed by :attr:`Cell.fill`), so
    a heatmap is legible here even though this mode drops colour.
    """

    name = "text-utf"
    unicode = True

    def serialize(self, grid: CellGrid) -> str:
        lines = []
        for row in grid.rows:
            out = [_utf_glyph(cell) for cell in row]
            lines.append("".join(out).rstrip())
        return "\n".join(lines)


class TextAsciiSerializer(Serializer):
    """Portable floor: 7-bit ASCII only, monochrome.

    Degradation palette (open decision resolved here):

    * ``DOTS``   -> density ramp ``. : + #`` by braille sub-dot popcount
      (:data:`~plotly.io._text.rasterizer.ASCII_DENSITY`).
    * ``BAR``    -> fill ramp ``. : + #`` by fraction
      (:data:`~plotly.io._text.rasterizer.ASCII_BAR_RAMP`).
    * ``FRAME``  -> ``| - +`` box fallback
      (:data:`~plotly.io._text.rasterizer.FRAME_ASCII`).
    * ``MARKER`` -> the distinct 7-bit counterpart of the series glyph
      (:data:`~plotly.io._text.rasterizer.MARKER_ASCII`), so multi-series plots
      stay distinguishable; an already-ASCII glyph passes through, and a
      genuinely unknown non-ASCII glyph falls back to ``*``.
    * ``LABEL``  -> the character if ASCII, else ``?``.
    * ``HEATMAP``-> the 7-bit shade ramp
      (:data:`~plotly.io._text.rasterizer.SHADE_ASCII`) by :attr:`Cell.fill`.
    """

    name = "text-ascii"
    unicode = False

    def serialize(self, grid: CellGrid) -> str:
        lines = []
        for row in grid.rows:
            out = [_ascii_glyph(cell) for cell in row]
            lines.append("".join(out).rstrip())
        return "\n".join(lines)


register_serializer(TextUtfSerializer())
register_serializer(TextAsciiSerializer())


# ---------------------------------------------------------------------------
# Colour-mode serializers. Same glyph grid as ``text-utf``; they add a
# colorizer that reads ``Cell.fg`` / ``Cell.bg`` (set by the colour-aware Canvas
# calls and by ``Canvas.heatmap``).
# ---------------------------------------------------------------------------


#: ANSI SGR reset — clears every colour attribute back to the terminal default.
ANSI_RESET = "\x1b[0m"


def _ansi_prefix(fg, bg) -> str:
    """Build the truecolor SGR prefix for a ``(fg, bg)`` pair (absolute colours).

    Each escape sets an *absolute* 24-bit colour, so pairing it with a preceding
    :data:`ANSI_RESET` clears any stale attribute (e.g. a previous run's bg).
    Colours are parsed tolerantly; an unparseable ``fg``/``bg`` contributes no
    escape (that channel renders in the default colour) rather than raising.
    """
    parts = []
    fg_rgb = color_to_rgb(fg) if fg is not None else None
    if fg_rgb is not None:
        r, g, b = fg_rgb
        parts.append(f"\x1b[38;2;{r};{g};{b}m")
    bg_rgb = color_to_rgb(bg) if bg is not None else None
    if bg_rgb is not None:
        r, g, b = bg_rgb
        parts.append(f"\x1b[48;2;{r};{g};{b}m")
    return "".join(parts)


def _row_cells(row) -> list:
    """(glyph, fg, bg) per cell, with trailing uncoloured blanks trimmed.

    Trimming trailing blank+uncoloured cells keeps colour output as compact as
    the monochrome modes' ``rstrip``; a coloured trailing cell (e.g. a heatmap bg)
    is kept so its colour is not lost.
    """
    cells = [(_utf_glyph(c), c.fg, c.bg) for c in row]
    while cells and cells[-1] == (" ", None, None):
        cells.pop()
    return cells


def _runs(cells):
    """Yield ``(glyph_text, fg, bg)`` runs batching adjacent same-colour cells."""
    i = 0
    n = len(cells)
    while i < n:
        _, fg, bg = cells[i]
        j = i
        buf = []
        while j < n and cells[j][1] == fg and cells[j][2] == bg:
            buf.append(cells[j][0])
            j += 1
        yield "".join(buf), fg, bg
        i = j


class TextAnsiSerializer(Serializer):
    """Colour mode: ``text-utf`` glyphs + 24-bit ANSI truecolor escapes (v2).

    Reuses the ``text-utf`` glyph mapping (braille / block / shade ramps, box
    frame, markers) and wraps coloured runs in ``\\x1b[38;2;r;g;bm`` (foreground,
    from :attr:`Cell.fg`) and ``\\x1b[48;2;r;g;bm`` (background, from
    :attr:`Cell.bg`, e.g. heatmap cells). Adjacent same-colour cells are
    **run-length-batched** into one escape, and every line ends with a reset
    (``\\x1b[0m``) so colour never leaks across lines. A run that transitions to a
    different (or no) colour emits a reset first, so a stale background can't bleed
    onto later cells. Cells with no colour hint fall back to the default terminal
    colour (no escape). Never queries a TTY — the caller opts in by picking this
    renderer string.
    """

    name = "text-ansi"
    unicode = True

    def serialize(self, grid: CellGrid) -> str:
        lines = []
        for row in grid.rows:
            cells = _row_cells(row)
            parts = []
            active = False  # is a non-default colour currently in effect?
            for text, fg, bg in _runs(cells):
                prefix = _ansi_prefix(fg, bg)
                if prefix:  # an actual, parseable colour to apply
                    if active:
                        parts.append(ANSI_RESET)  # clear stale attrs first
                    parts.append(prefix)
                    parts.append(text)
                    active = True
                else:  # no colour (or unparseable) -> render plain
                    if active:
                        parts.append(ANSI_RESET)
                        active = False
                    parts.append(text)
            if active:
                parts.append(ANSI_RESET)
            lines.append("".join(parts))
        return "\n".join(lines)


def _html_escape(text: str) -> str:
    """Escape the HTML-significant characters in glyph text.

    Braille / block / shade glyphs are safe; only the rare ``&``, ``<``, ``>`` in
    a label need escaping.
    """
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


class TextHtmlSerializer(Serializer):
    """Colour mode: ``text-utf`` glyphs + class-based HTML fragment.

    Emits a self-contained fragment: a scoped
    ``<style>`` block of *de-duplicated* colour classes (``.plotly-text .c0`` per
    distinct :attr:`Cell.fg`, ``.plotly-text .b0`` per distinct :attr:`Cell.bg`)
    followed by a ``<pre class="plotly-text">`` whose ``<span class="…">`` runs
    carry the colour. Classes beat inline ``style=`` because they survive
    inline-style-stripping sanitizers and stay compact — each distinct colour is
    defined once, not repeated per span. Adjacent same-class cells are batched into
    a single span; class numbering is by first appearance (deterministic). Reuses
    the ``text-utf`` glyph mapping and HTML-escapes glyph text.
    """

    name = "text-html"
    unicode = True

    def serialize(self, grid: CellGrid) -> str:
        # First pass: assign class indices by first appearance (deterministic).
        fg_classes: Dict[str, int] = {}
        bg_classes: Dict[str, int] = {}
        grid_cells = [_row_cells(row) for row in grid.rows]
        for cells in grid_cells:
            for _, fg, bg in cells:
                fgh = norm_hex(fg) if fg is not None else None
                if fgh is not None and fgh not in fg_classes:
                    fg_classes[fgh] = len(fg_classes)
                bgh = norm_hex(bg) if bg is not None else None
                if bgh is not None and bgh not in bg_classes:
                    bg_classes[bgh] = len(bg_classes)

        style_rules = []
        for hexc, idx in fg_classes.items():
            style_rules.append(f".plotly-text .c{idx}{{color:{hexc}}}")
        for hexc, idx in bg_classes.items():
            style_rules.append(f".plotly-text .b{idx}{{background-color:{hexc}}}")
        style = "<style>\n" + "\n".join(style_rules)
        if style_rules:
            style += "\n"
        style += "</style>"

        # Second pass: batch runs into class-tagged spans.
        lines = []
        for cells in grid_cells:
            parts = []
            for text, fg, bg in _runs(cells):
                esc = _html_escape(text)
                classes = []
                fgh = norm_hex(fg) if fg is not None else None
                if fgh is not None:
                    classes.append(f"c{fg_classes[fgh]}")
                bgh = norm_hex(bg) if bg is not None else None
                if bgh is not None:
                    classes.append(f"b{bg_classes[bgh]}")
                if classes:
                    parts.append(f'<span class="{" ".join(classes)}">{esc}</span>')
                else:  # no colour, or an unparseable one -> plain (uncoloured)
                    parts.append(esc)
            lines.append("".join(parts))
        pre = '<pre class="plotly-text">' + "\n".join(lines) + "</pre>"
        return style + "\n" + pre


register_serializer(TextAnsiSerializer())
register_serializer(TextHtmlSerializer())
