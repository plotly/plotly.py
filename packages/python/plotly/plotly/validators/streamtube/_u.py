

import _plotly_utils.basevalidators as _bv


class UValidator(_bv.DataArrayValidator):
    def __init__(self, plotly_name='u',
                       parent_name='streamtube',
                       **kwargs):
        super(UValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
        **kwargs)