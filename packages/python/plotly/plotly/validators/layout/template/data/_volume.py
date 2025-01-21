

import _plotly_utils.basevalidators as _bv


class VolumeValidator(_bv.CompoundArrayValidator):
    def __init__(self, plotly_name='volume',
                       parent_name='layout.template.data',
                       **kwargs):
        super(VolumeValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'Volume'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)