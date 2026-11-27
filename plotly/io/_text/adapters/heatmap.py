"""``heatmap`` / ``histogram2d`` adapter.

Density grids -> shaded cells via :meth:`Canvas.heatmap`, with a per-cell ``bg``
colour sampled from the trace's ``colorscale`` (default Viridis). ``histogram2d``
reduces to the same path after binning its raw ``x``/``y`` into a 2D count grid.
The colour modes (``text-ansi`` / ``text-html``) are the natural showcase; in the
monochrome modes only the shade ramp (``░▒▓█`` / ``.:+#``) shows.

numpy is used when present (fast path) with a pure-Python fallback so the
renderer stays numpy-optional — the same discipline the ``histogram`` adapter
uses. ``z`` (and the ``histogram2d`` samples) are normalized through
:func:`~plotly.io._text.adapters._as_sequence` so a base64 typed-array from
``fig.to_dict()`` on numpy data is decoded rather than iterated by its dict keys
(the v1 numpy blocker, guarded against here too).
"""

from __future__ import annotations

from typing import List, Optional, Sequence, Tuple

from plotly.io._text.adapters import (
    AdapterContext,
    _as_float,
    _as_sequence,
    _color_to_hex,
    _decode_typed_array,
    _numpy,
    is_typed_array_spec,
    register_adapter,
)
from plotly.io._text.canvas import Canvas

#: Default per-axis bin count for a ``histogram2d`` when the trace sets no
#: ``nbinsx`` / ``nbinsy``.
DEFAULT_HIST2D_BINS = 20


def _decode_2d_typed_array(z: dict) -> Optional[List[List[float]]]:
    """Reshape a **2D** typed-array spec ``{"dtype", "bdata", "shape": "r, c"}``.

    ``fig.to_dict()`` base64-encodes a 2D numpy ``z`` as a *flat* buffer plus a
    ``"r, c"`` shape string. :func:`_decode_typed_array` alone would yield a flat
    list — iterated as rows that would be single-element garbage (the v1 numpy
    blocker, in 2D). Here we decode flat then reshape per ``shape``. A 1D typed
    array (no 2-tuple shape) becomes a single row; a non-spec returns ``None`` so
    the caller falls back to the generic path.
    """
    if not is_typed_array_spec(z):
        return None
    flat = _decode_typed_array(z)
    shape = z.get("shape")
    if isinstance(shape, str):
        dims = [int(s) for s in shape.split(",") if s.strip()]
        if len(dims) == 2:
            r, c = dims
            if c > 0:
                return [flat[i * c : (i + 1) * c] for i in range(r)]
    return [list(flat)] if flat else None


def heatmap_z(trace: dict) -> Optional[List[List[float]]]:
    """Extract the 2D ``z`` grid from a ``heatmap`` trace, or ``None``.

    Handles three shapes of ``z``:

    * a **2D typed-array spec** (numpy ``z`` through ``fig.to_dict()``) — decoded
      *and reshaped* per its ``shape`` (:func:`_decode_2d_typed_array`) so a
      numpy heatmap isn't flattened into garbage rows (the v1 numpy blocker);
    * a nested list / list-of-arrays — each row normalized via
      :func:`_as_sequence` (decoding any per-row typed array);
    * a raw 2D numpy array (materialized to rows).

    Non-rectangular ``z`` is preserved row-by-row; the Canvas resamples each row
    independently. Returns ``None`` when there is no usable 2D grid.
    """
    z = trace.get("z")
    if z is None:
        return None

    reshaped = _decode_2d_typed_array(z)
    if reshaped is not None:
        return reshaped or None

    rows = _as_sequence(z)
    if rows is None:
        return None
    out: List[List[float]] = []
    for row in rows:
        r = _as_sequence(row)
        if r is not None:
            out.append(list(r))
    return out or None


def _finite_xy_pairs(trace: dict) -> Tuple[List[float], List[float]]:
    """Return the finite ``(xs, ys)`` sample pairs from a ``histogram2d`` trace.

    ``x``/``y`` are normalized via :func:`_as_sequence` (typed-array decode) then
    paired and filtered to finite floats — a pair is dropped if either coordinate
    is missing/non-numeric so a NaN never lands in a bin.
    """
    xr = _as_sequence(trace.get("x")) or []
    yr = _as_sequence(trace.get("y")) or []
    n = min(len(xr), len(yr))
    xs: List[float] = []
    ys: List[float] = []
    for i in range(n):
        fx = _as_float(xr[i])
        fy = _as_float(yr[i])
        if fx is not None and fy is not None:
            xs.append(fx)
            ys.append(fy)
    return xs, ys


def _hist2d_nbins(trace: dict) -> int:
    """Per-axis bin count for a ``histogram2d`` (honours ``nbinsx``/``nbinsy``)."""
    for key in ("nbinsx", "nbinsy"):
        v = _as_float(trace.get(key))
        if v is not None and v >= 1:
            return int(v)
    return DEFAULT_HIST2D_BINS


def _bin_index(v: float, lo: float, hi: float, n: int) -> int:
    """Clamp ``v`` into one of ``n`` equal bins over ``[lo, hi]`` (last closed)."""
    if hi <= lo:
        return 0
    idx = int((v - lo) / (hi - lo) * n)
    if idx < 0:
        return 0
    if idx >= n:
        return n - 1
    return idx


