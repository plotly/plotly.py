import _plotly_utils.basevalidators as _bv


class DimensionsValidator(_bv.CompoundArrayValidator):
    def __init__(self, plotly_name="dimensions", parent_name="parcoords", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            data_class_str=kwargs.pop("data_class_str", "Dimension"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs,
        )
