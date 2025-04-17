import _plotly_utils.basevalidators as _bv


class ConeValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name="cone", parent_name="", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            data_class_str=kwargs.pop("data_class_str", "Cone"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs,
        )
