

import _plotly_utils.basevalidators as _bv


class LayersValidator(_bv.CompoundArrayValidator):
    def __init__(self, plotly_name='layers',
                       parent_name='layout.map',
                       **kwargs):
        super(LayersValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'Layer'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)