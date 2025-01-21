

import _plotly_utils.basevalidators as _bv


class CapsValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name='caps',
                       parent_name='isosurface',
                       **kwargs):
        super(CapsValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'Caps'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)