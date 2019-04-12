from _plotly_utils.files import *

# Deprecations
from _plotly_future_ import _future_flags
if 'remove_deprecations' not in _future_flags:
    from chart_studio.files import *
