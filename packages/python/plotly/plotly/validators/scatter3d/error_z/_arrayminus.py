

import _plotly_utils.basevalidators as _bv


class ArrayminusValidator(_bv.DataArrayValidator):
    def __init__(self, plotly_name='arrayminus',
                       parent_name='scatter3d.error_z',
                       **kwargs):
        super(ArrayminusValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
        **kwargs)