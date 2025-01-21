

import _plotly_utils.basevalidators as _bv


class XValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name='x',
                       parent_name='volume.slices',
                       **kwargs):
        super(XValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'X'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)