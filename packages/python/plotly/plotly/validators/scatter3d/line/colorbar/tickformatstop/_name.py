

import _plotly_utils.basevalidators as _bv


class NameValidator(_bv.StringValidator):
    def __init__(self, plotly_name='name',
                       parent_name='scatter3d.line.colorbar.tickformatstop',
                       **kwargs):
        super(NameValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
        **kwargs)