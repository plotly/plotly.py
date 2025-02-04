

import _plotly_utils.basevalidators as _bv


class HovermodeValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name='hovermode',
                       parent_name='layout',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'modebar'),
                 values=kwargs.pop('values', ['x', 'y', 'closest', False, 'x unified', 'y unified']),
        **kwargs)