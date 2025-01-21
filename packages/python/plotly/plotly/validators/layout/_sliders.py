

import _plotly_utils.basevalidators as _bv


class SlidersValidator(_bv.CompoundArrayValidator):
    def __init__(self, plotly_name='sliders',
                       parent_name='layout',
                       **kwargs):
        super(SlidersValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'Slider'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)