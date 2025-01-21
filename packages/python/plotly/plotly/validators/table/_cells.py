

import _plotly_utils.basevalidators as _bv


class CellsValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name='cells',
                       parent_name='table',
                       **kwargs):
        super(CellsValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'Cells'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)