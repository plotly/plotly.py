

import _plotly_utils.basevalidators as _bv


class ZsrcValidator(_bv.SrcValidator):
    def __init__(self, plotly_name='zsrc',
                       parent_name='contour',
                       **kwargs):
        super(ZsrcValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'none'),
        **kwargs)