

import _plotly_utils.basevalidators as _bv


class BorderpadValidator(_bv.NumberValidator):
    def __init__(self, plotly_name='borderpad',
                       parent_name='layout.scene.annotation',
                       **kwargs):
        super(BorderpadValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
                 min=kwargs.pop('min', 0),
        **kwargs)