

import _plotly_utils.basevalidators as _bv


class SequentialminusValidator(_bv.ColorscaleValidator):
    def __init__(self, plotly_name='sequentialminus',
                       parent_name='layout.colorscale',
                       **kwargs):
        super(SequentialminusValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
        **kwargs)