def _histogram2d_to_z(
    x: Sequence[float], y: Sequence[float], nbins: int = DEFAULT_HIST2D_BINS
) -> List[List[float]]:
    """Bin raw ``x``/``y`` samples into an ``nbins`` x ``nbins`` count grid.

    The returned grid is ``z[row][col]`` with ``col`` the x bin (ascending left
    -> right) and ``row`` the y bin ordered **top -> bottom for descending y**
    (row 0 is the highest-y bin) so it lines up with :meth:`Canvas.heatmap`
    drawing ``z[0]`` at the top of the plot region against a y axis that
    increases upward. numpy's :func:`numpy.histogram2d` is used when importable
    (fast path); otherwise a pure-Python equal-width binning — matching the
    ``histogram`` adapter's numpy-optional approach. Returns ``[]`` when there is
    no data.
    """
    xs = [float(v) for v in x]
    ys = [float(v) for v in y]
    if not xs or not ys:
        return []
    n = max(1, int(nbins))

    np = _numpy()
    if np is not None:
        h, _xe, _ye = np.histogram2d(
            np.asarray(xs, dtype=float), np.asarray(ys, dtype=float), bins=n
        )
        # h[xi, yi] -> want z[yrow][xcol]; transpose then flip y so row 0 = top.
        z = h.T[::-1]
        return [[float(c) for c in row] for row in z]

    xlo, xhi = min(xs), max(xs)
    ylo, yhi = min(ys), max(ys)
    grid = [[0 for _ in range(n)] for _ in range(n)]  # grid[yi][xi], yi ascending
    for xv, yv in zip(xs, ys):
        xi = _bin_index(xv, xlo, xhi, n)
        yi = _bin_index(yv, ylo, yhi, n)
        grid[yi][xi] += 1
    # Flip y so row 0 is the highest-y bin (top of the plot).
    return [[float(c) for c in row] for row in grid[::-1]]


def _normalize_colorscale(cs):
    """Bridge a trace's ``colorscale`` to what :meth:`Canvas.heatmap` accepts.

    ``fig.to_dict()`` expands a named colorscale (``"Viridis"``, ``"Greys"``,
    ...) into a list of ``[stop, "rgb(...)"]`` pairs — which the Canvas colour
    sampler can't parse (it expects ``#hex``). Here we convert each entry's
    colour to hex. ``None`` and a bare named string pass through unchanged (the
    Canvas resolves those itself); an entry we can't convert makes the whole
    thing fall back to ``None`` so the Canvas uses its default scale rather than
    crashing.
    """
    if cs is None or isinstance(cs, str):
        return cs
    try:
        pairs = []
        for stop, color in cs:
            hx = _color_to_hex(color)
            if hx is None:
                return None
            pairs.append([float(stop), hx])
    except (TypeError, ValueError):
        return None
    return pairs or None


def _finite_floats(v) -> List[float]:
    """Finite floats from an array-like (typed-array decoded), non-numeric dropped."""
    out: List[float] = []
    for item in _as_sequence(v) or []:
        f = _as_float(item)
        if f is not None:
            out.append(f)
    return out


def heatmap_extent(trace: dict):
    """``(xs, ys)`` data extent a ``heatmap`` trace contributes to the frame.

    Uses the trace's ``x``/``y`` coordinate arrays when present (finite values
    only); otherwise the grid index extents (``0..ncols-1`` / ``0..nrows-1``) so
    the axes span the ``z`` grid. Returns ``None`` when there is no usable grid.
    """
    z = heatmap_z(trace)
    if not z:
        return None
    nrows = len(z)
    ncols = max((len(r) for r in z), default=0)
    if ncols == 0:
        return None

    xs = _finite_floats(trace.get("x"))
    ys = _finite_floats(trace.get("y"))
    if not xs:
        xs = [0.0, float(ncols - 1)]
    if not ys:
        ys = [0.0, float(nrows - 1)]
    return xs, ys


def histogram2d_extent(trace: dict):
    """``(xs, ys)`` data extent a ``histogram2d`` trace contributes to the frame.

    The finite raw ``x``/``y`` samples — the axes span the binned data range.
    Returns ``None`` when there are no finite samples.
    """
    xs, ys = _finite_xy_pairs(trace)
    if not xs or not ys:
        return None
    return xs, ys


def heatmap_adapter(trace: dict, canvas: Canvas, ctx: AdapterContext) -> None:
    """Draw one ``heatmap`` / ``histogram2d`` trace onto ``canvas``.

    1. for ``histogram2d``, bin the finite ``trace["x"]``/``trace["y"]`` samples
       via :func:`_histogram2d_to_z`; for ``heatmap``, read :func:`heatmap_z`
       (typed-array-decoded);
    2. call ``canvas.heatmap(z, colorscale=trace.get("colorscale"))`` — the
       Canvas normalizes ``z`` and samples per-cell ``bg`` colours from the
       colorscale (default Viridis), resampling ``z`` to the plot region.

    Never raises on empty / malformed data (returns quietly) so ``fig.show``
    degrades cleanly.
    """
    ttype = trace.get("type")
    if ttype == "histogram2d":
        xs, ys = _finite_xy_pairs(trace)
        if not xs or not ys:
            return
        # Already oriented row 0 = highest-y bin (top of the plot region).
        z = _histogram2d_to_z(xs, ys, nbins=_hist2d_nbins(trace))
    else:
        z = heatmap_z(trace)
        if z:
            # Plotly draws ``z[0]`` at the **bottom** (y increases upward), but
            # :meth:`Canvas.heatmap` draws row 0 at the top — reverse so the
            # orientation matches the on-screen chart.
            z = z[::-1]

    if not z:
        return
    canvas.heatmap(z, colorscale=_normalize_colorscale(trace.get("colorscale")))


register_adapter("heatmap", heatmap_adapter)
register_adapter("histogram2d", heatmap_adapter)
