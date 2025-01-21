

import _plotly_utils.basevalidators as _bv


class MarginValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name='margin',
                       parent_name='layout',
                       **kwargs):
        super(MarginValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'Margin'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)