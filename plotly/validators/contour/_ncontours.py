import _plotly_utils.basevalidators


class NcontoursValidator(_plotly_utils.basevalidators.IntegerValidator):

    def __init__(
        self, plotly_name='ncontours', parent_name='contour', **kwargs
    ):
        super(NcontoursValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            min=1,
            role='style',
            **kwargs
        )
