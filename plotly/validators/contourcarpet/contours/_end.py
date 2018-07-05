import _plotly_utils.basevalidators


class EndValidator(_plotly_utils.basevalidators.NumberValidator):

    def __init__(
        self,
        plotly_name='end',
        parent_name='contourcarpet.contours',
        **kwargs
    ):
        super(EndValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='plot',
            implied_edits={'^autocontour': False},
            role='style',
            **kwargs
        )
