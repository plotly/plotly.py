"""Colour-mode tests — colour through the trace adapters, the heatmap /
histogram2d adapter, colour-source precedence, and colour-mode renderer
registration.

These validate the **adapter surface independently of the serializer bodies**:
colour is asserted by inspecting the drawn grid cells' ``fg`` / ``bg`` (set by the
Canvas), and heatmaps by their ``HEATMAP`` cells. The end-to-end colour-mode
render tests (``text-ansi`` / ``text-html``) and the ``text-utf`` heatmap-shade
test depend on the serializers; each skips cleanly with ``NotImplementedError``
if a serializer is not yet available, so the adapter-level assertions stand on
their own.

Sibling to ``test_adapters_renderers.py`` in the same directory.
"""

import math

import pytest

import plotly.graph_objects as go
import plotly.io as pio
from plotly.io._text import adapters as A
from plotly.io._text.adapters import COLOR_PALETTE, figure_to_canvas
from plotly.io._text.adapters import heatmap as H
from plotly.io._text.canvas import Canvas, CellRole

np = pytest.importorskip("numpy")


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------


def _fg_set(canvas, role):
    """Distinct non-empty ``fg`` hints among cells of ``role`` in ``canvas``."""
    return {c.fg for row in canvas.grid.rows for c in row if c.role == role and c.fg}


def _heatmap_cells(canvas):
    return [c for row in canvas.grid.rows for c in row if c.role == CellRole.HEATMAP]


def _fill_matrix(canvas):
    """The ``fill`` of every plot cell, rounded — for list-vs-numpy equality."""
    return [
        [round(c.fill, 6) if c.role == CellRole.HEATMAP else None for c in row]
        for row in canvas.grid.rows
    ]


# ===========================================================================
# 1. Colour through the built-in adapters (scatter / bar / histogram).
# ===========================================================================


def test_scatter_forwards_palette_color_to_line_and_markers():
    fig = go.Figure(go.Scatter(x=[0, 1, 2, 3], y=[0, 1, 0, 1], mode="lines+markers"))
    r = figure_to_canvas(fig.to_dict(), width=40, height=14)
    # series 0 -> palette[0]; both the braille line cells and the marker cells
    # must carry it (before v2 the adapter forwarded no colour at all).
    assert _fg_set(r.canvas, CellRole.DOTS) == {COLOR_PALETTE[0]}
    assert _fg_set(r.canvas, CellRole.MARKER) == {COLOR_PALETTE[0]}


def test_scatter_explicit_marker_color_wins_over_palette():
    fig = go.Figure(
        go.Scatter(x=[0, 1, 2], y=[0, 1, 2], mode="markers", marker_color="#ff0000")
    )
    d = fig.to_dict()
    expected = A._color_to_hex(d["data"][0]["marker"]["color"])
    r = figure_to_canvas(d, width=40, height=14)
    assert _fg_set(r.canvas, CellRole.MARKER) == {expected}
    assert expected not in COLOR_PALETTE  # really the explicit colour, not palette


def test_scatter_explicit_line_color_wins():
    fig = go.Figure(
        go.Scatter(x=[0, 1, 2], y=[0, 1, 2], mode="lines", line_color="#0a0b0c")
    )
    d = fig.to_dict()
    expected = A._color_to_hex(d["data"][0]["line"]["color"])
    r = figure_to_canvas(d, width=40, height=14)
    assert _fg_set(r.canvas, CellRole.DOTS) == {expected}


def test_multi_series_get_distinct_palette_colors():
    fig = go.Figure()
    for i in range(3):
        fig.add_scatter(x=[0, 1, 2], y=[i, i + 1, i], mode="markers")
    r = figure_to_canvas(fig.to_dict(), width=50, height=18)
    seen = _fg_set(r.canvas, CellRole.MARKER)
    # three series -> three distinct palette colours actually reached the cells.
    assert seen == set(COLOR_PALETTE[:3])


def test_bar_forwards_color_to_cells():
    r = figure_to_canvas(
        go.Figure(go.Bar(x=[0, 1, 2], y=[1, 2, 3])).to_dict(), width=40, height=14
    )
    assert _fg_set(r.canvas, CellRole.BAR) == {COLOR_PALETTE[0]}


def test_bar_explicit_marker_color_wins():
    d = go.Figure(go.Bar(x=[0, 1, 2], y=[1, 2, 3], marker_color="#123456")).to_dict()
    expected = A._color_to_hex(d["data"][0]["marker"]["color"])
    r = figure_to_canvas(d, width=40, height=14)
    assert _fg_set(r.canvas, CellRole.BAR) == {expected}


