import _plotly_utils.basevalidators


class TemplateValidator(_plotly_utils.basevalidators.AnyValidator):

    def __init__(self, plotly_name='template', parent_name='layout', **kwargs):
        super(TemplateValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            role='info',
            **kwargs
        )
