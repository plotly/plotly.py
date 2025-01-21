

import plotly.validators as _bv


class DataValidator(_bv.DataValidator):
    def __init__(self, plotly_name='data',
                       parent_name='frame',
                       **kwargs):
        super(DataValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
        **kwargs)