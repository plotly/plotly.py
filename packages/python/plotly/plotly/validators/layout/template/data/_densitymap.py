

import _plotly_utils.basevalidators as _bv


class DensitymapValidator(_bv.CompoundArrayValidator):
    def __init__(self, plotly_name='densitymap',
                       parent_name='layout.template.data',
                       **kwargs):
        super(DensitymapValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'Densitymap'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)