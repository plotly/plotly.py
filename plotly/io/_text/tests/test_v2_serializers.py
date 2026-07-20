"""Behaviour tests for the colour serializers + heatmap visibility.

Covers the two colour modes (``text-ansi`` 24-bit truecolor, ``text-html``
class-based fragment) and the ``HEATMAP`` role rendered by the monochrome
modes. The Canvas is deterministic and never queries a TTY, so these assert on
exact escape/markup structure and on byte-identical repeats.
"""

import re

from plotly.io._text.canvas import Canvas, Cell, CellGrid, CellRole
from plotly.io._text.rasterizer import SHADE_ASCII, SHADE_RAMP


# ---------------------------------------------------------------------------
# Helpers — build small grids directly so a test controls exactly one cell.
# ---------------------------------------------------------------------------


def _grid(cells_by_row):
    """Build a CellGrid from a list of rows of Cell."""
    h = len(cells_by_row)
    w = max(len(r) for r in cells_by_row)
    g = CellGrid.blank(w, h)
    for y, row in enumerate(cells_by_row):
        for x, cell in enumerate(row):
            g.rows[y][x] = cell
    return g


def _serialize(grid, mode):
    from plotly.io._text.serializers import get_serializer

    return get_serializer(mode).serialize(grid)


# ---------------------------------------------------------------------------
# text-ansi — truecolor escapes, present, reset, run-length-batched.
# ---------------------------------------------------------------------------


def _colored_line_canvas():
    c = Canvas(width=30, height=10)
    c.frame(x_range=(0, 6.2), y_range=(-1, 1), title="c")
    c.line([(x * 0.2, (x * 0.2)) for x in range(0, 31)], color="#636efa")
    return c


def test_ansi_emits_truecolor_fg_escape():
    out = _serialize(
        _grid([[Cell(role=CellRole.DOTS, dots=0x01, fg="#636efa")]]), "text-ansi"
    )
    # #636efa -> (99, 110, 250)
    assert "\x1b[38;2;99;110;250m" in out
    assert out.endswith("\x1b[0m")


def test_ansi_resets_at_end_of_each_line():
    grid = _grid(
        [
            [Cell(role=CellRole.DOTS, dots=0x01, fg="#636efa")],
            [Cell(role=CellRole.DOTS, dots=0x01, fg="#EF553B")],
        ]
    )
    out = _serialize(grid, "text-ansi")
    for line in out.split("\n"):
        # Any line that opened a colour must close it.
        if "\x1b[38" in line or "\x1b[48" in line:
            assert line.endswith("\x1b[0m")


def test_ansi_run_length_batches_same_color():
    # Five adjacent same-colour cells -> one fg escape, not five.
    row = [Cell(role=CellRole.DOTS, dots=0x01, fg="#636efa") for _ in range(5)]
    out = _serialize(_grid([row]), "text-ansi")
    assert out.count("\x1b[38;2;99;110;250m") == 1
    # The five glyphs ride under that single escape.
    assert out.count("⠁") == 5


def test_ansi_uncolored_cells_emit_no_escape():
    row = [Cell(role=CellRole.DOTS, dots=0x01)]  # no fg
    out = _serialize(_grid([row]), "text-ansi")
    assert "\x1b" not in out


def test_ansi_transition_resets_before_uncolored_run():
    # colored, uncolored(blank interior), colored -> stale bg must not bleed.
    row = [
        Cell(role=CellRole.HEATMAP, fill=1.0, bg="#440154"),
        Cell(role=CellRole.DOTS, dots=0x01),  # uncolored interior
        Cell(role=CellRole.HEATMAP, fill=1.0, bg="#fde725"),
    ]
    out = _serialize(_grid([row]), "text-ansi")
    # The middle glyph must be preceded by a reset so it isn't painted with the
    # first cell's background.
    braille = "⠁"
    idx = out.index(braille)
    assert "\x1b[0m" in out[:idx]


def test_ansi_real_figure_line_has_color():
    out = _colored_line_canvas().render("text-ansi")
    assert "\x1b[38;2;99;110;250m" in out
    assert "\x1b[0m" in out


# ---------------------------------------------------------------------------
# text-html — class-based fragment, de-duplicated classes, batched spans.
# ---------------------------------------------------------------------------


