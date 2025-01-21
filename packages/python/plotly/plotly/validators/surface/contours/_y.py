

import _plotly_utils.basevalidators as _bv


class YValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name='y',
                       parent_name='surface.contours',
                       **kwargs):
        super(YValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'Y'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)