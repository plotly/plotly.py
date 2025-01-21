

import _plotly_utils.basevalidators as _bv


class LightpositionValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name='lightposition',
                       parent_name='mesh3d',
                       **kwargs):
        super(LightpositionValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'Lightposition'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)