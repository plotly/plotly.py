

import _plotly_utils.basevalidators as _bv


class YperiodValidator(_bv.AnyValidator):
    def __init__(self, plotly_name='yperiod',
                       parent_name='contour',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
                 implied_edits=kwargs.pop('implied_edits', {'ytype': 'scaled'}),
        **kwargs)