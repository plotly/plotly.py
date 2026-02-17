"""
Recommendations mode: optional warnings when constructing graph_objects (Figure,
trace types, Layout) if arguments don't match certain criteria. Frame is not
included for now.

Enable/disable globally:
  - Environment: set PLOTLY_RECOMMENDATIONS=1 (or "true", "yes") to enable.
  - In code: plotly.recommendations.config.enabled = True

Example:
    import plotly.recommendations
    import plotly.graph_objects as go

    plotly.recommendations.config.enabled = True

    go.Figure(data=[go.Scatter(y=[1, 2, 3])])  # may emit recommendation warnings
"""

import os
import warnings

# -----------------------------------------------------------------------------
# Global enable/disable
# -----------------------------------------------------------------------------

def _env_enabled():
    v = os.environ.get("PLOTLY_RECOMMENDATIONS", "").strip().lower()
    return v in ("1", "true", "yes", "on")


class _RecommendationsConfig:
    """
    Global config for recommendations mode.
    When enabled, recommendation checkers run after Figure/trace/Layout
    construction and may emit warnings.
    """

    def __init__(self):
        self._enabled = _env_enabled()

    @property
    def enabled(self):
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        self._enabled = bool(value)

# Singleton used by the rest of the package
config = _RecommendationsConfig()


# -----------------------------------------------------------------------------
# Recommendation checkers (extensible list)
# -----------------------------------------------------------------------------


def _check_scatter_xy_length(obj, context):
    """Warn if a scatter trace has x or y with length >= 10."""
    if context != "trace":
        return
    if getattr(obj, "plotly_name", None) != "scatter":
        return
    for prop in ("x", "y"):
        try:
            val = obj[prop]
            if val is not None and hasattr(val, "__len__") and len(val) >= 10:
                warnings.warn(
                    "Scatter trace '%s' has length %d (recommended < 10)."
                    % (prop, len(val)),
                    UserWarning,
                    stacklevel=2,
                )
        except (KeyError, TypeError):
            pass


def _recommendation_checkers():
    """
    Return the list of (context_filter, checker_func) to run.
    checker_func(obj, context) may call warnings.warn().
    context is one of "figure", "trace", "layout".
    context_filter: set of contexts this checker applies to, or None for all.
    """
    return [
        ({"trace"}, _check_scatter_xy_length),
    ]


def run_recommendations(obj, context):
    """
    Run all recommendation checkers for the given object and context.
    Called internally after Figure/trace/Layout construction when
    recommendations mode is enabled.

    Parameters
    ----------
    obj : BaseFigure | BasePlotlyType
        The constructed figure, trace, or layout.
    context : str
        One of "figure", "trace", "layout".
    """
    if not config.enabled:
        return
    checkers = _recommendation_checkers()
    # For figures, run trace checkers on each trace (traces have props set by then)
    if context == "figure" and hasattr(obj, "data"):
        for trace in obj.data:
            for ctx_filter, checker in checkers:
                if ctx_filter is not None and "trace" not in ctx_filter:
                    continue
                try:
                    checker(trace, "trace")
                except Exception:
                    pass
    # Run checkers for this context
    for ctx_filter, checker in checkers:
        if ctx_filter is not None and context not in ctx_filter:
            continue
        try:
            checker(obj, context)
        except Exception:
            # Don't let a recommender break construction
            pass
