

import _plotly_utils.basevalidators as _bv


class OutlinecolorValidator(_bv.ColorValidator):
    def __init__(self, plotly_name='outlinecolor',
                       parent_name='scattermapbox.marker.colorbar',
                       **kwargs):
        super(OutlinecolorValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
        **kwargs)