import _plotly_utils.basevalidators


class PaperBgcolorValidator(_plotly_utils.basevalidators.ColorValidator):

    def __init__(
        self, plotly_name='paper_bgcolor', parent_name='layout', **kwargs
    ):
        super(PaperBgcolorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='plot',
            role='style',
            **kwargs
        )
