import _plotly_utils.basevalidators as _bv


class ContourValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name="contour", parent_name="volume", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            data_class_str=kwargs.pop("data_class_str", "Contour"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs,
        )
