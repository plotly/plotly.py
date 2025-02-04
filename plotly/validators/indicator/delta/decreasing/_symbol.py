

import _plotly_utils.basevalidators as _bv


class SymbolValidator(_bv.StringValidator):
    def __init__(self, plotly_name='symbol',
                       parent_name='indicator.delta.decreasing',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'plot'),
        **kwargs)