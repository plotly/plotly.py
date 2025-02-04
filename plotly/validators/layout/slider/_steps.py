

import _plotly_utils.basevalidators as _bv


class StepsValidator(_bv.CompoundArrayValidator):
    def __init__(self, plotly_name='steps',
                       parent_name='layout.slider',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'Step'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)