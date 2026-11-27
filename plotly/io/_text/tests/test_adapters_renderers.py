"""Tests for the figure adapters, driver, and renderer registration.

Covers:

* numpy-built figure renders identical to the list-built one (typed-array
  decode) — on both the numpy and the numpy-absent fallback paths;
* grouped bars/histograms fan out into sub-columns (no silent overwrite);
* histogram binning on a known input;
* graceful degradation notes (unsupported + mixed figures);
* undersized canvas degrades to a note instead of raising;
* renderer registration + forced-UTF-8 output.

Sibling to ``test_canvas_serializers.py`` in the same directory.
"""

import io
import math
import sys

import pytest

import plotly.graph_objects as go
import plotly.io as pio
from plotly.io._text import adapters as A
from plotly.io._text.adapters import figure_to_canvas
from plotly.io._text.adapters.histogram import histogram_bins

np = pytest.importorskip("numpy")


# ---------------------------------------------------------------------------
# B1 — typed-array decode: numpy data must render identically to list data.
# ---------------------------------------------------------------------------


def _sin_dicts(n=60):
    xs = [i * (2 * math.pi) / (n - 1) for i in range(n)]
    ys = [math.sin(x) for x in xs]
    list_fig = go.Figure(go.Scatter(x=xs, y=ys)).to_dict()
    np_fig = go.Figure(
        go.Scatter(
            x=np.linspace(0, 2 * math.pi, n), y=np.sin(np.linspace(0, 2 * math.pi, n))
        )
    ).to_dict()
    return list_fig, np_fig


def test_numpy_figure_matches_list_figure_numpy_path():
    list_fig, np_fig = _sin_dicts()
    ra = figure_to_canvas(list_fig, width=60, height=20)
    rb = figure_to_canvas(np_fig, width=60, height=20)
    assert ra.canvas is not None and rb.canvas is not None
    a = ra.canvas.render("text-utf")
    b = rb.canvas.render("text-utf")
    assert a == b
    # And it is not the degenerate diagonal: the curve must span multiple rows.
    assert b.count("\n") > 3


def test_numpy_figure_matches_list_figure_pure_python_fallback():
    list_fig, np_fig = _sin_dicts()
    r_expected = figure_to_canvas(list_fig, width=60, height=20)
    assert r_expected.canvas is not None
    expected = r_expected.canvas.render("text-utf")
    A._FORCE_NO_NUMPY = True
    try:
        r_got = figure_to_canvas(np_fig, width=60, height=20)
        assert r_got.canvas is not None
        got = r_got.canvas.render("text-utf")
    finally:
        A._FORCE_NO_NUMPY = False
    assert got == expected


def test_typed_array_decode_dtypes():
    for arr in (
        np.array([1, 2, 3], dtype="int8"),
        np.array([1, 2, 3], dtype="int32"),
        np.array([1.5, 2.5, 3.5], dtype="float32"),
        np.array([1.5, 2.5, 3.5], dtype="float64"),
    ):
        fig = go.Figure(go.Scatter(y=arr)).to_dict()
        spec = fig["data"][0]["y"]
        assert A.is_typed_array_spec(spec)  # sanity: it really is base64-encoded
        decoded = A._decode_typed_array(spec)
        assert [round(v, 3) for v in decoded] == [round(float(v), 3) for v in arr]
        A._FORCE_NO_NUMPY = True
        try:
            fb = A._decode_typed_array(spec)
        finally:
            A._FORCE_NO_NUMPY = False
        assert [round(v, 3) for v in fb] == [round(v, 3) for v in decoded]


# ---------------------------------------------------------------------------
# B2 — grouped bars must show BOTH series.
# ---------------------------------------------------------------------------


def test_grouped_bars_show_both_series():
    fig = go.Figure()
    fig.add_bar(x=["q1", "q2", "q3"], y=[10, 10, 10], name="A")
    fig.add_bar(x=["q1", "q2", "q3"], y=[3, 3, 3], name="B")
    r = figure_to_canvas(fig.to_dict(), width=64, height=16)
    assert r.canvas is not None
    out = r.canvas.render("text-utf")
    rows = out.split("\n")
    # Tall series A reaches the top rows; short series B only the bottom rows.
    top = "\n".join(rows[:5])
    bottom = "\n".join(rows[8:13])
    tall_bars = top.count("█")

    # The short series adds bar cells low down that the tall series' columns
    # don't occupy — i.e. more distinct bar columns near the baseline.
    def bar_cols(block):
        cols = set()
        for line in block.split("\n"):
            for i, ch in enumerate(line):
                if ch in "█▁▂▃▄▅▆▇":
                    cols.add(i)
        return cols

    assert len(bar_cols(bottom)) > len(bar_cols(top)), out
    assert tall_bars > 0


def test_grouped_offset_distinct_positions():
    # Two bar series over the same categories get shifted to different x.
    fig = go.Figure()
    fig.add_bar(x=[0, 1, 2], y=[1, 1, 1])
    fig.add_bar(x=[0, 1, 2], y=[2, 2, 2])
    calls = []

    class Rec:
        def __init__(self, width=60, height=20):
            self.width = width
            self.height = height

        def frame(self, *a, **k):
            pass

        def bar(self, positions, values, *, orientation="v", base=0.0, color=None):
            calls.append(list(positions))

    orig = A.Canvas
    A.Canvas = Rec
    try:
        figure_to_canvas(fig.to_dict(), width=60, height=20)
    finally:
        A.Canvas = orig
    assert len(calls) == 2
    assert calls[0] != calls[1]  # the two series are offset apart
    # centred: series0 shifted left of the category, series1 shifted right
    assert calls[0][0] < 0 < calls[1][0]


