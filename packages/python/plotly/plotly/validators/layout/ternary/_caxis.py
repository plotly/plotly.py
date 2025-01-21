

import _plotly_utils.basevalidators as _bv


class CaxisValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name='caxis',
                       parent_name='layout.ternary',
                       **kwargs):
        super(CaxisValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'Caxis'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)