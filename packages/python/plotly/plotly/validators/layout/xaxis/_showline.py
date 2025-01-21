

import _plotly_utils.basevalidators as _bv


class ShowlineValidator(_bv.BooleanValidator):
    def __init__(self, plotly_name='showline',
                       parent_name='layout.xaxis',
                       **kwargs):
        super(ShowlineValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'ticks+layoutstyle'),
        **kwargs)