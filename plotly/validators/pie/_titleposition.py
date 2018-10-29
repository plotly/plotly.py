import _plotly_utils.basevalidators


class TitlepositionValidator(_plotly_utils.basevalidators.EnumeratedValidator):

    def __init__(
        self, plotly_name='titleposition', parent_name='pie', **kwargs
    ):
        super(TitlepositionValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop('edit_type', 'calc'),
            role=kwargs.pop('role', 'info'),
            values=kwargs.pop(
                'values', [
                    'top left', 'top center', 'top right', 'middle center',
                    'bottom left', 'bottom center', 'bottom right'
                ]
            ),
            **kwargs
        )
