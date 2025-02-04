

import _plotly_utils.basevalidators as _bv


class WidthsrcValidator(_bv.SrcValidator):
    def __init__(self, plotly_name='widthsrc',
                       parent_name='barpolar.marker.line',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'none'),
        **kwargs)