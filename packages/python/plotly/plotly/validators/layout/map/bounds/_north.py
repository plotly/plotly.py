

import _plotly_utils.basevalidators as _bv


class NorthValidator(_bv.NumberValidator):
    def __init__(self, plotly_name='north',
                       parent_name='layout.map.bounds',
                       **kwargs):
        super(NorthValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'plot'),
        **kwargs)