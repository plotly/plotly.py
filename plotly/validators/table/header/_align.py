import _plotly_utils.basevalidators


class AlignValidator(_plotly_utils.basevalidators.EnumeratedValidator):

    def __init__(
        self, plotly_name='align', parent_name='table.header', **kwargs
    ):
        super(AlignValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=True,
            edit_type='calc',
            role='style',
            values=['left', 'center', 'right'],
            **kwargs
        )
