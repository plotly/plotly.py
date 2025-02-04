

import _plotly_utils.basevalidators as _bv


class ShowactiveValidator(_bv.BooleanValidator):
    def __init__(self, plotly_name='showactive',
                       parent_name='layout.updatemenu',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'arraydraw'),
        **kwargs)