

import _plotly_utils.basevalidators as _bv


class ChoroplethmapValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name='choroplethmap',
                       parent_name='',
                       **kwargs):
        super(ChoroplethmapValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'Choroplethmap'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)