import _plotly_utils.basevalidators as _bv


class LightingValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name="lighting", parent_name="streamtube", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            data_class_str=kwargs.pop("data_class_str", "Lighting"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs,
        )
