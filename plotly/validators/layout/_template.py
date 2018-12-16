import _plotly_utils.basevalidators


class TemplateValidator(_plotly_utils.basevalidators.BaseTemplateValidator):

    def __init__(self, plotly_name='template', parent_name='layout', **kwargs):
        super(TemplateValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop('data_class_str', 'Template'),
            data_docs=kwargs.pop(
                'data_docs', """
            data
                plotly.graph_objs.layout.template.Data instance
                or dict with compatible properties
            layout
                plotly.graph_objs.layout.template.Layout
                instance or dict with compatible properties
"""
            ),
            **kwargs
        )
