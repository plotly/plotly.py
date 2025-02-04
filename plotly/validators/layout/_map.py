

import _plotly_utils.basevalidators as _bv


class MapValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name='map',
                       parent_name='layout',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'Map'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)