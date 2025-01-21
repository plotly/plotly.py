

import _plotly_utils.basevalidators as _bv


class PadValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name='pad',
                       parent_name='layout.updatemenu',
                       **kwargs):
        super(PadValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'Pad'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)