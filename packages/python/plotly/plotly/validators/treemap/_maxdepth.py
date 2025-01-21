

import _plotly_utils.basevalidators as _bv


class MaxdepthValidator(_bv.IntegerValidator):
    def __init__(self, plotly_name='maxdepth',
                       parent_name='treemap',
                       **kwargs):
        super(MaxdepthValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'plot'),
        **kwargs)