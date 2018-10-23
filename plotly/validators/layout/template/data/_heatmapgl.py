import _plotly_utils.basevalidators


class HeatmapglsValidator(_plotly_utils.basevalidators.CompoundArrayValidator):

    def __init__(
        self,
        plotly_name='heatmapgl',
        parent_name='layout.template.data',
        **kwargs
    ):
        super(HeatmapglsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop('data_class_str', 'Heatmapgl'),
            data_docs=kwargs.pop('data_docs', """
"""),
            **kwargs
        )
