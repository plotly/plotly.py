import _plotly_utils.basevalidators as _bv


class AxisValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name="axis", parent_name="splom.dimension", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            data_class_str=kwargs.pop("data_class_str", "Axis"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs,
        )
