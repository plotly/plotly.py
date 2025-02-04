

import _plotly_utils.basevalidators as _bv


class ColorscalesValidator(_bv.CompoundArrayValidator):
    def __init__(self, plotly_name='colorscales',
                       parent_name='sankey.link',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'Colorscale'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)