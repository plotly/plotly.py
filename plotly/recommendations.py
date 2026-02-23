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

from functools import partial
import inspect
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
# Property resolution (single place for "does this property exist")
# -----------------------------------------------------------------------------


def _targets(obj, context, prefix):
    """Yield each object (layout or trace) that this prefix applies to."""
    if context == "figure":
        if prefix == "layout" and hasattr(obj, "layout"):
            yield obj.layout
        if hasattr(obj, "data"):
            for t in obj.data:
                if prefix == "trace" or getattr(t, "plotly_name", None) == prefix:
                    yield t
    elif (context == "trace" or context == "layout") and (
        prefix == "trace" or prefix == "layout" or getattr(obj, "plotly_name", None) == prefix
    ):
        yield obj


def _get_stacklevel():
    """Find the first frame outside the plotly package so the warning points at user code."""
    plotly_dir = os.path.abspath(os.path.dirname(__file__))
    stack = inspect.stack()
    for i, frame in enumerate(stack):
        try:
            frame_path = os.path.abspath(frame.filename)
        except (AttributeError, TypeError):
            frame_path = getattr(frame, "filename", "") or ""
        if not frame_path.startswith(plotly_dir):
            break
    else:
        i = len(stack) - 1
    return i


def _is_empty(obj):
    """
    Quick check if the object has no values assigned yet (e.g. just constructed).
    Figure: no traces. Trace/layout: no properties in _props.
    """
    if hasattr(obj, "_data"):
        return len(obj._data) == 0
    if hasattr(obj, "_props"):
        props = obj._props
        return props is None or len(props) == 0
    return False


def _get_value(whole_obj, path, context):
    """
    Resolve a full path (e.g. "scatter.x", "layout.title.text") from the whole
    object (figure, or current trace/layout). Returns a list of values, one per
    applicable target; missing properties yield None.
    """
    prefix, suffix = path.split(".", 1) if "." in path else (path, "")
    result = []
    for target in _targets(whole_obj, context, prefix):
        if not suffix:
            result.append(target)
            continue
        try:
            v = target
            for p in suffix.split("."):
                v = v[p]
            result.append(v)
        except (KeyError, TypeError, AttributeError):
            result.append(None)
    return result


# -----------------------------------------------------------------------------
# Recommendation checkers (extensible list)
# -----------------------------------------------------------------------------


def max_length(input_list, max_length):
    """
    Check if input_list has length >= max_length (e.g. recommended to keep shorter).
    Returns a string describing the issue, or None if no issue was found.
    """
    if input_list is not None and hasattr(input_list, "__len__") and len(input_list) >= max_length:
        return f"has length {len(input_list)} (recommended <= {max_length})."
    return None


def _recommendation_checkers():
    """
    Return the list of (path_def, checker_func).

    path_def: a dot-separated path string (e.g. "scatter.x") or list of same.
    checker_func: called with one value per path (or None if missing). Returns
        an issue string to warn about, or None.
    """
    return [
        ("scatter.x", partial(max_length, max_length=1000)),
        ("scatter.y", partial(max_length, max_length=1000)),
    ]


def run_recommendations(obj, context):
    """
    Run all recommendation checkers for the given object and context.
    Called internally after Figure/trace/Layout construction when
    recommendations mode is enabled.

    Property resolution is done here: for each checker we resolve the
    path(s) on the applicable object(s), pass the values (or None) to the
    checker, and catch exceptions so one checker cannot break others.

    Parameters
    ----------
    obj : BaseFigure | BasePlotlyType
        The constructed figure, trace, or layout.
    context : str
        One of "figure", "trace", "layout".
    """

    if (not config.enabled) or _is_empty(obj):
        return

    checkers = _recommendation_checkers()
    stacklevel = 0

    for path_def, checker in checkers:
        if not path_def:
            continue
        paths = [path_def] if isinstance(path_def, str) else path_def
        value_lists = [_get_value(obj, p, context) for p in paths]
        try:
            for value_tuple in zip(*value_lists):
                issue = checker(*value_tuple)
                if issue:
                    stacklevel = stacklevel or _get_stacklevel()
                    warnings.warn(
                        f"{path_def}: {issue}",
                        UserWarning,
                        stacklevel=stacklevel,
                    )
        except Exception:
            pass

