

import _plotly_utils.basevalidators as _bv


class Copy_YstyleValidator(_bv.BooleanValidator):
    def __init__(self, plotly_name='copy_ystyle',
                       parent_name='bar.error_x',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'plot'),
        **kwargs)