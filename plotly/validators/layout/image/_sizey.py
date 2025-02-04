

import _plotly_utils.basevalidators as _bv


class SizeyValidator(_bv.NumberValidator):
    def __init__(self, plotly_name='sizey',
                       parent_name='layout.image',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'arraydraw'),
        **kwargs)