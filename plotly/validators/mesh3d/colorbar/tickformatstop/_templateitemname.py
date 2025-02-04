

import _plotly_utils.basevalidators as _bv


class TemplateitemnameValidator(_bv.StringValidator):
    def __init__(self, plotly_name='templateitemname',
                       parent_name='mesh3d.colorbar.tickformatstop',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'colorbars'),
        **kwargs)