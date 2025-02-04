

import _plotly_utils.basevalidators as _bv


class DrValidator(_bv.NumberValidator):
    def __init__(self, plotly_name='dr',
                       parent_name='scatterpolargl',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
        **kwargs)