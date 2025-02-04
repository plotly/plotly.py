

import _plotly_utils.basevalidators as _bv


class ZhoverformatValidator(_bv.StringValidator):
    def __init__(self, plotly_name='zhoverformat',
                       parent_name='histogram2d',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'none'),
        **kwargs)