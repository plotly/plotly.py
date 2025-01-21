

import _plotly_utils.basevalidators as _bv


class NotchspanValidator(_bv.DataArrayValidator):
    def __init__(self, plotly_name='notchspan',
                       parent_name='box',
                       **kwargs):
        super(NotchspanValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
        **kwargs)