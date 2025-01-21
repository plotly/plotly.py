

import _plotly_utils.basevalidators as _bv


class WValidator(_bv.DataArrayValidator):
    def __init__(self, plotly_name='w',
                       parent_name='streamtube',
                       **kwargs):
        super(WValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
        **kwargs)