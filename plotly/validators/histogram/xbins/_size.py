

import _plotly_utils.basevalidators as _bv


class SizeValidator(_bv.AnyValidator):
    def __init__(self, plotly_name='size',
                       parent_name='histogram.xbins',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
        **kwargs)