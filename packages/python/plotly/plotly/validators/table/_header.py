

import _plotly_utils.basevalidators as _bv


class HeaderValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name='header',
                       parent_name='table',
                       **kwargs):
        super(HeaderValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'Header'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)