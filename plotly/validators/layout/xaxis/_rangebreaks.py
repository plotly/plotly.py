

import _plotly_utils.basevalidators as _bv


class RangebreaksValidator(_bv.CompoundArrayValidator):
    def __init__(self, plotly_name='rangebreaks',
                       parent_name='layout.xaxis',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'Rangebreak'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)