

import _plotly_utils.basevalidators as _bv


class IsominValidator(_bv.NumberValidator):
    def __init__(self, plotly_name='isomin',
                       parent_name='volume',
                       **kwargs):
        super(IsominValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
        **kwargs)