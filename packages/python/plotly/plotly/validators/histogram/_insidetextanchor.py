

import _plotly_utils.basevalidators as _bv


class InsidetextanchorValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name='insidetextanchor',
                       parent_name='histogram',
                       **kwargs):
        super(InsidetextanchorValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'plot'),
                 values=kwargs.pop('values', ['end', 'middle', 'start']),
        **kwargs)