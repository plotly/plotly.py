

import _plotly_utils.basevalidators as _bv


class DatarevisionValidator(_bv.AnyValidator):
    def __init__(self, plotly_name='datarevision',
                       parent_name='layout',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
        **kwargs)