

import _plotly_utils.basevalidators as _bv


class RotationValidator(_bv.AngleValidator):
    def __init__(self, plotly_name='rotation',
                       parent_name='pie',
                       **kwargs):
        super(RotationValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
        **kwargs)