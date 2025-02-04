

import _plotly_utils.basevalidators as _bv


class HoverlabelValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name='hoverlabel',
                       parent_name='pie',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'Hoverlabel'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)