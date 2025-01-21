

import _plotly_utils.basevalidators as _bv


class HovertemplatesrcValidator(_bv.SrcValidator):
    def __init__(self, plotly_name='hovertemplatesrc',
                       parent_name='scatter3d',
                       **kwargs):
        super(HovertemplatesrcValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'none'),
        **kwargs)