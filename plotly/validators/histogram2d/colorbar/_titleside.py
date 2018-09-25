import _plotly_utils.basevalidators


class TitlesideValidator(_plotly_utils.basevalidators.EnumeratedValidator):

    def __init__(
        self,
        plotly_name='titleside',
        parent_name='histogram2d.colorbar',
        **kwargs
    ):
        super(TitlesideValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop('edit_type', 'colorbars'),
            role=kwargs.pop('role', 'style'),
            values=kwargs.pop('values', ['right', 'top', 'bottom']),
            **kwargs
        )
