

import _plotly_utils.basevalidators as _bv


class ShowoceanValidator(_bv.BooleanValidator):
    def __init__(self, plotly_name='showocean',
                       parent_name='layout.geo',
                       **kwargs):
        super(ShowoceanValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'plot'),
        **kwargs)