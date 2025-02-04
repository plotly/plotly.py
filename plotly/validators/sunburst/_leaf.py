

import _plotly_utils.basevalidators as _bv


class LeafValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name='leaf',
                       parent_name='sunburst',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'Leaf'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)