def test_histogram_forwards_color_to_cells():
    r = figure_to_canvas(
        go.Figure(go.Histogram(x=[1, 1, 2, 2, 2, 3, 3, 4])).to_dict(),
        width=40,
        height=14,
    )
    assert _fg_set(r.canvas, CellRole.BAR) == {COLOR_PALETTE[0]}


# ===========================================================================
# 2. Colour-source precedence (_assign_color / _single_trace_color).
# ===========================================================================


def test_assign_color_explicit_marker_wins_regardless_of_index():
    # B1: the explicit CSS-name colour is normalized to hex before it can reach a
    # cell (the colour serializers parse #hex only) — precedence still holds.
    assert A._assign_color({"marker": {"color": "red"}}, 5) == "#ff0000"


def test_assign_color_line_color_used():
    assert A._assign_color({"line": {"color": "#abcdef"}}, 2) == "#abcdef"


def test_assign_color_normalizes_rgb_and_named():
    assert A._assign_color({"line": {"color": "rgb(255, 0, 0)"}}, 0) == "#ff0000"
    assert A._assign_color({"marker": {"color": "steelblue"}}, 1) == "#4682b4"


def test_assign_color_unresolvable_falls_back_to_palette():
    # An unparseable colour must never reach a cell as a raw string -> palette.
    assert A._assign_color({"marker": {"color": "not-a-color"}}, 2) == COLOR_PALETTE[2]
    hsl = {"line": {"color": "hsl(0, 100%, 50%)"}}
    assert A._assign_color(hsl, 0) == COLOR_PALETTE[0]


def test_color_to_hex_forms():
    assert A._color_to_hex("#ABC") == "#aabbcc"  # #rgb -> #rrggbb, lowercased
    assert A._color_to_hex("#FF0000") == "#ff0000"
    assert A._color_to_hex("rgb(0,128,255)") == "#0080ff"
    assert A._color_to_hex("rgba(0,128,255,0.5)") == "#0080ff"  # alpha dropped
    assert A._color_to_hex("red") == "#ff0000"
    assert A._color_to_hex("garbage") is None
    assert A._color_to_hex(123) is None
    assert A._color_to_hex("") is None


def test_every_plotly_named_color_resolves():
    # Full coverage: any CSS name plotly accepts must map to a hex here, so an
    # explicit named trace colour never falls through to the palette by accident.
    from _plotly_utils.basevalidators import ColorValidator

    for name in ColorValidator.named_colors:
        hx = A._color_to_hex(name)
        assert hx is not None and hx.startswith("#") and len(hx) == 7, name


def test_assign_color_marker_beats_line():
    trace = {"marker": {"color": "#111111"}, "line": {"color": "#222222"}}
    assert A._assign_color(trace, 0) == "#111111"


def test_assign_color_array_is_not_a_series_color():
    # A per-point colour array is not a single series colour -> palette by index.
    assert A._single_trace_color({"marker": {"color": [1, 2, 3]}}) is None
    assert A._assign_color({"marker": {"color": [1, 2, 3]}}, 1) == COLOR_PALETTE[1]


def test_assign_color_default_palette_cycles():
    n = len(COLOR_PALETTE)
    assert A._assign_color({}, 0) == COLOR_PALETTE[0]
    assert A._assign_color({}, n) == COLOR_PALETTE[0]  # wraps
    assert A._assign_color({}, 1) == COLOR_PALETTE[1]


# ===========================================================================
# 3. Heatmap adapter — cells, numpy decode, colorscale.
# ===========================================================================


def test_heatmap_populates_cells_with_fill_and_bg():
    z = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    r = figure_to_canvas(go.Figure(go.Heatmap(z=z)).to_dict(), width=40, height=14)
    cells = _heatmap_cells(r.canvas)
    assert cells, "heatmap drew no HEATMAP cells"
    fills = [c.fill for c in cells]
    assert min(fills) == pytest.approx(0.0)
    assert max(fills) == pytest.approx(1.0)
    # every heatmap cell carries a sampled hex bg for the colour serializers.
    assert all(isinstance(c.bg, str) and c.bg.startswith("#") for c in cells)


def test_heatmap_numpy_z_matches_list_z():
    z_list = [[float(v) for v in range(c, c + 4)] for c in (1, 5, 9)]
    z_np = np.arange(1, 13, dtype="float64").reshape(3, 4)
    a = figure_to_canvas(go.Figure(go.Heatmap(z=z_list)).to_dict(), width=40, height=14)
    b = figure_to_canvas(go.Figure(go.Heatmap(z=z_np)).to_dict(), width=40, height=14)
    a, b = a.canvas, b.canvas
    assert _fill_matrix(a) == _fill_matrix(b)
    assert _heatmap_cells(b)  # not empty (the numpy blocker would give garbage/none)


