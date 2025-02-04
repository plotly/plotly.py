

import _plotly_utils.basevalidators as _bv


class PrefixValidator(_bv.StringValidator):
    def __init__(self, plotly_name='prefix',
                       parent_name='table.header',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 array_ok=kwargs.pop('array_ok', True),
                 edit_type=kwargs.pop('edit_type', 'calc'),
        **kwargs)