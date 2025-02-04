

import _plotly_utils.basevalidators as _bv


class FontValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name='font',
                       parent_name='histogram2d.colorbar.title',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'Font'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)