def test_html_is_style_plus_pre_fragment():
    out = _serialize(
        _grid([[Cell(role=CellRole.DOTS, dots=0x01, fg="#636efa")]]), "text-html"
    )
    assert out.startswith("<style>")
    assert '<pre class="plotly-text">' in out
    assert out.endswith("</pre>")
    # not a full document
    assert "<html" not in out.lower()


def test_html_deduplicates_colors_into_classes():
    # Same colour used in three cells -> exactly one class rule.
    row = [Cell(role=CellRole.DOTS, dots=0x01, fg="#636efa") for _ in range(3)]
    out = _serialize(_grid([row]), "text-html")
    assert out.count(".plotly-text .c0{color:#636efa}") == 1
    # Three same-colour cells batch into a single span, not three.
    assert out.count("<span") == 1


def test_html_class_ordering_is_by_first_appearance():
    row = [
        Cell(role=CellRole.DOTS, dots=0x01, fg="#636efa"),
        Cell(role=CellRole.DOTS, dots=0x01, fg="#EF553B"),
    ]
    out = _serialize(_grid([row]), "text-html")
    # first-seen colour -> c0, second -> c1
    assert ".plotly-text .c0{color:#636efa}" in out
    assert ".plotly-text .c1{color:#ef553b}" in out  # normalized lowercase
    assert out.index("c0") < out.index("c1")


def test_html_heatmap_uses_bg_classes():
    row = [Cell(role=CellRole.HEATMAP, fill=1.0, bg="#fde725")]
    out = _serialize(_grid([row]), "text-html")
    assert ".plotly-text .b0{background-color:#fde725}" in out
    assert 'class="b0"' in out


def test_html_escapes_special_label_chars():
    out = _serialize(
        _grid([[Cell(role=CellRole.LABEL, char="<", fg="#636efa")]]), "text-html"
    )
    assert "&lt;" in out
    assert "<span" in out  # the real span tag is still there


# ---------------------------------------------------------------------------
# HEATMAP visibility across modes (the barrier coordination point).
# ---------------------------------------------------------------------------


