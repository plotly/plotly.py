

import _plotly_utils.basevalidators as _bv


class CornerradiusValidator(_bv.AnyValidator):
    def __init__(self, plotly_name='cornerradius',
                       parent_name='bar.marker',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
        **kwargs)