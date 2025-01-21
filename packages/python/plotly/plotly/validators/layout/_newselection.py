

import _plotly_utils.basevalidators as _bv


class NewselectionValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name='newselection',
                       parent_name='layout',
                       **kwargs):
        super(NewselectionValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'Newselection'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)