import _plotly_utils.basevalidators as _bv


class BoundsValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name="bounds", parent_name="layout.map", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            data_class_str=kwargs.pop("data_class_str", "Bounds"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs,
        )
