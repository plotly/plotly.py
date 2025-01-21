

import _plotly_utils.basevalidators as _bv


class ZaxisValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name='zaxis',
                       parent_name='layout.scene',
                       **kwargs):
        super(ZaxisValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'ZAxis'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)