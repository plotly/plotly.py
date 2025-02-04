

import _plotly_utils.basevalidators as _bv


class OutlierwidthValidator(_bv.NumberValidator):
    def __init__(self, plotly_name='outlierwidth',
                       parent_name='violin.marker.line',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'style'),
                 min=kwargs.pop('min', 0),
        **kwargs)