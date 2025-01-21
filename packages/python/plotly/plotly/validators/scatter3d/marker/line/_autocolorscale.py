

import _plotly_utils.basevalidators as _bv


class AutocolorscaleValidator(_bv.BooleanValidator):
    def __init__(self, plotly_name='autocolorscale',
                       parent_name='scatter3d.marker.line',
                       **kwargs):
        super(AutocolorscaleValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
                 implied_edits=kwargs.pop('implied_edits', {}),
        **kwargs)