import _plotly_utils.basevalidators


class UpdatemenuValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(
        self, plotly_name='updatemenudefaults', parent_name='layout', **kwargs
    ):
        super(UpdatemenuValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop('data_class_str', 'Updatemenu'),
            data_docs=kwargs.pop('data_docs', """
"""),
            **kwargs
        )
