

import _plotly_utils.basevalidators as _bv


class ModebarValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name='modebar',
                       parent_name='layout',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'Modebar'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)