

import _plotly_utils.basevalidators as _bv


class SouthValidator(_bv.NumberValidator):
    def __init__(self, plotly_name='south',
                       parent_name='layout.map.bounds',
                       **kwargs):
        super(SouthValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'plot'),
        **kwargs)