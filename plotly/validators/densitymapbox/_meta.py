

import _plotly_utils.basevalidators as _bv


class MetaValidator(_bv.AnyValidator):
    def __init__(self, plotly_name='meta',
                       parent_name='densitymapbox',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 array_ok=kwargs.pop('array_ok', True),
                 edit_type=kwargs.pop('edit_type', 'plot'),
        **kwargs)