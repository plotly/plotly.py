

import _plotly_utils.basevalidators as _bv


class SpanmodeValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name='spanmode',
                       parent_name='violin',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
                 values=kwargs.pop('values', ['soft', 'hard', 'manual']),
        **kwargs)