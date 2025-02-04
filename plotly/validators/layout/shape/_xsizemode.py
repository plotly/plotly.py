

import _plotly_utils.basevalidators as _bv


class XsizemodeValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name='xsizemode',
                       parent_name='layout.shape',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc+arraydraw'),
                 values=kwargs.pop('values', ['scaled', 'pixel']),
        **kwargs)