

import _plotly_utils.basevalidators as _bv


class CoastlinecolorValidator(_bv.ColorValidator):
    def __init__(self, plotly_name='coastlinecolor',
                       parent_name='layout.geo',
                       **kwargs):
        super(CoastlinecolorValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'plot'),
        **kwargs)