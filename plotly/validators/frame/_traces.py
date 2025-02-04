

import _plotly_utils.basevalidators as _bv


class TracesValidator(_bv.AnyValidator):
    def __init__(self, plotly_name='traces',
                       parent_name='frame',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
        **kwargs)