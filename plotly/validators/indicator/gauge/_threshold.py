

import _plotly_utils.basevalidators as _bv


class ThresholdValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name='threshold',
                       parent_name='indicator.gauge',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'Threshold'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)