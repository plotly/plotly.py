import _plotly_utils.basevalidators


class LayersValidator(_plotly_utils.basevalidators.CompoundValidator):
    def __init__(self, plotly_name="layers", parent_name="layout.mapbox", **kwargs):
        super(LayersValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop("data_class_str", "Layers"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs
        )
