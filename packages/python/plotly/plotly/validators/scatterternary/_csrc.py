

import _plotly_utils.basevalidators as _bv


class CsrcValidator(_bv.SrcValidator):
    def __init__(self, plotly_name='csrc',
                       parent_name='scatterternary',
                       **kwargs):
        super(CsrcValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'none'),
        **kwargs)