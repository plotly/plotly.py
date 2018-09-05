import _plotly_utils.basevalidators


class UnselectedValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(
        self, plotly_name='unselected', parent_name='scatterpolar', **kwargs
    ):
        super(UnselectedValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='Unselected',
            data_docs="""
            marker
                plotly.graph_objs.scatterpolar.unselected.Marke
                r instance or dict with compatible properties
            textfont
                plotly.graph_objs.scatterpolar.unselected.Textf
                ont instance or dict with compatible properties
""",
            **kwargs
        )
