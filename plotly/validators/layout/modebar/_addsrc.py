

import _plotly_utils.basevalidators as _bv


class AddsrcValidator(_bv.SrcValidator):
    def __init__(self, plotly_name='addsrc',
                       parent_name='layout.modebar',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'none'),
        **kwargs)