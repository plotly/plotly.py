

import _plotly_utils.basevalidators as _bv


class FillcolorValidator(_bv.ColorValidator):
    def __init__(self, plotly_name='fillcolor',
                       parent_name='scatter',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 anim=kwargs.pop('anim', True),
                 edit_type=kwargs.pop('edit_type', 'style'),
        **kwargs)