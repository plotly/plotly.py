

import _plotly_utils.basevalidators as _bv


class ScattercarpetValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name='scattercarpet',
                       parent_name='',
                       **kwargs):
        super(ScattercarpetValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'Scattercarpet'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)