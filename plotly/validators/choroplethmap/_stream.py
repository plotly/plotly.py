import _plotly_utils.basevalidators as _bv


class StreamValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name="stream", parent_name="choroplethmap", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            data_class_str=kwargs.pop("data_class_str", "Stream"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs,
        )
