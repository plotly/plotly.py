

import _plotly_utils.basevalidators as _bv


class DtickValidator(_bv.AnyValidator):
    def __init__(self, plotly_name='dtick',
                       parent_name='scatterpolargl.marker.colorbar',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
                 implied_edits=kwargs.pop('implied_edits', {'tickmode': 'linear'}),
        **kwargs)