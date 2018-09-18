import _plotly_utils.basevalidators


class TextinfoValidator(_plotly_utils.basevalidators.FlaglistValidator):

    def __init__(self, plotly_name='textinfo', parent_name='pie', **kwargs):
        super(TextinfoValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            extras=['none'],
            flags=['label', 'text', 'value', 'percent'],
            role='info',
            **kwargs
        )
