

import _plotly_utils.basevalidators as _bv


class ReferenceValidator(_bv.NumberValidator):
    def __init__(self, plotly_name='reference',
                       parent_name='indicator.delta',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
        **kwargs)