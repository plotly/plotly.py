

import _plotly_utils.basevalidators as _bv


class LegendgroupValidator(_bv.StringValidator):
    def __init__(self, plotly_name='legendgroup',
                       parent_name='scatterpolar',
                       **kwargs):
        super(LegendgroupValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'style'),
        **kwargs)