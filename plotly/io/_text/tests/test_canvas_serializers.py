"""Golden-output snapshot tests for the Canvas + monochrome serializers.

The Canvas is deterministic and never queries a TTY, so byte-exact snapshots are
a valid contract: any drift in the rasterizer, frame layout, or a serializer's
glyph mapping shows up as a diff here. The adapter/renderer tests live beside
this file in ``test_adapters_renderers.py``.
"""

import math

from plotly.io._text.canvas import Canvas, Tick
from plotly.io._text.rasterizer import MARKER_ASCII, MARKER_GLYPHS


# ---------------------------------------------------------------------------
# sin(x) framed line — the exit-criterion picture, in both v1 modes.
# ---------------------------------------------------------------------------


def _sin_canvas():
    c = Canvas(width=60, height=16)
    pts = [(x * 0.1, math.sin(x * 0.1)) for x in range(0, 63)]
    c.frame(
        x_range=(0, 6.2),
        y_range=(-1, 1),
        x_ticks=[Tick(0, "0"), Tick(3.14, "pi"), Tick(6.28, "2pi")],
        y_ticks=[Tick(-1, "-1"), Tick(0, "0"), Tick(1, "1")],
        title="sin(x)",
    )
    c.line(pts)
    return c


SIN_UTF = (
    "                           sin(x)\n"
    " 1┤         ⢀⡠⠒⠉⠉⠉⠑⠒⠢⢄⡀\n"
    "  │       ⡠⠔⠁         ⠘⠤⡀\n"
    "  │     ⢀⠔⠁             ⠈⠢⡀\n"
    "  │    ⡔⠁                 ⠘⡄\n"
    "  │  ⢠⠊                    ⠈⠢⡀\n"
    "  │ ⡰⠁                       ⠘⢄\n"
    " 0┤⠜                           ⢣\n"
    "  │                             ⠣⡀                       ⡠⠊\n"
    "  │                              ⠈⢢                     ⡰⠁\n"
    "  │                                ⠣⡀                 ⢠⠊\n"
    "  │                                 ⠈⠢⡀             ⡠⠔⠁\n"
    "  │                                   ⠈⠢⡀         ⣀⠔⠁\n"
    "-1┤                                     ⠈⠒⠤⠤⣀⣀⣀⡠⠔⠉\n"
    "  └┬───────────────────────────┬──────────────────────────┬\n"
    "   0                          pi                         2pi"
)

SIN_ASCII = (
    "                           sin(x)\n"
    " 1+         ...........\n"
    "  |       ...         ...\n"
    "  |     ...             ...\n"
    "  |    :.                 ..\n"
    "  |  ..                    ...\n"
    "  | :.                       ..\n"
    " 0+:                           :\n"
    "  |                             :.                       ..\n"
    "  |                              .:                     :.\n"
    "  |                                :.                 ..\n"
    "  |                                 ...             ...\n"
    "  |                                   ...         ...\n"
    "-1+                                     ..........\n"
    "  ++---------------------------+--------------------------+\n"
    "   0                          pi                         2pi"
)


def test_sin_text_utf_golden():
    assert _sin_canvas().render("text-utf") == SIN_UTF


def test_sin_text_ascii_golden():
    assert _sin_canvas().render("text-ascii") == SIN_ASCII


def test_render_is_deterministic():
    a = _sin_canvas().render("text-utf")
    b = _sin_canvas().render("text-utf")
    assert a == b
    assert _sin_canvas().render("text-ascii") == _sin_canvas().render("text-ascii")


def test_text_ascii_is_pure_7bit():
    out = _sin_canvas().render("text-ascii")
    assert out.isascii()


# ---------------------------------------------------------------------------
# Bars with fractional fill (block ramp caps the partial top cell).
# ---------------------------------------------------------------------------


def _bar_canvas():
    c = Canvas(width=30, height=10)
    c.frame(
        x_range=(-0.5, 2.5),
        y_range=(0, 10),
        x_ticks=[Tick(0, "a"), Tick(1, "b"), Tick(2, "c")],
        y_ticks=[Tick(0, "0"), Tick(10, "10")],
        title="bars",
    )
    c.bar([0, 1, 2], [2.5, 7.3, 9.9])
    return c


BAR_UTF = (
    "             bars\n"
    "10┤                     ▇\n"
    "  │             ▁       █\n"
    "  │             █       █\n"
    "  │             █       █\n"
    "  │             █       █\n"
    "  │    ▆        █       █\n"
    " 0┤    █        █       █\n"
    "  └────┬────────┬───────┬────\n"
    "       a        b       c"
)


def test_bar_fractional_fill_golden():
    assert _bar_canvas().render("text-utf") == BAR_UTF


# ---------------------------------------------------------------------------
# A1 fix: bar collision must max-merge, never shrink (honesty rule).
# ---------------------------------------------------------------------------


def test_bar_collision_keeps_tallest_regardless_of_order():
    big_first = Canvas(10, 8)
    big_first.frame(x_range=(0, 10), y_range=(0, 100))
    big_first.bar([5.0, 5.05], [100, 1])

    small_first = Canvas(10, 8)
    small_first.frame(x_range=(0, 10), y_range=(0, 100))
    small_first.bar([5.05, 5.0], [1, 100])

    # Draw order must not change the picture; the tall bar always survives.
    assert big_first.render("text-utf") == small_first.render("text-utf")
    # And the surviving bar is the tall one (reaches the top rows).
    out = big_first.render("text-utf")
    assert "█" in out.splitlines()[1]


# ---------------------------------------------------------------------------
# A2 fix: multi-series ascii markers stay distinct (no collapse to '*').
# ---------------------------------------------------------------------------


def test_ascii_markers_are_distinct_per_series():
    c = Canvas(width=24, height=8)
    c.frame(
        x_range=(0, 4),
        y_range=(0, 4),
        x_ticks=[Tick(0, "0"), Tick(4, "4")],
        y_ticks=[Tick(0, "0"), Tick(4, "4")],
    )
    c.markers([(1, 1)], MARKER_GLYPHS[0])
    c.markers([(2, 2)], MARKER_GLYPHS[1])
    c.markers([(3, 3)], MARKER_GLYPHS[2])
    out = c.render("text-ascii")

    expected = [MARKER_ASCII[g] for g in MARKER_GLYPHS[:3]]
    assert len(set(expected)) == 3  # palette is genuinely distinct
    for ch in expected:
        assert ch in out
    assert "*" not in out  # nothing collapsed to the unknown-glyph fallback


def test_marker_palette_tables_are_index_aligned():
    from plotly.io._text.rasterizer import MARKER_GLYPHS_ASCII

    assert len(MARKER_GLYPHS) == len(MARKER_GLYPHS_ASCII)
    assert len(set(MARKER_GLYPHS_ASCII)) == len(MARKER_GLYPHS_ASCII)


# ---------------------------------------------------------------------------
# A3 fix: undersized canvas raises an actionable ValueError.
# ---------------------------------------------------------------------------


def test_undersized_frame_raises_actionable_error():
    import pytest

    c = Canvas(width=4, height=3)
    with pytest.raises(ValueError) as exc:
        c.frame(
            x_range=(0, 1),
            y_range=(0, 1),
            title="too big",
            x_title="x",
            y_title="y",
        )
    msg = str(exc.value)
    assert "too small" in msg
    assert "4x3" in msg  # states the actual canvas size
