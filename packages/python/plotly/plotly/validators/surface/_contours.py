

import _plotly_utils.basevalidators as _bv


class ContoursValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name='contours',
                       parent_name='surface',
                       **kwargs):
        super(ContoursValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'Contours'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)