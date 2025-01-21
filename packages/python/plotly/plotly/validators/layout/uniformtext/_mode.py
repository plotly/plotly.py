

import _plotly_utils.basevalidators as _bv


class ModeValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name='mode',
                       parent_name='layout.uniformtext',
                       **kwargs):
        super(ModeValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'plot'),
                 values=kwargs.pop('values', [False, 'hide', 'show']),
        **kwargs)