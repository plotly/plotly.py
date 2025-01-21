

import _plotly_utils.basevalidators as _bv


class TitleValidator(_bv.TitleValidator):
    def __init__(self, plotly_name='title',
                       parent_name='parcoords.line.colorbar',
                       **kwargs):
        super(TitleValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'Title'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)