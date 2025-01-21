

import _plotly_utils.basevalidators as _bv


class SoliditysrcValidator(_bv.SrcValidator):
    def __init__(self, plotly_name='soliditysrc',
                       parent_name='histogram.marker.pattern',
                       **kwargs):
        super(SoliditysrcValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'none'),
        **kwargs)