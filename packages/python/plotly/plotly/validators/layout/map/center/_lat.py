

import _plotly_utils.basevalidators as _bv


class LatValidator(_bv.NumberValidator):
    def __init__(self, plotly_name='lat',
                       parent_name='layout.map.center',
                       **kwargs):
        super(LatValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'plot'),
        **kwargs)