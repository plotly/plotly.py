import _plotly_utils.basevalidators as _bv


class ShapedefaultsValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name="shapedefaults", parent_name="layout", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            data_class_str=kwargs.pop("data_class_str", "Shape"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs,
        )
