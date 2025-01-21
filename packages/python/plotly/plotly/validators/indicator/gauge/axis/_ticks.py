

import _plotly_utils.basevalidators as _bv


class TicksValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name='ticks',
                       parent_name='indicator.gauge.axis',
                       **kwargs):
        super(TicksValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'plot'),
                 values=kwargs.pop('values', ['outside', 'inside', '']),
        **kwargs)