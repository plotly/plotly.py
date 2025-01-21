

import _plotly_utils.basevalidators as _bv


class Error_YValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name='error_y',
                       parent_name='bar',
                       **kwargs):
        super(Error_YValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'ErrorY'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)