

import _plotly_utils.basevalidators as _bv


class CategoryarraysrcValidator(_bv.SrcValidator):
    def __init__(self, plotly_name='categoryarraysrc',
                       parent_name='carpet.baxis',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'none'),
        **kwargs)