def test_heatmap_numpy_z_pure_python_fallback_matches():
    z_np = np.arange(1, 13, dtype="float64").reshape(3, 4)
    d = go.Figure(go.Heatmap(z=z_np)).to_dict()
    expected = _fill_matrix(figure_to_canvas(d, width=40, height=14).canvas)
    A._FORCE_NO_NUMPY = True
    try:
        got = _fill_matrix(figure_to_canvas(d, width=40, height=14).canvas)
    finally:
        A._FORCE_NO_NUMPY = False
    assert got == expected


def test_heatmap_2d_typed_array_reshape_roundtrip():
    z_np = np.arange(12, dtype="float64").reshape(3, 4)
    spec = go.Figure(go.Heatmap(z=z_np)).to_dict()["data"][0]["z"]
    assert A.is_typed_array_spec(spec)  # sanity: base64-encoded 2D array
    grid = H.heatmap_z({"z": spec})
    assert grid == [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]


def test_heatmap_colorscale_honored_greys_is_grayscale():
    d = go.Figure(go.Heatmap(z=[[0, 1], [2, 3]], colorscale="Greys")).to_dict()
    r = figure_to_canvas(d, width=20, height=10)
    bgs = {c.bg for c in _heatmap_cells(r.canvas) if c.bg}
    # grayscale: r == g == b for every sampled colour.
    for hx in bgs:
        rr, gg, bb = hx[1:3], hx[3:5], hx[5:7]
        assert rr == gg == bb, hx


def test_heatmap_default_colorscale_is_viridis_not_gray():
    d = go.Figure(go.Heatmap(z=[[0, 1], [2, 3]])).to_dict()
    r = figure_to_canvas(d, width=20, height=10)
    bgs = {c.bg for c in _heatmap_cells(r.canvas) if c.bg}
    # at least one Viridis colour is not neutral gray (r != g or g != b).
    assert any(not (h[1:3] == h[3:5] == h[5:7]) for h in bgs)


def test_normalize_colorscale_rgb_to_hex():
    cs = [[0.0, "rgb(0,0,0)"], [1.0, "rgb(255,255,255)"]]
    assert H._normalize_colorscale(cs) == [[0.0, "#000000"], [1.0, "#ffffff"]]


def test_normalize_colorscale_passthrough_and_bail():
    assert H._normalize_colorscale(None) is None
    assert H._normalize_colorscale("Viridis") == "Viridis"  # named -> Canvas resolves
    # CSS-named stops resolve now that the shared bridge knows the name table.
    assert H._normalize_colorscale([[0.0, "chartreuse"], [1.0, "#fff"]]) == [
        [0.0, "#7fff00"],
        [1.0, "#ffffff"],
    ]
    # an unconvertible colour still makes the whole scale bail to None (Canvas default).
    assert H._normalize_colorscale([[0.0, "hsl(0,100%,50%)"], [1.0, "#fff"]]) is None


# ===========================================================================
# 4. histogram2d adapter — binning + cells + count conservation.
# ===========================================================================


def test_histogram2d_populates_cells():
    rs = np.random.RandomState(0)
    x = rs.rand(500)
    y = rs.rand(500)
    d = go.Figure(go.Histogram2d(x=x, y=y, nbinsx=10, nbinsy=10)).to_dict()
    r = figure_to_canvas(d, width=40, height=14)
    assert _heatmap_cells(r.canvas), "histogram2d drew no HEATMAP cells"


def test_histogram2d_to_z_conserves_counts_numpy_and_pure_python():
    xs = [0.1, 0.2, 0.9, 0.9, 0.5]
    ys = [0.1, 0.15, 0.9, 0.8, 0.5]
    z_np = H._histogram2d_to_z(xs, ys, nbins=4)
    assert len(z_np) == 4 and all(len(r) == 4 for r in z_np)
    assert sum(sum(r) for r in z_np) == len(xs)

    A._FORCE_NO_NUMPY = True
    try:
        z_py = H._histogram2d_to_z(xs, ys, nbins=4)
    finally:
        A._FORCE_NO_NUMPY = False
    assert sum(sum(r) for r in z_py) == len(xs)


def test_histogram2d_drops_nonfinite_pairs():
    xs, ys = H._finite_xy_pairs({"x": [1.0, float("nan"), 3.0], "y": [1.0, 2.0, None]})
    assert xs == [1.0] and ys == [1.0]


