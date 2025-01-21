

import _plotly_utils.basevalidators as _bv


class ColorscaleValidator(_bv.ColorscaleValidator):
    def __init__(self, plotly_name='colorscale',
                       parent_name='scatter3d.marker',
                       **kwargs):
        super(ColorscaleValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
                 implied_edits=kwargs.pop('implied_edits', {'autocolorscale': False}),
        **kwargs)