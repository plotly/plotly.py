import _plotly_utils.basevalidators as _bv


class ConnectorValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name="connector", parent_name="waterfall", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            data_class_str=kwargs.pop("data_class_str", "Connector"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs,
        )
