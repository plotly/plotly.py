

import _plotly_utils.basevalidators as _bv


class BsrcValidator(_bv.SrcValidator):
    def __init__(self, plotly_name='bsrc',
                       parent_name='contourcarpet',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'none'),
        **kwargs)