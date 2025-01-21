

import _plotly_utils.basevalidators as _bv


class NbinsyValidator(_bv.IntegerValidator):
    def __init__(self, plotly_name='nbinsy',
                       parent_name='histogram2d',
                       **kwargs):
        super(NbinsyValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
                 min=kwargs.pop('min', 0),
        **kwargs)