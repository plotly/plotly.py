import _plotly_utils.basevalidators as _bv


class TilingValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name="tiling", parent_name="treemap", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            data_class_str=kwargs.pop("data_class_str", "Tiling"),
            data_docs=kwargs.pop(
                "data_docs",
                """
""",
            ),
            **kwargs,
        )
