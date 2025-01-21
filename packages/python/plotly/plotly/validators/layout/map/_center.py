

import _plotly_utils.basevalidators as _bv


class CenterValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name='center',
                       parent_name='layout.map',
                       **kwargs):
        super(CenterValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'Center'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)