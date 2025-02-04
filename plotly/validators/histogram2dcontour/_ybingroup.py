

import _plotly_utils.basevalidators as _bv


class YbingroupValidator(_bv.StringValidator):
    def __init__(self, plotly_name='ybingroup',
                       parent_name='histogram2dcontour',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
        **kwargs)