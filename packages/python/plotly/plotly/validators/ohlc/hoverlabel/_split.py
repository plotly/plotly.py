

import _plotly_utils.basevalidators as _bv


class SplitValidator(_bv.BooleanValidator):
    def __init__(self, plotly_name='split',
                       parent_name='ohlc.hoverlabel',
                       **kwargs):
        super(SplitValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'style'),
        **kwargs)