

import _plotly_utils.basevalidators as _bv


class LabelsideValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name='labelside',
                       parent_name='parcoords',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'plot'),
                 values=kwargs.pop('values', ['top', 'bottom']),
        **kwargs)