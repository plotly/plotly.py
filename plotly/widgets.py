from __future__ import absolute_import

from _plotly_future_ import _future_flags


if 'remove_deprecations' not in _future_flags:
    from _plotly_future_ import _chart_studio_warning
    _chart_studio_warning('widgets')
    from chart_studio.widgets import *
