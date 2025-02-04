

import _plotly_utils.basevalidators as _bv


class DividercolorValidator(_bv.ColorValidator):
    def __init__(self, plotly_name='dividercolor',
                       parent_name='layout.xaxis',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'ticks'),
        **kwargs)