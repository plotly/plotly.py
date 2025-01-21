

import _plotly_utils.basevalidators as _bv


class DomainValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name='domain',
                       parent_name='table',
                       **kwargs):
        super(DomainValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'Domain'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)