

import _plotly_utils.basevalidators as _bv


class RotationValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name='rotation',
                       parent_name='layout.geo.projection',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'Rotation'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)