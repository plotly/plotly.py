

import _plotly_utils.basevalidators as _bv


class AngularaxisValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name='angularaxis',
                       parent_name='layout.polar',
                       **kwargs):
        super(AngularaxisValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'AngularAxis'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)