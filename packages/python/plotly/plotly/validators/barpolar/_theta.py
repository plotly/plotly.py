

import _plotly_utils.basevalidators as _bv


class ThetaValidator(_bv.DataArrayValidator):
    def __init__(self, plotly_name='theta',
                       parent_name='barpolar',
                       **kwargs):
        super(ThetaValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc+clearAxisTypes'),
        **kwargs)