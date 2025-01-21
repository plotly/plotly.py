

import _plotly_utils.basevalidators as _bv


class TiltValidator(_bv.NumberValidator):
    def __init__(self, plotly_name='tilt',
                       parent_name='layout.geo.projection',
                       **kwargs):
        super(TiltValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'plot'),
        **kwargs)