

import _plotly_utils.basevalidators as _bv


class SpikethicknessValidator(_bv.NumberValidator):
    def __init__(self, plotly_name='spikethickness',
                       parent_name='layout.scene.xaxis',
                       **kwargs):
        super(SpikethicknessValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'plot'),
                 min=kwargs.pop('min', 0),
        **kwargs)