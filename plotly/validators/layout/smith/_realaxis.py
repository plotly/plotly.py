

import _plotly_utils.basevalidators as _bv


class RealaxisValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name='realaxis',
                       parent_name='layout.smith',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'Realaxis'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)