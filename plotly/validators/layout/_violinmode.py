

import _plotly_utils.basevalidators as _bv


class ViolinmodeValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name='violinmode',
                       parent_name='layout',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
                 values=kwargs.pop('values', ['group', 'overlay']),
        **kwargs)