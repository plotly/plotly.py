

import _plotly_utils.basevalidators as _bv


class StopValidator(_bv.NumberValidator):
    def __init__(self, plotly_name='stop',
                       parent_name='scatter.fillgradient',
                       **kwargs):
        super(StopValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
        **kwargs)