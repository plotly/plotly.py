

import _plotly_utils.basevalidators as _bv


class ColorValidator(_bv.ColorValidator):
    def __init__(self, plotly_name='color',
                       parent_name='layout.shape.line',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 anim=kwargs.pop('anim', True),
                 edit_type=kwargs.pop('edit_type', 'arraydraw'),
        **kwargs)