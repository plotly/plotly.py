

import _plotly_utils.basevalidators as _bv


class TicklenValidator(_bv.NumberValidator):
    def __init__(self, plotly_name='ticklen',
                       parent_name='layout.smith.realaxis',
                       **kwargs):
        super(TicklenValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'plot'),
                 min=kwargs.pop('min', 0),
        **kwargs)