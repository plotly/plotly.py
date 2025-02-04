

import _plotly_utils.basevalidators as _bv


class XrefValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name='xref',
                       parent_name='scatterpolargl.marker.colorbar',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
                 values=kwargs.pop('values', ['container', 'paper']),
        **kwargs)