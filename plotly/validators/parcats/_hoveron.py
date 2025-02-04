

import _plotly_utils.basevalidators as _bv


class HoveronValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name='hoveron',
                       parent_name='parcats',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'plot'),
                 values=kwargs.pop('values', ['category', 'color', 'dimension']),
        **kwargs)