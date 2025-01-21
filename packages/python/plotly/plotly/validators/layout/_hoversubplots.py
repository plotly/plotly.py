

import _plotly_utils.basevalidators as _bv


class HoversubplotsValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name='hoversubplots',
                       parent_name='layout',
                       **kwargs):
        super(HoversubplotsValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'none'),
                 values=kwargs.pop('values', ['single', 'overlaying', 'axis']),
        **kwargs)