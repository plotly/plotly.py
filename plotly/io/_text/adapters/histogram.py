"""``histogram`` adapter.

Histograms bin at *render* time in plotly.js, so the figure JSON usually carries
only raw ``x`` (or ``y``) samples — the adapter must reproduce Plotly's binning
(honouring ``xbins``/``nbinsx`` when present, else approximating) and then draw
the result exactly like :mod:`~plotly.io._text.adapters.bar`. Binning is *not
free* and may disagree with the real chart at bin edges — a known fidelity
limitation. numpy is imported lazily inside the body so it stays an optional
dependency.
"""

from __future__ import annotations

import math
from typing import List, Optional, Sequence, Tuple

from plotly.io._text.adapters import (
    AdapterContext,
    _coerce_numeric,
    _group_offset,
    _grouped_density_warning,
    _is_finite_number,
    _numpy,
    register_adapter,
)
from plotly.io._text.canvas import Canvas


def _nice_step(raw: float) -> float:
    """Round ``raw`` up to a 1/2/2.5/5/10 * 10^k "nice" number.

    Mirrors the round-number bin widths Plotly's autobin favours, so our bins
    line up with the real chart more often than naive equal-width slicing.
    """
    if raw <= 0:
        return 1.0
    mag = 10.0 ** math.floor(math.log10(raw))
    for m in (1.0, 2.0, 2.5, 5.0, 10.0):
        if m * mag >= raw:
            return m * mag
    return 10.0 * mag


def _auto_target_bins(n: int) -> int:
    """Target bin count for autobinning (square-root rule, clamped)."""
    if n <= 1:
        return 1
    return max(1, min(60, int(math.ceil(math.sqrt(n)))))


def _bin_edges(
    samples: Sequence[float],
    bins_spec: Optional[dict],
    nbins: Optional[int],
) -> List[float]:
    """Compute bin edges honouring ``xbins``/``ybins`` then ``nbinsx``/``nbinsy``.

    ``bins_spec`` (Plotly's ``{"start", "end", "size"}``) wins when a ``size`` is
    present; otherwise a "nice" step spanning the data range is chosen for the
    requested (or auto) number of bins.
    """
    if not samples:
        return [0.0, 1.0]

    lo, hi = min(samples), max(samples)

    # Explicit xbins with a size -> honour start/end/size.
    if isinstance(bins_spec, dict) and bins_spec.get("size"):
        size = float(bins_spec["size"])
        start = bins_spec.get("start")
        end = bins_spec.get("end")
        start = float(start) if start is not None else lo
        end = float(end) if end is not None else hi
        if size <= 0 or end <= start:
            return [lo, hi if hi > lo else lo + 1.0]
        edges = [start]
        e = start
        # +size/2 guard against float drift; ensure the last sample is covered.
        while e < end - size * 1e-9:
            e += size
            edges.append(e)
        if edges[-1] < end:
            edges.append(edges[-1] + size)
        return edges

    if lo == hi:
        return [lo - 0.5, hi + 0.5]

    target = int(nbins) if nbins else _auto_target_bins(len(samples))
    target = max(1, target)
    step = _nice_step((hi - lo) / target)
    start = math.floor(lo / step) * step
    edges = [start]
    e = start
    while e < hi - step * 1e-9:
        e += step
        edges.append(e)
    if edges[-1] <= hi:
        edges.append(edges[-1] + step)
    return edges


def _bin_counts(samples: Sequence[float], edges: Sequence[float]) -> List[int]:
    """Count samples per ``[edge_i, edge_{i+1})`` bin (last bin closed on both).

    Uses numpy when importable (fast path, matching its half-open convention),
    else a pure-Python bisect — numpy stays an optional dependency.
    """
    nbins = len(edges) - 1
    if nbins <= 0:
        return []

    np = _numpy()
    if np is not None:
        counts, _ = np.histogram(np.asarray(samples, dtype=float), bins=list(edges))
        return [int(c) for c in counts]

    from bisect import bisect_right

    counts = [0] * nbins
    edge_list = list(edges)
    last = edge_list[-1]
    for s in samples:
        if s < edge_list[0] or s > last:
            continue
        if s == last:
            counts[-1] += 1
            continue
        idx = bisect_right(edge_list, s) - 1
        if 0 <= idx < nbins:
            counts[idx] += 1
    return counts


def histogram_bins(
    trace: dict,
) -> Tuple[List[float], List[int], List[float], str]:
    """Return ``(centers, counts, edges, orientation)`` for a histogram trace.

    Vertical histograms bin the ``x`` samples; horizontal ones bin ``y``. Bin
    specification comes from ``xbins``/``ybins`` then ``nbinsx``/``nbinsy``,
    falling back to an auto "nice" binning.
    """
    orientation = trace.get("orientation") or "v"
    if orientation == "h":
        raw = trace.get("y")
        bins_spec = trace.get("ybins")
        nbins = trace.get("nbinsy")
    else:
        raw = trace.get("x")
        bins_spec = trace.get("xbins")
        nbins = trace.get("nbinsx")

    samples = _coerce_numeric(raw) if raw is not None else []
    samples = [s for s in samples if _is_finite_number(s)]

    edges = _bin_edges(samples, bins_spec, nbins)
    counts = _bin_counts(samples, edges)
    centers = [(edges[i] + edges[i + 1]) / 2.0 for i in range(len(edges) - 1)]
    return centers, counts, edges, orientation


def histogram_adapter(trace: dict, canvas: Canvas, ctx: AdapterContext) -> None:
    """Bin one ``histogram`` trace and draw it as bars onto ``canvas``.

    Computes bin edges + counts from the raw samples (pure Python or a lazily
    imported numpy), then calls :meth:`Canvas.bar` with the bin centres and
    counts, honouring ``trace.get("orientation", "v")``.
    """
    centers, counts, _edges, orientation = histogram_bins(trace)
    if not centers:
        return
    centers, collided = _group_offset(centers, ctx, orientation, canvas)
    if collided:
        note = _grouped_density_warning(ctx.mode)
        if note not in ctx.warnings:
            ctx.warnings.append(note)
    canvas.bar(
        centers,
        [float(c) for c in counts],
        orientation=orientation,
        base=0.0,
        color=ctx.color,
    )


register_adapter("histogram", histogram_adapter)
