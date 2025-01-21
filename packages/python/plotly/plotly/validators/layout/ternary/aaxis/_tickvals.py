

import _plotly_utils.basevalidators as _bv


class TickvalsValidator(_bv.DataArrayValidator):
    def __init__(self, plotly_name='tickvals',
                       parent_name='layout.ternary.aaxis',
                       **kwargs):
        super(TickvalsValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'plot'),
        **kwargs)