def test_grouped_density_warning_when_too_narrow():
    fig = go.Figure()
    for _ in range(6):
        fig.add_bar(x=list(range(20)), y=[1] * 20)
    result = figure_to_canvas(fig.to_dict(), width=24, height=12)
    assert any("grouped bars exceed" in w for w in result.warnings), result.warnings


# ---------------------------------------------------------------------------
# Histogram binning on a known input.
# ---------------------------------------------------------------------------


def test_histogram_bins_known_input():
    samples = [1, 2, 2, 3, 3, 3, 4]
    trace = go.Histogram(
        x=samples, xbins=dict(start=0.5, end=4.5, size=1.0)
    ).to_plotly_json()
    centers, counts, edges, orient = histogram_bins(trace)
    assert edges == [0.5, 1.5, 2.5, 3.5, 4.5]
    assert counts == [1, 2, 3, 1]
    assert sum(counts) == len(samples)
    assert orient == "v"


def test_histogram_counts_sum_pure_python_and_numpy():
    rng = [((i * 7919) % 1000) / 100.0 for i in range(300)]
    trace = go.Histogram(x=rng).to_plotly_json()
    _, counts_np, _, _ = histogram_bins(trace)
    A._FORCE_NO_NUMPY = True
    try:
        _, counts_py, _, _ = histogram_bins(trace)
    finally:
        A._FORCE_NO_NUMPY = False
    assert sum(counts_np) == len(rng)
    assert counts_py == counts_np


# ---------------------------------------------------------------------------
# Degradation notes — unsupported and mixed figures.
# ---------------------------------------------------------------------------


def test_unsupported_trace_degrades():
    result = figure_to_canvas(
        go.Figure(go.Pie(labels=["a", "b"], values=[1, 2])).to_dict(), mode="text-utf"
    )
    assert result.warnings == ["⚠ pie traces aren't supported by the text renderer"]
    # frame still drawn, no crash
    assert result.canvas is not None


def test_unsupported_trace_ascii_prefix():
    result = figure_to_canvas(
        go.Figure(go.Pie(labels=["a"], values=[1])).to_dict(), mode="text-ascii"
    )
    assert result.warnings == ["! pie traces aren't supported by the text renderer"]


def test_mixed_figure_renders_supported_notes_skipped():
    fig = go.Figure()
    fig.add_scatter(x=[0, 1, 2], y=[0, 1, 2], mode="lines")
    fig.add_trace(go.Pie(labels=["a", "b"], values=[1, 2]))
    fig.add_bar(x=[0, 1], y=[3, 4])
    result = figure_to_canvas(fig.to_dict())
    assert result.canvas is not None
    assert result.warnings == ["⚠ pie traces aren't supported by the text renderer"]
    # supported traces actually drew something
    assert result.canvas.render("text-utf").strip() != ""


# ---------------------------------------------------------------------------
# B3 — undersized canvas degrades gracefully.
# ---------------------------------------------------------------------------


def test_undersized_canvas_degrades_in_driver():
    result = figure_to_canvas(
        go.Figure(go.Scatter(x=[1, 2, 3], y=[1, 2, 3])).to_dict(), width=2, height=2
    )
    assert result.canvas is None
    assert len(result.warnings) == 1
    assert "canvas too small to render" in result.warnings[0]


def test_undersized_canvas_show_does_not_crash():
    buf = io.StringIO()
    old = sys.stdout
    sys.stdout = buf
    try:
        pio.show(
            go.Figure(go.Scatter(x=[1, 2, 3], y=[1, 2, 3])),
            renderer="text-utf",
            width=2,
            height=2,
        )
    finally:
        sys.stdout = old
    assert "canvas too small to render" in buf.getvalue()


# ---------------------------------------------------------------------------
# Registration + multi-series glyphs + forced UTF-8.
# ---------------------------------------------------------------------------


def test_renderers_registered():
    assert "text-utf" in pio.renderers
    assert "text-ascii" in pio.renderers


def test_adapters_registered():
    assert {"scatter", "scattergl", "bar", "histogram"}.issubset(A.ADAPTERS)


def test_multi_series_distinct_glyphs():
    fig = go.Figure()
    for i in range(3):
        fig.add_scatter(x=[0, 1], y=[i, i + 1], mode="markers")
    seen = []

    class Rec:
        def __init__(self, width=60, height=20):
            self.width = width
            self.height = height

        def frame(self, *a, **k):
            pass

        def line(self, *a, **k):
            pass

        def markers(self, points, glyph, *, color=None):
            seen.append(glyph)

    orig = A.Canvas
    A.Canvas = Rec
    try:
        figure_to_canvas(fig.to_dict())
    finally:
        A.Canvas = orig
    assert len(set(seen)) == 3
    assert seen == list(A.GLYPH_PALETTE[:3])


def test_renderer_forces_utf8_bytes_and_appends_warning():
    class FakeBuffer:
        def __init__(self):
            self.data = b""

        def write(self, b):
            self.data += b

        def flush(self):
            pass

    class FakeStdout:
        def __init__(self):
            self.buffer = FakeBuffer()

    fake = FakeStdout()
    old = sys.stdout
    sys.stdout = fake
    try:
        pio.renderers["text-utf"].render(
            go.Figure(go.Pie(labels=["a"], values=[1])).to_dict()
        )
    finally:
        sys.stdout = old
    out = fake.buffer.data.decode("utf-8")
    assert "⚠ pie traces aren't supported by the text renderer" in out
