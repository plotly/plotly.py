

import _plotly_utils.basevalidators as _bv


class FunnelareaValidator(_bv.CompoundArrayValidator):
    def __init__(self, plotly_name='funnelarea',
                       parent_name='layout.template.data',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'Funnelarea'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)