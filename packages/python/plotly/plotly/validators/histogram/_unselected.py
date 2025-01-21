

import _plotly_utils.basevalidators as _bv


class UnselectedValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name='unselected',
                       parent_name='histogram',
                       **kwargs):
        super(UnselectedValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'Unselected'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)