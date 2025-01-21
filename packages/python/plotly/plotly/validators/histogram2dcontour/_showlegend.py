

import _plotly_utils.basevalidators as _bv


class ShowlegendValidator(_bv.BooleanValidator):
    def __init__(self, plotly_name='showlegend',
                       parent_name='histogram2dcontour',
                       **kwargs):
        super(ShowlegendValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'style'),
        **kwargs)