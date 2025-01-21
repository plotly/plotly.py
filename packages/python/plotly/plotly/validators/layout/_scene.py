

import _plotly_utils.basevalidators as _bv


class SceneValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name='scene',
                       parent_name='layout',
                       **kwargs):
        super(SceneValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'Scene'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)