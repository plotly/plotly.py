

import _plotly_utils.basevalidators as _bv


class MinreducedheightValidator(_bv.NumberValidator):
    def __init__(self, plotly_name='minreducedheight',
                       parent_name='layout',
                       **kwargs):
        super(MinreducedheightValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'plot'),
                 min=kwargs.pop('min', 2),
        **kwargs)