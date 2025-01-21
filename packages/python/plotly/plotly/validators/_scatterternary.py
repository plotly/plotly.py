

import _plotly_utils.basevalidators as _bv


class ScatterternaryValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name='scatterternary',
                       parent_name='',
                       **kwargs):
        super(ScatterternaryValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'Scatterternary'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)