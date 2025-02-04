

import _plotly_utils.basevalidators as _bv


class StartarrowheadValidator(_bv.IntegerValidator):
    def __init__(self, plotly_name='startarrowhead',
                       parent_name='layout.annotation',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'arraydraw'),
                 max=kwargs.pop('max', 8),
                 min=kwargs.pop('min', 0),
        **kwargs)