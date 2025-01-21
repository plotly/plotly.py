

import _plotly_utils.basevalidators as _bv


class MinexponentValidator(_bv.NumberValidator):
    def __init__(self, plotly_name='minexponent',
                       parent_name='icicle.marker.colorbar',
                       **kwargs):
        super(MinexponentValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'colorbars'),
                 min=kwargs.pop('min', 0),
        **kwargs)