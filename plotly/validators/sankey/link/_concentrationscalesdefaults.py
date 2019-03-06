import _plotly_utils.basevalidators


class ConcentrationscalesValidator(
    _plotly_utils.basevalidators.CompoundValidator
):

    def __init__(
        self,
        plotly_name='concentrationscalesdefaults',
        parent_name='sankey.link',
        **kwargs
    ):
        super(ConcentrationscalesValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop('data_class_str', 'Concentrationscales'),
            data_docs=kwargs.pop('data_docs', """
"""),
            **kwargs
        )
