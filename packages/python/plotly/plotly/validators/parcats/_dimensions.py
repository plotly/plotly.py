

import _plotly_utils.basevalidators as _bv


class DimensionsValidator(_bv.CompoundArrayValidator):
    def __init__(self, plotly_name='dimensions',
                       parent_name='parcats',
                       **kwargs):
        super(DimensionsValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'Dimension'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)