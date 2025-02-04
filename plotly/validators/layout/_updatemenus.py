

import _plotly_utils.basevalidators as _bv


class UpdatemenusValidator(_bv.CompoundArrayValidator):
    def __init__(self, plotly_name='updatemenus',
                       parent_name='layout',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'Updatemenu'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)