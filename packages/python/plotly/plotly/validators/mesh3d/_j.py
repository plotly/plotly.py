

import _plotly_utils.basevalidators as _bv


class JValidator(_bv.DataArrayValidator):
    def __init__(self, plotly_name='j',
                       parent_name='mesh3d',
                       **kwargs):
        super(JValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
        **kwargs)