

import _plotly_utils.basevalidators as _bv


class Histogram2DValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name='histogram2d',
                       parent_name='',
                       **kwargs):
        super(Histogram2DValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'Histogram2d'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)