

import _plotly_utils.basevalidators as _bv


class FillcolorValidator(_bv.ColorValidator):
    def __init__(self, plotly_name='fillcolor',
                       parent_name='violin',
                       **kwargs):
        super(FillcolorValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'style'),
        **kwargs)