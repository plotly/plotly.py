

import _plotly_utils.basevalidators as _bv


class SizexValidator(_bv.NumberValidator):
    def __init__(self, plotly_name='sizex',
                       parent_name='layout.image',
                       **kwargs):
        super(SizexValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'arraydraw'),
        **kwargs)