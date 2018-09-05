import _plotly_utils.basevalidators


class UnselectedValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(
        self, plotly_name='unselected', parent_name='scattergeo', **kwargs
    ):
        super(UnselectedValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='Unselected',
            data_docs="""
            marker
                plotly.graph_objs.scattergeo.unselected.Marker
                instance or dict with compatible properties
            textfont
                plotly.graph_objs.scattergeo.unselected.Textfon
                t instance or dict with compatible properties
""",
            **kwargs
        )