def _heatmap_canvas():
    c = Canvas(width=8, height=6)
    # a smooth gradient so several shade levels appear
    z = [[0, 1, 2, 3], [1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
    c.heatmap(z)
    return c


def test_heatmap_shows_shade_ramp_in_text_utf():
    out = _heatmap_canvas().render("text-utf")
    # at least the full block (max density) and a mid shade appear
    assert "█" in out  # full block for the maximum
    assert any(ch in out for ch in ("░", "▒", "▓"))  # a mid shade


def test_heatmap_min_cell_is_visible_not_blank_in_utf():
    # A uniform-min region must still be visible (floor at the lightest shade).
    c = Canvas(width=4, height=3)
    c.heatmap([[0, 0], [0, 0]])
    out = c.render("text-utf")
    # every region cell is a visible shade, none blank (space)
    assert " " not in out
    assert any(s in out for s in SHADE_RAMP[1:])


def test_heatmap_shows_ramp_in_text_ascii():
    out = _heatmap_canvas().render("text-ascii")
    assert out.isascii()
    assert "#" in out  # full-density ascii shade
    assert any(ch in out for ch in SHADE_ASCII[1:])


def test_heatmap_has_colored_bg_in_ansi():
    out = _heatmap_canvas().render("text-ansi")
    assert "\x1b[48;2;" in out  # a background truecolor escape
    assert "\x1b[0m" in out


def test_heatmap_has_bg_class_in_html():
    out = _heatmap_canvas().render("text-html")
    assert "background-color:#" in out
    assert re.search(r'class="b\d+"', out)


# ---------------------------------------------------------------------------
# Determinism — byte-identical on repeat, for every v2 mode + heatmap.
# ---------------------------------------------------------------------------


def test_ansi_is_deterministic():
    a = _colored_line_canvas().render("text-ansi")
    b = _colored_line_canvas().render("text-ansi")
    assert a == b


def test_html_is_deterministic():
    a = _colored_line_canvas().render("text-html")
    b = _colored_line_canvas().render("text-html")
    assert a == b


def test_heatmap_is_deterministic_across_modes():
    for mode in ("text-utf", "text-ascii", "text-ansi", "text-html"):
        assert _heatmap_canvas().render(mode) == _heatmap_canvas().render(mode)


# ---------------------------------------------------------------------------
# Fix wave — robustness. Non-finite z, non-hex Cell colours, rgb() colorscale.
# ---------------------------------------------------------------------------


def test_nan_in_heatmap_z_renders_without_crashing_in_every_mode():
    # A1: NaN must not crash any mode (was ValueError: cannot convert NaN).
    c = Canvas(width=6, height=4)
    c.heatmap([[1, 2, float("nan")], [4, 5, 6]])
    for mode in ("text-utf", "text-ascii", "text-ansi", "text-html"):
        out = c.render(mode)  # no exception
        assert isinstance(out, str)


def test_infinite_in_heatmap_z_is_skipped():
    # +-inf treated like NaN: excluded from range, cell left blank.
    c = Canvas(width=6, height=4)
    c.heatmap([[1, 2, float("inf")], [4, 5, float("-inf")]])
    out = c.render("text-utf")  # no crash, finite range from {1,2,4,5}
    assert isinstance(out, str)


def test_non_finite_cell_fill_degrades_to_blank_not_crash():
    # A1 belt: a HEATMAP cell that somehow carries a NaN fill -> blank, no raise.
    grid = _grid([[Cell(role=CellRole.HEATMAP, fill=float("nan"))]])
    for mode in ("text-utf", "text-ascii", "text-ansi", "text-html"):
        out = _serialize(grid, mode)
        assert isinstance(out, str)


def test_non_hex_fg_serializes_uncolored_in_ansi():
    # A3: an unparseable fg must render plain, never raise.
    grid = _grid([[Cell(role=CellRole.DOTS, dots=0x01, fg="notacolor")]])
    out = _serialize(grid, "text-ansi")
    assert "\x1b" not in out  # no escape emitted for the bad colour


def test_non_hex_fg_serializes_uncolored_in_html():
    grid = _grid([[Cell(role=CellRole.DOTS, dots=0x01, fg="notacolor")]])
    out = _serialize(grid, "text-html")
    assert "<span" not in out  # no coloured span for the bad colour
    assert ".plotly-text .c0" not in out  # no class rule either


def test_named_css_color_degrades_cleanly():
    # A CSS name (adapter's job to resolve) must not crash the serializer.
    grid = _grid([[Cell(role=CellRole.MARKER, char="o", fg="red")]])
    assert isinstance(_serialize(grid, "text-ansi"), str)
    assert isinstance(_serialize(grid, "text-html"), str)


def test_canvas_colorscale_accepts_rgb_pairs():
    # A2: a Canvas colorscale given rgb()/rgba() stops must render (not crash).
    c = Canvas(width=6, height=4)
    c.heatmap(
        [[1, 2], [3, 4]],
        colorscale=[[0.0, "rgb(68,1,84)"], [1.0, "rgba(253,231,37,0.5)"]],
    )
    out_utf = c.render("text-utf")
    assert isinstance(out_utf, str)
    out_ansi = c.render("text-ansi")
    assert "\x1b[48;2;" in out_ansi  # bg colour sampled from the rgb() scale
    out_html = c.render("text-html")
    assert "background-color:#" in out_html  # sampled colours normalized to hex


def test_ansi_fg_color_matches_hex_and_rgb_forms():
    # #636efa and rgb(99,110,250) are the same colour -> same escape.
    hex_out = _serialize(
        _grid([[Cell(role=CellRole.DOTS, dots=0x01, fg="#636efa")]]), "text-ansi"
    )
    rgb_out = _serialize(
        _grid([[Cell(role=CellRole.DOTS, dots=0x01, fg="rgb(99,110,250)")]]),
        "text-ansi",
    )
    assert "\x1b[38;2;99;110;250m" in hex_out
    assert "\x1b[38;2;99;110;250m" in rgb_out


def test_shared_color_helpers_live_in_rasterizer():
    # A4: canonical helpers imported by both canvas and serializers.
    from plotly.io._text import rasterizer

    assert rasterizer.color_to_rgb("#636efa") == (99, 110, 250)
    assert rasterizer.color_to_rgb("rgb(1,2,3)") == (1, 2, 3)
    assert rasterizer.color_to_rgb("bogus") is None
    assert rasterizer.norm_hex("#636EFA") == "#636efa"
    assert rasterizer.norm_hex("bogus") is None