def test_hist2d_nbins_honors_nbinsx():
    assert H._hist2d_nbins({"nbinsx": 7}) == 7
    assert H._hist2d_nbins({}) == H.DEFAULT_HIST2D_BINS


# ===========================================================================
# 5. Extent / framing for heatmap + histogram2d.
# ===========================================================================


def test_heatmap_extent_spans_grid_indices():
    trace = go.Heatmap(z=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]).to_plotly_json()
    extent = A._trace_extent(trace, "heatmap")
    assert extent is not None
    xs, ys = extent
    assert (min(xs), max(xs)) == (0.0, 3.0)  # 4 columns -> 0..3
    assert (min(ys), max(ys)) == (0.0, 2.0)  # 3 rows -> 0..2


def test_heatmap_extent_uses_explicit_coords():
    trace = go.Heatmap(
        z=[[1, 2, 3], [4, 5, 6]], x=[10, 20, 30], y=[100, 200]
    ).to_plotly_json()
    extent = A._trace_extent(trace, "heatmap")
    assert extent is not None
    xs, ys = extent
    assert (min(xs), max(xs)) == (10.0, 30.0)
    assert (min(ys), max(ys)) == (100.0, 200.0)


def test_histogram2d_extent_spans_sample_range():
    trace = go.Histogram2d(x=[0.0, 5.0, 10.0], y=[-2.0, 0.0, 3.0]).to_plotly_json()
    extent = A._trace_extent(trace, "histogram2d")
    assert extent is not None
    xs, ys = extent
    assert (min(xs), max(xs)) == (0.0, 10.0)
    assert (min(ys), max(ys)) == (-2.0, 3.0)


def test_heatmap_frame_uses_extent_ticks():
    # The driver frames from the extent: a wide grid must not degrade to (0,1).
    z = [[i + j for j in range(6)] for i in range(5)]
    r = figure_to_canvas(go.Figure(go.Heatmap(z=z)).to_dict(), width=50, height=16)
    assert r.canvas is not None
    out = r.canvas.render("text-utf")
    assert "5" in out  # x extent 0..5 -> a '5' tick label appears


# ===========================================================================
# 6. Registration (adapters + v2 renderers).
# ===========================================================================


def test_heatmap_and_histogram2d_registered():
    assert A.get_adapter("heatmap") is not None
    assert A.get_adapter("histogram2d") is not None


def test_v2_renderers_registered_with_mode():
    for mode in ("text-ansi", "text-html"):
        assert mode in pio.renderers
        assert pio.renderers[mode].mode == mode


# ===========================================================================
# 7. End-to-end through the serializers (skips if one is unavailable).
# ===========================================================================


def _render_or_skip(canvas, mode):
    try:
        return canvas.render(mode)
    except NotImplementedError:
        pytest.skip(f"{mode} serializer not available")


def test_heatmap_renders_shade_ramp_text_utf():
    z = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    r = figure_to_canvas(go.Figure(go.Heatmap(z=z)).to_dict(), width=44, height=14)
    assert r.canvas is not None
    out = r.canvas.render("text-utf")
    assert any(ch in out for ch in "░▒▓█"), out


def _row_max_fill(canvas, y):
    fills = [c.fill for c in canvas.grid.rows[y] if c.role == CellRole.HEATMAP]
    return max(fills) if fills else None


def test_heatmap_orientation_low_z_row_at_bottom():
    # z[0] is the low row; plotly draws it at the bottom. After the adapter's
    # row-reverse, the bottom plot rows should be lighter (low fill) than the top.
    z = [[0, 0, 0, 0], [9, 9, 9, 9]]
    r = figure_to_canvas(go.Figure(go.Heatmap(z=z)).to_dict(), width=30, height=12)
    c = r.canvas
    assert c is not None
    hm_rows = [y for y in range(c.height) if _row_max_fill(c, y) is not None]
    top_fill = _row_max_fill(c, hm_rows[0])
    bottom_fill = _row_max_fill(c, hm_rows[-1])
    assert top_fill is not None and bottom_fill is not None
    assert top_fill > bottom_fill


def test_color_reaches_ansi_output():
    # Palette colour #636efa -> 24-bit ANSI triple 99;110;250 in the escape.
    r = figure_to_canvas(
        go.Figure(go.Scatter(x=[0, 1, 2], y=[0, 1, 2], mode="markers")).to_dict(),
        width=40,
        height=14,
    )
    out = _render_or_skip(r.canvas, "text-ansi")
    assert "99;110;250" in out, "series palette colour did not reach the ANSI output"


