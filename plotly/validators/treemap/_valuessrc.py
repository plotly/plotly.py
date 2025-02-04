

import _plotly_utils.basevalidators as _bv


class ValuessrcValidator(_bv.SrcValidator):
    def __init__(self, plotly_name='valuessrc',
                       parent_name='treemap',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'none'),
        **kwargs)