

import _plotly_utils.basevalidators as _bv


class SurfaceValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name='surface',
                       parent_name='volume',
                       **kwargs):
        super(SurfaceValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'Surface'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)