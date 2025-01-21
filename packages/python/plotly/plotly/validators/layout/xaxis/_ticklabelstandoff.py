

import _plotly_utils.basevalidators as _bv


class TicklabelstandoffValidator(_bv.IntegerValidator):
    def __init__(self, plotly_name='ticklabelstandoff',
                       parent_name='layout.xaxis',
                       **kwargs):
        super(TicklabelstandoffValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'ticks'),
        **kwargs)