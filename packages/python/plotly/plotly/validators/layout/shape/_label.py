

import _plotly_utils.basevalidators as _bv


class LabelValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name='label',
                       parent_name='layout.shape',
                       **kwargs):
        super(LabelValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'Label'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)