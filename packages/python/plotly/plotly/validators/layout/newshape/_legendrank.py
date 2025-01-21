

import _plotly_utils.basevalidators as _bv


class LegendrankValidator(_bv.NumberValidator):
    def __init__(self, plotly_name='legendrank',
                       parent_name='layout.newshape',
                       **kwargs):
        super(LegendrankValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'none'),
        **kwargs)