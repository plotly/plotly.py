

import _plotly_utils.basevalidators as _bv


class AllowoverlapValidator(_bv.BooleanValidator):
    def __init__(self, plotly_name='allowoverlap',
                       parent_name='scattermap.marker',
                       **kwargs):
        super(AllowoverlapValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
        **kwargs)