import _plotly_utils.basevalidators


class UnselectedValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(
        self, plotly_name='unselected', parent_name='violin', **kwargs
    ):
        super(UnselectedValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str='Unselected',
            data_docs="""
            marker
                plotly.graph_objs.violin.unselected.Marker
                instance or dict with compatible properties
""",
            **kwargs
        )
