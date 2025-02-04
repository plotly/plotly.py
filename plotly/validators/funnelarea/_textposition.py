

import _plotly_utils.basevalidators as _bv


class TextpositionValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name='textposition',
                       parent_name='funnelarea',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 array_ok=kwargs.pop('array_ok', True),
                 edit_type=kwargs.pop('edit_type', 'plot'),
                 values=kwargs.pop('values', ['inside', 'none']),
        **kwargs)