

import _plotly_utils.basevalidators as _bv


class LValidator(_bv.NumberValidator):
    def __init__(self, plotly_name='l',
                       parent_name='layout.margin',
                       **kwargs):
        super(LValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'plot'),
                 min=kwargs.pop('min', 0),
        **kwargs)