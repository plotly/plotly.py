

import _plotly_utils.basevalidators as _bv


class RadialaxisValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name='radialaxis',
                       parent_name='layout.polar',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'RadialAxis'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)