

import _plotly_utils.basevalidators as _bv


class Q3SrcValidator(_bv.SrcValidator):
    def __init__(self, plotly_name='q3src',
                       parent_name='box',
                       **kwargs):
        super(Q3SrcValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'none'),
        **kwargs)