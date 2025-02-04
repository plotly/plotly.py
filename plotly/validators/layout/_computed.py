

import _plotly_utils.basevalidators as _bv


class ComputedValidator(_bv.AnyValidator):
    def __init__(self, plotly_name='computed',
                       parent_name='layout',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'none'),
        **kwargs)