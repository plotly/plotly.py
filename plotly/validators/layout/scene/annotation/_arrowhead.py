

import _plotly_utils.basevalidators as _bv


class ArrowheadValidator(_bv.IntegerValidator):
    def __init__(self, plotly_name='arrowhead',
                       parent_name='layout.scene.annotation',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
                 max=kwargs.pop('max', 8),
                 min=kwargs.pop('min', 0),
        **kwargs)