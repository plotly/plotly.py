import _plotly_utils.basevalidators as _bv


class LightpositionValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name="lightposition", parent_name="surface", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            data_class_str=kwargs.pop("data_class_str", "Lightposition"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs,
        )
