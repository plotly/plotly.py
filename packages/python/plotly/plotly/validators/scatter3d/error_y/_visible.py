

import _plotly_utils.basevalidators as _bv


class VisibleValidator(_bv.BooleanValidator):
    def __init__(self, plotly_name='visible',
                       parent_name='scatter3d.error_y',
                       **kwargs):
        super(VisibleValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
        **kwargs)