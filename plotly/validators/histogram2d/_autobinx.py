

import _plotly_utils.basevalidators as _bv


class AutobinxValidator(_bv.BooleanValidator):
    def __init__(self, plotly_name='autobinx',
                       parent_name='histogram2d',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
        **kwargs)