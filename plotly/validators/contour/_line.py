import _plotly_utils.basevalidators as _bv


class LineValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name="line", parent_name="contour", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            data_class_str=kwargs.pop("data_class_str", "Line"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs,
        )
