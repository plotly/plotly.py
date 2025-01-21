

import _plotly_utils.basevalidators as _bv


class BaseValidator(_bv.AnyValidator):
    def __init__(self, plotly_name='base',
                       parent_name='bar',
                       **kwargs):
        super(BaseValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 array_ok=kwargs.pop('array_ok', True),
                 edit_type=kwargs.pop('edit_type', 'calc'),
        **kwargs)