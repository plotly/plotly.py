

import _plotly_utils.basevalidators as _bv


class TemplateValidator(_bv.BaseTemplateValidator):
    def __init__(self, plotly_name='template',
                       parent_name='layout',
                       **kwargs):
        super(TemplateValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'Template'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)