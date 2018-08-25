import _plotly_utils.basevalidators


class NotchwidthValidator(_plotly_utils.basevalidators.NumberValidator):

    def __init__(self, plotly_name='notchwidth', parent_name='box', **kwargs):
        super(NotchwidthValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            max=0.5,
            min=0,
            role='style',
            **kwargs
        )
