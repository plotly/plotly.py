import _plotly_utils.basevalidators


class BoxgapValidator(_plotly_utils.basevalidators.NumberValidator):

    def __init__(self, plotly_name='boxgap', parent_name='layout', **kwargs):
        super(BoxgapValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            max=1,
            min=0,
            role='style',
            **kwargs
        )
