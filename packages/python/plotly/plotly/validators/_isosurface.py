

import _plotly_utils.basevalidators as _bv


class IsosurfaceValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name='isosurface',
                       parent_name='',
                       **kwargs):
        super(IsosurfaceValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'Isosurface'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)