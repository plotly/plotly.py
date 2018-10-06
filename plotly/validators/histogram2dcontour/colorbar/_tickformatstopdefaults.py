import _plotly_utils.basevalidators


class TickformatstopValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(
        self,
        plotly_name='tickformatstopdefaults',
        parent_name='histogram2dcontour.colorbar',
        **kwargs
    ):
        super(TickformatstopValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop('data_class_str', 'Tickformatstop'),
            data_docs=kwargs.pop('data_docs', """
"""),
            **kwargs
        )
