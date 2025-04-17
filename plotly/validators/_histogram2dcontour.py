import _plotly_utils.basevalidators as _bv


class Histogram2DcontourValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name="histogram2dcontour", parent_name="", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            data_class_str=kwargs.pop("data_class_str", "Histogram2dContour"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs,
        )
