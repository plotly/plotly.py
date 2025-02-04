

import _plotly_utils.basevalidators as _bv


class VsrcValidator(_bv.SrcValidator):
    def __init__(self, plotly_name='vsrc',
                       parent_name='cone',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'none'),
        **kwargs)