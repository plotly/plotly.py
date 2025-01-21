

import _plotly_utils.basevalidators as _bv


class AxValidator(_bv.AnyValidator):
    def __init__(self, plotly_name='ax',
                       parent_name='layout.annotation',
                       **kwargs):
        super(AxValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc+arraydraw'),
        **kwargs)