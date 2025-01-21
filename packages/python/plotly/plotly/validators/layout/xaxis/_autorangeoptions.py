

import _plotly_utils.basevalidators as _bv


class AutorangeoptionsValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name='autorangeoptions',
                       parent_name='layout.xaxis',
                       **kwargs):
        super(AutorangeoptionsValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'Autorangeoptions'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)