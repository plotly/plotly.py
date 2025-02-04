

import _plotly_utils.basevalidators as _bv


class LayoutValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name='layout',
                       parent_name='layout.template',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'Layout'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)