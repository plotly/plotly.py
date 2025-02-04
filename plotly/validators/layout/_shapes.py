

import _plotly_utils.basevalidators as _bv


class ShapesValidator(_bv.CompoundArrayValidator):
    def __init__(self, plotly_name='shapes',
                       parent_name='layout',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'Shape'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)