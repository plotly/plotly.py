

import _plotly_utils.basevalidators as _bv


class ColorscaledefaultsValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name='colorscaledefaults',
                       parent_name='sankey.link',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'Colorscale'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)