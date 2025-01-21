

import _plotly_utils.basevalidators as _bv


class FontValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name='font',
                       parent_name='ohlc.hoverlabel',
                       **kwargs):
        super(FontValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'Font'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)