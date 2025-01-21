

import _plotly_utils.basevalidators as _bv


class BarpolarValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name='barpolar',
                       parent_name='',
                       **kwargs):
        super(BarpolarValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'Barpolar'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)