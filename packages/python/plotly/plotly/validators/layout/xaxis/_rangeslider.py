

import _plotly_utils.basevalidators as _bv


class RangesliderValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name='rangeslider',
                       parent_name='layout.xaxis',
                       **kwargs):
        super(RangesliderValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'Rangeslider'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)