def test_heatmap_bg_reaches_ansi_output():
    r = figure_to_canvas(
        go.Figure(go.Heatmap(z=[[0, 1], [2, 3]])).to_dict(), width=24, height=10
    )
    out = _render_or_skip(r.canvas, "text-ansi")
    # a background escape (48;2;...) appears for the heatmap cells.
    assert "48;2;" in out


def test_heatmap_renders_html():
    r = figure_to_canvas(
        go.Figure(go.Heatmap(z=[[0, 1], [2, 3]])).to_dict(), width=24, height=10
    )
    out = _render_or_skip(r.canvas, "text-html")
    assert "<pre" in out and "span" in out


def test_sin_curve_still_renders_multiline_text_utf():
    # guard: colour forwarding didn't change monochrome geometry.
    n = 60
    xs = [i * (2 * math.pi) / (n - 1) for i in range(n)]
    ys = [math.sin(x) for x in xs]
    d = go.Figure(go.Scatter(x=xs, y=ys)).to_dict()
    r = figure_to_canvas(d, width=60, height=20)
    assert r.canvas is not None
    out = r.canvas.render("text-utf")
    assert out.count("\n") > 3


# ===========================================================================
# 8. B1 regression — non-hex explicit colours must render, not crash.
# ===========================================================================


@pytest.mark.parametrize("color", ["red", "rgb(255,0,0)", "rgba(255,0,0,0.5)"])
@pytest.mark.parametrize("mode", ["text-ansi", "text-html"])
def test_non_hex_trace_color_renders_without_crash(color, mode):
    # The exact class of bug QA hit: a CSS name / rgb() flowed verbatim into a
    # cell and crashed the #hex-only colour serializer. Now it's normalized.
    fig = go.Figure(
        go.Scatter(
            x=[1, 2, 3], y=[1, 2, 3], mode="lines+markers", line=dict(color=color)
        )
    )
    r = figure_to_canvas(fig.to_dict(), width=40, height=14)
    assert _fg_set(r.canvas, CellRole.DOTS) == {"#ff0000"}  # hex reached the cell
    out = _render_or_skip(r.canvas, mode)  # must not raise
    if mode == "text-ansi":
        assert "255;0;0" in out
    else:  # text-html: the hex lands in the scoped style block
        assert "ff0000" in out.lower()


def test_non_hex_color_full_show_path_no_crash():
    # The literal coordinator repro, driven through the renderer's render().
    class FakeStdout:
        def __init__(self):
            self.buffer = _FakeBuffer()

    import sys

    fake = FakeStdout()
    old = sys.stdout
    sys.stdout = fake
    try:
        pio.renderers["text-ansi"].render(
            go.Figure(
                go.Scatter(x=[1, 2, 3], y=[1, 2, 3], line=dict(color="red"))
            ).to_dict()
        )
    finally:
        sys.stdout = old
    out = fake.buffer.data.decode("utf-8")
    assert "255;0;0" in out  # rendered the red line, no crash


class _FakeBuffer:
    def __init__(self):
        self.data = b""

    def write(self, b):
        self.data += b

    def flush(self):
        pass


# ===========================================================================
# 9. B2 regression — a serialize-time error is not mislabelled "canvas too small".
# ===========================================================================


def test_is_too_small_error_predicate():
    assert A._is_too_small_error(
        ValueError("Canvas too small for the requested frame: ...")
    )
    assert A._is_too_small_error(ValueError("Canvas size must be at least 1x1 cells"))
    # an unrelated error is NOT a size error.
    assert not A._is_too_small_error(
        ValueError("invalid literal for int() with base 16: 'rg'")
    )


def test_unrelated_serialize_error_surfaces_accurately(monkeypatch):
    # A serialize-time ValueError that isn't a size problem must re-raise, not be
    # swallowed and reported as the (confidently wrong) "canvas too small" note.
    from plotly.io._text import adapters as AD
    from plotly.io._text.adapters import DrawResult

    class BoomCanvas(Canvas):
        def render(self, mode="text-utf"):
            raise ValueError("totally unrelated boom")

    def _fake(*a, **k):
        return DrawResult(BoomCanvas(), [])

    monkeypatch.setattr(AD, "figure_to_canvas", _fake)

    import sys

    old = sys.stdout
    sys.stdout = FakeStdoutForBoom()
    try:
        with pytest.raises(ValueError, match="totally unrelated boom"):
            pio.renderers["text-utf"].render(
                go.Figure(go.Scatter(y=[1, 2, 3])).to_dict()
            )
    finally:
        sys.stdout = old


class FakeStdoutForBoom:
    def __init__(self):
        self.buffer = _FakeBuffer()
